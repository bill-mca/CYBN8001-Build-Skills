# Tutorial: Development on the Arduino board ESP32S3-Sense

As per the Arduino website:
> Arduino is an open-source electronics platform based on easy-to-use hardware and software. It's intended for anyone making interactive projects.

The ESP32S3-Sense is built by Seeed Studio an IoT hardware company from China. Despite its miniature form factor, as can be seen below, the Sense is designed for the collection of multimedia and streaming over wifi. 

![The ESP32S3-Sense](https://files.seeedstudio.com/wiki/SeeedStudio-XIAO-ESP32S3/img/xiaoesp32s3sense.jpg)

![front interfaces](https://files.seeedstudio.com/wiki/SeeedStudio-XIAO-ESP32S3/img/front-indication.png)

<!---

![rear interfaces](https://files.seeedstudio.com/wiki/SeeedStudio-XIAO-ESP32S3/img/back-indication.png)

![pins](https://files.seeedstudio.com/wiki/SeeedStudio-XIAO-ESP32S3/img/2.jpg)

--->

## Setup Arduino IDE in Linux 🐧 

Arduino offers two IDEs one is a legacy IDE (versions <2) and is more stable. The other is more feature rich and has a nicer interface. For complex programs on the Xiao ESP32S3 you'll need the more recent versions of the IDE.

 2. Download the App-Image of the 64-bit IDE for Linux from [here](https://www.arduino.cc/en/software)
 3. Move the downloaded app-image somewhere. You could put it on the desktop.
 4. Make your AppImage executable: `chmod u+x arduino.AppImage`
 5. Run the arduino appimage ./arduino.AppImage
 6. You might need to install fuse if the AppImage won't run: `sudo apt install libfuse2`
 7. Confirm that the program boots.
 8. Plug in your esp32s3 so that it registers that there is an arduino plugged in. Leave it plugged so that we can edit the port permissions in the next step. Confirm that it has assigned the port `ttyACM0` to your Arduino, then shut the IDE down. We need to run some more commands.
 9. to ensure that your user account has permision to access serial devices, you'll need to add yourself to the dialout group. Run the following command to achieve that `sudo usermod -a -G dialout <your username>`
 10. Make the arduino's serial port writable by everyone by running the following command `sudo chmod a+rw /dev/ttyACM0`
 11. Restart the computer.
 12. Open the Arduino IDE.


## Setup the serial connection to your ESP board 🤖

Once you have confirmed that the program will boot you still have to setup the IDE to work with the ESP32S3.

 1. To get the latest versions of the ESP32 software, go to preferences in the Arduino IDE and past the following URL into the "Additional Boards Manager URLs" field [https://raw.githubusercontent.com/espressif/arduino-esp32/gh-pages/package_esp32_index.json](https://raw.githubusercontent.com/espressif/arduino-esp32/gh-pages/package_esp32_index.json) ![https://files.seeedstudio.com/wiki/SeeedStudio-XIAO-ESP32S3/img/6.png](https://files.seeedstudio.com/wiki/SeeedStudio-XIAO-ESP32S3/img/6.png)
 3. Then enter the board manager and install the latest version of the ESP32 software by Espressif Systems once it has installed correctly you'll see the `remove` button next to it as shown below. ![https://files.seeedstudio.com/wiki/SeeedStudio-XIAO-ESP32S3/img/9.png](https://files.seeedstudio.com/wiki/SeeedStudio-XIAO-ESP32S3/img/9.png)
 5. Once that has installed,you've got all the libraries and dependencies that you would need to compile software for ESP32 boards. You've also got protocols for communicating with these devices over serial.
 6. The next step is to select a protocol and establish serial communication with a device. Plug your ESP32S3 into the comuper via a data-enabled USB-C cable. You should see it available in the drop down menu that has the USB icon.
 7. If you open the IDE's seial monitor you should now see something there... or at least a blank screen 🤷 Try uplugging and re-plugging the device with the monitor open. When it isn't connected, you'll get an orange message here that says so.

## Flash your first programs ⚡

Getting the habit of easily flashing programs is where you take off in Arduino development.

 1. In the file menu, there's an example section. Under 'digital' open the button program.
 2. Confirm that your board is connected and selected.
 3. Press the upload button (it is a right arrow) and watch to see if it successfully compiles and flashes.
 4. once it is finished, you may need to press reset on the ESP32S3.
 5. Success.
 6. Open the "CameraWebServer" sketch from `examples > ESP32 > Camera`
 7. Notice that this is a more complicated sketch with many iles in a folder.
 8. Enable prasm from the tools menu
 9. Flash this sketch to the board

## Tips 🤹

 - Arduino works as 'sketches'. These are compiled into binaries and flashed onto the memory of the board.
 - The default programming language for ESP32S3 boards is much the same as C++

## Troubleshooting 👻

 - Learn to recognise the difference between compilation and communication issues. Understanding the error messages is a big step towards developing this skill. be Prepared to study and learn properly.
 - First, always check that you have the right board and port selected.
 - Make sure you are using a valid sketch. You can grab snippets of code from the internet and paste them into a file, but, unless that file is saved in a folder with a few C++ header files and a `partitions.csv` file, it won't successfully compile into a binary.
 - If you get communication errors, try putting your ESP32 into bootloader mode and flashing a simple program to it.
