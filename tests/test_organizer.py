from unimog import Action, Organizer


class TestOrganizer:
    def test_failure(self):
        class MyAction1(Action):
            def perform(self):
                raise Exception("step 1 fails")
            
        class MyAction2(Action):
            def perform(self):
                return {"step2": True}

        organizer = Organizer(MyAction1, MyAction2)
        result = organizer()

        assert result.is_failure()

    def test_success(self):
        class MyAction1(Action):
            def perform(self):
                return {"step1": True}

        class MyAction2(Action):
            def perform(self):
                return {"step2": True}

        organizer = Organizer(MyAction1, MyAction2)
        result = organizer()

        assert result.is_success()
