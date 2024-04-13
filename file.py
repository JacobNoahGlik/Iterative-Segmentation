class Function:
  def __init__(self, name: str, args: list[str], body: str, prefix_text: str = ''):
    self.name: str = name
    self.args: list[str] = args
    self.body: str = body
    self.prefix: str = prefix_text

class Class:
  def __init__(self, name: str, body: str):
    self.name: str = name
    self.body: str = body
    self.functions: list[Function] = []
    self.indentation: str = ''
    self.deps: list[str] = []
    self._scan_body()

class File:
  def __init__(self, name: str):
    self.name: str = name
    self.body: str = ''
    self.classes: list[Class] = []
    self.functions: list[Function] = []
    self.deps: list[str] = []
    self._scan_file()
