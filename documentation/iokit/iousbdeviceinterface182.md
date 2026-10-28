# IOUSBDeviceInterface182

**Framework**: IOKit  
**Kind**: struct  
**Role**: Structure

The object you use to access USB devices from user space, returned by the IOUSBFamily version 1.8.2 and above.

**Availability**:
- Mac Catalyst 18.4+
- macOS 10.1+

## Declaration

```c
typedef struct IOUSBDeviceStruct182 {
    ...
} IOUSBDeviceInterface182;
```

## Overview

The functions listed here include all of the functions defined for the IOUSBDeviceInterface and some new functions that are available in macOS 10.0.4 and later.

## Topics

### Instance Properties
- [AddRef](./iousbdeviceinterface182/api-1559462-addref.md)
- [CreateDeviceAsyncEventSource](./iousbdeviceinterface182/api-1559339-createdeviceasynceventsource.md)
- [CreateDeviceAsyncPort](./iousbdeviceinterface182/api-1558912-createdeviceasyncport.md)
- [CreateInterfaceIterator](./iousbdeviceinterface182/api-1559026-createinterfaceiterator.md)
- [DeviceRequest](./iousbdeviceinterface182/api-1559630-devicerequest.md)
- [DeviceRequestAsync](./iousbdeviceinterface182/api-1559509-devicerequestasync.md)
- [DeviceRequestAsyncTO](./iousbdeviceinterface182/api-1558785-devicerequestasyncto.md)
  Sends an asynchronous USB request on the default control pipe.
- [DeviceRequestTO](./iousbdeviceinterface182/api-1559217-devicerequestto.md)
  Sends a USB request on the default control pipe.
- [GetBusFrameNumber](./iousbdeviceinterface182/api-1559657-getbusframenumber.md)
- [GetConfiguration](./iousbdeviceinterface182/api-1559061-getconfiguration.md)
- [GetConfigurationDescriptorPtr](./iousbdeviceinterface182/api-1559827-getconfigurationdescriptorptr.md)
- [GetDeviceAddress](./iousbdeviceinterface182/api-1558899-getdeviceaddress.md)
- [GetDeviceAsyncEventSource](./iousbdeviceinterface182/api-1559085-getdeviceasynceventsource.md)
- [GetDeviceAsyncPort](./iousbdeviceinterface182/api-1559360-getdeviceasyncport.md)
- [GetDeviceBusPowerAvailable](./iousbdeviceinterface182/api-1559227-getdevicebuspoweravailable.md)
- [GetDeviceClass](./iousbdeviceinterface182/api-1559157-getdeviceclass.md)
- [GetDeviceProduct](./iousbdeviceinterface182/api-1559307-getdeviceproduct.md)
- [GetDeviceProtocol](./iousbdeviceinterface182/api-1559117-getdeviceprotocol.md)
- [GetDeviceReleaseNumber](./iousbdeviceinterface182/api-1559087-getdevicereleasenumber.md)
- [GetDeviceSpeed](./iousbdeviceinterface182/api-1559790-getdevicespeed.md)
- [GetDeviceSubClass](./iousbdeviceinterface182/api-1559076-getdevicesubclass.md)
- [GetDeviceVendor](./iousbdeviceinterface182/api-1559685-getdevicevendor.md)
- [GetLocationID](./iousbdeviceinterface182/api-1559361-getlocationid.md)
- [GetNumberOfConfigurations](./iousbdeviceinterface182/api-1559304-getnumberofconfigurations.md)
- [QueryInterface](./iousbdeviceinterface182/api-1559450-queryinterface.md)
- [Release](./iousbdeviceinterface182/api-1558819-release.md)
- [ResetDevice](./iousbdeviceinterface182/api-1559665-resetdevice.md)
- [SetConfiguration](./iousbdeviceinterface182/api-1559418-setconfiguration.md)
- [USBDeviceAbortPipeZero](./iousbdeviceinterface182/api-1559458-usbdeviceabortpipezero.md)
  Aborts a transaction on the default control pipe.
- [USBDeviceClose](./iousbdeviceinterface182/api-1558923-usbdeviceclose.md)
- [USBDeviceOpen](./iousbdeviceinterface182/api-1559782-usbdeviceopen.md)
- [USBDeviceOpenSeize](./iousbdeviceinterface182/api-1559151-usbdeviceopenseize.md)
  Opens the IOUSBDevice for exclusive access.
- [USBDeviceSuspend](./iousbdeviceinterface182/api-1559768-usbdevicesuspend.md)
  Tells the USB Family to either suspend or resume the port to which a device is attached.
- [USBGetManufacturerStringIndex](./iousbdeviceinterface182/api-1558708-usbgetmanufacturerstringindex.md)
  Returns the manufacturer string index in the device descriptor.
- [USBGetProductStringIndex](./iousbdeviceinterface182/api-1558836-usbgetproductstringindex.md)
  Returns the product string index in the device descriptor.
- [USBGetSerialNumberStringIndex](./iousbdeviceinterface182/api-1559750-usbgetserialnumberstringindex.md)
  Returns the serial number string index in the device descriptor.

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

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iousbdeviceinterface182)*