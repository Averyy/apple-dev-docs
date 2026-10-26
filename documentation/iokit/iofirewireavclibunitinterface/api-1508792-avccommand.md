# AVCCommand

**Framework**: IOKit  
**Kind**: structp  
**Role**: Instance Property

Sends an AVC command to the device and returns the response.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.2+

## Declaration

```c
IOReturn (*AVCCommand)(void *self, const UInt8 *command, UInt32 cmdLen, UInt8 *response, UInt32 *responseLen);
```

#### Discussion

This function will block until the device returns a response or the kernel driver times out.

## Parameters

- `self`: Pointer to IOFireWireAVCLibUnitInterface.
- `command`: Pointer to command to send.
- `cmdLen`: Length (in bytes) of command.
- `response`: Pointer to place to store the response sent by the device.
- `responseLen`: Pointer to place to store the length of the response.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iofirewireavclibunitinterface/1508792-avccommand)*