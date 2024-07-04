import sys
from Application import Application
from MainWindow import MainWindow
from login import LoginPassword
from registration import Registration


app = Application(sys.argv)


auth = LoginPassword()


if not auth.exec() and auth.status is True:
    print(True)
    main_window = MainWindow()
    main_window.show()
else:
    print(False)
    reg = Registration()
    reg.show()

app.exec()
