from selenium.webdriver.common.by import By
from page_objects.basepage_lingoda import BasePage


class TodoMvc(BasePage):
    WELCOMETEXT = (By.XPATH, "/html/body/div[2]/header/div[1]/p")
    TABJS = (By.CSS_SELECTOR, "[data-target='js'] .center-center")
    POLYMER = (By.XPATH, "/html/body/div[2]/div[1]/div[2]/iron-pages/div[1]/ul/li[8]/a")
    TODOBOX = (By.ID, "new-todo")
    TODOITEM2 = (By.CSS_SELECTOR, ".td-todos:nth-of-type(2) div")
    TODOITEM2EDIT = (By.XPATH, "/html//input[@id='edit']")

    def __init__(self, driver):
        super().__init__(driver)

    def get_page_title(self, title):
        return self.get_title(title)

    def get_welcometext(self):
        return self.get_element_text(self.WELCOMETEXT)

    def click_jstab(self):
        self.do_click(self.TABJS)

    def check_text_jstab(self):
        return self.get_element_text(self.TABJS)

    def check_polymer(self):
        return self.is_visible(self.POLYMER)

    def click_polymer(self):
        self.do_click(self.POLYMER)

    def todo_item1(self, firstitem):
        self.do_click(self.TODOBOX)
        self.do_send_keys(self.TODOBOX, firstitem)

    def todo_item2(self, seconditem):
        self.do_click(self.TODOBOX)
        self.do_send_keys(self.TODOBOX, seconditem)

    def changetodo(self, newitem):
        self.do_send_keys(self.TODOITEM2, newitem)

    def todo_changeitem2(self, appendtext):
        self.do_send_keys(self.TODOITEM2EDIT, appendtext)

    def check_newseconditem(self):
        return self.get_element_text(self.TODOITEM2)
