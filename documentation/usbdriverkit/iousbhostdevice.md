# IOUSBHostDevice

**Framework**: USBDriverKit  
**Kind**: class

A provider object that represents the USB device.

**Availability**:
- DriverKit 19.0+

## Declaration

```swift
class IOUSBHostDevice;
```

#### Overview

An [`IOUSBHostDevice`](iousbhostdevice.md) object represents a USB device connected to the user’s Mac. Use this object to retrieve the device’s configuration descriptor and capabilities. You can also iterate over the interfaces that the device uses to communicate.

Typically, you don’t create [`IOUSBHostDevice`](iousbhostdevice.md) objects directly. Instead, the system creates one during the matching process for the USB device and passes it as the provider object to your custom driver.

To use a host device object, call [`Open`](iousbhostdevice/open.md) to create a new session between the device and your driver. After successfully opening your session, you can request information from the device, fetch descriptors, and iterate over the available interfaces. Remember to close the session you opened in the [`Stop`](https://developer.apple.com/documentation/kernel/ioservice/3180713-stop) method of your driver.

## Topics

### Managing the Device Session
- [Open](iousbhostdevice/open.md)
  Opens a session to a host device.
- [Close](iousbhostdevice/close.md)
  Closes the session to the host device.
- [Reset](iousbhostdevice/reset.md)
  Terminates the device and attempts to reenumerate it.
### Getting the Device Descriptors
- [CopyCapabilityDescriptors](iousbhostdevice/copycapabilitydescriptors.md)
  Returns the device’s capability descriptors.
- [CopyConfigurationDescriptor](iousbhostdevice/copyconfigurationdescriptor-lej1.md)
  Returns the configuration descriptor with the specified index.
- [CopyConfigurationDescriptor](iousbhostdevice/copyconfigurationdescriptor-6qgew.md)
  Returns the currently selected configuration descriptor.
- [CopyConfigurationDescriptorWithValue](iousbhostdevice/copyconfigurationdescriptorwithvalue.md)
  Returns the configuration descriptor with the specified configuration value.
- [CopyDeviceDescriptor](iousbhostdevice/copydevicedescriptor.md)
  Returns the device descriptor.
- [CopyStringDescriptor](iousbhostdevice/copystringdescriptor-28ybo.md)
  Returns a string descriptor from the device.
- [CopyStringDescriptor](iousbhostdevice/copystringdescriptor-9h8l2.md)
  Returns a string descriptor from the device.
- [CopyDescriptor](iousbhostdevice/copydescriptor.md)
  Retrieves any type of descriptor from the cache or the device.
- [tIOUSBDeviceRequestTypeValue](tiousbdevicerequesttypevalue.md)
  Constants indicating the type of request to make from a device.
- [tIOUSBDeviceRequestRecipientValue](tiousbdevicerequestrecipientvalue.md)
  Constants indicating the type of object that receives the results of a request.
- [Descriptor Utilities](descriptor-utilities.md)
  Iterate over the descriptors of a USB device and fetch specific values.
### Disposing of Descriptors
- [IOUSBHostFreeDescriptor](iousbhostfreedescriptor-2hkne.md)
  Releases the specified device descriptor.
- [IOUSBHostFreeDescriptor](iousbhostfreedescriptor-2r7k.md)
  Releases the specified configuration descriptor.
- [IOUSBHostFreeDescriptor](iousbhostfreedescriptor-5j4pp.md)
  Releases the specified BOS descriptor.
- [IOUSBHostFreeDescriptor](iousbhostfreedescriptor-3fve6.md)
  Releases the specified string descriptor.
### Requesting Information from the Device
- [DeviceRequest](iousbhostdevice/devicerequest.md)
  Sends a synchronous request to the device on the default control endpoint.
- [AsyncDeviceRequest](iousbhostdevice/asyncdevicerequest.md)
  Enqueues a request on the default control endpoint of the device.
- [CompleteAsyncDeviceRequest](iousbhostdevice/completeasyncdevicerequest.md)
  The type definition for an asynchronous device request completion routine.
- [AbortDeviceRequests](iousbhostdevice/abortdevicerequests.md)
  Aborts device requests that you made previously from the current device client.
### Creating Memory Buffers
- [CreateIOBuffer](iousbhostdevice/createiobuffer.md)
  Allocates a buffer for use during I/O operations.
### Iterating Over the Device Interfaces
- [CreateInterfaceIterator](iousbhostdevice/createinterfaceiterator.md)
  Creates an iterator to get the list of interfaces from the device.
- [CopyInterface](iousbhostdevice/copyinterface.md)
  Gets the next host interface child associated with this device.
- [DestroyInterfaceIterator](iousbhostdevice/destroyinterfaceiterator.md)
  Destroys an interface iterator that you created.
### Getting Device Information
- [GetAddress](iousbhostdevice/getaddress.md)
  Returns the address of the device.
- [GetSpeed](iousbhostdevice/getspeed.md)
  Retrieves the device’s operational speed.
- [GetFrameNumber](iousbhostdevice/getframenumber.md)
  Gets the current frame number of the USB controller.
- [GetPortStatus](iousbhostdevice/getportstatus.md)
  Returns the current port status of the device.
- [tIOUSBHostConnectionSpeed](tiousbhostconnectionspeed.md)
  Constants indicating the connection speed of the device.
- [tIOUSBHostPortStatus](tiousbhostportstatus.md)
  Constants indicating the state of a port.
- [tIOUSBHostPortType](tiousbhostporttype.md)
  Constants indicating a port’s type.
### Configuring the Device
- [SetConfiguration](iousbhostdevice/setconfiguration.md)
  Selects a new configuration for the device.

## Relationships

### Inherits From
- [IOService](../DriverKit/IOService.md)

## See Also

- [IOUSBHostInterface](iousbhostinterface.md)
  A provider object that manages interactions with an interface of the USB device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usbdriverkit/iousbhostdevice)*