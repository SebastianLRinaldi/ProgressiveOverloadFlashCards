import os
import sys
import time
import re

import threading
from threading import Thread
from enum import Enum
from queue import Queue
from typing import List
from datetime import timedelta


from PyQt6.QtCore import *
from PyQt6.QtWidgets import * 
from PyQt6.QtGui import *

from PyQt6.QtNetwork import QNetworkAccessManager, QNetworkRequest, QNetworkReply
from FrontEnd.E_GroupBuilds.TabGroupBuilds import *
from G_WindowBuild.windowBuild import *


def run_pyqt(win):
    
    window.setup_central_widget(
        exploreTab,
    )
    window.show_window()
      


    