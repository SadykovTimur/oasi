from coms.qa.frontend.pages.component import Component, ComponentWrapper
from coms.qa.frontend.pages.component.button import Button
from coms.qa.frontend.pages.component.text import Text

__all__ = ['Menu']


class MenuWrapper(ComponentWrapper):
    item_functions = Component(xpath='//div[text()=" Госуслуги и функции "]')
    item_information = Button(xpath='//div[text()=" Информация "]')
    registry = Button(xpath='//div[text()=" Реестры "]')
    logo = Component(id="sidebar_logo")
    title = Text(id="sidebar_system-name")


class Menu(Component):
    def __get__(self, instance, owner) -> MenuWrapper:
        return MenuWrapper(instance.app, self.find(instance), self._locator)
