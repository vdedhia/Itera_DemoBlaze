from selenium.webdriver.common.by import By

Menu_Bar = {
    'Home': (By.XPATH, '/html/body/nav/div[1]/ul/li[1]/a'),
    'Contact': (By.XPATH, '/html/body/nav/div[1]/ul/li[2]/a'),
    'About_Us': (By.XPATH, '/html/body/nav/div[1]/ul/li[3]/a'),
    'Cart': (By.XPATH, '/html/body/nav/div[1]/ul/li[4]/a'),
    'Login_In': (By.XPATH, '/html/body/nav/div[1]/ul/li[5]/a'),
    'Sign_Up': (By.XPATH, '/html/body/nav/div[1]/ul/li[8]/a')
}