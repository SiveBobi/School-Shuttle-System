from abc import ABC, abstractmethod

# Product Interfaces
class Button(ABC):
    @abstractmethod
    def render(self):
        pass

class Checkbox(ABC):
    @abstractmethod
    def render(self):
        pass

# Concrete Products
class WindowsButton(Button):
    def render(self):
        return "Windows Button Rendered"

class MacOSButton(Button):
    def render(self):
        return "MacOS Button Rendered"

class WindowsCheckbox(Checkbox):
    def render(self):
        return "Windows Checkbox Rendered"

class MacOSCheckbox(Checkbox):
    def render(self):
        return "MacOS Checkbox Rendered"

# Factory Interface
class GUIFactory(ABC):
    @abstractmethod
    def create_button(self):
        pass

    @abstractmethod
    def create_checkbox(self):
        pass

# Concrete Factories
class WindowsFactory(GUIFactory):
    def create_button(self):
        return WindowsButton()

    def create_checkbox(self):
        return WindowsCheckbox()

class MacOSFactory(GUIFactory):
    def create_button(self):
        return MacOSButton()

    def create_checkbox(self):
        return MacOSCheckbox()
