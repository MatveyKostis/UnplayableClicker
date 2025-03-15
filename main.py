from brython_easier import *

localstorage.set_storage("UnplayableClicker")
localstorage.get_or_create("score", 0)
localstorage.get_or_create("amount", 1)

shop_reject = [
    "Shop is useless here",
    "You can't buy anything there",
    "Don't press this button!",
    "This is useless button",
    "Stop clicking this button"
]

@timers.set_interval_decorator("seconds", 0.09)
def update_score():
    html.setText("#score", str(localstorage.get("score")))

@bind.bind(".click_button", "click")
def decrease_score(event):
    localstorage.set("score", localstorage.get("score") - localstorage.get("amount"))
    update_score()

@bind.bind(".get_into_store", "click")
def get_into_store(event):
    def return_back():
        html.setText(".get_into_store", "Get Into Store")
    html.setText(".get_into_store", f"{random.choice(shop_reject)}")
    timers.set_timeout_seconds(return_back, 3)