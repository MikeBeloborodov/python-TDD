import unittest
from pydantic import ValidationError
from functions.data_schema import User

class TestCreateUser(unittest.TestCase):

    def test_cast_good_user_input_with_pydantic(self) -> None:
        user_input: dict = {"name": "Mike", "age": 29, "employment_status": True}
        created_user: User = User(**user_input)
        assert created_user.name == "Mike"
        assert created_user.age == 29
        assert created_user.employment_status == True

    def test_cast_bad_user_input_with_pydantic(self) -> None:
        user_input: dict = {"name": 21, "age": "Twenty Nine", "employment_status": "Not sure"}
        try:
            created_user: User = User(**user_input)
        except Exception as Error:
            assert type(Error) == ValidationError