import json

from pydantic import ValidationError
from pydantic_core import InitErrorDetails


def create_json_from_validation_error(exception: ValidationError):
    return {
        'error': json.loads(exception.json()),
        'error_count': exception.error_count(),
        'title': str(exception.title)
    }


def create_validation_error(title, loc_name, type):
    raise ValidationError.from_exception_data(
        title=title,
        line_errors=[
            InitErrorDetails(
                loc=(loc_name,),
                type=type,
                input=None
            )
        ],
        input_type="python",
    )
