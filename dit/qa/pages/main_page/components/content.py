from coms.qa.frontend.pages.component import Component, ComponentWrapper
from coms.qa.frontend.pages.component.button import Button
from coms.qa.frontend.pages.component.text import Text

__all__ = ['Content']


class ContentWrapper(ComponentWrapper):
    title = Text(xpath="//h3[text()='  Здравствуйте, Функциональный Мониторинг! '] ")
    information_text = Text(xpath="//h4[text()=' Информационные системы  ']")
    user_info = Text(xpath="//h4[text()=' Быстрые ссылки  ']")
    news = Text(xpath="//h4[text()=' Новости  ']")
    registry = Text(xpath="//h4[text()=' Реестров в избранном —  ']")
    favorites = Text(xpath="//h4[text()=' Возможностей в избранном — 0 ']")
    support = Component(class_name="support")
    exit = Button(xpath="//a[text()=' Выйти ']")


class Content(Component):
    def __get__(self, instance, owner) -> ContentWrapper:
        return ContentWrapper(instance.app, self.find(instance), self._locator)
