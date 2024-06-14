from botasaurus.browser import browser, Driver
from botasaurus.request import request, Request


@request
def get_using_request(request: Request, data):
    response = request.get(data["link"])
    return response.text


@browser()
def get_using_browser(driver: Driver, data):
    driver.google_get(data["link"])
    return driver.page_html
