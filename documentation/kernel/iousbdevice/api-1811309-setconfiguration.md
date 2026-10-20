# SetConfiguration(IOService *, UInt8, bool)

**Framework**: Kernel  
**Kind**: instm

## Declaration

```cpp
virtual IOReturn SetConfiguration(
 IOService *forClient,
 UInt8 configValue,
 bool startInterfaceMatching=true);
```

#### Overview

Do a USB SetConfiguration call to the device. The caller must have the device open() in order to actually cause a configuration change. If the device is currently configured, all IOUSBInterface objects associated with the device are freed. After the new configuration has been set, all of its IOUSBInterface objects are instantiated automatically.

## Parameters

- `forClient`: The client requesting the configuration change
- `configValue`: The desired configuration value.
- `startInterfaceMatching`: A boolean specifying whether IOKit should begin the process of finding matching drivers for the new IOUSBInterface objects.

## See Also

### Miscellaneous
- [CreateInterfaceIterator](./api-1810047-createinterfaceiterator.md)
- [DeviceRequest(IOUSBDevRequest *, UInt32, UInt32, IOUSBCompletion *)](./api-1810072-devicerequest.md)
  execute a control request to the default control pipe (pipe zero)
- [DeviceRequest(IOUSBDevRequestDesc *, UInt32, UInt32, IOUSBCompletion *)](./api-1810098-devicerequest.md)
  execute a control request to the default control pipe (pipe zero)
- [DisplayUserNotification](./api-1810124-displayusernotification.md)
  Will use the Notification Center to display a notification to the user. Only Low Power and Overcurrent notifications are supported.
- [DoLocationOverrideAndModelMatch](./api-1810151-dolocationoverrideandmodelmatch.md)
  Will look for a kOverrideIfAtLocationID array proerty with locationID entries and a "MacModel" property. If any of the locationIDs match to the Mac Model, will return true. If there is no kOverrideAtLocationID property, it will also return true.
- [FindNextInterface](./api-1810185-findnextinterface.md)
- [FindNextInterfaceDescriptor](./api-1810212-findnextinterfacedescriptor.md)
- [GetAddress](./api-1810231-getaddress.md)
- [GetBus](./api-1810263-getbus.md)
- [GetBusPowerAvailable](./api-1810284-getbuspoweravailable.md)
- [GetChildLocationID](./api-1810305-getchildlocationid.md)
- [GetConfiguration](./api-1810333-getconfiguration.md)
- [GetConfigurationDescriptor](./api-1810384-getconfigurationdescriptor.md)
- [GetDeviceInformation](./api-1810425-getdeviceinformation.md)
  Returns status information about the USB device, such as whether the device is captive or whether it is in the suspended state.
- [GetDeviceRelease](./api-1810457-getdevicerelease.md)
- [GetDeviceStatus](./api-1810482-getdevicestatus.md)
- [GetExtraPowerAllocated](./api-1810520-getextrapowerallocated.md)
  Clients can use this API to ask how much extra power has already been reserved by this device. Units are milliAmps (mA).
- [GetFullConfigurationDescriptor](./api-1810553-getfullconfigurationdescriptor.md)
- [GetHubParent](./api-1810591-gethubparent.md)
  Used by the hub driver to give the nub a pointer to its HubPolicyMaker object
- [GetManufacturerStringIndex](./api-1810637-getmanufacturerstringindex.md)
- [GetMaxPacketSize](./api-1810681-getmaxpacketsize.md)
- [GetNumConfigurations](./api-1810710-getnumconfigurations.md)
- [GetPipeZero](./api-1810748-getpipezero.md)
- [GetProductID](./api-1810809-getproductid.md)
- [GetProductStringIndex](./api-1810867-getproductstringindex.md)
- [GetSerialNumberStringIndex](./api-1810912-getserialnumberstringindex.md)
- [GetSpeed](./api-1810998-getspeed.md)
- [GetStringDescriptor](./api-1811033-getstringdescriptor.md)
- [GetVendorID](./api-1811065-getvendorid.md)
- [MakePipe](./api-1811080-makepipe.md)
  build a pipe on a given endpoint
- [OpenOrCloseAllInterfacePipes](./api-1811109-openorcloseallinterfacepipes.md)
  Iterates over all interfaces and either opens all the pipes, or closes them all
- [ReEnumerateDevice](./api-1811132-reenumeratedevice.md)
  Instruct the hub to which this device is attached to reset the port to which this device is attached. This causes the IOUSBDevice object and any child objects (IOUSBInterface objects or driver objects) to be terminated, and the device to be completely reenumerated, as if it had been detached and reattached.
- [RequestExtraPower](./api-1811162-requestextrapower.md)
  Clients can use this API to reserve extra power for use by this device while the machine is asleep or while it is awake. Units are milliAmps (mA).
- [ResetDevice](./api-1811205-resetdevice.md)
- [ReturnExtraPower](./api-1811251-returnextrapower.md)
  Clients can use this API to tell the system that they will not use power that was previously reserved by using the RequestExtraPower API.
- [SetAddress](./api-1811282-setaddress.md)
- [SetConfiguration(IOService *, UInt8, bool, bool)](./api-1811340-setconfiguration.md)
- [SetHubParent](./api-1811377-sethubparent.md)
  Used by the hub driver to give the nub a pointer to its HubPolicyMaker object
- [SuspendDevice](./api-1811400-suspenddevice.md)
  Instruct the hub to which this device is attached to suspend or resume the port to which the device is attached. Note that if there are any outstanding transactions on any pipes in the device, those transactions will get returned with a kIOReturnNotResponding error.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iousbdevice/1811309-setconfiguration)*