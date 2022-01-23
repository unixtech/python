from dataclasses import dataclass, field
from pprint import pprint
import inspect



@dataclass(frozen=True)
class Comment:
    id: int
    text: str = field(default='')
    replies: list[int] = field(default_factory=list, compare=False, hash=False, repr=False)


def main():
    comment = Comment(1, 'I just subscribed')
    print(comment)

    pprint(inspect.getmembers(Comment, inspect.isfunction))


if __name__ == "__main__":
    main()
