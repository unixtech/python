import json

import pydantic
import json


def main() -> None:
    '''

    Main Function
    Read the JSON file.
    Here were are loading the data
    '''
    with open('/root/PY/data/pydantic_data.json') as file:
        data = json.load(file)
        print(data[0]['title'])


if __name__ == "__main__":
    main()


