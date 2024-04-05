import allure
from coms.qa.fixtures.application import Application
from coms.qa.frontend.helpers.attach_helper import screenshot_attach
from selenium.common.exceptions import NoSuchElementException

from dit.qa.pages.main_page import MainPage
from dit.qa.pages.registry_page import RegistryPage
from dit.qa.pages.start_page import StartPage

__all__ = ['open_start_page', 'open_auth_form', 'sign_in', 'logout', 'open_registry_page', 'open_main_page']


def open_start_page(app: Application) -> None:
    with allure.step('Opening Start page'):
        try:
            page = StartPage(app)
            page.open()
            page.wait_for_loading()

            screenshot_attach(app, 'start_page')
        except Exception as e:
            screenshot_attach(app, 'start_page_error')

            raise TimeoutError('Start page was not loaded') from e


def open_auth_form(app: Application) -> None:
    with allure.step('Opening Auth form'):
        try:
            page = StartPage(app)
            page.login.click()
            page.auth_form.wait_for_loading()

            screenshot_attach(app, 'auth_form')
        except Exception as e:
            screenshot_attach(app, 'auth_form_error')

            raise TimeoutError('Auth form was not loaded') from e


def sign_in(app: Application, login: str, password: str) -> None:
    with allure.step(f'{login} signing in'):
        try:
            auth_form = StartPage(app).auth_form

            auth_form.login.send_keys(login)
            auth_form.password.send_keys(password)

            screenshot_attach(app, 'auth_data')
        except Exception as e:
            screenshot_attach(app, 'auth_data_error')

            raise NoSuchElementException('Entering data exception') from e

        auth_form.submit.click()


def open_main_page(app: Application) -> None:
    with allure.step('Opening Main page'):
        try:
            MainPage(app).wait_for_loading()

            screenshot_attach(app, 'main_page')
        except Exception as e:
            screenshot_attach(app, 'main_page_error')

            raise TimeoutError('Main page was not loaded') from e


def open_registry_page(app: Application) -> None:
    with allure.step('Opening Registry page'):
        try:
            page = MainPage(app)
            page.sidebar.item_information.click()
            page.sidebar.registry.click()

            RegistryPage(app).wait_for_loading()

            screenshot_attach(app, 'registry_page')
        except Exception as e:
            screenshot_attach(app, 'registry_error')

            raise TimeoutError('Registry page was not loaded') from e


def logout(app: Application) -> None:
    with allure.step('Logging out'):
        try:
            MainPage(app).exit.click()

            StartPage(app).wait_for_loading_after_logout()

            screenshot_attach(app, 'logout_page')
        except Exception as e:
            screenshot_attach(app, 'logout_page_error')

            raise TimeoutError('Logout page was not loaded') from e
