# ivozzo-pyBoilerplate
## A Personal Python Boilerplate

Ever been tired of rewriting the same code for every project?

Well, I do. Or at least, I'm bored of copy pasting the same configuration for some basic functionalities I often use, so I wrote my own boilerplate.
Any suggestion (or PR) is obviously welcome!

## Usage

### Logger class

If you need a logger class using logging with file writing and console appending use this class.

```python
from boilerplate.logger import Logger

# with FileHandler and StreamHandler
logger = Logger(path="insert path here", filename="insert filename here", level="ERROR / WARN / INFO / DEBUG")

# with StreamHandler only
logger = Logger(level="ERROR / WARN / INFO / DEBUG")

logger.info("message")
2021-02-10 08:44:44,086|[MainThread  ]|[INFO ]| message
```

### MongoDatabase class

If you need a Mongo client with some basic functionalities extends this class.

```python
from boilerplate.mongodatabase import MongoDatabase

class MyMongoClient(MongoDatabase):
    def __init__(self, host, user, password, database):
        self.database = super().__init__(host=host, user=user, password=password, database=database)
        
    def [extensions]

```