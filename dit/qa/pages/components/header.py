from coms.qa.frontend.pages.component import Component, ComponentWrapper
from coms.qa.frontend.pages.component.button import Button
from coms.qa.frontend.pages.component.text import Text

__all__ = ['Header']


class HeaderWrapper(ComponentWrapper):
    logo = Component(css='[class*="page__logo"]')
    title = Text(xpath="//h1[text()='Правительство Москвы']")
    login = Button(css='[class*="title_login"]')
    exit = Button(xpath="//a[text()=' Выйти '] ")
    come_page = Text(xpath="//span[text()='Войти как госслужащий']")
    login_page = Text(xpath="//span[text()='Другие способы входа']")


class Header(Component):
    def __get__(self, instance, owner) -> HeaderWrapper:
        return HeaderWrapper(instance.app, self.find(instance), self._locator)
