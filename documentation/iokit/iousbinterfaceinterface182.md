# IOUSBInterfaceInterface182

**Framework**: IOKit  
**Kind**: struct  
**Role**: Structure

The object you use to access a USB device interface from user space, returned by the IOUSBFamily version 1.8.2 and above.

**Availability**:
- Mac Catalyst 18.4+
- macOS 10.1+

## Declaration

```c
typedef struct IOUSBInterfaceStruct182 {
    ...
} IOUSBInterfaceInterface182;
```

## Overview

The functions listed here include all of the functions defined for the IOUSBInterfaceInterface and some new functions that are available in macOS 10.0.4 and later.

## Topics

### Instance Properties
- [AbortPipe](./iousbinterfaceinterface182/api-1559341-abortpipe.md)
- [AddRef](./iousbinterfaceinterface182/api-1559539-addref.md)
- [ClearPipeStall](./iousbinterfaceinterface182/api-1559468-clearpipestall.md)
- [ControlRequest](./iousbinterfaceinterface182/api-1559697-controlrequest.md)
- [ControlRequestAsync](./iousbinterfaceinterface182/api-1558833-controlrequestasync.md)
- [ControlRequestAsyncTO](./iousbinterfaceinterface182/api-1559506-controlrequestasyncto.md)
  Sends an asynchronous USB request on a control pipe.
- [ControlRequestTO](./iousbinterfaceinterface182/api-1558963-controlrequestto.md)
  Sends a USB request on a control pipe.
- [CreateInterfaceAsyncEventSource](./iousbinterfaceinterface182/api-1558706-createinterfaceasynceventsource.md)
- [CreateInterfaceAsyncPort](./iousbinterfaceinterface182/api-1558704-createinterfaceasyncport.md)
- [GetAlternateSetting](./iousbinterfaceinterface182/api-1558843-getalternatesetting.md)
- [GetBusFrameNumber](./iousbinterfaceinterface182/api-1559501-getbusframenumber.md)
- [GetConfigurationValue](./iousbinterfaceinterface182/api-1558872-getconfigurationvalue.md)
- [GetDevice](./iousbinterfaceinterface182/api-1559783-getdevice.md)
- [GetDeviceProduct](./iousbinterfaceinterface182/api-1558935-getdeviceproduct.md)
- [GetDeviceReleaseNumber](./iousbinterfaceinterface182/api-1558870-getdevicereleasenumber.md)
- [GetDeviceVendor](./iousbinterfaceinterface182/api-1559482-getdevicevendor.md)
- [GetInterfaceAsyncEventSource](./iousbinterfaceinterface182/api-1558894-getinterfaceasynceventsource.md)
- [GetInterfaceAsyncPort](./iousbinterfaceinterface182/api-1559745-getinterfaceasyncport.md)
- [GetInterfaceClass](./iousbinterfaceinterface182/api-1558845-getinterfaceclass.md)
- [GetInterfaceNumber](./iousbinterfaceinterface182/api-1559110-getinterfacenumber.md)
- [GetInterfaceProtocol](./iousbinterfaceinterface182/api-1559758-getinterfaceprotocol.md)
- [GetInterfaceSubClass](./iousbinterfaceinterface182/api-1558758-getinterfacesubclass.md)
- [GetLocationID](./iousbinterfaceinterface182/api-1559103-getlocationid.md)
- [GetNumEndpoints](./iousbinterfaceinterface182/api-1559572-getnumendpoints.md)
- [GetPipeProperties](./iousbinterfaceinterface182/api-1559448-getpipeproperties.md)
- [GetPipeStatus](./iousbinterfaceinterface182/api-1558936-getpipestatus.md)
- [QueryInterface](./iousbinterfaceinterface182/api-1559130-queryinterface.md)
- [ReadIsochPipeAsync](./iousbinterfaceinterface182/api-1559705-readisochpipeasync.md)
- [ReadPipe](./iousbinterfaceinterface182/api-1559746-readpipe.md)
- [ReadPipeAsync](./iousbinterfaceinterface182/api-1559650-readpipeasync.md)
- [ReadPipeAsyncTO](./iousbinterfaceinterface182/api-1559295-readpipeasyncto.md)
  Performs an asynchronous read on a **BULK IN** pipe, with specified timeout values.
- [ReadPipeTO](./iousbinterfaceinterface182/api-1559627-readpipeto.md)
  Performs a read on a **BULK IN** pipe, specifying timeout values.
- [Release](./iousbinterfaceinterface182/api-1559674-release.md)
- [ResetPipe](./iousbinterfaceinterface182/api-1559305-resetpipe.md)
- [SetAlternateInterface](./iousbinterfaceinterface182/api-1559716-setalternateinterface.md)
- [USBInterfaceClose](./iousbinterfaceinterface182/api-1559474-usbinterfaceclose.md)
- [USBInterfaceGetStringIndex](./iousbinterfaceinterface182/api-1559792-usbinterfacegetstringindex.md)
  Returns the string index in the interface descriptor.
- [USBInterfaceOpen](./iousbinterfaceinterface182/api-1559429-usbinterfaceopen.md)
- [WriteIsochPipeAsync](./iousbinterfaceinterface182/api-1559173-writeisochpipeasync.md)
- [WritePipe](./iousbinterfaceinterface182/api-1558811-writepipe.md)
- [WritePipeAsync](./iousbinterfaceinterface182/api-1559396-writepipeasync.md)
- [WritePipeAsyncTO](./iousbinterfaceinterface182/api-1559059-writepipeasyncto.md)
  Performs an asynchronous write on a **BULK OUT** pipe, with specified timeout values.
- [WritePipeTO](./iousbinterfaceinterface182/api-1558982-writepipeto.md)
  Performs an asynchronous write on a **BULK OUT** pipe, with specified timeout values.

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

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iousbinterfaceinterface182)*