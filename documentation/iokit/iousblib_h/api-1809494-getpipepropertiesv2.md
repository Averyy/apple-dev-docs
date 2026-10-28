# GetPipePropertiesV2

**Framework**: IOKit  
**Kind**: func

Gets the properties for a pipe, including the USB SuperSpeed endpoint companion properties.

## Declaration

```c
IOReturn ( *GetPipePropertiesV2)(
   void *self,
   UInt8 pipeRef,
   UInt8 *direction,
   UInt8 *number,
   UInt8 *transferType,
   UInt16 *maxPacketSize,
   UInt8 *interval,
   UInt8 *maxBurst,
   UInt8 *mult,
   UInt16 *bytesPerInterval);
```

## Return Value

Returns kIOReturnSuccess if successful, kIOReturnNoDevice if there is no connection to an IOService, or kIOReturnNotOpen if the interface is not open for exclusive access.

## Overview

Once an interface is opened, all of the pipes in that interface get created by the kernel. The number of pipes can be retrieved by GetNumEndpoints. The client can then get the properties of any pipe using an index of 1 to GetNumEndpoints. Pipe 0 is the default control pipe in the device.

## Parameters

- `self`: Pointer to the IOUSBInterfaceInterface.
- `pipeRef`: Index for the desired pipe (1 - GetNumEndpoints).
- `direction`: Pointer to an UInt8 to get the direction of the pipe.
- `number`: Pointer to an UInt8 to get the pipe number.
- `transferType`: Pointer to an UInt8 to get the transfer type of the pipe.
- `maxPacketSize`: Pointer to an UInt16 to get the maxPacketSize of the pipe.
- `interval`: Pointer to an UInt8 to get the interval for polling the pipe for data (in milliseconds).
- `maxBurst`: Pointer to an UInt8 to get the bMaxBurst value of the SuperSpeed Endpoint Companion descriptor
- `mult`: Pointer to an UInt8 to get the mult value of the bmAttributes field of the SuperSpeed Endpoint Companion descriptor, valid only for an isochronous endpoint
- `bytesPerInterval`: Pointer to an UInt16 to get the wBytesPerInterval value of the SuperSpeed Endpoint Companion descriptor, valid only for periodic endpoints

## See Also

### Miscellaneous
- [FindNextAltInterface](./api-1809466-findnextaltinterface.md)
- [FindNextAssociatedDescriptor](./api-1809475-findnextassociateddescriptor.md)
  Find the next descriptor of the requested type associated with the interface.
- [GetBusFrameNumberWithTime](./api-1809485-getbusframenumberwithtime.md)
  Gets a recent frame number of the bus to which the device is attached, along with a system time corresponding to the start of that frame


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iousblib_h/1809494-getpipepropertiesv2)*