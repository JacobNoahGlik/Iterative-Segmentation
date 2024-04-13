class Function:
  def __init__(self, name, args, body, prefix_text = ''):
    self.name = name
    self.args = args
    self.body = body
    self.prefix = prefix_text

class Class:
  def __init__(self, name, body):
    self.name = name
    self.body = body
    self.functions = []
    self.indentation = ''
    self.deps = []
    self._scan_body()

class File:
  def __init__(self, name):
    self.name = name
    self.body = ''
    self.classes = []
    self.functions = []
    self.deps = []
    self._scan_file()
