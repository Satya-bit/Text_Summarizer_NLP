#Step-6
from src.Text_Summarizer_NLP.logging import logger
from src.Text_Summarizer_NLP.pipeline.stage_1_data_ingestion_pipeline import DataIngestionTrainingPipeline # type: ignore
from src.Text_Summarizer_NLP.pipeline.stage_2_data_transformation_pipeline import DataTransformationPipeline # type: ignore
from src.Text_Summarizer_NLP.pipeline.stage_3_model_trainer_pipeline import ModelTrainerTrainingPipeline # type: ignore
from Text_Summarizer_NLP.pipeline.stage_4_model_evaluation_pipeline import ModelEvaluationPipeline # type: ignore
STAGE_NAME = "Data Ingestion stage"

try:
    logger.info(f"stage {STAGE_NAME} initiated")
    data_ingestion_pipeline=DataIngestionTrainingPipeline()
    data_ingestion_pipeline.initiate_data_ingestion()
    logger.info(f"stage {STAGE_NAME} completed")

except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Data Transformation stage"

try:
    logger.info(f"stage {STAGE_NAME} initiated")
    data_ingestion_pipeline=DataTransformationPipeline()
    data_ingestion_pipeline.initiate_data_transformation()
    logger.info(f"stage {STAGE_NAME} completed")

except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME="Model Trainer stage"

try:
    logger.info(f"stage {STAGE_NAME} initiated")
    model_trainer_pipeline=ModelTrainerTrainingPipeline()
    model_trainer_pipeline.initiate_model_trainer()
    logger.info(f"Stage {STAGE_NAME} Completed")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Model Evaluation stage"
try: 
   logger.info(f"*******************")
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
   model_evaluation = ModelEvaluationPipeline()
   model_evaluation.initiate_model_evaluation()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e
