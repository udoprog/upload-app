

#
# File representation entity.
#
class File:
  def setName(self, name):
    self.name = name;
  
  def getName(self):
    return self.name;

  def getSize(self):
    return int(self.size);

  def setSize(self, size):
    self.size = size;
  
  def setUrlPath(self, url_path):
    self.url_path = url_path;

  def getUrlPath(self):
    return self.url_path;
  
  name = property(getName, setName);
  size = property(getSize, setSize);
  url_path = property(getUrlPath, setUrlPath);
