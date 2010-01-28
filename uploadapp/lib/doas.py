import sys;
import os;
import pwd;
import pickle;
import traceback;

def doas(uid, gid, cb, *args, **kw):
  """
  Create a child process which executes a specific command as a specific uid/gid combination.
  This is to preserve the the user information for the parent process.
  """
  
  r, w = os.pipe();
  
  if os.fork() != 0:
    os.close(w);
    exc = os.fdopen(r, "r").read();
    
    if len(exc) > 0:
      child_exception = pickle.loads(exc);
      raise child_exception;
    
    # wait for childprocess to finish
    return os.wait();
  
  os.close(r);
  w_p = os.fdopen(w, "w");
  
  try:
    os.setgid(gid);
    os.setuid(uid);
    cb(*args, **kw);
  except:
    # code/concept borrowed from the subprocess module
    # theres not a lot of other ways in which you can do this nicely.
    exc_type, exc_value, tb = sys.exc_info()
    exc_lines = traceback.format_exception(exc_type,
                                           exc_value,
                                           tb)
    exc_value.child_traceback = ''.join(exc_lines)
    w_p.write(pickle.dumps(exc_value));
  
  w_p.flush();
  w_p.close();
  os._exit(0);

# example code
def main(argv):
  def echo(s):
    print s;
  
  u = pwd.getpwnam("udoprog");
  
  pid, status = doas(u.pw_uid, u.pw_gid, echo, "Hello World");
  
  print status;
  print os.getgid();
  print os.getuid();
  
  pid, status = doas(u.pw_uid, u.pw_gid, open, "/test.txt", "w");
  
  return 0;

if __name__ == "__main__":
  sys.exit(main(sys.argv[1:]));
