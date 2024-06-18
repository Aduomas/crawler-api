from botasaurus.browser import browser, Driver
from botasaurus.request import request, Request
import time


@request
def get_using_request(request: Request, data):
    response = request.get(data["link"])
    return response.text


@browser(
    cache=True,
    max_retry=5,  # Retry up to 5 times, which is a good default
    reuse_driver=True,  # Reuse the same driver for all tasks
    output=None,
    close_on_crash=True,
    raise_exception=True,
    create_error_logs=False,
)
def get_using_browser(driver: Driver, data):
    driver.google_get(data["link"], bypass_cloudflare=True)

    timeout = 10

    MESSAGE = "Tikriname jūsų naršyklę."
    elem = driver.get_element_containing_text(MESSAGE)
    while elem:
        time.sleep(1)
        elem = driver.get_element_containing_text(MESSAGE)
        timeout -= 1
        if timeout == 0:
            raise Exception("Timeout")

    return driver.page_html
