from plyer import notification
import time

while True:
    notification.notify(
        title="DRINK WATER",
        message="Please sip some water",
        timeout=3
    )
    time.sleep(60*60)