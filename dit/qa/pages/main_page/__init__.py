from __future__ import annotations

from coms.qa.core.helpers import wait_for
from coms.qa.frontend.pages import Page
from coms.qa.frontend.pages.component import Component
from coms.qa.frontend.pages.component.button import Button
from selenium.common.exceptions import NoSuchElementException

from dit.qa.pages.main_page.components.header import Header
from dit.qa.pages.main_page.components.menu import Menu

__all__ = ['MainPage']


class MainPage(Page):
    header = Header(tag='cdp-navbar')
    sidebar = Menu(tag='cdp-sidebar')
    title = Component(xpath="//h3[text()='  Здравствуйте, Функциональный Мониторинг! '] ")
    information_text = Component(xpath="//h4[text()=' Информационные системы  ']")
    user_info = Component(xpath="//h4[text()=' Быстрые ссылки  ']")
    news = Component(xpath="//h4[text()=' Новости  ']")
    registry = Component(xpath="//h4[text()=' Реестров в избранном —  ']")
    favorites = Component(xpath="//h4[text()=' Возможностей в избранном — 0 ']")
    support = Component(class_name="support")
    exit = Button(xpath="//a[text()=' Выйти ']")

    def wait_for_loading(self) -> None:
        def condition() -> bool:
            try:
                assert self.header.menu.visible
                assert self.header.user_info.visible
                assert self.header.exit.visible

                assert self.sidebar.logo.visible
                assert self.sidebar.title == 'Правительство Москвы'
                assert self.sidebar.item_functions.visible
                assert self.sidebar.item_information.visible

                assert self.title.visible
                assert self.information_text.visible
                assert self.user_info.visible
                assert self.news.visible
                assert self.registry.visible
                assert self.favorites.visible

                return self.support.visible

            except NoSuchElementException:

                return False

        self.app.set_implicitly_wait(1)
        wait_for(condition, msg='Page was not loaded')
        self.app.restore_implicitly_wait()
