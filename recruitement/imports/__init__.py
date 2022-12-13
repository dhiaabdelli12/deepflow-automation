from asyncio.windows_events import NULL
from operator import index
from Google import Create_Service
from googleapiclient.http import MediaFileUpload, MediaIoBaseDownload
import pandas as pd
import requests
from google_drive_downloader import GoogleDriveDownloader as gdd
import io
import os
import gspread
import logging
import shutup
import time
import sys
import json
shutup.please()


CLIENT_SECRET_FILE = 'credentials.json'
API_NAME = 'drive'
API_VERSION = 'v3'
SCOPES = ['https://www.googleapis.com/auth/drive',
          'https://www.googleapis.com/auth/spreadsheets']

service, cred = Create_Service(
    CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)


root_folder_id = '1AEqhHxaHsv1VxrI-M307SgfFw3ywLWhV'


file = gspread.authorize(cred)

eval_sheet_id = '1QtP3cKSkqHaQgHlYP4JB2BZon6M9Im11tDPPphj-i2Y'

answers_sheet_id = '1OHVG9YdLnwKNA2qmSiBQj0X93CcQFFF_-5PIkDHkYSc'