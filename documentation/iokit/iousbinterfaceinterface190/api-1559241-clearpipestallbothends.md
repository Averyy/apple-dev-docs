# ClearPipeStallBothEnds

**Framework**: IOKit  
**Kind**: structp  
**Role**: Instance Property

Equivalent to ClearPipeStall.

**Availability**:
- Mac Catalyst 18.4+
- macOS 10.2+

## Declaration

```c
IOReturn (*ClearPipeStallBothEnds)(void *self, UInt8 pipeRef);
```

#### Return Value

Returns kIOReturnSuccess if successful, kIOReturnNoDevice if there is no connection to an IOService, or kIOReturnNotOpen if the interface is not open for exclusive access.

#### Discussion

This function is equivalent to ClearPipeStall except that it also attempts to clear the halt and toggle bits on the device's endpoint for the pipe by sending a ClearFeature(ENDPOINT_HALT) to the default control pipe in the device, specifying the endpoint for the pipe represented by pipeRef. For most devices, this resynchronizes the data toggle between the two endpoints to ensure that there is no loss of data.

## Parameters

- `self`: Pointer to the IOUSBInterfaceInterface.
- `pipeRef`: Index for the desired pipe (1 - GetNumEndpoints).


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iousbinterfaceinterface190/1559241-clearpipestallbothends)*