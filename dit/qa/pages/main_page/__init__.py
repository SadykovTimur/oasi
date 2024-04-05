from __future__ import annotations

from coms.qa.core.helpers import wait_for
from coms.qa.frontend.pages import Page
from selenium.common.exceptions import NoSuchElementException

from dit.qa.pages.main_page.components.content import Content
from dit.qa.pages.main_page.components.header import Header
from dit.qa.pages.main_page.components.menu import Menu

__all__ = ['MainPage']


class MainPage(Page):
    sidebar_header = Header(id="sidebar_header")
    sidebar_menu = Menu(id="sidebar_menu")
    skeleton_content = Content(id="skeleton_content")

    def wait_for_loading(self) -> None:
        def condition() -> bool:
            try:
                assert self.sidebar_header.logo.visible
                assert self.sidebar_header.title == 'Правительство Москвы'

                assert self.sidebar_menu.item_functions == 'Госуслуги и функции'
                assert self.sidebar_menu.item_information.visible

                assert self.skeleton_content.title == 'Здравствуйте, Функциональный Мониторинг!'
                assert self.skeleton_content.information_text == 'Информационные системы'
                assert self.skeleton_content.user_info == 'Быстрые ссылки'
                assert self.skeleton_content.news == 'Новости'
                assert self.skeleton_content.registry == 'Реестров в избранном —'
                assert self.skeleton_content.favorites == 'Возможностей в избранном — 0'

                return self.skeleton_content.support.visible

            except NoSuchElementException:

                return False

        self.app.set_implicitly_wait(1)
        wait_for(condition, msg='Page was not loaded')
        self.app.restore_implicitly_wait()
