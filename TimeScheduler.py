from win10toast import  ToastNotifier
import time
time.sleep(10)
notifier = ToastNotifier()
notifier.show_toast("One Hour Completed!", "Now Take a Walk!", duration = 25)