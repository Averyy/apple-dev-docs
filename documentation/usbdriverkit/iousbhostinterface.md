# IOUSBHostInterface

**Framework**: USBDriverKit  
**Kind**: class

A provider object that manages interactions with an interface of the USB device.

**Availability**:
- DriverKit 19.0+

## Declaration

```swift
class IOUSBHostInterface;
```

#### Overview

An [`IOUSBHostInterface`](iousbhostinterface.md) object represents one of the interfaces the USB device supports. When implementing a custom driver, use an [`IOUSBHostInterface`](iousbhostinterface.md) object to get information about the specific interface and to communicate with the device using that interface.

Typically, you don’t create [`IOUSBHostInterface`](iousbhostinterface.md) objects directly. During configuration of your driver, you can specify that your driver relies on an [`IOUSBHostInterface`](iousbhostinterface.md) as its provider, in which case the system creates the object for you automatically during the matching process. Alternatively, if your driver uses an [`IOUSBHostDevice`](iousbhostdevice.md) object as its provider, you can iterate over all of the device’s interfaces to retrieve the specific [`IOUSBHostInterface`](iousbhostinterface.md) object you need.

To use a host interface object, call [`Open`](iousbhostinterface/open.md) to create a new session between the interface and your driver. After successfully opening your session, you can request information from the interface and set up pipes to communicate with the interface’s endpoints. Remember to close the session you opened in the [`Stop`](https://developer.apple.com/documentation/DriverKit/IOService/Stop) method of your driver.

## Topics

### Managing the Device Session
- [Open](iousbhostinterface/open.md)
  Opens a session to the host interface.
- [Close](iousbhostinterface/close.md)
  Closes the session to the host interface.
### Getting Interface-Related Descriptors
- [CopyConfigurationDescriptor](iousbhostinterface/copyconfigurationdescriptor.md)
  Retrieves the parent configuration descriptor for this interface.
- [GetInterfaceDescriptor](iousbhostinterface/getinterfacedescriptor.md)
  Returns the version of the interface descriptor that is associated with the specified configuration.
- [CopyStringDescriptor](iousbhostinterface/copystringdescriptor-83du1.md)
  Returns a descriptor from the device in the specified language.
- [CopyStringDescriptor](iousbhostinterface/copystringdescriptor-8k65j.md)
  Returns a string descriptor from the device.
### Getting an Endpoint Pipe
- [CopyPipe](iousbhostinterface/copypipe.md)
  Returns the pipe for the specified endpoint address.
### Getting the Device
- [CopyDevice](iousbhostinterface/copydevice.md)
  Returns the host device object that contains this interface.
### Requesting Data from the Default Control Endpoint
- [DeviceRequest](iousbhostinterface/devicerequest.md)
  Sends a synchronous request to the device on the default control endpoint.
- [AsyncDeviceRequest](iousbhostinterface/asyncdevicerequest.md)
  Enqueues a request on the default control endpoint of the device.
- [AbortDeviceRequests](iousbhostinterface/abortdevicerequests.md)
  Aborts device requests that you made previously from the current interface client.
### Configuring the Interface
- [GetFrameNumber](iousbhostinterface/getframenumber.md)
  Gets the current frame number of the USB controller.
- [GetPortStatus](iousbhostinterface/getportstatus.md)
  Gets the current port status.
- [SelectAlternateSetting](iousbhostinterface/selectalternatesetting.md)
  Selects an alternative setting for this interface.
- [GetIdlePolicy](iousbhostinterface/getidlepolicy.md)
  Gets the current idle suspend timeout for the interface.
- [SetIdlePolicy](iousbhostinterface/setidlepolicy.md)
  Sets the desired idle suspend timeout for the interface.
- [tIOUSBHostPortStatus](tiousbhostportstatus.md)
  Constants indicating the state of a port.
### Creating Memory Buffers
- [CreateIOBuffer](iousbhostinterface/createiobuffer.md)
  Allocates a buffer for use during I/O operations.
### Instance Methods
- [CurrentMicroframe](iousbhostinterface/currentmicroframe.md)
- [ReferenceMicroframe](iousbhostinterface/referencemicroframe.md)

## Relationships

### Inherits From
- [IOService](../DriverKit/IOService.md)

## See Also

- [IOUSBHostDevice](iousbhostdevice.md)
  A provider object that represents the USB device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usbdriverkit/iousbhostinterface)*