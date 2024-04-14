import os
import base64
from dataclasses import dataclass


@dataclass
class Sh2Py:
    """
    Convert a python script into a decrypted shell script. \n
    If this shell script is run it will create the original python script. \n
    This can be used for obfuscation purposes or to hide the code
    when sharing it with others. \n
    """
    def __init__(self, path: str) -> None:
        self.python_script: str = self.__parse(path)
        self.custom_output_path: str = ""
        self.output_name: str = ""
        if not self.output_name:
            self.filename: str = f"{self.custom_output_path}{os.path.basename(path)}"
        else:
            self.filename: str = f"{self.custom_output_path}{self.output_name}"
        self.shell_script: str = "#!/bin/bash\n"

    def __parse(self, path: str) -> str:
        """
        Parses the python script.

        Parameters
        ----------
        path : str
            The path to the python script.

        Returns
        -------
        str
            The python script as a binary string.
        """

        with open(path, "rb") as file:
            return file.read()

    def __fileout(self) -> None:
        """
        Writes the shell script to a file.
        """
        with open("shell_script.sh", "w") as file:
            file.write(self.shell_script)

    def base64_encode(self):
        """
        Encodes the python script into base64.
        """
        b64: str = base64.b64encode(self.python_script).decode()
        self.shell_script += f"b64={b64}"
        self.shell_script += f"\necho $b64 | base64 -d > {self.filename}"
        self.__fileout()



def test():
    s2p = Sh2Py(os.path.join(os.getcwd(), "tests/_test.py"))
    # for custom output path use:
    # s2p.custom_output_path = "path/to/output/"
    #
    # for custom output filename use:
    # s2p.output_name = "filename.py"
    s2p.base64_encode()
    print(s2p.shell_script)

if __name__ == "__main__":
    test()
