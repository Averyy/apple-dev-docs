# IOUSBInterfaceInterface183

**Framework**: IOKit  
**Kind**: struct  
**Role**: Structure

The object you use to access a USB device interface from user space, returned by the IOUSBFamily version 1.8.3 and above.

**Availability**:
- Mac Catalyst 18.4+
- macOS 10.1+

## Declaration

```c
typedef struct IOUSBInterfaceStruct183 {
    ...
} IOUSBInterfaceInterface183;
```

#### Overview

The functions listed here include all of the functions defined for the IOUSBInterfaceInterface, IOUSBInterfaceInterface182, and some new functions that are available in macOS 10.1 and later.

## Topics

### Instance Properties
- [AbortPipe](./iousbinterfaceinterface183/api-1559436-abortpipe.md)
- [AddRef](./iousbinterfaceinterface183/api-1559680-addref.md)
- [ClearPipeStall](./iousbinterfaceinterface183/api-1559302-clearpipestall.md)
- [ControlRequest](./iousbinterfaceinterface183/api-1559634-controlrequest.md)
- [ControlRequestAsync](./iousbinterfaceinterface183/api-1559732-controlrequestasync.md)
- [ControlRequestAsyncTO](./iousbinterfaceinterface183/api-1559631-controlrequestasyncto.md)
- [ControlRequestTO](./iousbinterfaceinterface183/api-1559621-controlrequestto.md)
- [CreateInterfaceAsyncEventSource](./iousbinterfaceinterface183/api-1559321-createinterfaceasynceventsource.md)
- [CreateInterfaceAsyncPort](./iousbinterfaceinterface183/api-1559526-createinterfaceasyncport.md)
- [GetAlternateSetting](./iousbinterfaceinterface183/api-1559564-getalternatesetting.md)
- [GetBusFrameNumber](./iousbinterfaceinterface183/api-1559377-getbusframenumber.md)
- [GetConfigurationValue](./iousbinterfaceinterface183/api-1558997-getconfigurationvalue.md)
- [GetDevice](./iousbinterfaceinterface183/api-1559496-getdevice.md)
- [GetDeviceProduct](./iousbinterfaceinterface183/api-1559756-getdeviceproduct.md)
- [GetDeviceReleaseNumber](./iousbinterfaceinterface183/api-1558867-getdevicereleasenumber.md)
- [GetDeviceVendor](./iousbinterfaceinterface183/api-1559811-getdevicevendor.md)
- [GetInterfaceAsyncEventSource](./iousbinterfaceinterface183/api-1559616-getinterfaceasynceventsource.md)
- [GetInterfaceAsyncPort](./iousbinterfaceinterface183/api-1558984-getinterfaceasyncport.md)
- [GetInterfaceClass](./iousbinterfaceinterface183/api-1558839-getinterfaceclass.md)
- [GetInterfaceNumber](./iousbinterfaceinterface183/api-1559675-getinterfacenumber.md)
- [GetInterfaceProtocol](./iousbinterfaceinterface183/api-1559165-getinterfaceprotocol.md)
- [GetInterfaceSubClass](./iousbinterfaceinterface183/api-1559708-getinterfacesubclass.md)
- [GetLocationID](./iousbinterfaceinterface183/api-1558881-getlocationid.md)
- [GetNumEndpoints](./iousbinterfaceinterface183/api-1559384-getnumendpoints.md)
- [GetPipeProperties](./iousbinterfaceinterface183/api-1559140-getpipeproperties.md)
- [GetPipeStatus](./iousbinterfaceinterface183/api-1559013-getpipestatus.md)
- [QueryInterface](./iousbinterfaceinterface183/api-1559270-queryinterface.md)
- [ReadIsochPipeAsync](./iousbinterfaceinterface183/api-1559259-readisochpipeasync.md)
- [ReadPipe](./iousbinterfaceinterface183/api-1559175-readpipe.md)
- [ReadPipeAsync](./iousbinterfaceinterface183/api-1559699-readpipeasync.md)
- [ReadPipeAsyncTO](./iousbinterfaceinterface183/api-1559070-readpipeasyncto.md)
- [ReadPipeTO](./iousbinterfaceinterface183/api-1559372-readpipeto.md)
- [Release](./iousbinterfaceinterface183/api-1558822-release.md)
- [ResetPipe](./iousbinterfaceinterface183/api-1559706-resetpipe.md)
- [SetAlternateInterface](./iousbinterfaceinterface183/api-1559407-setalternateinterface.md)
- [USBInterfaceClose](./iousbinterfaceinterface183/api-1558910-usbinterfaceclose.md)
- [USBInterfaceGetStringIndex](./iousbinterfaceinterface183/api-1559511-usbinterfacegetstringindex.md)
- [USBInterfaceOpen](./iousbinterfaceinterface183/api-1559439-usbinterfaceopen.md)
- [USBInterfaceOpenSeize](./iousbinterfaceinterface183/api-1559513-usbinterfaceopenseize.md)
  Opens the IOUSBInterface for exclusive access.
- [WriteIsochPipeAsync](./iousbinterfaceinterface183/api-1559535-writeisochpipeasync.md)
- [WritePipe](./iousbinterfaceinterface183/api-1559752-writepipe.md)
- [WritePipeAsync](./iousbinterfaceinterface183/api-1559532-writepipeasync.md)
- [WritePipeAsyncTO](./iousbinterfaceinterface183/api-1559569-writepipeasyncto.md)
- [WritePipeTO](./iousbinterfaceinterface183/api-1559014-writepipeto.md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iousbinterfaceinterface183)*