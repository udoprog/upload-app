"""Helper functions

Consists of functions to typically be used within templates, but also
available to Controllers. This module is available to templates as 'h'.
"""
# Import helpers as desired, or define your own, ie:
from webhelpers.html.tags import *
from routes import url_for

import os, stat, mimetypes;

from uploadapp.model.file import File
from uploadapp.model.dir import Dir
from uploadapp.lib.mimetypes import MimeType

import pwd;

def list_directory(root, path, filter_gid=None):
    abs_root = os.path.join(root, path);
    
    if not abs_root:
      return [], [];

    try:
      abs_root_stat = os.stat(abs_root);
      base_mode = abs_root_stat[stat.ST_MODE];
    except OSError, e:
      return [], [];
    
    if not stat.S_ISDIR(base_mode):
      return [], [];
    
    files = list();
    dirs = list();
    
    rd = open_dir(path, ".", abs_root_stat, abs_root)
    dirs.append(rd);
    rd.url_path = path;
    
    for name in os.listdir(abs_root):
      file_path = os.path.join(abs_root, name);
      
      file_stat = os.stat(file_path);
      mode = file_stat[stat.ST_MODE];
      
      if filter_gid:
        if filter_gid != file_stat[stat.ST_GID]:
          continue;
      
      if stat.S_ISDIR(mode):
        dirs.append(open_dir(path, name, file_stat));
      elif stat.S_ISREG(mode):
        files.append(open_file(root, path, name, file_stat))
    
    return rd, sorted(files, lambda f1, f2: cmp(f1.name, f2.name)), sorted(dirs, lambda d1, d2: cmp(d1.name, d2.name));

def open_dir(path, name, dir_stat, abs_path=None):
  d = Dir();
  d.name = name;
  d.url_path = os.path.join(path, name)
  d.abs_path = abs_path;
  
  mode = dir_stat[stat.ST_MODE];
  uid = dir_stat[stat.ST_UID];
  owner = pwd.getpwuid(uid);
  
  d.owner = owner.pw_name;
  d.mode = mode;
  d.mode_s = ''.join(
    [ mode & stat.S_IRUSR > 0 and "r" or "-",
      mode & stat.S_IWUSR > 0 and "w" or "-",
      mode & stat.S_IXUSR > 0 and "x" or "-",
      mode & stat.S_IRGRP > 0 and "r" or "-",
      mode & stat.S_IWGRP > 0 and "w" or "-",
      mode & stat.S_IXGRP > 0 and "x" or "-",
      mode & stat.S_IROTH > 0 and "r" or "-",
      mode & stat.S_IWOTH > 0 and "w" or "-",
      mode & stat.S_IXOTH > 0 and "x" or "-" ]
  );
  
  return d;


def open_file(root, path, name, file_stat=None):
  file_path = os.path.join(root, path, name)
  
  if file_stat is None:
    file_stat = os.stat(file_path);

  if not name:
    name = os.path.basename(file_path);
  
  mode = file_stat[stat.ST_MODE];
  
  if not stat.S_ISREG(mode):
    return None;
  
  f = File();
  f.name = name;
  f.size = file_stat[stat.ST_SIZE];
  f.url_path = os.path.join(path, name)
  f.mime = MimeType(name).mimetype();

  uid = file_stat[stat.ST_UID];
  owner = pwd.getpwuid(uid);

  f.owner = owner.pw_name;
  
  f.mode = mode;
  f.mode_s = ''.join(
    [ mode & stat.S_IRUSR > 0 and "r" or "-",
      mode & stat.S_IWUSR > 0 and "w" or "-",
      mode & stat.S_IXUSR > 0 and "x" or "-",
      mode & stat.S_IRGRP > 0 and "r" or "-",
      mode & stat.S_IWGRP > 0 and "w" or "-",
      mode & stat.S_IXGRP > 0 and "x" or "-",
      mode & stat.S_IROTH > 0 and "r" or "-",
      mode & stat.S_IWOTH > 0 and "w" or "-",
      mode & stat.S_IXOTH > 0 and "x" or "-" ]
  );

  return f;

TB=1e12
GB=1e9
MB=1e6
KB=1e3

def fmt_size(size):
    if size >= GB:
        return "%.2f&nbsp;GB"%(size / GB)
    
    if size >= MB:
        return "%.2f&nbsp;MB"%(size / MB)
        
    if size >= KB:
        return "%.2f&nbsp;KB"%(size / KB)
    
    return "%d&nbsp;B"%(size)

class Flash:
  def __init__(self, message=None):
    from pylons import session
    if message is None:
      self.setMessage(session.get('flash', None))
    else:
      self.setMessage(message);
      session['flash'] = message;
      session.save();
  
  def setMessage(self, message):
    self.message = message;

  def getMessage(self):
    return self.message
  
  def flush(self):
    from pylons import session
    
    if session.has_key('flash'):
      del session['flash']
      session.save();
  
  message = property(getMessage, setMessage);

def path_root(root, *path, **kw):
  """
  Assert that a specific path begins with root, otherwise, fuck it.
  """
  import os

  filter_gid = kw.get("filter_gid", None);
  no_stat = kw.get("no_stat", False);
  
  p = os.path.normpath(os.path.join(root, *path));
  if not p.startswith(root):
    return None, None;
  
  p_s = None;
  
  if not no_stat:
    try:
      p_s = os.stat(p);
    except OSError, e:
      return None, None;
    
    if filter_gid:
      if p_s[stat.ST_GID] != filter_gid:
        return None, None;
  
  return p_s, p;
