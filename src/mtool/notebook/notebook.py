"""
This file contains the Notebook class, with methods for loading in a .ipynb
file and checking its parameterization information.
"""

import os

def init_notebook_run(outfile_root):
    """ initializes the notebook folder"""
    from src.mtool.util import sqlite_util
    from src.mtool.cli import display
    
    if not os.path.exists(outfile_root):
        os.mkdir(outfile_root)
        display.display_init_run_notebook(outfile_root)


class Notebook:
    """ this is the notebook class, which is an instance of a notebook"""
    def __init__(self, path, library_path):
        from src.mtool.cli import display
        #TODO: add support for reading from a URL

        self._hasParameters = False
        self._environmentVars = []

        self._path = os.path.join(os.path.expandvars(library_path), path)
        split = os.path.split(path)
        self.name = split[-1]
        self.library_name = os.path.split(split[0])[-1]
        try:
            f = open(self._path)
            self.extract_params(f)
        except(FileNotFoundError):
            display.notebook_does_not_exist_error(self.name)
    
    def getpath(self):
        return self._path

    def extract_params(self, openFile):
        import ijson

        objects = ijson.items(openFile, 'cells.item')
        code_cells = (o for o in objects if o['cell_type'] == 'code')
        for cell in code_cells:
            metadata = cell.get("metadata")
            if metadata and "parameters" in metadata.get("tags"):
                self._hasParameters = True
                self.extract_envVars(cell.get("source"))
                return

    def extract_envVars(self, source):
        if(isinstance(source, list)):
            lines = source
        else:
            lines = source.splitlines()
        for line in lines:
            if "=" in line and not line.startswith("#"):
                self._environmentVars.append(line.split("=")[0].strip())


