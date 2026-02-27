import webdriver_manager
from webdriver_manager.chrome import ChromeDriverManager
print('webdriver-manager version', webdriver_manager.__version__)

# instantiate manager and inspect last known version
driver = ChromeDriverManager()
print('cache path', driver.cache_path)

# show available versions maybe
try:
    print('latest version from manager:', driver.driver.get_version())
except Exception as e:
    print('error getting version', e)
