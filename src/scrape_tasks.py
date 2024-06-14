from botasaurus.browser import browser, Driver
from botasaurus.request import request, Request


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

    MESSAGE = "Tikriname jūsų naršyklę."

    # Wait for the page to load

    return driver.page_html
