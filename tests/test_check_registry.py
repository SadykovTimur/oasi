from typing import Callable

import allure
import pytest
from _pytest.fixtures import FixtureRequest
from coms.qa.fixtures.application import Application
from coms.qa.frontend.constants import CLIENT_BROWSERS, CLIENT_DEVICE_TYPE

from tests.steps import open_auth_form, open_main_page, open_registry_page, open_start_page, sign_in


@allure.label('owner', 't.sadykov')
@allure.label('component', 'DIT')
@allure.epic('OASI')
@allure.story('Переход на элемент навигатора "Реестры"')
@allure.title('Проверка доступности элемента навигатора "Реестры"')
@allure.severity(allure.severity_level.BLOCKER)
@pytest.mark.parametrize('browser', CLIENT_BROWSERS)
@pytest.mark.parametrize('device_type', CLIENT_DEVICE_TYPE)
def test_check_registry(
    request: FixtureRequest, make_app: Callable[..., Application], browser: str, device_type: str
) -> None:

    app = make_app(browser, device_type)

    open_start_page(app)
    open_auth_form(app)

    sign_in(app, request.config.option.username, request.config.option.password)
    open_main_page(app)

    open_registry_page(app)
