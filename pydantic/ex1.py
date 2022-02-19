import json

import pydantic
import json
from typing import Optional, List
from pydantic import validators


class ISBN10FormatError(Exception):
    '''
    Custom error that is raised when ISBN10 doesn't have the right format.
    '''
    def __init__(self, value: str, message: str) -> None:
        self.value = value
        self.message = message
        super.__init__(message)




class ISBNMissingError(Exception):
    '''
    Custom Error that is raised when ISBN10 and ISBN13 are missing
    '''

    def __init(self, title: str, message: str) -> None:
        self.title = title
        self.message = message
        super().__init__(message)

class Book(pydantic.BaseModel):
    title: str
    author: str
    publisher: str
    price: float
    isbn_10: Optional[str]
    isbn_13: Optional[str]
    subtitle: Optional[str]


    # Every book has to be one of two 'isbn_10' or 'isbn_13'
    @pydantic.root_validator(pre=True)
    @classmethod
    def check_isbn10_or_isbn13(cls, values):
        '''
        Make sure that there is either ISBN_10 or ISBN_13 methods
        '''
        if "isbn_10" not in values and "isbn_13" not in values:
            raise ISBNMissingError(title=values["title"], message="Doc should have either")
        return values


    @pydantic.validator("isbn_10")
    @classmethod
    def isbn_10_valid(cls, value) :
        '''
        Validator to check whether ISBN10 has a valie value
        
        '''
        chars = [ c for c in value if c in "0123456789Xx" ]
        if len(chars) != 10:
            raise Exception("MSG",value=value)


        def char_to_int(char: str) -> int:
            if char in "xX":
                return 10
            return int(char)
        
        weighted_sum = sum((10 - i) * char_to_int(x) for i, x in enumerate(chars))
        if weighted_sum % 11 != 0:
            raise ISBN10FormatError(value=value, message='ISBN10 divisible by 11.')


        return value


    class config:
        '''
        Pydantic config class
        '''
        allow_mutation = False


def main() -> None:
    '''

    Main Function
    Read the JSON file.
    Here were are loading the data
    '''
    with open('/root/PY/data/pydantic_data.json') as file:
        data = json.load(file)
        '''
        This is the line that I don't understand but okay for now as we tend 
        to overpass the tiem, For now remember to deconstruct the classes like this.
        '''
        books = [Book(**item) for item in data]
        print(data[0]['title'])
        print(books[0].title)
        print(books[0].dict(include={'price', 'title'}))


if __name__ == "__main__":
    main()


