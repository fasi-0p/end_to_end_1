import logging as logger
#pfrom src.datascience import logger
from src.datascience.pipeline.data_ingestion import DataIngestionTrainingPipeline
from src.datascience.pipeline.data_validation import DataValidationTrainingPipeline


STAGE_NAME="Data ingestion stage"

try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    obj=DataIngestionTrainingPipeline()
    obj.initiate_data_ingestion()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME="Data validation stage"

try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    obj=DataValidationTrainingPipeline()
    obj.initiate_data_validation()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e