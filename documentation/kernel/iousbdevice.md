# IOUSBDevice

**Framework**: Kernel  
**Kind**: cl  
**Role**: Class

An input/output service object that represents a device on the USB bus.

**Availability**:
- macOS 10.0+ - Deprecated in 10.10

> **Deprecated**: Use [`IOUSBHostDevice`](./iousbhostdevice.md) instead.

## Declaration

```cpp
class IOUSBDevice : IOService
```

## Overview

Use this class to configure a device and create [`IOUSBInterface`](./iousbinterface.md) objects that represent the interfaces of the device.

## Topics

### Miscellaneous
- [CreateInterfaceIterator](./iousbdevice/api-1810047-createinterfaceiterator.md)
- [DeviceRequest(IOUSBDevRequest *, UInt32, UInt32, IOUSBCompletion *)](./iousbdevice/api-1810072-devicerequest.md)
  execute a control request to the default control pipe (pipe zero)
- [DeviceRequest(IOUSBDevRequestDesc *, UInt32, UInt32, IOUSBCompletion *)](./iousbdevice/api-1810098-devicerequest.md)
  execute a control request to the default control pipe (pipe zero)
- [DisplayUserNotification](./iousbdevice/api-1810124-displayusernotification.md)
  Will use the Notification Center to display a notification to the user. Only Low Power and Overcurrent notifications are supported.
- [DoLocationOverrideAndModelMatch](./iousbdevice/api-1810151-dolocationoverrideandmodelmatch.md)
  Will look for a kOverrideIfAtLocationID array proerty with locationID entries and a "MacModel" property. If any of the locationIDs match to the Mac Model, will return true. If there is no kOverrideAtLocationID property, it will also return true.
- [FindNextInterface](./iousbdevice/api-1810185-findnextinterface.md)
- [FindNextInterfaceDescriptor](./iousbdevice/api-1810212-findnextinterfacedescriptor.md)
- [GetAddress](./iousbdevice/api-1810231-getaddress.md)
- [GetBus](./iousbdevice/api-1810263-getbus.md)
- [GetBusPowerAvailable](./iousbdevice/api-1810284-getbuspoweravailable.md)
- [GetChildLocationID](./iousbdevice/api-1810305-getchildlocationid.md)
- [GetConfiguration](./iousbdevice/api-1810333-getconfiguration.md)
- [GetConfigurationDescriptor](./iousbdevice/api-1810384-getconfigurationdescriptor.md)
- [GetDeviceInformation](./iousbdevice/api-1810425-getdeviceinformation.md)
  Returns status information about the USB device, such as whether the device is captive or whether it is in the suspended state.
- [GetDeviceRelease](./iousbdevice/api-1810457-getdevicerelease.md)
- [GetDeviceStatus](./iousbdevice/api-1810482-getdevicestatus.md)
- [GetExtraPowerAllocated](./iousbdevice/api-1810520-getextrapowerallocated.md)
  Clients can use this API to ask how much extra power has already been reserved by this device. Units are milliAmps (mA).
- [GetFullConfigurationDescriptor](./iousbdevice/api-1810553-getfullconfigurationdescriptor.md)
- [GetHubParent](./iousbdevice/api-1810591-gethubparent.md)
  Used by the hub driver to give the nub a pointer to its HubPolicyMaker object
- [GetManufacturerStringIndex](./iousbdevice/api-1810637-getmanufacturerstringindex.md)
- [GetMaxPacketSize](./iousbdevice/api-1810681-getmaxpacketsize.md)
- [GetNumConfigurations](./iousbdevice/api-1810710-getnumconfigurations.md)
- [GetPipeZero](./iousbdevice/api-1810748-getpipezero.md)
- [GetProductID](./iousbdevice/api-1810809-getproductid.md)
- [GetProductStringIndex](./iousbdevice/api-1810867-getproductstringindex.md)
- [GetSerialNumberStringIndex](./iousbdevice/api-1810912-getserialnumberstringindex.md)
- [GetSpeed](./iousbdevice/api-1810998-getspeed.md)
- [GetStringDescriptor](./iousbdevice/api-1811033-getstringdescriptor.md)
- [GetVendorID](./iousbdevice/api-1811065-getvendorid.md)
- [MakePipe](./iousbdevice/api-1811080-makepipe.md)
  build a pipe on a given endpoint
- [OpenOrCloseAllInterfacePipes](./iousbdevice/api-1811109-openorcloseallinterfacepipes.md)
  Iterates over all interfaces and either opens all the pipes, or closes them all
- [ReEnumerateDevice](./iousbdevice/api-1811132-reenumeratedevice.md)
  Instruct the hub to which this device is attached to reset the port to which this device is attached. This causes the IOUSBDevice object and any child objects (IOUSBInterface objects or driver objects) to be terminated, and the device to be completely reenumerated, as if it had been detached and reattached.
- [RequestExtraPower](./iousbdevice/api-1811162-requestextrapower.md)
  Clients can use this API to reserve extra power for use by this device while the machine is asleep or while it is awake. Units are milliAmps (mA).
- [ResetDevice](./iousbdevice/api-1811205-resetdevice.md)
- [ReturnExtraPower](./iousbdevice/api-1811251-returnextrapower.md)
  Clients can use this API to tell the system that they will not use power that was previously reserved by using the RequestExtraPower API.
- [SetAddress](./iousbdevice/api-1811282-setaddress.md)
- [SetConfiguration(IOService *, UInt8, bool)](./iousbdevice/api-1811309-setconfiguration.md)
- [SetConfiguration(IOService *, UInt8, bool, bool)](./iousbdevice/api-1811340-setconfiguration.md)
- [SetHubParent](./iousbdevice/api-1811377-sethubparent.md)
  Used by the hub driver to give the nub a pointer to its HubPolicyMaker object
- [SuspendDevice](./iousbdevice/api-1811400-suspenddevice.md)
  Instruct the hub to which this device is attached to suspend or resume the port to which the device is attached. Note that if there are any outstanding transactions on any pipes in the device, those transactions will get returned with a kIOReturnNotResponding error.
### Instance Methods
- [- getMetaClass](./iousbdevice/api-3609093-getmetaclass.md)
- [- messageClients](./iousbdevice/api-4090593-messageclients.md)
- [- start](./iousbdevice/api-3609094-start.md)
- [- stop](./iousbdevice/api-3609095-stop.md)

## Relationships

### Inherits From
- [IOService](./ioservice.md)

## See Also

### IOKit
- [IOUSBInterface](./iousbinterface.md)
  An object that represents an interface of a device on the USB bus.
- [IOOFPathMatching](./api-1575304-ioofpathmatching.md)
- [IOUSBHostInterface](./iousbhostinterface.md)
- [IOUSBHostDevice](./iousbhostdevice.md)
- [IOUSBHostPipe](./iousbhostpipe.md)
- [IOUSBHostIOSource](./iousbhostiosource.md)
- [IOUSBHostStream](./iousbhoststream.md)
- [IOHIDEventDriver](./iohideventdriver.md)
- [IOHIDEventService](./iohideventservice.md)
  IOService represents an device or OS service in IOKit and DriverKit.
- [IOHIDInterface](./iohidinterface.md)
  IOService represents an device or OS service in IOKit and DriverKit.
- [IOHIDSystem](./iohidsystem.md)
- [IOHIKeyboardMapper](./iohikeyboardmapper.md)
- [IOHIKeyboard](./iohikeyboard.md)
- [IOHIPointing](./iohipointing.md)
- [IOHIDevice](./iohidevice.md)
- [IOHIDElement](./iohidelement.md)
- [IOHIDWorkLoop](./iohidworkloop.md)
- [IOEthernetInterface](./ioethernetinterface.md)
  The Ethernet interface object.
- [IOEthernetController](./ioethernetcontroller.md)
  Abstract superclass for Ethernet controllers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iousbdevice)*