# GetBandwidthAvailable

**Framework**: IOKit  
**Kind**: structp  
**Role**: Instance Property

Returns the amount of bandwidth available on the bus for allocation to isochronous pipes. If the device is a high speed device, it will be the number of bytes per microframe (125 µsecs). If it is a full speed device, it will be the number of bytes per frame (1ms)

**Availability**:
- Mac Catalyst 18.4+
- macOS 10.2+

## Declaration

```c
IOReturn (*GetBandwidthAvailable)(void *self, UInt32 *bandwidth);
```

#### Return Value

Returns kIOReturnSuccess if successful, kIOReturnNoDevice if there is no connection to an IOService.

#### Discussion

This function is useful for determining the correct AltInterface setting as well as for using SetPipePolicy.

The interface does not have to be open to use this function.

## Parameters

- `self`: Pointer to the IOUSBInterfaceInterface.
- `bandwidth`: Pointer to UInt32 to hold the amount of bandwidth available (in bytes per 1ms frame).


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iousbinterfaceinterface190/1559414-getbandwidthavailable)*