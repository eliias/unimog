from dataclasses import dataclass

from unimog import Action, Organizer, Context


class TestOrganizer:
    def test_failure(self):
        class MyAction1(Action):
            def perform(self):
                raise Exception("step 1 fails")
            
        class MyAction2(Action):
            def perform(self):
                pass

        organizer = Organizer(MyAction1(), MyAction2())
        result = organizer()

        assert result.is_failure()

    def test_success(self):
        @dataclass
        class Step1Input(Context):
            pass

        @dataclass
        class Step1Output(Context):
            step1: bool = None

        @dataclass
        class Step2Input(Context):
            step1: bool

        @dataclass
        class Step2Output(Context):
            step1: bool = None
            step2: bool = None

        class MyAction1(Action):
            def perform(self):
                self.output.step1 = True

        class MyAction2(Action):
            def perform(self):
                self.output.step2 = True

        organizer = Organizer(
            MyAction1(Step1Input, Step1Output),
            MyAction2(Step2Input, Step2Output))
        result = organizer()

        assert result.is_success()
