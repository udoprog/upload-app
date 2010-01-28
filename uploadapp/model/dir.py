#
# File representation entity.
#
class Dir:
  def setName(self, name):
    self.name = name;
  
  def getName(self):
    return self.name;
  
  def setUrlPath(self, url_path):
    self.url_path = url_path;

  def getUrlPath(self):
    return self.url_path;
  
  name = property(getName, setName);
  url_path = property(getUrlPath, setUrlPath);
