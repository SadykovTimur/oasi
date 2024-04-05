from __future__ import annotations

from coms.qa.core.helpers import wait_for
from coms.qa.frontend.pages import Page
from coms.qa.frontend.pages.component.button import Button
from selenium.common.exceptions import NoSuchElementException

from dit.qa.pages.main_page.components.header import Header
from dit.qa.pages.main_page.components.menu import Menu
from dit.qa.pages.registry_page.components.content import Content

__all__ = ['RegistryPage']


class RegistryPage(Page):
    sidebar_header = Header(id="sidebar_header")
    sidebar_menu = Menu(id="sidebar_menu")
    skeleton_content = Content(id="skeleton_content")
    favorites_bnt = Button(css='[class*="swiper-slide-next"]')

    def wait_for_loading(self) -> None:
        def condition() -> bool:
            try:
                assert self.sidebar_header.logo.visible
                assert self.sidebar_header.title == 'Правительство Москвы'

                assert self.sidebar_menu.item_functions == 'Госуслуги и функции'
                assert self.sidebar_menu.item_information.visible

                assert self.skeleton_content.title == 'Реестры'
                assert self.skeleton_content.all_registry == 'Всего реестров — 36'

                return self.skeleton_content.table_grid[0].visible

            except NoSuchElementException:

                return False

        self.app.set_implicitly_wait(1)
        wait_for(condition, msg='Page was not loaded')
        self.app.restore_implicitly_wait()

    def wait_for_loading_table_favorites(self) -> None:
        def condition() -> bool:
            try:
                assert self.sidebar_header.logo.visible
                assert self.sidebar_header.title == 'Правительство Москвы'

                assert self.sidebar_menu.item_functions == 'Госуслуги и функции'
                assert self.sidebar_menu.item_information.visible

                return self.skeleton_content.grid_container[0].visible

            except NoSuchElementException:

                return False

        self.app.set_implicitly_wait(1)
        wait_for(condition, msg='Page was not loaded')
        self.app.restore_implicitly_wait()
