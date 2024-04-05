from coms.qa.frontend.pages.component import Component, ComponentWrapper
from coms.qa.frontend.pages.component.button import Button

__all__ = ['Header']


class HeaderWrapper(ComponentWrapper):
    exit = Button(xpath="//a[text()=' Выйти ']")
    menu = Component(id="nav-header")
    user_info = Component(xpath='//a[text()=" Фоми Функциональный Мониторинг "]')


class Header(Component):
    def __get__(self, instance, owner) -> HeaderWrapper:
        return HeaderWrapper(instance.app, self.find(instance), self._locator)
