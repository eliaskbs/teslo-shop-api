from pydantic import BaseModel, Field


class PaginationParams(BaseModel):
    limit: int = Field(default=10, gt=0, description="Items per page")
    offset: int = Field(default=0, ge=0, description="Items to skip")
