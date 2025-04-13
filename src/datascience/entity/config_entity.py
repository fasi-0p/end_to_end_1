from dataclasses import dataclass
from pathlib import Path 

@dataclass 
class DataIngestconfig:   #all these parameters are matching config.yaml data_ingestion
    root_dir: Path 
    source_URL: str
    local_data_file: Path 
    unzip_dir: Path

