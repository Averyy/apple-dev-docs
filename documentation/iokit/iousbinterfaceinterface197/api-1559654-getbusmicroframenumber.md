# GetBusMicroFrameNumber

**Framework**: IOKit  
**Kind**: structp  
**Role**: Instance Property

Gets the current micro frame number of the bus to which the interface and its device are attached.

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

The interface does not have to be open to use this function.

## Parameters

- `self`: Pointer to the IOUSBInterfaceInterface.
- `microFrame`: Pointer to UInt64 to hold the microrame number.
- `atTime`: Pointer to an AbsoluteTime, which should be within 1ms of the time when the bus frame number was attained.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iousbinterfaceinterface197/1559654-getbusmicroframenumber)*