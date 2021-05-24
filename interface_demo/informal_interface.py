"""
    This module demonstrates about informal interfaces and their properties
    Key Take away:
    # 1. Abstract --> has only declaration not implementation
    # 2. isInstanceCheck
    # 3. Why Informal interface are not good for big projects
    # 4. Method resolution order(__mro__)
"""


class RemoteController:
    def power_on(self):
        pass

    def mute(self):
        pass

    def power_off(self):
        pass


class TVRemoteController(RemoteController):
    def power_on(self):
        print("power on for TV")

    def mute(self):
        print("Mute for TV")


class SetupBoxRemoteController(RemoteController):
    def power_on(self):
        print("power on for TV")

    def mute(self):
        print("Mute for TV")

    def power_off(self):
        print("power off for TV")


remote_controller = None;
choice = "tv"


def get_remote():
    if choice == "tv":
        return TVRemoteController();
    else:
        return SetupBoxRemoteController()


def main():
    abstract_cls_obj = RemoteController()
    tv_remote = TVRemoteController()
    setup_box_remote = SetupBoxRemoteController()
    """Note this tv remote didnt implemented power_off, but 
    informal interface will allow u to create object and it wont strictly check the type
    """
    print(issubclass(TVRemoteController,RemoteController)) # True
    print(issubclass(SetupBoxRemoteController,RemoteController)) # True
    remote = get_remote();
    remote.power_on()
    """This power off method not implemented in TV class.
    Hence it will refer from parent class, which has no implementation"""
    remote.power_off()

    """MRO tells tells you the superclasses of the class in question, 
    as well as the order in which they’re searched for executing a method
    """
    print(TVRemoteController.__mro__)

if __name__ == '__main__':
    main()
