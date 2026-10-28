# IOUSBInterfaceInterface192

**Framework**: IOKit  
**Kind**: struct  
**Role**: Structure

The object you use to access a USB device interface from user space, returned by the IOUSBFamily version 1.9.2 and above.

**Availability**:
- Mac Catalyst 18.4+
- macOS 10.2+

## Declaration

```c
typedef struct IOUSBInterfaceStruct192 {
    ...
} IOUSBInterfaceInterface192;
```

## Overview

The functions listed here include all of the functions defined for the IOUSBInterfaceInterface, IOUSBInterfaceInterface182, IOUSBInterfaceInterface183, IOUSBInterfaceInterface190, and some new functions that are available in macOS 10.2.3 and later.

## Topics

### Instance Properties
- [AbortPipe](./iousbinterfaceinterface192/api-1559432-abortpipe.md)
- [AddRef](./iousbinterfaceinterface192/api-1558925-addref.md)
- [ClearPipeStall](./iousbinterfaceinterface192/api-1559281-clearpipestall.md)
- [ClearPipeStallBothEnds](./iousbinterfaceinterface192/api-1559533-clearpipestallbothends.md)
- [ControlRequest](./iousbinterfaceinterface192/api-1558740-controlrequest.md)
- [ControlRequestAsync](./iousbinterfaceinterface192/api-1559257-controlrequestasync.md)
- [ControlRequestAsyncTO](./iousbinterfaceinterface192/api-1558783-controlrequestasyncto.md)
- [ControlRequestTO](./iousbinterfaceinterface192/api-1558799-controlrequestto.md)
- [CreateInterfaceAsyncEventSource](./iousbinterfaceinterface192/api-1559405-createinterfaceasynceventsource.md)
- [CreateInterfaceAsyncPort](./iousbinterfaceinterface192/api-1559550-createinterfaceasyncport.md)
- [GetAlternateSetting](./iousbinterfaceinterface192/api-1559767-getalternatesetting.md)
- [GetBandwidthAvailable](./iousbinterfaceinterface192/api-1558864-getbandwidthavailable.md)
- [GetBusFrameNumber](./iousbinterfaceinterface192/api-1559544-getbusframenumber.md)
- [GetConfigurationValue](./iousbinterfaceinterface192/api-1559666-getconfigurationvalue.md)
- [GetDevice](./iousbinterfaceinterface192/api-1559822-getdevice.md)
- [GetDeviceProduct](./iousbinterfaceinterface192/api-1558993-getdeviceproduct.md)
- [GetDeviceReleaseNumber](./iousbinterfaceinterface192/api-1559123-getdevicereleasenumber.md)
- [GetDeviceVendor](./iousbinterfaceinterface192/api-1558960-getdevicevendor.md)
- [GetEndpointProperties](./iousbinterfaceinterface192/api-1559088-getendpointproperties.md)
- [GetInterfaceAsyncEventSource](./iousbinterfaceinterface192/api-1559591-getinterfaceasynceventsource.md)
- [GetInterfaceAsyncPort](./iousbinterfaceinterface192/api-1558883-getinterfaceasyncport.md)
- [GetInterfaceClass](./iousbinterfaceinterface192/api-1559334-getinterfaceclass.md)
- [GetInterfaceNumber](./iousbinterfaceinterface192/api-1559250-getinterfacenumber.md)
- [GetInterfaceProtocol](./iousbinterfaceinterface192/api-1558801-getinterfaceprotocol.md)
- [GetInterfaceSubClass](./iousbinterfaceinterface192/api-1559010-getinterfacesubclass.md)
- [GetLocationID](./iousbinterfaceinterface192/api-1559540-getlocationid.md)
- [GetNumEndpoints](./iousbinterfaceinterface192/api-1559089-getnumendpoints.md)
- [GetPipeProperties](./iousbinterfaceinterface192/api-1559662-getpipeproperties.md)
- [GetPipeStatus](./iousbinterfaceinterface192/api-1559549-getpipestatus.md)
- [LowLatencyCreateBuffer](./iousbinterfaceinterface192/api-1559237-lowlatencycreatebuffer.md)
  Allocates a buffer of type bufferType.
- [LowLatencyDestroyBuffer](./iousbinterfaceinterface192/api-1559420-lowlatencydestroybuffer.md)
  Releases a buffer that was previously allocated using LowLatencyCreateBuffer().
- [LowLatencyReadIsochPipeAsync](./iousbinterfaceinterface192/api-1559722-lowlatencyreadisochpipeasync.md)
  Performs an asynchronous read on a isochronous pipe and updates the frame list at primary interrupt time.
- [LowLatencyWriteIsochPipeAsync](./iousbinterfaceinterface192/api-1559336-lowlatencywriteisochpipeasync.md)
  Performs an asynchronous write on an isochronous pipe and updates the frame list at primary interrupt time.
- [QueryInterface](./iousbinterfaceinterface192/api-1558922-queryinterface.md)
- [ReadIsochPipeAsync](./iousbinterfaceinterface192/api-1559661-readisochpipeasync.md)
- [ReadPipe](./iousbinterfaceinterface192/api-1559683-readpipe.md)
- [ReadPipeAsync](./iousbinterfaceinterface192/api-1559602-readpipeasync.md)
- [ReadPipeAsyncTO](./iousbinterfaceinterface192/api-1559589-readpipeasyncto.md)
- [ReadPipeTO](./iousbinterfaceinterface192/api-1559531-readpipeto.md)
- [Release](./iousbinterfaceinterface192/api-1558926-release.md)
- [ResetPipe](./iousbinterfaceinterface192/api-1559354-resetpipe.md)
- [SetAlternateInterface](./iousbinterfaceinterface192/api-1558902-setalternateinterface.md)
- [SetPipePolicy](./iousbinterfaceinterface192/api-1559273-setpipepolicy.md)
- [USBInterfaceClose](./iousbinterfaceinterface192/api-1559365-usbinterfaceclose.md)
- [USBInterfaceGetStringIndex](./iousbinterfaceinterface192/api-1559828-usbinterfacegetstringindex.md)
- [USBInterfaceOpen](./iousbinterfaceinterface192/api-1558701-usbinterfaceopen.md)
- [USBInterfaceOpenSeize](./iousbinterfaceinterface192/api-1559032-usbinterfaceopenseize.md)
- [WriteIsochPipeAsync](./iousbinterfaceinterface192/api-1559174-writeisochpipeasync.md)
- [WritePipe](./iousbinterfaceinterface192/api-1558904-writepipe.md)
- [WritePipeAsync](./iousbinterfaceinterface192/api-1559503-writepipeasync.md)
- [WritePipeAsyncTO](./iousbinterfaceinterface192/api-1559145-writepipeasyncto.md)
- [WritePipeTO](./iousbinterfaceinterface192/api-1559292-writepipeto.md)

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
- [IOUSBInterfaceInterface190](./iousbinterfaceinterface190.md)
  The object you use to access a USB device interface from user space, returned by the IOUSBFamily version 1.9 and above.
- [IOUSBInterfaceInterface197](./iousbinterfaceinterface197.md)
  The object you use to access a USB device interface from user space, returned by the IOUSBFamily version 1.9.7 and above.
- [MMCDeviceInterface](./mmcdeviceinterface.md)
  Basic interface for an MMC-2 Compliant Device.
- [SCSITaskDeviceInterface](./scsitaskdeviceinterface.md)
  Basic interface for a SCSITask Device.
- [SCSITaskInterface](./scsitaskinterface.md)
  Basic interface for a SCSITask.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iousbinterfaceinterface192)*