from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from webdriver_manager.firefox import GeckoDriverManager
from page_objects.basepage_lingoda import BasePage
from page_objects.basepage_lingoda import TestDataMVC
from page_objects.todomvc import TodoMvc
from selenium.webdriver.firefox.options import Options
options = Options()
options.headless = True
driver = webdriver.Firefox(executable_path=GeckoDriverManager().install(),options=options)
driver.get(TestDataMVC.base_url)
base_page = BasePage(driver=driver)


class Test_MVC:
    def test_homepage_title(self):
        self.TodoMvc = TodoMvc(driver=driver)
        """Check page title is correct"""
        title = self.TodoMvc.get_title(TestDataMVC.page_title)
        assert title == TestDataMVC.page_title

    def test_welcometext(self):
        self.TodoMvc = TodoMvc(driver=driver)
        """Check welcome text"""
        welcometext = self.TodoMvc.get_welcometext()
        assert welcometext == TestDataMVC.welcome_text

    def test_jstab(self):
        self.TodoMvc = TodoMvc(driver=driver)
        """Check javascript tab text is correct"""
        tabtext = self.TodoMvc.check_text_jstab()
        assert tabtext == TestDataMVC.tab_js_name
        self.TodoMvc.click_jstab()
        """Check polymer link is present & clickable"""
        flag = self.TodoMvc.check_polymer()
        assert flag
        self.TodoMvc.click_polymer()
        """Check when polymer link clicked user lands on correct url"""
        curr_url = driver.current_url
        assert curr_url == TestDataMVC.polymer_url

    def test_todo(self):
        self.TodoMvc = TodoMvc(driver=driver)
        """Create 1st todo item"""
        self.TodoMvc.todo_item1(TestDataMVC.firstitem)
        act = ActionChains(driver)
        act.send_keys(Keys.RETURN).perform()
        """Create 2nd todo item"""
        self.TodoMvc.todo_item2(TestDataMVC.seconditem)
        act = ActionChains(driver)
        act.send_keys(Keys.RETURN).perform()
        """Edit 2nd todo item"""
        act.double_click(driver.find_element_by_css_selector(".td-todos:nth-of-type(2) div")).perform()
        self.TodoMvc.todo_changeitem2(TestDataMVC.appendtext)
        act.send_keys(Keys.RETURN).perform()
        """Check edited 2nd todo item is correct"""
        newsecondtodo = self.TodoMvc.check_newseconditem()
        assert newsecondtodo == TestDataMVC.newseconditem

        driver.quit()
