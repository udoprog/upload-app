#!/usr/bin/python
import os
import stat;
import sys;

import pwd, grp;

class SystemUser:
  def __init__(self, username=None, anonymous=False, nobody="nobody"):
    groups = list();
    groupnames = dict();

    if not username:
      username = nobody;
    
    result = pwd.getpwnam(username);
    
    for group in grp.getgrall():
      if username in group.gr_mem:
        groups.append(group.gr_gid);
        groupnames[group.gr_gid] = group.gr_name;
    
    self.username = result.pw_name;
    self.uid = result.pw_uid;
    self.gid = result.pw_gid;
    self.anonymous = anonymous;
    
    self.groups = groups;
    self.nobody_uid = pwd.getpwnam(nobody).pw_uid
  
  def read(self, path):
    uid, gid, mode = self._stat_path(path);
    
    if uid == self.nobody_uid:
      return True;
    
    if self.uid == uid:
      return True;
    
    if gid in self.groups:
      return mode & stat.S_IRGRP > 0;
    
    return mode & stat.S_IROTH > 0;

  def write(self, path):
    uid, gid, mode = self._stat_path(path);
    
    if uid == self.nobody_uid:
      return True;
    
    if self.uid == uid:
      return True;
    
    if gid in self.groups:
      return mode & stat.S_IWGRP > 0;
    
    return mode & stat.S_IWOTH > 0;

  def execute(self, path):
    uid, gid, mode = self._stat_path(path);
    
    if uid == self.nobody_uid:
      return True;
    
    if self.uid == uid:
      return True;
    
    if gid in self.groups:
      return mode & stat.S_IXGRP > 0;
    
    return mode & stat.S_IXOTH > 0;

  def _stat_path(self, path):
    st = os.stat(path);
    return st[stat.ST_UID], st[stat.ST_GID], st[stat.ST_MODE]

  def __str__(self):
    return "<SystemUser username=%s>"%(self.username)

def main(args):
  import os;
  
  user = SystemUser("udoprog");
  print user.write("/tmp");
  
  print user.username
  print user.uid
  print user.groups
  
  return 1;

if __name__ == "__main__":
  sys.exit(main(sys.argv[1:]))
