
from PySide6.QtWidgets import QApplication
import sys
import addonmanager

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = addonmanager.AddonManager()
    w.show()
    sys.exit(app.exec())