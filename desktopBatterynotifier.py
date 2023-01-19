import psutil
from plyer import notification
import time

while (True):
    battery = psutil.sensors_battery()
    percentage = battery.percent

    notification.notify(
        title="Battery Percentage",
        message=str(percentage) + "% Battery remaining",
        timeout=10
    )

    time.sleep(60 * 60)

    continue