# close

**Framework**: IOKit  
**Kind**: structp  
**Role**: Instance Property

Closes the task's connection to the IOHIDDevice.

**Availability**:
- Mac Catalyst 18.4+
- macOS 10.5+

## Declaration

```c
IOReturn (*close)(void *self, IOOptionBits options);
```

#### Return Value

Returns kIOReturnSuccess if successful, kIOReturnNoDevice if there is no connection to an IOService.

#### Discussion

Releases the client's access to the IOHIDDevice.

## Parameters

- `self`: Pointer to the IOHIDDeviceDeviceInterface.
- `options`: Option bits to be passed down to the user client.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iohiddevicedeviceinterface/1395719-close)*