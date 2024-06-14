from botasaurus_api import Api

# Create an instance of the API client
api = Api(create_response_files=False)
# Create an asynchronous task
data = {
    "link": "https://www.kainos.lt/veido-kremai/uriage-roseliane-riebus-veido-kremas-50-ml-v1123855",
}
task = api.create_sync_task(data, scraper_name="get_using_browser")
# Fetch the task
task = api.get_task(task["id"])
# Fetch the task results
results = api.get_task_results(task["id"])
print(results)

# Abort the task
# api.abort_task(task["id"])
# Delete the task
api.delete_task(task["id"])
# --- Bulk Operations ---
# Create multiple synchronous tasks
# data_items = [
#     {
#         "link": "https://www.omkar.cloud/",
#     },
#     {
#         "link": "https://www.omkar.cloud/",
#     },
# ]
# tasks = api.create_sync_tasks(data_items, scraper_name="get_using_request")
# # Fetch all tasks
# all_tasks = api.get_tasks()
# # Bulk abort tasks
# api.abort_tasks(*[task["id"] for task in tasks])
# # Bulk delete tasks
# api.delete_tasks(*[task["id"] for task in tasks])
