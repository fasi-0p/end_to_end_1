from src.datascience.config.configuration import ConfigurationManager
from src.datascience.components.data_ingestion import DataIngestion
import logging as logger

STAGE_NAME="Data ingestion stage"

class DataIngestionTrainingPipeline:
    def __init__(self):
        pass

    def initiate_data_ingestion(self):
            config=ConfigurationManager()
            data_ingestion_config=config.get_data_ingestion_config()
            # Corrected line 14 and indented:
            data_ingestion=DataIngestion(config=data_ingestion_config)
            # Indented lines 15 and 16:
            data_ingestion.download_file()
            data_ingestion.extract_zip_file()

if __name__=="__main__":
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj=DataIngestionTrainingPipeline()
        obj.initiate_data_ingestion()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e