# GetBusFrameNumberWithTime

**Framework**: IOKit  
**Kind**: structp  
**Role**: Instance Property

Gets a recent frame number of the bus to which the device is attached, along with a system time corresponding to the start of that frame

**Availability**:
- Mac Catalyst 18.4+
- macOS 10.5+

## Declaration

```c
IOReturn (*GetBusFrameNumberWithTime)(void *self, UInt64 *frame, AbsoluteTime *atTime);
```

#### Return Value

Returns kIOReturnSuccess if successful, kIOReturnNoDevice if there is no connection to an IOService, or kIOReturnUnsupported is the bus doesn't support this function.

#### Discussion

The device does not have to be open to use this function.

## Parameters

- `self`: Pointer to the IOUSBDeviceInterface.
- `frame`: Pointer to UInt64 to hold the frame number.
- `atTime`: Pointer to a returned AbsoluteTime, which is the system time ("wall time") as close as possible to the beginning of that USB frame. The jitter on this value may be as much as 200 microseconds.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iousbdeviceinterface300/1559121-getbusframenumberwithtime)*