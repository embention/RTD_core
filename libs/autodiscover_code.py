import os, sys, fnmatch

def find_files(directory, pattern):
  for root, dirs, files in os.walk(directory):
    for basename in files:
      if fnmatch.fnmatch(basename, pattern):
        filename = os.path.join(root, basename)
        yield filename


def section_header(sectionName, isSubsection = False ):
  """Function to obtain a section or subsection header

  Args:
      sectionName (str): Section or Subsection name
      isSubsection (bool): Is a subsection or not, default False

  Returns:
      (str): Section or Subsection Header ready to print
  """
  sectionHeader = "=="
  if isSubsection:
    sectionHeader = "--"

  count = 0
  while count < len(sectionName):
    if not isSubsection:
      sectionHeader += "=="
    else:
      sectionHeader += "--"
    count += 1

  sectionHeader = """

""" + sectionName +"""
""" + sectionHeader +"""

  """
  return sectionHeader


def autodiscover_python_code( path_code, path_repo, filepath_discovered_code, file_header ):
  """Function to autodiscover Python Code inside a folder

  Args:
      path_code (string): Path to code folder for autodiscover in repository
      path_repo (string): Path to repository folder in the current system
      filepath_discovered_code  (string): Pathfile where the autodiscoverd code will be written
      file_header (string): File Header

  """

  with open(filepath_discovered_code,"w") as f:
    f.write( section_header(file_header) )

    for x in find_files(path_code,"*.py"):
      new_path = x.replace(path_repo,"").replace("/",".")
      if(os.name== 'nt'): # Detection if python is running on Windows
        new_path = new_path.replace("\\",".")
      new_path= new_path[:-3]

      f.write( section_header( new_path, True) + 
"""
.. automodule:: """ + new_path +"""
    :members:
    :undoc-members:
    :show-inheritance:
"""
      )
    f.close()