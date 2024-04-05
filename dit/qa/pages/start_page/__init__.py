from __future__ import annotations

from coms.qa.core.helpers import wait_for
from coms.qa.frontend.pages import Page
from coms.qa.frontend.pages.component import Component
from coms.qa.frontend.pages.component.button import Button
from coms.qa.frontend.pages.component.text import Text
from selenium.common.exceptions import NoSuchElementException

from dit.qa.pages.start_page.components.auth_form import AuthForm

__all__ = ['StartPage']


class StartPage(Page):
    footer = Component(css='[class*="page-footer"]')
    auth_form = AuthForm(class_name="overlay-login")
    logo = Component(css='[class*="page__logo"]')
    title = Text(class_name='login-page__title')
    login = Button(css='[class*="title_login"]')
    exit = Button(xpath="//a[text()=' Выйти '] ")
    come_page = Component(xpath="//span[text()='Войти как госслужащий']")
    login_page = Component(xpath="//span[text()='Другие способы входа']")

    def wait_for_loading(self) -> None:
        def condition() -> bool:
            try:
                assert self.logo.visible
                assert self.title == "Правительство Москвы"
                assert self.login.visible

                return self.footer.visible

            except NoSuchElementException:

                return False

        self.app.set_implicitly_wait(1)
        wait_for(condition, msg='Page was not loaded')
        self.app.restore_implicitly_wait()

    def wait_for_loading_after_logout(self) -> None:
        def condition() -> bool:
            try:
                assert self.logo.visible
                assert self.title == "Правительство Москвы"
                assert self.come_page.visible
                assert self.login_page.visible

                return self.footer.visible

            except NoSuchElementException:

                return False

        self.app.set_implicitly_wait(1)
        wait_for(condition, msg='Page was not loaded')
        self.app.restore_implicitly_wait()
