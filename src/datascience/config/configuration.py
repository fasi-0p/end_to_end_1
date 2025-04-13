from src.datascience.constants import *
from src.datascience.utils.common import create_directories, read_yaml #i cant import *
from src.datascience.entity.config_entity import DataIngestconfig

# You might need this if read_yaml returns a Box object for dot notation access
# from box import ConfigBox

class ConfigurationManager:
    def __init__(self,
                 config_filepath=CONFIG_FILE_PATH, #defined in constant
                 params_filepath=PARAMS_FILE_PATH,
                 schema_filepath=SCHEMA_FILE_PATH):
                 #schema_filepath=Path("schema.yaml")): # Comment kept for context

        # Read the YAML files and store their content
        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)
        self.schema = read_yaml(schema_filepath)

        # Now self.config holds the content of config.yaml
        # Ensure 'artifacts_root' is a top-level key in your config.yaml
        create_directories([self.config.artifacts_root])

    def get_data_ingestion_config(self)-> DataIngestconfig:
        # This part should now work correctly as self.config holds the loaded data
        config = self.config.data_ingestion
        create_directories([config.root_dir])

        data_ingestion_config = DataIngestconfig(
            root_dir=config.root_dir,  #since its config we can access it using .key
            source_URL=config.source_URL,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir # Use the corrected name

        )
        return data_ingestion_config
