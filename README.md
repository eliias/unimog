# unimog

> Elegant service objects for Python.

A robust and flexible framework that facilitates composable business logic and
ensures uniform error handling for various business logic actions. The
fundamental concept revolves around the idea that a single action should
perform a specific task, and these actions can be seamlessly organized into
groups. Notably, these groups and actions can be intricately nested, forming
complex Directed Acyclic Graphs (DAGs).

To enhance readability and maintainability, we leverage the concept of service
objects to encapsulate intricate business logic in an easily understandable
format. Establishing a normalized interface for all service calls not only
streamlines the overall architecture but also enables the chaining of service
calls. This consistent approach to handling errors across the entire framework
ensures a standardized and predictable error-handling mechanism, contributing
to the reliability of the system.

## Usage

```bash
pip install unimog
```

### Action

```python
import gzip

from unimog import Action


class CompressText(Action):
    def perform(self):
        compressed_text = gzip.compress(self.context.input)
        return {"compressed_text": compressed_text}

result = CompressText()(input="Hello, World!")
result.is_success() # True
result.compressed_text # b'\x1f\x8b\x08\x00r\x92\xb7e…
```

### Organizer

```python
import gzip

from unimog import Action, Organizer


class CompressText(Action):
    def perform(self):
        compressed_text = gzip.compress(self.context.input)
        return {"compressed_text": compressed_text}

    
class DecompressText(Action):
    def perform(self):
        text = gzip.decompress(self.context.data)
        return {"text": text}

CompressAndDecompressText = Organizer(CompressText, DecompressText)

result = CompressAndDecompressText(input="Hello, World!")
result.is_success() # True
result.text # "Hello, World!"
```

## Contributing

### Tests

```bash
python -m pytest
```
