import requests
import sys
import re
import mbox
import webbrowser

DRIVER_VERSION = 11.9
URL = 'https://www.cisco.com/c/en/us/support/collaboration-endpoints/spark-room-kit-series/products-command-reference-list.html'
MBOX_TITLE = 'Cisco API Notifier'

def main():
    # Validate driver version
    if not isinstance(DRIVER_VERSION, float):
        show_error('Invalid driver version')

    # Send request and attempt to get webpage text
    response = requests.get(URL)
    code = response.status_code
    if code == 200:  # if successful
        page_text = response.text
    elif code >= 400 and code < 600:  # if error
        show_error(f'Error {code} {response.reason}')

    # Parse webpage text and find all RoomOS API versions (if any)
    regex = re.compile('API Reference Guide \(RoomOS ([0-9]+\.[0-9]+)\)')
    versions = sorted(set(re.findall(regex, page_text)))
    if not versions:
        show_error('No RoomOS versions found')

    # Check for new version and show message box
    version = float(versions.pop())  # last item is latest version
    if version > DRIVER_VERSION:  # if new version found
        btn_select = mbox.show(title=MBOX_TITLE, text=f'New RoomOS {version} API found', button='OKCANCEL')
        if btn_select == 'OK':  # if OK button selected
            webbrowser.open(URL)  # open API webpage
    else:
        text = 'No new RoomOS API\'s found'
        mbox.show(title=MBOX_TITLE, text=text)

def show_error(text):
    mbox.show(title=MBOX_TITLE, text=text, icon='ICONERROR')  # report error to user
    sys.exit()  # exit program

if __name__ == '__main__':
    main()
