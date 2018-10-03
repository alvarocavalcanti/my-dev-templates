# Python Configurations, Tips and Utils

## Duck-typing helper

```python
class Duck:
    def __init__(self, **kwds):
        self.__dict__.update(kwds)
```
