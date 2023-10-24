# capstone_nfc
Project for Capstone Design

# NFC-Based Face Detection and Server Communication with Raspberry Pi

This project demonstrates how to use a Raspberry Pi along with an NFC module and a camera to detect users' faces when an NFC card is detected and communicate the data with a server. It serves as a basic framework that can be extended and customized for specific use cases.

## Prerequisites

- Raspberry Pi (e.g., Raspberry Pi 3, Raspberry Pi 4)
- NFC module compatible with Raspberry Pi (e.g., PN532 or RC522)
- A USB camera
- Python 3 installed on your Raspberry Pi
- [nfcpy](https://github.com/nfcpy/nfcpy) library for NFC communication
- [OpenCV](https://pypi.org/project/opencv-python/) library for face detection
- Internet connectivity (Wi-Fi or Ethernet)

## Installation

1. **Install nfcpy:**

   Install the nfcpy library by running the following command:

   ```bash
   pip install nfcpy


Install OpenCV:

Install OpenCV using pip:

pip install opencv-python


Hardware Setup:

Connect the NFC module to your Raspberry Pi according to the manufacturer's instructions.
Attach a compatible USB camera to your Raspberry Pi.
Face Detection Model:


