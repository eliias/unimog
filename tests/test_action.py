from dataclasses import dataclass

from unimog import Action, Context


class TestAction:
    def test_failure(self):
        class MyAction(Action):
            def perform(self):
                raise Exception("this should fail")
            
        action = MyAction()
        result = action()
        
        assert result.is_failure

    def test_success(self):
        class MyAction(Action):
            def perform(self):
                pass

        action = MyAction()
        result = action()

        assert result.is_success
        
    def test_empty_kwargs(self):
        class MyAction(Action):
            def perform(self):
                pass

        action = MyAction()
        result = action()

        assert result.is_success
        
    def test_kwargs(self):
        @dataclass
        class Input(Context):
            hello: str

        @dataclass
        class Output(Context):
            hello: str

        class MyAction(Action):
            def perform(self):
                pass

        action = MyAction(Input, Output)
        result = action(hello="world")

        assert result.hello == "world"
        
    def test_many_kwargs(self):
        @dataclass
        class Input(Context):
            hello: str
            foo: str

        @dataclass
        class Output(Context):
            hello: str
            foo: str

        class MyAction(Action):
            def perform(self):
                pass

        action = MyAction(Input, Output)
        result = action(hello="world", foo="bar")

        assert result.hello == "world"
        assert result.foo == "bar"
