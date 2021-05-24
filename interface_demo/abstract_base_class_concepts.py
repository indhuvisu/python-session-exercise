from abc import ABCMeta, abstractmethod

"""
    This module demonstrates about formal interfaces and their properties
    Key Take away:
    # 1. Abstract --> has only declaration not implementation
    # 2. __subclasshook__ method to override instance equality check
    # 3. @abstractmethod - a decorator to enforce the 
    implementation of base class method in child
    # 4. class.register() to leverage the strict check
"""


class RemoteController(metaclass=ABCMeta):
    @classmethod
    def __subclasshook__(cls, subclass):
        return (hasattr(subclass, 'power_on') and
                callable(subclass.power_on) and
                hasattr(subclass, 'mute') and
                callable(subclass.mute) and
                hasattr(subclass, 'power_off') and
                callable(subclass.power_off) or
                NotImplemented)


# Note I have not used in class def (Remotecontroller) to inherit.
"""Uncomment below line to leverage is subclass check"""


# @RemoteController.register
class TVRemoteController:
    def power_on(self):
        print("power on for TV")

    def mute(self):
        print("Mute for TV")


class SetupBoxRemoteController:
    def power_on(self):
        print("power on for TV")

    def mute(self):
        print("Mute for TV")

    def power_off(self):
        print("power off for TV")

    def switch_mode(self, choice):
        pass


remote_controller = None;
choice = "tv"


def get_remote():
    if choice == "tv":
        return TVRemoteController();
    else:
        return SetupBoxRemoteController()


"""Lets strictly enforce validation"""


class Shape(metaclass=ABCMeta):
    @abstractmethod
    def draw(self):
        pass


class Circle(Shape):
    def draw(self):
        print("circle draw done")


class Triangle(Shape):
    pass


def main():
    print(issubclass(TVRemoteController, RemoteController))
    print(issubclass(SetupBoxRemoteController, RemoteController))
    remote = get_remote();
    remote.power_on()
    """below line will raise exception.since power off not implemented in subclass tv"""
    # remote.power_off()

    """MRO tells tells you the superclasses of the class in question, 
    as well as the order in which they’re searched for executing a method
    Note: After defining formal interface, Remotecontroller becomes virtual base class
    which is not included in the hierarchy"""
    print(TVRemoteController.__mro__)

    """This line will raise exception, 
    Since triangle failed to implement method draw"""
   # triangle = Triangle()
   # triangle.draw()


if __name__ == '__main__':
    main()
