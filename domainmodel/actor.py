

class Actor:

    def __init__(self, actor_full_name: str):
        if actor_full_name == "" or type(actor_full_name) is not str:
            self.__actor_full_name = None
        else:
            self.__actor_full_name = actor_full_name.strip()
        self.__actor_colleagues_set = []

    @property
    def actor_full_name(self) -> str:
        return self.__actor_full_name

    def __repr__(self):
        return f"<Actor {self.__actor_full_name}>"

    def __eq__(self, other):
        return self.__actor_full_name == other.actor_full_name

    def __lt__(self, other):
        return self.__actor_full_name < other.actor_full_name

    def __hash__(self):
        return hash(self.__actor_full_name)

    def add_actor_colleague(self, colleague):
        self.__actor_colleagues_set.append(colleague)

    def check_if_this_actor_worked_with(self, colleague):
        if colleague in self.__actor_colleagues_set:
            return True
        else:
            return False



class TestActorMethods:

    def test_init(self):
        actor1 = Actor("Angelina Jolie")
        assert repr(actor1) == "<Angelina Jolie>"
        actor2 = Actor("")
        assert actor2.actor_full_name is None
        actor3 = Actor(42)
        assert actor3.actor_full_name is None
