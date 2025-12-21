# IOUSBHostPipe

**Framework**: USBDriverKit  
**Kind**: class

An object you use to transfer data to or from a USB endpoint.

**Availability**:
- DriverKit 19.0+

## Declaration

```swift
class IOUSBHostPipe;
```

#### Overview

Use an [`IOUSBHostPipe`](iousbhostpipe.md) object to manage data transfers to and from a device. A pipe represents a one-way data conduit between your driver and one of the device’s USB endpoints. You use pipes to perform synchronous, asynchronous, or isochronous data transfers between your code and the device.

Don’t create an [`IOUSBHostPipe`](iousbhostpipe.md) object directly. To retrieve a pipe for a specific endpoint, call the [`CopyPipe`](iousbhostinterface/copypipe.md) method of [`IOUSBHostInterface`](iousbhostinterface.md). You can get the addresses for the device’s pipes from the endpoint descriptors associated with each device interface.

## Topics

### Interacting with Bulk and Interrupt Endpoints
- [IO](iousbhostpipe/io.md)
  Performs a synchronous request on a bulk or interrupt endpoint.
- [AsyncIO](iousbhostpipe/asyncio.md)
  Enqueues an asynchronous request on a bulk or interrupt endpoint.
- [CompleteAsyncIO](iousbhostpipe/completeasyncio.md)
  Handles the completion of an asynchronous I/O request.
### Interacting with Isochronous Endpoints
- [IsochIO](iousbhostpipe/isochio.md)
  Performs a synchronous or asynchronous request on an isochronous endpoint.
- [CompleteAsyncIsochIO](iousbhostpipe/completeasyncisochio.md)
  Handles the completion of an asynchronous request.
- [IOUSBIsochronousFrame](iousbisochronousframe.md)
  A structure representing a single frame in an isochronous transfer.
### Interacting with Descriptor Rings
- [CreateMemoryDescriptorRing](IOUSBHostPipe/CreateMemoryDescriptorRing.md)
- [SetMemoryDescriptor](IOUSBHostPipe/SetMemoryDescriptor.md)
- [AsyncIOBundled](iousbhostpipe/asynciobundled.md)
  Enqueues a contiguous group of requests from the descriptor ring.
- [CompleteAsyncIOBundled](iousbhostpipe/completeasynciobundled.md)
  Handles the completion of an asynchronous bundled transfer.
- [Bundling Constants](bundling_constants-enum.md)
  Constants associated with bulk I/O transfers.
### Aborting I/O Requests
- [Abort](iousbhostpipe/abort.md)
  Aborts all of the pipe’s pending I/O requests.
- [IOUSBAbortOptions](iousbabortoptions.md)
  Options to use when aborting an I/O request.
### Adjusting the Pipe’s Status
- [AdjustPipe](iousbhostpipe/adjustpipe.md)
  Adjusts the behavior of periodic endpoints to consume a different amount of bus bandwidth.
- [ClearStall](iousbhostpipe/clearstall.md)
  Clears the halt condition of the pipe.
### Getting the Endpoint Descriptors
- [GetDescriptors](iousbhostpipe/getdescriptors.md)
  Retrieves the endpoint descriptors associated with this pipe.
- [IOUSBStandardEndpointDescriptors](iousbstandardendpointdescriptors.md)
  Encapsulates the descriptors for a single endpoint.
- [IOUSBGetEndpointDescriptorOptions](iousbgetendpointdescriptoroptions.md)
  Options for fetching the endpoint descriptors of a pipe.
### Managing the Pipe’s Idle Policy
- [GetIdlePolicy](iousbhostpipe/getidlepolicy.md)
  Retrieves the pipe’s current idle timeout.
- [SetIdlePolicy](iousbhostpipe/setidlepolicy.md)
  Sets the pipe’s desired idle timeout.
### Getting the Device Attributes
- [GetSpeed](iousbhostpipe/getspeed.md)
  Retrieves the device’s operational speed.
- [GetDeviceAddress](iousbhostpipe/getdeviceaddress.md)
  Retrieves the address of the device.
- [tIOUSBHostConnectionSpeed](tiousbhostconnectionspeed.md)
  Constants indicating the connection speed of the device.
### Instance Methods
- [CreateMemoryDescriptorRing](iousbhostpipe/creatememorydescriptorring.md)
- [SetMemoryDescriptor](iousbhostpipe/setmemorydescriptor.md)

## Relationships

### Inherits From
- [OSObject](../DriverKit/OSObject.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/usbdriverkit/iousbhostpipe)*