# Cisco API Notifier

# Overview
This project was created to automate a work task of mine to ensure our [Extron](https://www.extron.com/) device drivers for [Cisco](https://www.cisco.com/) video conferencing systems stay up-to-date with the latest API documentation. This is done by executing a script file on a weekly basis, via Windows Task Scheduler, to search the following Cisco [API reference page](https://www.cisco.com/c/en/us/support/collaboration-endpoints/spark-room-kit-series/products-command-reference-list.html) to see if new documentation is available by comparing the latest API version found to the version the current driver uses. This project serves as a substitute for not be able to receive API update notifications directly from Cisco since both a customer account and a paid subscription are required for these services.

# Description
A simple web scraper in Python used to automatically check and notify a user if new documentation is available from a specific webpage.

# Usage
Upon running the script file, one of the following message boxes will appear:

#### If new API documentation found:
![New RoomOS API found](images/New%20RoomOS%20API%20found.png)
- This means new API documentation was found and the current driver should be updated.
- Selecting the **OK** button will open the [API reference page](https://www.cisco.com/c/en/us/support/collaboration-endpoints/spark-room-kit-series/products-command-reference-list.html), selecting **Cancel** will terminate the program.

#### If no new API documentation found:
![No new RoomOS API's found](images/No%20new%20RoomOS%20API's%20found.png)
- This means the current driver is using the latest API documentation and no action is required.
- Selecting the **OK** button will terminate the program.

#### If no API documentation found:
![No RoomOS versions found](images/No%20RoomOS%20versions%20found.png)
- This means no API documentation was found on the page at all.
- Selecting the **OK** button will terminate the program.

#### If driver version is invalid:
![Invalid driver version](images/Invalid%20driver%20version.png)
- This means the driver version provided is invalid (must be float type).
- Selecting the **OK** button will terminate the program.

#### If webpage is unreachable:
![Error 404 Not Found](images/Error%20404%20Not%20Found.png)
- This message will vary depending on which specific HTTP error occurred.
- Selecting the **OK** button will terminate the program.

# Dependencies
- Python 3.6 or above
- requests 2.31.0
- Windows

# License
Licensed under the [MIT License](LICENSE)