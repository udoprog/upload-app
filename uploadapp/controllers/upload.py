import logging

from pylons import request, response, session, tmpl_context as c
from pylons.controllers.util import abort, redirect_to, redirect
from pylons import config

from uploadapp.model.file import File
from uploadapp.lib.base import BaseController, render
from uploadapp.lib.helpers import Flash, path_root
from uploadapp.lib.doas import doas
import uploadapp.lib.helpers as h

from pylons.decorators import validate

log = logging.getLogger(__name__)

import os;

from uploadapp.lib.mimetypes import MimeType

class UploadController(BaseController):
    def login(self):
      return redirect(h.url_for(action="list", path=""))
    
    def list(self, path):
        import os
        root = config['uploadapp.root'];
        
        f = Flash();
        
        if f.message is not None:
          c.err = True;
          c.err_msg = f.message;
          f.flush();
        else:
          c.err = False
        
        abs_root_stat, abs_root = path_root(root, path, filter_gid=c.group.gr_gid);
      
        c.files = list();
        c.dirs = list();
        c.tree = list();
        c.writable = False;
        
        while True:
          if not abs_root:
            c.err = True;
            c.err_msg = "Cannot resolve path";
            break;

          if not os.path.isdir(abs_root):
            c.err = True;
            c.err_msg = "Path is not a directory";
            break;

          if not c.user.read(abs_root):
            c.err = True;
            c.err_msg = "Path is not readable by you";
            break;
          
          c.current_dir, c.files, c.dirs = h.list_directory(root, path, c.group.gr_gid);

          parts = path.split('/');
          
          if path == "":
            c.tree = list();
          else:
            c.tree = [(parts[i], "%s"%('/'.join(parts[0:i+1]))) for i in range(len(parts))];
          
          c.writable = c.user.write(c.current_dir.abs_path)
          break;
        
        c.tree.insert(0, ('root', ''))
        return render('upload/list.mako');
    
    def download(self, path):
      import os
      root = config['uploadapp.root'];

      abs_root_stat, abs_root = path_root(root, path);

      while True:
        if not abs_root:
          Flash("Cannot download file; unable to resolve path");
          break;
        
        if not os.path.isfile(abs_root):
          Flash("Cannot download file; file does not exist");
          break;

        if not c.user.read(abs_root):
          Flash("Cannot download file; permission denied");
          break;
        
        accel_base = config.get("uploadapp.accel_base")
        accel_path = accel_base%(path);

        response.headers["X-Accel-Redirect"] = accel_path;
        response.content_type = MimeType(path).mimetype()
        response.headers["Content-Disposition"] = "attachment"
        return "";

      return redirect(h.url_for(action="list", path=""));
  
    def upload(self, path):
      import os, stat;
      root = config['uploadapp.root'];
      
      while True:
        if "dir" in request.params:
          abs_dir_stat, abs_dir = path_root(root, path, request.params.get("dir"), no_stat=True)
          
          if not abs_dir:
            Flash("Cannot resolve directory");
            break;
          
          if os.path.exists(abs_dir):
            Flash("Directory already exists");
            break;
          
          # check if current user can write to parent directory
          if not c.user.write(os.path.dirname(abs_dir)):
            Flash("Cannot create directory; permission denied");
            break;
          
          try:
            doas(c.user.uid, c.group.gr_gid, os.mkdir, abs_dir);
          except OSError, e:
            log.error(e);
            Flash(e.strerror);
        elif "file" in request.params:
          p_file = request.params.get("file");
          
          abs_path_stat, abs_path = path_root(root, path, p_file.filename, no_stat=True)
          
          if not abs_path:
            Flash("Cannot resolve path");
            break;
          
          if os.path.exists(abs_path):
            Flash("File already exists");
            break;
          
          # check if current user can write to parent directory
          if not c.user.write(os.path.dirname(abs_path)):
            Flash("Cannot create file; permission denied");
            break;
          
          try:

            def read_entire_file(file_e, to_path):
              to_f = open(to_path, 'w');
              
              while True:
                d = file_e.file.read(2**14);
                
                if not d:
                  break;
                
                to_f.write(d)
            
            pid, status = doas(c.user.uid, c.group.gr_gid, read_entire_file, p_file, abs_path);
          except IOError, e:
            log.error(e);
            Flash(e.strerror);
        
        break;
      
      return redirect(h.url_for(action="list", path=path));
    
    def _action_chmod( self, upload_path, paths ):
      import stat;
      
      root = config['uploadapp.root'];
      
      failed = list();

      mode = 0;

      if "ur" in request.POST:
        mode |= stat.S_IRUSR;
      
      if "uw" in request.POST:
        mode |= stat.S_IWUSR;
      
      if "ux" in request.POST:
        mode |= stat.S_IXUSR;
      
      if "gr" in request.POST:
        mode |= stat.S_IRGRP;
      
      if "gw" in request.POST:
        mode |= stat.S_IWGRP;
      
      if "gx" in request.POST:
        mode |= stat.S_IXGRP;
      
      if "or" in request.POST:
        mode |= stat.S_IROTH;
      
      if "ow" in request.POST:
        mode |= stat.S_IWOTH;
      
      if "ox" in request.POST:
        mode |= stat.S_IXOTH;
      
      for path in paths:
        abs_path_stat, abs_path = path_root( root, upload_path, path )
        
        if not abs_path:
          # this is a bad path
          # probably someone malicious sending requests which addresses relative paths.
          failed.append((path, "Could not resolve path"));
          continue;
        
        if not c.user.write(abs_path):
          failed.append((path, "Cannot chmod path; permission denied"));
          continue;
        
        try:
          os.chmod(abs_path, mode);
        except OSError, e:
          failed.append((path, e.strerror));
      
      if len( failed ) > 0:
        Flash( str(failed) );
      
      return redirect(h.url_for(action="list", path=upload_path));
    
    def _action_delete( self, upload_path, paths ):
      import os, stat;
      
      root = config['uploadapp.root'];
      
      failed = list();
      
      for path in paths:
        abs_path_stat, abs_path = path_root( root, upload_path, path )
        
        if not abs_path:
          # this is a bad path
          # probably someone malicious sending requests which addresses relative paths.
          failed.append((path, "Could not resolve path"));
          continue;

        if not c.user.write(abs_path):
          failed.append((path, "Cannot remove path; permission denied"));
          continue;
        
        if os.path.isdir(abs_path):
          if not c.user.write( abs_path ):
            failed.append((path, "Cannote remove directory since it is not writable by you"));
            continue;
          
          try:
            pid, status = doas(c.user.uid, c.group.gr_gid, os.rmdir, abs_path);
          except OSError, e:
            failed.append((path, e.strerror));
            continue;
          
          if status != 0:
            failed.append((path, "Failed to remove directory"));
            continue;
        elif os.path.isfile( abs_path ):
          if not c.user.write( os.path.dirname(abs_path) ):
            failed.append((path, "Cannote remove file since directory is not writable"));
            continue;
          
          try:
            pid, status = doas(c.user.uid, c.group.gr_gid, os.remove, abs_path);
          except OSError, e:
            failed.append((path, e.strerror));
            continue;

          if status != 0:
            failed.append((path, "Failed to remove file"));
            continue;

      if len( failed ) > 0:
        Flash( str(failed) );
      
      return redirect(h.url_for(action="list", path=upload_path));
    
    def action(self, path, action):
      if "delete" in request.POST:
        return self._action_delete( path, request.POST.getall( 'paths' ) );
      
      if "chmod" in request.POST:
        return self._action_chmod( path, request.POST.getall( 'paths' ) );

    def view(self, path):
      import os

      root = config['uploadapp.root'];
      
      abs_path_stat, abs_file = path_root(root, path);
      
      while True:
        if not abs_file:
          Flash("Cannot resolve file");
          break;
          
        if not os.path.isfile(abs_file):
          Flash("File does not exist");
          break;
        
        if not c.user.read(abs_file):
          Flash("Cannot view file; permission denied");
          break;
        
        basename = os.path.basename(path)
        
        f = h.open_file(root, os.path.dirname(path), basename);
        
        if f.size > 1e7:
          return "File too big, download instead of view";
        
        accel_path = config.get("uploadapp.accel_base")%(path);
        
        response.content_type=MimeType(basename).mimetype();
        response.headers["X-Accel-Redirect"] = accel_path;
        return "";
      
      return redirect(h.url_for(action="list", path=""));
