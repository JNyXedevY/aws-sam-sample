import json

from aws_lambda_powertools.utilities.typing import LambdaContext


def lambda_handler(event: dict, context: LambdaContext) -> dict:
    return {
        "statusCode": 200,
        "body": json.dumps({})
    }
