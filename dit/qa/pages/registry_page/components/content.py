from coms.qa.frontend.pages.component import Component, Components, ComponentWrapper
from coms.qa.frontend.pages.component.text import Text

__all__ = ['Content']


class ContentWrapper(ComponentWrapper):
    title = Text(xpath="//h3[text()=' Реестры  ']")
    all_registry = Text(xpath="//h4[text()=' Всего реестров — 36 ']")
    table_grid = Components(css='[role*="gridcell"]')
    grid_container = Components(css='[class*="btn btn-default"] ')


class Content(Component):
    def __get__(self, instance, owner) -> ContentWrapper:
        return ContentWrapper(instance.app, self.find(instance), self._locator)
