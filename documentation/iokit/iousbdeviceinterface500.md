# IOUSBDeviceInterface500

**Framework**: IOKit  
**Kind**: struct  
**Role**: Structure

The object you use to access USB devices from user space, returned by the IOUSBFamily version 3.2.0 and above.

**Availability**:
- Mac Catalyst 18.4+
- macOS 10.7+

## Declaration

```c
typedef struct IOUSBDeviceStruct500 {
    ...
} IOUSBDeviceInterface500;
```

## Overview

The functions listed here include all of the functions defined for the IOUSBDeviceInterface, IOUSBDeviceInterface182, IOUSBDeviceInterface187, IOUSBDeviceInterface197, IOUSBDeviceInterface245, IOUSBDeviceInterface300, or IOUSBDeviceInterface320 and some new functions that are available in macOS 10.7.3 and later.

## Topics

### Instance Properties
- [AddRef](./iousbdeviceinterface500/api-1559223-addref.md)
- [CreateDeviceAsyncEventSource](./iousbdeviceinterface500/api-1559119-createdeviceasynceventsource.md)
- [CreateDeviceAsyncPort](./iousbdeviceinterface500/api-1558968-createdeviceasyncport.md)
- [CreateInterfaceIterator](./iousbdeviceinterface500/api-1558738-createinterfaceiterator.md)
- [DeviceRequest](./iousbdeviceinterface500/api-1559689-devicerequest.md)
- [DeviceRequestAsync](./iousbdeviceinterface500/api-1559406-devicerequestasync.md)
- [DeviceRequestAsyncTO](./iousbdeviceinterface500/api-1558773-devicerequestasyncto.md)
- [DeviceRequestTO](./iousbdeviceinterface500/api-1559393-devicerequestto.md)
- [GetBandwidthAvailableForDevice](./iousbdeviceinterface500/api-1559035-getbandwidthavailablefordevice.md)
  Returns the amount of bandwidth available on the bus for allocation to periodic pipes. If the device is a high or super speed device, it will be the number of bytes per microframe (125 µsecs). If it is a full speed device, it will be the number of bytes per frame (1ms)
- [GetBusFrameNumber](./iousbdeviceinterface500/api-1559096-getbusframenumber.md)
- [GetBusFrameNumberWithTime](./iousbdeviceinterface500/api-1559663-getbusframenumberwithtime.md)
- [GetBusMicroFrameNumber](./iousbdeviceinterface500/api-1559211-getbusmicroframenumber.md)
- [GetConfiguration](./iousbdeviceinterface500/api-1559268-getconfiguration.md)
- [GetConfigurationDescriptorPtr](./iousbdeviceinterface500/api-1559709-getconfigurationdescriptorptr.md)
- [GetDeviceAddress](./iousbdeviceinterface500/api-1558877-getdeviceaddress.md)
- [GetDeviceAsyncEventSource](./iousbdeviceinterface500/api-1559435-getdeviceasynceventsource.md)
- [GetDeviceAsyncPort](./iousbdeviceinterface500/api-1558831-getdeviceasyncport.md)
- [GetDeviceBusPowerAvailable](./iousbdeviceinterface500/api-1558834-getdevicebuspoweravailable.md)
- [GetDeviceClass](./iousbdeviceinterface500/api-1558709-getdeviceclass.md)
- [GetDeviceProduct](./iousbdeviceinterface500/api-1559744-getdeviceproduct.md)
- [GetDeviceProtocol](./iousbdeviceinterface500/api-1559799-getdeviceprotocol.md)
- [GetDeviceReleaseNumber](./iousbdeviceinterface500/api-1558880-getdevicereleasenumber.md)
- [GetDeviceSpeed](./iousbdeviceinterface500/api-1559787-getdevicespeed.md)
- [GetDeviceSubClass](./iousbdeviceinterface500/api-1559638-getdevicesubclass.md)
- [GetDeviceVendor](./iousbdeviceinterface500/api-1558776-getdevicevendor.md)
- [GetExtraPowerAllocated](./iousbdeviceinterface500/api-1559201-getextrapowerallocated.md)
- [GetIOUSBLibVersion](./iousbdeviceinterface500/api-1558931-getiousblibversion.md)
- [GetLocationID](./iousbdeviceinterface500/api-1559234-getlocationid.md)
- [GetNumberOfConfigurations](./iousbdeviceinterface500/api-1558874-getnumberofconfigurations.md)
- [GetUSBDeviceInformation](./iousbdeviceinterface500/api-1559082-getusbdeviceinformation.md)
- [QueryInterface](./iousbdeviceinterface500/api-1558835-queryinterface.md)
- [Release](./iousbdeviceinterface500/api-1559726-release.md)
- [RequestExtraPower](./iousbdeviceinterface500/api-1559375-requestextrapower.md)
- [ResetDevice](./iousbdeviceinterface500/api-1559566-resetdevice.md)
- [ReturnExtraPower](./iousbdeviceinterface500/api-1558967-returnextrapower.md)
- [SetConfiguration](./iousbdeviceinterface500/api-1559580-setconfiguration.md)
- [USBDeviceAbortPipeZero](./iousbdeviceinterface500/api-1558806-usbdeviceabortpipezero.md)
- [USBDeviceClose](./iousbdeviceinterface500/api-1559817-usbdeviceclose.md)
- [USBDeviceOpen](./iousbdeviceinterface500/api-1558745-usbdeviceopen.md)
- [USBDeviceOpenSeize](./iousbdeviceinterface500/api-1559097-usbdeviceopenseize.md)
- [USBDeviceReEnumerate](./iousbdeviceinterface500/api-1558873-usbdevicereenumerate.md)
- [USBDeviceSuspend](./iousbdeviceinterface500/api-1559415-usbdevicesuspend.md)
- [USBGetManufacturerStringIndex](./iousbdeviceinterface500/api-1559252-usbgetmanufacturerstringindex.md)
- [USBGetProductStringIndex](./iousbdeviceinterface500/api-1558920-usbgetproductstringindex.md)
- [USBGetSerialNumberStringIndex](./iousbdeviceinterface500/api-1559610-usbgetserialnumberstringindex.md)

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
- [IOUSBDeviceInterface320](./iousbdeviceinterface320.md)
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

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iousbdeviceinterface500)*