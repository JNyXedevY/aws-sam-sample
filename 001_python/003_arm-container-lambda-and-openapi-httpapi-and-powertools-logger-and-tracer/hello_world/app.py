import json

from aws_lambda_powertools.utilities.typing import LambdaContext
from aws_lambda_powertools.logging.formatter import LambdaPowertoolsFormatter
from aws_lambda_powertools.logging import correlation_paths
from aws_lambda_powertools import Logger, Tracer

logger = Logger(logger_formatter=LambdaPowertoolsFormatter(utc=True, log_record_order=["message"]))
tracer = Tracer()


@logger.inject_lambda_context(correlation_id_path=correlation_paths.API_GATEWAY_HTTP)
@tracer.capture_lambda_handler
def lambda_handler(event: dict, context: LambdaContext) -> dict:
    logger.info(f"Received event: {event}")
    logger.info(f"Received context: {context}")
    return {
        "statusCode": 200,
        "body": json.dumps({})
    }
