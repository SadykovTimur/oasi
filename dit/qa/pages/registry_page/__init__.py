from __future__ import annotations

from coms.qa.core.helpers import wait_for
from coms.qa.frontend.pages import Page
from coms.qa.frontend.pages.component import Component, Components
from coms.qa.frontend.pages.component.button import Button
from selenium.common.exceptions import NoSuchElementException

from dit.qa.pages.main_page.components.header import Header
from dit.qa.pages.main_page.components.menu import Menu

__all__ = ['RegistryPage']


class RegistryPage(Page):
    header = Header(tag='cdp-navbar')
    sidebar = Menu(tag='cdp-sidebar')
    favorites = Button(xpath='//button[text()=" Избранные "]')
    all = Component(xpath='//button[text()=" Все "]')
    title = Component(xpath="//h3[text()=' Реестры  ']")
    all_registry = Component(xpath="//h4[contains(text(),' Всего реестров')]")
    table_grid = Components(xpath='//div[@role="gridcell"]/ancestor::div[1]')

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
                assert self.sidebar.registry.visible

                assert self.title.visible
                assert self.favorites.visible
                assert self.all.visible
                assert self.all_registry.visible

                return self.table_grid[0].visible

            except NoSuchElementException:

                return False

        self.app.set_implicitly_wait(1)
        wait_for(condition, msg='Page was not loaded')
        self.app.restore_implicitly_wait()
