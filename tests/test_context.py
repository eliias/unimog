from dataclasses import dataclass
from typing import Optional

from unimog import Context


class TestContext:
    def test_partial_context(self):
        @dataclass
        class SomeContext(Context):
            age: Optional[int] = None

        context = SomeContext()
        assert context.age is None
