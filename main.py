import requests
import sys
import re
import mbox
import webbrowser

URL = 'https://www.cisco.com/c/en/us/support/collaboration-endpoints/spark-room-kit-series/products-command-reference-list.html'
MBOX_TITLE = 'Cisco API Notifier'

def main(driver_version=11.1):
    # Validate provided parameter
    if not isinstance(driver_version, float):
        raise ValueError('Invalid driver_version parameter specified')

    # Send request and attempt to get webpage text
    response = requests.get(URL)
    code = response.status_code  # get HTTP status code
    if code == 200:  # if successful
        page_text = response.text
    elif code >= 400 and code < 600:  # if error
        text = 'Error {0} {1}'.format(code, response.reason)  # get HTTP error reason
        mbox.show(title=MBOX_TITLE, text=text, button='OK', icon='ICONERROR')  # report error to user
        sys.exit()  # exit program

    # Parse webpage text and find all RoomOS API versions (if any)
    regex = re.compile('API Reference Guide \(RoomOS ([0-9]+\.[0-9]+)\)')
    versions = sorted(set(re.findall(regex, page_text)))
    if not versions:
        text = 'No RoomOS versions found'
        mbox.show(title=MBOX_TITLE, text=text, button='OK', icon='ICONERROR')
        sys.exit()

    # Check for new version and show message box
    version = float(versions.pop())  # last item is latest version
    if version > driver_version:  # if new version found
        text = 'New RoomOS {} API found'.format(version)
        btn_select = mbox.show(title=MBOX_TITLE, text=text, button='OKCANCEL', icon='ICONINFORMATION')
        if btn_select == 'OK':  # if OK button selected
            webbrowser.open(URL)  # open API webpage
    else:
        text = 'No new RoomOS API\'s found'
        mbox.show(title=MBOX_TITLE, text=text, button='OK', icon='ICONINFORMATION')

if __name__ == '__main__':
    main(driver_version=11.5)  # current driver version
