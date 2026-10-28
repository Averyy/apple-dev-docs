# IOUSBInterfaceInterface190

**Framework**: IOKit  
**Kind**: struct  
**Role**: Structure

The object you use to access a USB device interface from user space, returned by the IOUSBFamily version 1.9 and above.

**Availability**:
- Mac Catalyst 18.4+
- macOS 10.2+

## Declaration

```c
typedef struct IOUSBInterfaceStruct190 {
    ...
} IOUSBInterfaceInterface190;
```

## Overview

The functions listed here include all of the functions defined for the IOUSBInterfaceInterface, IOUSBInterfaceInterface182, IOUSBInterfaceInterface183, and some new functions that are available in macOS 10.2 and later.

## Topics

### Instance Properties
- [AbortPipe](./iousbinterfaceinterface190/api-1559397-abortpipe.md)
- [AddRef](./iousbinterfaceinterface190/api-1559194-addref.md)
- [ClearPipeStall](./iousbinterfaceinterface190/api-1559200-clearpipestall.md)
- [ClearPipeStallBothEnds](./iousbinterfaceinterface190/api-1559241-clearpipestallbothends.md)
  Equivalent to ClearPipeStall.
- [ControlRequest](./iousbinterfaceinterface190/api-1559804-controlrequest.md)
- [ControlRequestAsync](./iousbinterfaceinterface190/api-1558809-controlrequestasync.md)
- [ControlRequestAsyncTO](./iousbinterfaceinterface190/api-1558734-controlrequestasyncto.md)
- [ControlRequestTO](./iousbinterfaceinterface190/api-1558921-controlrequestto.md)
- [CreateInterfaceAsyncEventSource](./iousbinterfaceinterface190/api-1559000-createinterfaceasynceventsource.md)
- [CreateInterfaceAsyncPort](./iousbinterfaceinterface190/api-1558861-createinterfaceasyncport.md)
- [GetAlternateSetting](./iousbinterfaceinterface190/api-1559622-getalternatesetting.md)
- [GetBandwidthAvailable](./iousbinterfaceinterface190/api-1559414-getbandwidthavailable.md)
  Returns the amount of bandwidth available on the bus for allocation to isochronous pipes. If the device is a high speed device, it will be the number of bytes per microframe (125 µsecs). If it is a full speed device, it will be the number of bytes per frame (1ms)
- [GetBusFrameNumber](./iousbinterfaceinterface190/api-1558730-getbusframenumber.md)
- [GetConfigurationValue](./iousbinterfaceinterface190/api-1558741-getconfigurationvalue.md)
- [GetDevice](./iousbinterfaceinterface190/api-1559430-getdevice.md)
- [GetDeviceProduct](./iousbinterfaceinterface190/api-1559473-getdeviceproduct.md)
- [GetDeviceReleaseNumber](./iousbinterfaceinterface190/api-1559344-getdevicereleasenumber.md)
- [GetDeviceVendor](./iousbinterfaceinterface190/api-1558946-getdevicevendor.md)
- [GetEndpointProperties](./iousbinterfaceinterface190/api-1558764-getendpointproperties.md)
  Returns the transfer type, max packet size, and interval of a specified endpoint, whether or not the endpoint has a pipe currently established.
- [GetInterfaceAsyncEventSource](./iousbinterfaceinterface190/api-1558749-getinterfaceasynceventsource.md)
- [GetInterfaceAsyncPort](./iousbinterfaceinterface190/api-1559421-getinterfaceasyncport.md)
- [GetInterfaceClass](./iousbinterfaceinterface190/api-1559658-getinterfaceclass.md)
- [GetInterfaceNumber](./iousbinterfaceinterface190/api-1558711-getinterfacenumber.md)
- [GetInterfaceProtocol](./iousbinterfaceinterface190/api-1559239-getinterfaceprotocol.md)
- [GetInterfaceSubClass](./iousbinterfaceinterface190/api-1558952-getinterfacesubclass.md)
- [GetLocationID](./iousbinterfaceinterface190/api-1558852-getlocationid.md)
- [GetNumEndpoints](./iousbinterfaceinterface190/api-1558947-getnumendpoints.md)
- [GetPipeProperties](./iousbinterfaceinterface190/api-1559379-getpipeproperties.md)
- [GetPipeStatus](./iousbinterfaceinterface190/api-1559456-getpipestatus.md)
- [QueryInterface](./iousbinterfaceinterface190/api-1559246-queryinterface.md)
- [ReadIsochPipeAsync](./iousbinterfaceinterface190/api-1559398-readisochpipeasync.md)
- [ReadPipe](./iousbinterfaceinterface190/api-1559687-readpipe.md)
- [ReadPipeAsync](./iousbinterfaceinterface190/api-1559322-readpipeasync.md)
- [ReadPipeAsyncTO](./iousbinterfaceinterface190/api-1559636-readpipeasyncto.md)
- [ReadPipeTO](./iousbinterfaceinterface190/api-1559144-readpipeto.md)
- [Release](./iousbinterfaceinterface190/api-1559773-release.md)
- [ResetPipe](./iousbinterfaceinterface190/api-1559518-resetpipe.md)
- [SetAlternateInterface](./iousbinterfaceinterface190/api-1559166-setalternateinterface.md)
- [SetPipePolicy](./iousbinterfaceinterface190/api-1558986-setpipepolicy.md)
  Changes the amount of bandwidth of an isochronous pipe or interrupt pipe, or the polling interval of an interrupt pipe.
- [USBInterfaceClose](./iousbinterfaceinterface190/api-1559288-usbinterfaceclose.md)
- [USBInterfaceGetStringIndex](./iousbinterfaceinterface190/api-1558913-usbinterfacegetstringindex.md)
- [USBInterfaceOpen](./iousbinterfaceinterface190/api-1558977-usbinterfaceopen.md)
- [USBInterfaceOpenSeize](./iousbinterfaceinterface190/api-1559226-usbinterfaceopenseize.md)
- [WriteIsochPipeAsync](./iousbinterfaceinterface190/api-1558715-writeisochpipeasync.md)
- [WritePipe](./iousbinterfaceinterface190/api-1559710-writepipe.md)
- [WritePipeAsync](./iousbinterfaceinterface190/api-1559603-writepipeasync.md)
- [WritePipeAsyncTO](./iousbinterfaceinterface190/api-1559278-writepipeasyncto.md)
- [WritePipeTO](./iousbinterfaceinterface190/api-1558875-writepipeto.md)

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
- [IOUSBDeviceInterface500](./iousbdeviceinterface500.md)
  The object you use to access USB devices from user space, returned by the IOUSBFamily version 3.2.0 and above.
- [IOUSBInterfaceInterface](./iousbinterfaceinterface.md)
  The object you use to access a USB device interface from user space, returned by all versions of the IOUSBFamily currently shipping.
- [IOUSBInterfaceInterface182](./iousbinterfaceinterface182.md)
  The object you use to access a USB device interface from user space, returned by the IOUSBFamily version 1.8.2 and above.
- [IOUSBInterfaceInterface183](./iousbinterfaceinterface183.md)
  The object you use to access a USB device interface from user space, returned by the IOUSBFamily version 1.8.3 and above.
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

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iousbinterfaceinterface190)*