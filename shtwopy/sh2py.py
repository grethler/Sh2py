import os
import base64
import textwrap
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
        self.python_script: str = open(path, "rb").read()
        self.custom_output_path: str = ""
        self.output_name: str = ""
        if not self.output_name:
            self.filename: str = f"{self.custom_output_path}{os.path.basename(path)}"
        else:
            self.filename: str = f"{self.custom_output_path}{self.output_name}"
        self.shell_script: str = "#!/bin/bash\n"

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
        if len(b64) > 64:
            b64 = textwrap.wrap(b64, width=64)
            self.shell_script += f"b64='{b64[0]}'\n"
            for i in range(1, len(b64)):
                self.shell_script += f"b64+='{b64[i]}'\n"
        else:
            self.shell_script += f"b64={b64}"
        self.shell_script += f"\necho $b64 | base64 -d > {self.filename}"
        self.__fileout()
