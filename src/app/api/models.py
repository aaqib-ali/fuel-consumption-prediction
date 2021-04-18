from pydantic import BaseModel, ValidationError, validator


class Features(BaseModel):
    Cylinders: int
    Displacement: float
    Horsepower: float
    Weight: float
    Acceleration: float
    Model_Year: int
    Europe: int
    Japan: int
    USA: int

    @validator('Europe')
    def europe_must_contain_zero_or_one(cls, v):
        if v != 0 and v != 1:
            raise ValueError('must contain a zero or one')
        return v

    @validator('Japan')
    def japan_must_contain_zero_or_one(cls, v):
        if v != 0 and v != 1:
            raise ValueError('must contain a zero or one')
        return v

    @validator('USA')
    def usa_must_contain_zero_or_one(cls, v):
        if v != 0 and v != 1:
            raise ValueError('must contain a zero or one')
        return v
