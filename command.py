from abc import ABC, abstractmethod

class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

class LightOnCommand(Command):
    def __init__(self, light):
        self.light = light

    def execute(self):
        self.light.on()

class LightOffCommand(Command):
    def __init__(self, light):
        self.light = light

    def execute(self):
        self.light.off()

class RemoteController:
    def __init__(self):
        self.controller = None
        self.last_commands = list()

    def add_controller(self, controller):
        self.controller = controller

    def command_list(self):
        return self.last_commands

    def run(self):
        self.last_commands.append(self.controller)
        return self.controller.execute()

    def back(self):
        self.last_commands.pop()
        if self.last_commands:
            self.controller = self.last_commands[::-1][0]
            return self.controller.execute()
        return None

class Light:

    def on(self):
        print('ON')

    def off(self):
        print('OFF')


l = Light()
l_on = LightOnCommand(l)
l_off = LightOffCommand(l)
r_controller = RemoteController()
r_controller.add_controller(l_on)
r_controller.run()
r_controller.add_controller(l_off)
r_controller.run()
print(r_controller.command_list())
r_controller.back()
