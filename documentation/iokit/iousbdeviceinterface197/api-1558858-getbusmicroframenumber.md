# GetBusMicroFrameNumber

**Framework**: IOKit  
**Kind**: structp  
**Role**: Instance Property

Gets the current micro frame number of the bus to which the device is attached.

**Availability**:
- Mac Catalyst 18.4+
- macOS 10.2+

## Declaration

```c
IOReturn (*GetBusMicroFrameNumber)(void *self, UInt64 *microFrame, AbsoluteTime *atTime);
```

## Return Value

Returns kIOReturnSuccess if successful, kIOReturnNoDevice if there is no connection to an IOService.

## Discussion

The device does not have to be open to use this function.

## Parameters

- `self`: Pointer to the IOUSBDeviceInterface.
- `microFrame`: Pointer to UInt64 to hold the microframe number.
- `atTime`: Pointer to an AbsoluteTime, which should be within 1ms of the time when the bus frame number was acquired.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iousbdeviceinterface197/1558858-getbusmicroframenumber)*