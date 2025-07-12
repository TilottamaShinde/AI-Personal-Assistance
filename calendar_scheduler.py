import os
import datetime
from calendar import calendar

from dotenv import load_dotenv
from google.auth.environment_vars import CREDENTIALS
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow

load_dotenv()

SCOPES = ['https://www.googleapis.com/auth/calender']
CREDENTIALS_FILE = 'credentials.json'

def get_calender_service():
    flow = InstalledAppFlow.from_client_secrets_file(CREDENTIALS_FILE, SCOPES)
    creds = flow.run_local_server(port = 0)
    return build('calender', 'v3', credentials = creds)

def schedule_event(event_description):
    try:
        now = datetime.datetime.utcnow()
        start_time = (now + datetime.timedelta(days=1)).isoformat() + 'Z'
        end_time = (now +datetime.timedelta(days = 1)).isformat() + 'Z'

        event = {
            'summary':event_description,
            'start':{'dateTime':start_time, 'timeZone':'Asia/Kolkata'},
            'end':{'dateTime':end_time, 'timeZone':'Asia/Kolkata'}
        }

        service = get_calender_service()
        event = service.events().insert(calendarID='primary', body = event).execute()
        return f"Event Created: {event.get('htmlLink')}"
    except Exception as e:
        return f"Failed to schedule event: {str(e)}"
