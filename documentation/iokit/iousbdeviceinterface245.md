# IOUSBDeviceInterface245

**Framework**: IOKit  
**Kind**: struct  
**Role**: Structure

The object you use to access USB devices from user space, returned by the IOUSBFamily version 2.4.5 and above.

**Availability**:
- Mac Catalyst 18.4+
- macOS 10.4+

## Declaration

```c
typedef struct IOUSBDeviceStruct245 {
    ...
} IOUSBDeviceInterface245;
```

#### Overview

The functions listed here include all of the functions defined for the IOUSBDeviceInterface, IOUSBDeviceInterface182, IOUSBDeviceInterface187, IOUSBDeviceInterface197, and some new functions that are available in macOS 10.2.3 and later.

## Topics

### Instance Properties
- [AddRef](./iousbdeviceinterface245/api-1559346-addref.md)
- [CreateDeviceAsyncEventSource](./iousbdeviceinterface245/api-1558965-createdeviceasynceventsource.md)
- [CreateDeviceAsyncPort](./iousbdeviceinterface245/api-1558990-createdeviceasyncport.md)
- [CreateInterfaceIterator](./iousbdeviceinterface245/api-1559644-createinterfaceiterator.md)
- [DeviceRequest](./iousbdeviceinterface245/api-1559574-devicerequest.md)
- [DeviceRequestAsync](./iousbdeviceinterface245/api-1559515-devicerequestasync.md)
- [DeviceRequestAsyncTO](./iousbdeviceinterface245/api-1559582-devicerequestasyncto.md)
- [DeviceRequestTO](./iousbdeviceinterface245/api-1559090-devicerequestto.md)
- [GetBusFrameNumber](./iousbdeviceinterface245/api-1559262-getbusframenumber.md)
- [GetBusMicroFrameNumber](./iousbdeviceinterface245/api-1559575-getbusmicroframenumber.md)
- [GetConfiguration](./iousbdeviceinterface245/api-1559678-getconfiguration.md)
- [GetConfigurationDescriptorPtr](./iousbdeviceinterface245/api-1558810-getconfigurationdescriptorptr.md)
- [GetDeviceAddress](./iousbdeviceinterface245/api-1559816-getdeviceaddress.md)
- [GetDeviceAsyncEventSource](./iousbdeviceinterface245/api-1559618-getdeviceasynceventsource.md)
- [GetDeviceAsyncPort](./iousbdeviceinterface245/api-1559733-getdeviceasyncport.md)
- [GetDeviceBusPowerAvailable](./iousbdeviceinterface245/api-1558916-getdevicebuspoweravailable.md)
- [GetDeviceClass](./iousbdeviceinterface245/api-1559427-getdeviceclass.md)
- [GetDeviceProduct](./iousbdeviceinterface245/api-1559388-getdeviceproduct.md)
- [GetDeviceProtocol](./iousbdeviceinterface245/api-1559179-getdeviceprotocol.md)
- [GetDeviceReleaseNumber](./iousbdeviceinterface245/api-1559795-getdevicereleasenumber.md)
- [GetDeviceSpeed](./iousbdeviceinterface245/api-1558996-getdevicespeed.md)
- [GetDeviceSubClass](./iousbdeviceinterface245/api-1558998-getdevicesubclass.md)
- [GetDeviceVendor](./iousbdeviceinterface245/api-1559064-getdevicevendor.md)
- [GetIOUSBLibVersion](./iousbdeviceinterface245/api-1559078-getiousblibversion.md)
- [GetLocationID](./iousbdeviceinterface245/api-1559106-getlocationid.md)
- [GetNumberOfConfigurations](./iousbdeviceinterface245/api-1559703-getnumberofconfigurations.md)
- [QueryInterface](./iousbdeviceinterface245/api-1558788-queryinterface.md)
- [Release](./iousbdeviceinterface245/api-1559601-release.md)
- [ResetDevice](./iousbdeviceinterface245/api-1558888-resetdevice.md)
- [SetConfiguration](./iousbdeviceinterface245/api-1559314-setconfiguration.md)
- [USBDeviceAbortPipeZero](./iousbdeviceinterface245/api-1559355-usbdeviceabortpipezero.md)
- [USBDeviceClose](./iousbdeviceinterface245/api-1559625-usbdeviceclose.md)
- [USBDeviceOpen](./iousbdeviceinterface245/api-1559561-usbdeviceopen.md)
- [USBDeviceOpenSeize](./iousbdeviceinterface245/api-1559469-usbdeviceopenseize.md)
- [USBDeviceReEnumerate](./iousbdeviceinterface245/api-1559282-usbdevicereenumerate.md)
- [USBDeviceSuspend](./iousbdeviceinterface245/api-1559551-usbdevicesuspend.md)
- [USBGetManufacturerStringIndex](./iousbdeviceinterface245/api-1558886-usbgetmanufacturerstringindex.md)
- [USBGetProductStringIndex](./iousbdeviceinterface245/api-1559757-usbgetproductstringindex.md)
- [USBGetSerialNumberStringIndex](./iousbdeviceinterface245/api-1558900-usbgetserialnumberstringindex.md)

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
- [IOUSBDeviceInterface300](./iousbdeviceinterface300.md)
  The object you use to access USB devices from user space, returned by the IOUSBFamily version 3.0.0 and above.
- [IOUSBDeviceInterface320](./iousbdeviceinterface320.md)
  The object you use to access USB devices from user space, returned by the IOUSBFamily version 3.2.0 and above.
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

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iousbdeviceinterface245)*