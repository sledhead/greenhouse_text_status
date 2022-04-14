
from dataclasses import dataclass
from pathlib import Path
import json

@dataclass
class LoadSettings:
  file_path: Path


  def LoadSettingFile(self) -> dict:

    if not self.file_path.exists():
      raise TypeError("file does not exist")

    with open(self.file_path, mode='r') as f_json_file:
      json_dict = json.load(f_json_file)
  
    return json_dict