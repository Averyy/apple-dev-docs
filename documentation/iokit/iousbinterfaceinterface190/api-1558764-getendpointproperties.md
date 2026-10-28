# GetEndpointProperties

**Framework**: IOKit  
**Kind**: structp  
**Role**: Instance Property

Returns the transfer type, max packet size, and interval of a specified endpoint, whether or not the endpoint has a pipe currently established.

**Availability**:
- Mac Catalyst 18.4+
- macOS 10.2+

## Declaration

```c
IOReturn (*GetEndpointProperties)(void *self, UInt8 alternateSetting, UInt8 endpointNumber, UInt8 direction, UInt8 *transferType, UInt16 *maxPacketSize, UInt8 *interval);
```

## Return Value

Returns kIOReturnSuccess if successful, kIOReturnNoDevice if there is no connection to an IOService.

## Discussion

This function may be useful for determining which alternate interface to select when trying to balance bandwidth allocations among isochronous pipes.

The interface does not have to be open to use this function.

## Parameters

- `self`: Pointer to the IOUSBInterfaceInterface.
- `alternateSetting`: Specifies the alternate setting within the current interface.
- `endpointNumber`: Specifies the desired endpoint number.
- `direction`: Specifies the desired direction.
- `transferType`: Pointer to UInt8 to hold the endpoint's transfer type (kUSBControl, kUSBIsoc, etc).
- `maxPacketSize`: Pointer to UInt16 to hold the maxPacketSize of the endpoint.
- `interval`: Pointer to UInt8 to hold the polling interval for interrupt endpoints.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iousbinterfaceinterface190/1558764-getendpointproperties)*