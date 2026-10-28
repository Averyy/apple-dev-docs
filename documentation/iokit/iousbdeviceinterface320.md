# IOUSBDeviceInterface320

**Framework**: IOKit  
**Kind**: struct  
**Role**: Structure

The object you use to access USB devices from user space, returned by the IOUSBFamily version 3.2.0 and above.

**Availability**:
- Mac Catalyst 18.4+
- macOS 10.6+

## Declaration

```c
typedef struct IOUSBDeviceStruct320 {
    ...
} IOUSBDeviceInterface320;
```

## Overview

The functions listed here include all of the functions defined for the IOUSBDeviceInterface, IOUSBDeviceInterface182, IOUSBDeviceInterface187, IOUSBDeviceInterface197, IOUSBDeviceInterface245, or IOUSBDeviceInterface300 and some new functions that are available in macOS 10.5.4 and later.

## Topics

### Instance Properties
- [AddRef](./iousbdeviceinterface320/api-1559653-addref.md)
- [CreateDeviceAsyncEventSource](./iousbdeviceinterface320/api-1559012-createdeviceasynceventsource.md)
- [CreateDeviceAsyncPort](./iousbdeviceinterface320/api-1558945-createdeviceasyncport.md)
- [CreateInterfaceIterator](./iousbdeviceinterface320/api-1558761-createinterfaceiterator.md)
- [DeviceRequest](./iousbdeviceinterface320/api-1559729-devicerequest.md)
- [DeviceRequestAsync](./iousbdeviceinterface320/api-1559047-devicerequestasync.md)
- [DeviceRequestAsyncTO](./iousbdeviceinterface320/api-1558757-devicerequestasyncto.md)
- [DeviceRequestTO](./iousbdeviceinterface320/api-1559754-devicerequestto.md)
- [GetBusFrameNumber](./iousbdeviceinterface320/api-1559741-getbusframenumber.md)
- [GetBusFrameNumberWithTime](./iousbdeviceinterface320/api-1558850-getbusframenumberwithtime.md)
- [GetBusMicroFrameNumber](./iousbdeviceinterface320/api-1559050-getbusmicroframenumber.md)
- [GetConfiguration](./iousbdeviceinterface320/api-1558817-getconfiguration.md)
- [GetConfigurationDescriptorPtr](./iousbdeviceinterface320/api-1559416-getconfigurationdescriptorptr.md)
- [GetDeviceAddress](./iousbdeviceinterface320/api-1559796-getdeviceaddress.md)
- [GetDeviceAsyncEventSource](./iousbdeviceinterface320/api-1558812-getdeviceasynceventsource.md)
- [GetDeviceAsyncPort](./iousbdeviceinterface320/api-1559701-getdeviceasyncport.md)
- [GetDeviceBusPowerAvailable](./iousbdeviceinterface320/api-1559052-getdevicebuspoweravailable.md)
- [GetDeviceClass](./iousbdeviceinterface320/api-1559702-getdeviceclass.md)
- [GetDeviceProduct](./iousbdeviceinterface320/api-1558823-getdeviceproduct.md)
- [GetDeviceProtocol](./iousbdeviceinterface320/api-1559747-getdeviceprotocol.md)
- [GetDeviceReleaseNumber](./iousbdeviceinterface320/api-1559224-getdevicereleasenumber.md)
- [GetDeviceSpeed](./iousbdeviceinterface320/api-1559051-getdevicespeed.md)
- [GetDeviceSubClass](./iousbdeviceinterface320/api-1559132-getdevicesubclass.md)
- [GetDeviceVendor](./iousbdeviceinterface320/api-1559343-getdevicevendor.md)
- [GetExtraPowerAllocated](./iousbdeviceinterface320/api-1559557-getextrapowerallocated.md)
  Clients can use this API to ask how much extra power has already been reserved by this device. Units are milliAmps (mA).
- [GetIOUSBLibVersion](./iousbdeviceinterface320/api-1559186-getiousblibversion.md)
- [GetLocationID](./iousbdeviceinterface320/api-1559135-getlocationid.md)
- [GetNumberOfConfigurations](./iousbdeviceinterface320/api-1558765-getnumberofconfigurations.md)
- [GetUSBDeviceInformation](./iousbdeviceinterface320/api-1559006-getusbdeviceinformation.md)
  Returns status information about the USB device, such as whether the device is captive or whether it is in the suspended state.
- [QueryInterface](./iousbdeviceinterface320/api-1559368-queryinterface.md)
- [Release](./iousbdeviceinterface320/api-1559411-release.md)
- [RequestExtraPower](./iousbdeviceinterface320/api-1559755-requestextrapower.md)
  Clients can use this API to reserve extra power for use by this device while the machine is asleep or while it is awake. Units are milliAmps (mA).
- [ResetDevice](./iousbdeviceinterface320/api-1559751-resetdevice.md)
- [ReturnExtraPower](./iousbdeviceinterface320/api-1559629-returnextrapower.md)
  Clients can use this API to tell the system that they will not use power that was previously reserved by using the RequestExtraPower API.
- [SetConfiguration](./iousbdeviceinterface320/api-1559712-setconfiguration.md)
- [USBDeviceAbortPipeZero](./iousbdeviceinterface320/api-1559232-usbdeviceabortpipezero.md)
- [USBDeviceClose](./iousbdeviceinterface320/api-1558895-usbdeviceclose.md)
- [USBDeviceOpen](./iousbdeviceinterface320/api-1559256-usbdeviceopen.md)
- [USBDeviceOpenSeize](./iousbdeviceinterface320/api-1558871-usbdeviceopenseize.md)
- [USBDeviceReEnumerate](./iousbdeviceinterface320/api-1559554-usbdevicereenumerate.md)
- [USBDeviceSuspend](./iousbdeviceinterface320/api-1559043-usbdevicesuspend.md)
- [USBGetManufacturerStringIndex](./iousbdeviceinterface320/api-1559395-usbgetmanufacturerstringindex.md)
- [USBGetProductStringIndex](./iousbdeviceinterface320/api-1558826-usbgetproductstringindex.md)
- [USBGetSerialNumberStringIndex](./iousbdeviceinterface320/api-1558896-usbgetserialnumberstringindex.md)

## See Also

### COM Interfaces
- [IOATASMARTInterface](./ioatasmartinterface.md)
  Self-Monitoring, Analysis, and Reporting Technology Interface.
- [IOFireWireAsyncStreamCommandInterface](./iofirewireasyncstreamcommandinterface.md)
- [IOFireWireAVCLibConsumerInterface](./iofirewireavclibconsumerinterface.md)
  Interface for an asynchronous connection consumer.
- [IOFireWireAVCLibProtocolInterface](./iofirewireavclibprotocolinterface.md)
  Initial interface discovered for all AVC protocol drivers.
- [IOFireWireAVCLibUnitInterface](./iofirewireavclibunitinterface.md)
  Initial interface discovered for all AVC Unit drivers.
- [IOFireWireCommandInterface](./iofirewirecommandinterface.md)
  IOFireWireLib command object.
- [IOFireWireCompareSwapCommandInterface](./iofirewirecompareswapcommandinterface.md)
- [IOFireWireCompareSwapCommandInterface_v3](./iofirewirecompareswapcommandinterface_v3.md)
- [IOFireWireConfigDirectoryInterface](./iofirewireconfigdirectoryinterface.md)
  IOFireWireLib device config ROM browsing interface
- [IOFireWireDCLCommandPoolInterface](./iofirewiredclcommandpoolinterface.md)
- [IOFireWireDeviceInterface](./iofirewiredeviceinterface.md)
  IOFireWireDeviceInterface is your primary gateway to the functionality contained in IOFireWireLib.
- [IOFireWireIsochChannelInterface](./iofirewireisochchannelinterface.md)
  FireWire user client isochronous channel object.
- [IOFireWireIsochPortInterface](./iofirewireisochportinterface.md)
  FireWire user client isochronous port interface
- [IOFireWireLibIRMAllocationInterface](./iofirewirelibirmallocationinterface.md)
- [IOFireWireLibPHYPacketListenerInterface](./iofirewirelibphypacketlistenerinterface.md)
  Represents and provides management functions for a phy packet listener object.
- [IOFireWireLibVectorCommandInterface](./iofirewirelibvectorcommandinterface.md)
  IOFireWireLib command object for grouping commands execution.
- [IOFireWireLocalIsochPortInterface](./iofirewirelocalisochportinterface.md)
  FireWire user client local isochronous port object.
- [IOFireWireLocalUnitDirectoryInterface](./iofirewirelocalunitdirectoryinterface.md)
- [IOFireWireNubInterface](./iofirewirenubinterface-ajp.md)
  IOFireWireDeviceInterface is your primary gateway to the functionality contained in IOFireWireLib.
- [IOFireWireNuDCLPoolInterface](./iofirewirenudclpoolinterface.md)
  Use this interface to build NuDCL-based DCL programs.
- [IOFireWirePHYCommandInterface](./iofirewirephycommandinterface.md)
- [IOFireWirePhysicalAddressSpaceInterface](./iofirewirephysicaladdressspaceinterface.md)
  IOFireWireLib physical address space object. ( interface name: IOFireWirePhysicalAddressSpaceInterface )
- [IOFireWirePseudoAddressSpaceInterface](./iofirewirepseudoaddressspaceinterface.md)
- [IOFireWireReadCommandInterface](./iofirewirereadcommandinterface.md)
  IOFireWireLib block read command object.
- [IOFireWireReadQuadletCommandInterface](./iofirewirereadquadletcommandinterface.md)
  IOFireWireReadQuadletCommandInterface -- IOFireWireLib quadlet read command object.
- [IOFireWireRemoteIsochPortInterface](./iofirewireremoteisochportinterface.md)
- [IOFireWireSBP2LibLoginInterface](./iofirewiresbp2liblogininterface.md)
  Supplies the login maintenance and Normal Command ORB execution portions of the API.
- [IOFireWireSBP2LibLUNInterface](./iofirewiresbp2libluninterface.md)
  Initial interface disovered for all drivers.
- [IOFireWireSBP2LibMgmtORBInterface](./iofirewiresbp2libmgmtorbinterface.md)
  Supplies non login related management ORBs. Management ORBs can be executed independent of a login, if necessary. Management ORBs are created using the IOFireWireSBP2LibLUNInterface.
- [IOFireWireSBP2LibORBInterface](./iofirewiresbp2liborbinterface.md)
  Represents an SBP2 normal command ORB. Supplies the APIs for configuring normal command ORBs. This includes setting the command block and writing the page tables for I/O. The ORBs are executed using the submitORB method in IOFireWireSBP2LibLoginInterface.
- [IOFireWireUnitInterface](./iofirewireunitinterface-apt.md)
  IOFireWireDeviceInterface is your primary gateway to the functionality contained in IOFireWireLib.
- [IOFireWireWriteCommandInterface](./iofirewirewritecommandinterface.md)
  IOFireWireLib block read command object.
- [IOFireWireWriteQuadletCommandInterface](./iofirewirewritequadletcommandinterface.md)
  IOFireWireLib quadlet read command object.
- [IOFWAsyncStreamListenerInterface](./iofwasyncstreamlistenerinterface.md)
  Represents and provides management functions for a asyn stream listener object.
- [IOHIDDeviceDeviceInterface](./iohiddevicedeviceinterface.md)
  The object you use to access HID devices from user space, returned by version 1.5 of the IOHIDFamily.
- [IOHIDDeviceInterface](./iohiddeviceinterface.md)
  CFPlugin object subclass which provides the primary interface to HID devices.
- [IOHIDDeviceInterface121](./iohiddeviceinterface121.md)
  CFPlugin object subclass which provides the primary interface to HID devices. This class is a subclass of IOHIDDeviceInterface.
- [IOHIDDeviceInterface122](./iohiddeviceinterface122.md)
  CFPlugin object subclass which provides the primary interface to HID devices. This class is a subclass of IOHIDDeviceInterface121.
- [IOHIDDeviceQueueInterface](./iohiddevicequeueinterface.md)
  The object you use to access a HID queue from user space, returned by version 1.5 of the IOHIDFamily.
- [IOHIDDeviceTransactionInterface](./iohiddevicetransactioninterface.md)
  The object you use to access a HID transaction from user space, returned by version 1.5 of the IOHIDFamily.
- [IOHIDOutputTransactionInterface](./iohidoutputtransactioninterface.md)
  CFPlugin object subclass which privides interface for output transactions to HID devices. Created by a IOHIDDeviceInterface object.
- [IOHIDQueueInterface](./iohidqueueinterface.md)
  CFPlugin object subclass which provides an interface for input queues from HID devices. Created by an IOHIDDeviceInterface object.
- [IOUPSPlugInInterface](./ioupsplugininterface.md)
  Represents and provides management functions for a UPS device.
- [IOUSBDeviceInterface](./iousbdeviceinterface.md)
  The object you use to access USB devices from user space, returned by all versions of the IOUSBFamily currently shipping.
- [IOUSBDeviceInterface182](./iousbdeviceinterface182.md)
  The object you use to access USB devices from user space, returned by the IOUSBFamily version 1.8.2 and above.
- [IOUSBDeviceInterface187](./iousbdeviceinterface187.md)
  The object you use to access USB devices from user space, returned by the IOUSBFamily version 10.8.7 and above.
- [IOUSBDeviceInterface197](./iousbdeviceinterface197.md)
  The object you use to access USB devices from user space, returned by the IOUSBFamily version 1.9.7 and above.
- [IOUSBDeviceInterface245](./iousbdeviceinterface245.md)
  The object you use to access USB devices from user space, returned by the IOUSBFamily version 2.4.5 and above.
- [IOUSBDeviceInterface300](./iousbdeviceinterface300.md)
  The object you use to access USB devices from user space, returned by the IOUSBFamily version 3.0.0 and above.
- [IOUSBDeviceInterface500](./iousbdeviceinterface500.md)
  The object you use to access USB devices from user space, returned by the IOUSBFamily version 3.2.0 and above.
- [IOUSBInterfaceInterface](./iousbinterfaceinterface.md)
  The object you use to access a USB device interface from user space, returned by all versions of the IOUSBFamily currently shipping.
- [IOUSBInterfaceInterface182](./iousbinterfaceinterface182.md)
  The object you use to access a USB device interface from user space, returned by the IOUSBFamily version 1.8.2 and above.
- [IOUSBInterfaceInterface183](./iousbinterfaceinterface183.md)
  The object you use to access a USB device interface from user space, returned by the IOUSBFamily version 1.8.3 and above.
- [IOUSBInterfaceInterface190](./iousbinterfaceinterface190.md)
  The object you use to access a USB device interface from user space, returned by the IOUSBFamily version 1.9 and above.
- [IOUSBInterfaceInterface192](./iousbinterfaceinterface192.md)
  The object you use to access a USB device interface from user space, returned by the IOUSBFamily version 1.9.2 and above.
- [IOUSBInterfaceInterface197](./iousbinterfaceinterface197.md)
  The object you use to access a USB device interface from user space, returned by the IOUSBFamily version 1.9.7 and above.
- [MMCDeviceInterface](./mmcdeviceinterface.md)
  Basic interface for an MMC-2 Compliant Device.
- [SCSITaskDeviceInterface](./scsitaskdeviceinterface.md)
  Basic interface for a SCSITask Device.
- [SCSITaskInterface](./scsitaskinterface.md)
  Basic interface for a SCSITask.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iousbdeviceinterface320)*