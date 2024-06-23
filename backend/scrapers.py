from botasaurus_server.server import Server
from botasaurus_server.sorts import Sort
from src.scrape_heading_task import scrape_heading_task
from src.scrape_tasks import get_using_request, get_using_browser
from dotenv import load_dotenv
import os

load_dotenv()
# Add the scraper to the server
# Server.add_scraper(scrape_heading_task)
Server.add_scraper(get_using_request)
Server.add_scraper(get_using_browser, sorts=[Sort("link")])

DATABASE_URL = os.getenv("DATABASE_URL")

Server.set_database_url(DATABASE_URL)
Server.set_rate_limit(browser=2)
