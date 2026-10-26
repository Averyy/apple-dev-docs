# ControlRequestTO

**Framework**: IOKit  
**Kind**: structp  
**Role**: Instance Property

Sends a USB request on a control pipe.

**Availability**:
- Mac Catalyst 18.4+
- macOS 10.1+

## Declaration

```c
IOReturn (*ControlRequestTO)(void *self, UInt8 pipeRef, IOUSBDevRequestTO *req);
```

#### Discussion

The IOUSBDevRequestTO structure allows the client to specify timeout values for this request. If the request is a standard request which will change the state of the device, the device must be open, which means you should be using the IOUSBDeviceInterface for this command.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iousbinterfaceinterface182/1558963-controlrequestto)*