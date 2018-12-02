#
# Module that defines methods that identify and extract import statements in
# code.

def look_for_dependency_in_source_file(path_to_source, module_name):
  """
  Parses a source file and looks for imports of a particular module.
  path_to_source: Absolute path to the source file that needs to be searched.
  module_name: The name of the module to be searched.
  Returns: bool indicating whether whether the module has been imported.
  """
