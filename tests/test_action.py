from typing import Optional, Any


from unimog import Action, Context


class TestAction:
    def test_failure(self):
        class MyAction(Action):
            def perform(self) -> Optional[dict[str, Any]]:
                raise Exception("this should fail")
            
        action = MyAction()
        result = action()
        
        assert result.is_failure()

    def test_success(self):
        class MyAction(Action):
            def perform(self) -> Optional[dict[str, Any]]:
                return {}

        action = MyAction()
        result = action()

        assert result.is_success()
        
    def test_empty_kwargs(self):
        class MyAction(Action):
            def perform(self) -> Optional[dict[str, Any]]:
                return {}

        action = MyAction()
        result = action()

        assert result.is_success()
        
    def test_kwargs(self):
        class MyAction(Action):
            def perform(self) -> Optional[dict[str, Any]]:
                return {}

        action = MyAction()
        result = action(hello="world")

        assert result.hello == "world"
        
    def test_many_kwargs(self):
        class MyAction(Action):
            def perform(self) -> Optional[dict[str, Any]]:
                return {}

        action = MyAction()
        result = action(hello="world", foo="bar")

        assert result.hello == "world"
        assert result.foo == "bar"
        
    def test_empty_context_argument(self):
        class MyAction(Action):
            def perform(self) -> Optional[dict[str, Any]]:
                return {}

        action = MyAction()
        context = Context()
        result = action(context)

        assert result.is_success()
        
    def test_context_argument(self):
        class MyAction(Action):
            def perform(self) -> Optional[dict[str, Any]]:
                return {}

        action = MyAction()
        context = Context(hello="world")
        result = action(context)

        assert result.hello == "world"
            
    def test_context_is_enriched(self):
        class MyAction(Action):
            def perform(self) -> Optional[dict[str, Any]]:
                return {"foo": "bar"}

        action = MyAction()
        result = action()
        
        assert result.is_success()
        assert result.foo == "bar"
