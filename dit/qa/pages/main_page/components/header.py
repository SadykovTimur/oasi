from coms.qa.frontend.pages.component import Component, ComponentWrapper
from coms.qa.frontend.pages.component.text import Text

__all__ = ['Header']


class HeaderWrapper(ComponentWrapper):
    logo = Component(id="sidebar_logo")
    title = Text(id="sidebar_system-name")


class Header(Component):
    def __get__(self, instance, owner) -> HeaderWrapper:
        return HeaderWrapper(instance.app, self.find(instance), self._locator)
