# GetAddress

**Framework**: Kernel  
**Kind**: instm

## Declaration

```swift
virtual USBDeviceAddress GetAddress(
 void);
```

#### Overview

returns the bus address of the device

## See Also

- [CreateInterfaceIterator](iousbdevice/1810047-createinterfaceiterator.md)
- [DeviceRequest(IOUSBDevRequest *, UInt32, UInt32, IOUSBCompletion *)](iousbdevice/1810072-devicerequest.md)
  execute a control request to the default control pipe (pipe zero)
- [DeviceRequest(IOUSBDevRequestDesc *, UInt32, UInt32, IOUSBCompletion *)](iousbdevice/1810098-devicerequest.md)
  execute a control request to the default control pipe (pipe zero)
- [DisplayUserNotification](iousbdevice/1810124-displayusernotification.md)
  Will use the Notification Center to display a notification to the user. Only Low Power and Overcurrent notifications are supported.
- [DoLocationOverrideAndModelMatch](iousbdevice/1810151-dolocationoverrideandmodelmatch.md)
  Will look for a kOverrideIfAtLocationID array proerty with locationID entries and a "MacModel" property. If any of the locationIDs match to the Mac Model, will return true. If there is no kOverrideAtLocationID property, it will also return true.
- [FindNextInterface](iousbdevice/1810185-findnextinterface.md)
- [FindNextInterfaceDescriptor](iousbdevice/1810212-findnextinterfacedescriptor.md)
- [GetBus](iousbdevice/1810263-getbus.md)
- [GetBusPowerAvailable](iousbdevice/1810284-getbuspoweravailable.md)
- [GetChildLocationID](iousbdevice/1810305-getchildlocationid.md)
- [GetConfiguration](iousbdevice/1810333-getconfiguration.md)
- [GetConfigurationDescriptor](iousbdevice/1810384-getconfigurationdescriptor.md)
- [GetDeviceInformation](iousbdevice/1810425-getdeviceinformation.md)
  Returns status information about the USB device, such as whether the device is captive or whether it is in the suspended state.
- [GetDeviceRelease](iousbdevice/1810457-getdevicerelease.md)
- [GetDeviceStatus](iousbdevice/1810482-getdevicestatus.md)
- [GetExtraPowerAllocated](iousbdevice/1810520-getextrapowerallocated.md)
  Clients can use this API to ask how much extra power has already been reserved by this device. Units are milliAmps (mA).
- [GetFullConfigurationDescriptor](iousbdevice/1810553-getfullconfigurationdescriptor.md)
- [GetHubParent](iousbdevice/1810591-gethubparent.md)
  Used by the hub driver to give the nub a pointer to its HubPolicyMaker object
- [GetManufacturerStringIndex](iousbdevice/1810637-getmanufacturerstringindex.md)
- [GetMaxPacketSize](iousbdevice/1810681-getmaxpacketsize.md)
- [GetNumConfigurations](iousbdevice/1810710-getnumconfigurations.md)
- [GetPipeZero](iousbdevice/1810748-getpipezero.md)
- [GetProductID](iousbdevice/1810809-getproductid.md)
- [GetProductStringIndex](iousbdevice/1810867-getproductstringindex.md)
- [GetSerialNumberStringIndex](iousbdevice/1810912-getserialnumberstringindex.md)
- [GetSpeed](iousbdevice/1810998-getspeed.md)
- [GetStringDescriptor](iousbdevice/1811033-getstringdescriptor.md)
- [GetVendorID](iousbdevice/1811065-getvendorid.md)
- [MakePipe](iousbdevice/1811080-makepipe.md)
  build a pipe on a given endpoint
- [OpenOrCloseAllInterfacePipes](iousbdevice/1811109-openorcloseallinterfacepipes.md)
  Iterates over all interfaces and either opens all the pipes, or closes them all
- [ReEnumerateDevice](iousbdevice/1811132-reenumeratedevice.md)
  Instruct the hub to which this device is attached to reset the port to which this device is attached. This causes the IOUSBDevice object and any child objects (IOUSBInterface objects or driver objects) to be terminated, and the device to be completely reenumerated, as if it had been detached and reattached.
- [RequestExtraPower](iousbdevice/1811162-requestextrapower.md)
  Clients can use this API to reserve extra power for use by this device while the machine is asleep or while it is awake. Units are milliAmps (mA).
- [ResetDevice](iousbdevice/1811205-resetdevice.md)
- [ReturnExtraPower](iousbdevice/1811251-returnextrapower.md)
  Clients can use this API to tell the system that they will not use power that was previously reserved by using the RequestExtraPower API.
- [SetAddress](iousbdevice/1811282-setaddress.md)
- [SetConfiguration(IOService *, UInt8, bool)](iousbdevice/1811309-setconfiguration.md)
- [SetConfiguration(IOService *, UInt8, bool, bool)](iousbdevice/1811340-setconfiguration.md)
- [SetHubParent](iousbdevice/1811377-sethubparent.md)
  Used by the hub driver to give the nub a pointer to its HubPolicyMaker object
- [SuspendDevice](iousbdevice/1811400-suspenddevice.md)
  Instruct the hub to which this device is attached to suspend or resume the port to which the device is attached. Note that if there are any outstanding transactions on any pipes in the device, those transactions will get returned with a kIOReturnNotResponding error.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iousbdevice/1810231-getaddress)*