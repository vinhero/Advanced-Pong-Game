class IGameObject:
    def __init__(self) -> None:
        """ Initialize this GameObject. """
        pass

    def update_actualPos(self) -> None:
        """ Updating the actual position this GameObject. """
        pass

    def update(self) -> None:
        """ Updating everything that has to do with rendering of this GameObject. """
        pass
