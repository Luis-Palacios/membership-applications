from pydantic import BaseModel, ConfigDict
from pydantic.alias_generators import to_camel


class PascalModel(BaseModel):
    model_config = ConfigDict(
        alias_generator=to_camel,
        populate_by_name=True  # Allows using both PascalCase and snake_case in Python
    )