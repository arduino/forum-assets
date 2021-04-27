The loop-back test is a troubleshooting procedure to determine if serial communication between the PC and Arduino board is working in a typical Arduino installation. The test proves that the host computer, hardware driver, USB cable, and USB to serial converter are all working.

Loop-Back Test Instructions...

1. Disconnect power from the board

2. Remove all connections and shields from the board

3. Force the processor to remain in reset by connecting a jumper from RESET to GND

4. Connect a jumper from the TX pin (Digital Pin 1) to the RX pin (Digital Pin 0)

5. Connect the board to your computer. After a brief pause Windows will produce a device-insertion tone if sound is enabled. Linux may or may not produce a device-insertion tone; an entry is added to the system log.

6. Start your favourite terminal application. Serial Monitor will work fine.

7. Connect the terminal application to the serial port for your board. The baud rate is irrelevant.

8. Send data by typing. Everything you type should be echoed back. To send data, some terminal applications, like Serial Monitor, require pressing the Enter key or clicking a Send button. If exactly what you send is echoed back then the board passes the test. This means that the host computer hardware driver, USB cable, and USB to serial converter are all working.

9. Shutdown the terminal application

10. Disconnect the board from the computer

11. Remove the two jumpers

Please post comments and suggestions about these instructions here...
https://forum.arduino.cc/t/loop-back-test-sticky/67080
