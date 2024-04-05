from __future__ import annotations

from coms.qa.core.helpers import wait_for
from coms.qa.frontend.pages import Page
from coms.qa.frontend.pages.component import Component
from selenium.common.exceptions import NoSuchElementException

from dit.qa.pages.components.header import Header
from dit.qa.pages.main_page.components.content import Content
from dit.qa.pages.start_page.components.auth_form import AuthForm

__all__ = ['StartPage']


class StartPage(Page):
    header = Header(id="overlay-data")
    footer = Component(css='[class*="page-footer"]')
    auth_form = AuthForm(class_name="overlay-login")
    skeleton_content = Content(id="skeleton_content")

    def wait_for_loading(self) -> None:
        def condition() -> bool:
            try:
                assert self.header.logo.visible
                assert self.header.title == "Правительство Москвы"
                assert self.header.login.visible

                return self.footer.visible

            except NoSuchElementException:

                return False

        self.app.set_implicitly_wait(1)
        wait_for(condition, msg='Page was not loaded')
        self.app.restore_implicitly_wait()

    def wait_for_loading_after_logout(self) -> None:
        def condition() -> bool:
            try:
                assert self.header.logo.visible
                assert self.header.title == "Правительство Москвы"
                assert self.header.come_page == "Войти как госслужащий"
                assert self.header.login_page == "Другие способы входа"

                return self.footer.visible

            except NoSuchElementException:

                return False

        self.app.set_implicitly_wait(1)
        wait_for(condition, msg='Page was not loaded')
        self.app.restore_implicitly_wait()
