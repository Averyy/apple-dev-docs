# ControlRequestAsyncTO

**Framework**: IOKit  
**Kind**: structp  
**Role**: Instance Property

Sends an asynchronous USB request on a control pipe.

**Availability**:
- Mac Catalyst 18.4+
- macOS 10.1+

## Declaration

```c
IOReturn (*ControlRequestAsyncTO)(void *self, UInt8 pipeRef, IOUSBDevRequestTO *req, IOAsyncCallback1 callback, void *refCon);
```

#### Discussion

The IOUSBDevRequestTO structure allows the client to specify timeout values for this request. Use pipeRef=0 for the default device control pipe. If the request is a standard request which will change the state of the device, the device must be open, which means you should be using the IOUSBDeviceInterface for this command.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iousbinterfaceinterface182/1559506-controlrequestasyncto)*