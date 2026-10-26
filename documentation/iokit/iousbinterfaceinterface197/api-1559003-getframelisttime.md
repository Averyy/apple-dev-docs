# GetFrameListTime

**Framework**: IOKit  
**Kind**: structp  
**Role**: Instance Property

Returns the number of microseconds in each USB Frame.

**Availability**:
- Mac Catalyst 18.4+
- macOS 10.2+

## Declaration

```c
IOReturn (*GetFrameListTime)(void *self, UInt32 *microsecondsInFrame);
```

#### Return Value

Returns kIOReturnSuccess if successful, kIOReturnNoDevice if there is no connection to an IOService.

#### Discussion

This function can be used to determine whether the device is functioning in full speed or a high speed. In the case of a full speed device, the returned value will be kUSBFullSpeedMicrosecondsInFrame. In the case of a high speed device, the return value will be kUSBHighSpeedMicrosecondsInFrame. (This API should really be called GetUSBFrameTime).

The interface does not have to be open to use this function.

## Parameters

- `self`: Pointer to the IOUSBInterfaceInterface.
- `microsecondsInFrame`: Pointer to UInt32 to hold the number of microseconds in each USB frame.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iousbinterfaceinterface197/1559003-getframelisttime)*