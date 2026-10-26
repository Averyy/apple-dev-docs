# SetPipePolicy

**Framework**: IOKit  
**Kind**: structp  
**Role**: Instance Property

Changes the amount of bandwidth of an isochronous pipe or interrupt pipe, or the polling interval of an interrupt pipe.

**Availability**:
- Mac Catalyst 18.4+
- macOS 10.2+

## Declaration

```c
IOReturn (*SetPipePolicy)(void *self, UInt8 pipeRef, UInt16 maxPacketSize, UInt8 maxInterval);
```

#### Return Value

Returns kIOReturnSuccess if successful, kIOReturnNoDevice if there is no connection to an IOService, or kIOReturnNotOpen if the interface is not open for exclusive access. May also return kIOReturnNoBandwidth if there is not enough bandwidth available on the bus, or kIOReturnBadArgument if the desired maxPacketSize is outside of the allowed range.

#### Discussion

A pipe may be made smaller or larger (up to the maxPacketSize specified in the endpoint descriptor). When an interface is first opened, all pipes are created with their descriptor-supplied maxPacketSize. For isochronous or interrupt pipes, if there is not enough bandwidth on the bus to allocate to the pipe, the pipe is created with a reserved bandwidth of zero. Any attempts to transfer data on a pipe with zero bandwidth will result in a kIOReturnNoBandwidth error. The pipe must first be given some bandwidth using this call. This can also be used to return bandwidth for an isochronous or an interrupt pipe. If the driver knows that the device will not be sending the maxPacketSize data, it can use this call to return that unused bandwidth to the system. If an interrupt pipe wants to change the polling interval, it can do so with this call.

The interface must be open for the pipe to exist.

## Parameters

- `self`: Pointer to the IOUSBInterfaceInterface.
- `pipeRef`: Index for the desired pipe (1 - GetNumEndpoints).
- `maxPacketSize`: The desired size for the isochronous or interrupt pipe. Valid values are 0 through the maxPacketSize defined in the endpoint descriptor.
- `maxInterval`: the desired polling interval in milliseconds, up to a maximum of 128 ms. The system can only poll devices powers of 2 (1, 2, 4, 8, 16, 32, 64, or 128 ms). A value of 0 is illegal.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iousbinterfaceinterface190/1558986-setpipepolicy)*