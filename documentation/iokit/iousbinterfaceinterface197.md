# IOUSBInterfaceInterface197

**Framework**: IOKit  
**Kind**: struct  
**Role**: Structure

The object you use to access a USB device interface from user space, returned by the IOUSBFamily version 1.9.7 and above.

**Availability**:
- Mac Catalyst 18.4+
- macOS 10.2+

## Declaration

```c
typedef struct IOUSBInterfaceStruct197 {
    ...
} IOUSBInterfaceInterface197;
```

#### Overview

The functions listed here include all of the functions defined for the IOUSBInterfaceInterface, IOUSBInterfaceInterface182, IOUSBInterfaceInterface183, IOUSBInterfaceInterface190, IOUSBInterfaceInterface192, and some new functions that are available in macOS 10.2.5 and later.

## Topics

### Instance Properties
- [AbortPipe](./iousbinterfaceinterface197/api-1559245-abortpipe.md)
- [AddRef](./iousbinterfaceinterface197/api-1559620-addref.md)
- [ClearPipeStall](./iousbinterfaceinterface197/api-1558860-clearpipestall.md)
- [ClearPipeStallBothEnds](./iousbinterfaceinterface197/api-1559651-clearpipestallbothends.md)
- [ControlRequest](./iousbinterfaceinterface197/api-1559826-controlrequest.md)
- [ControlRequestAsync](./iousbinterfaceinterface197/api-1559694-controlrequestasync.md)
- [ControlRequestAsyncTO](./iousbinterfaceinterface197/api-1559498-controlrequestasyncto.md)
- [ControlRequestTO](./iousbinterfaceinterface197/api-1559328-controlrequestto.md)
- [CreateInterfaceAsyncEventSource](./iousbinterfaceinterface197/api-1558795-createinterfaceasynceventsource.md)
- [CreateInterfaceAsyncPort](./iousbinterfaceinterface197/api-1558917-createinterfaceasyncport.md)
- [GetAlternateSetting](./iousbinterfaceinterface197/api-1558804-getalternatesetting.md)
- [GetBandwidthAvailable](./iousbinterfaceinterface197/api-1558995-getbandwidthavailable.md)
- [GetBusFrameNumber](./iousbinterfaceinterface197/api-1558962-getbusframenumber.md)
- [GetBusMicroFrameNumber](./iousbinterfaceinterface197/api-1559654-getbusmicroframenumber.md)
  Gets the current micro frame number of the bus to which the interface and its device are attached.
- [GetConfigurationValue](./iousbinterfaceinterface197/api-1558859-getconfigurationvalue.md)
- [GetDevice](./iousbinterfaceinterface197/api-1558849-getdevice.md)
- [GetDeviceProduct](./iousbinterfaceinterface197/api-1559479-getdeviceproduct.md)
- [GetDeviceReleaseNumber](./iousbinterfaceinterface197/api-1559192-getdevicereleasenumber.md)
- [GetDeviceVendor](./iousbinterfaceinterface197/api-1559024-getdevicevendor.md)
- [GetEndpointProperties](./iousbinterfaceinterface197/api-1559541-getendpointproperties.md)
- [GetFrameListTime](./iousbinterfaceinterface197/api-1559003-getframelisttime.md)
  Returns the number of microseconds in each USB Frame.
- [GetIOUSBLibVersion](./iousbinterfaceinterface197/api-1559624-getiousblibversion.md)
  Returns the version of the IOUSBLib and the version of the IOUSBFamily.
- [GetInterfaceAsyncEventSource](./iousbinterfaceinterface197/api-1559249-getinterfaceasynceventsource.md)
- [GetInterfaceAsyncPort](./iousbinterfaceinterface197/api-1559297-getinterfaceasyncport.md)
- [GetInterfaceClass](./iousbinterfaceinterface197/api-1559446-getinterfaceclass.md)
- [GetInterfaceNumber](./iousbinterfaceinterface197/api-1559191-getinterfacenumber.md)
- [GetInterfaceProtocol](./iousbinterfaceinterface197/api-1558949-getinterfaceprotocol.md)
- [GetInterfaceSubClass](./iousbinterfaceinterface197/api-1558789-getinterfacesubclass.md)
- [GetLocationID](./iousbinterfaceinterface197/api-1559062-getlocationid.md)
- [GetNumEndpoints](./iousbinterfaceinterface197/api-1559641-getnumendpoints.md)
- [GetPipeProperties](./iousbinterfaceinterface197/api-1559700-getpipeproperties.md)
- [GetPipeStatus](./iousbinterfaceinterface197/api-1559113-getpipestatus.md)
- [LowLatencyCreateBuffer](./iousbinterfaceinterface197/api-1559301-lowlatencycreatebuffer.md)
- [LowLatencyDestroyBuffer](./iousbinterfaceinterface197/api-1559465-lowlatencydestroybuffer.md)
- [LowLatencyReadIsochPipeAsync](./iousbinterfaceinterface197/api-1558979-lowlatencyreadisochpipeasync.md)
- [LowLatencyWriteIsochPipeAsync](./iousbinterfaceinterface197/api-1559445-lowlatencywriteisochpipeasync.md)
- [QueryInterface](./iousbinterfaceinterface197/api-1559553-queryinterface.md)
- [ReadIsochPipeAsync](./iousbinterfaceinterface197/api-1558747-readisochpipeasync.md)
- [ReadPipe](./iousbinterfaceinterface197/api-1559111-readpipe.md)
- [ReadPipeAsync](./iousbinterfaceinterface197/api-1559118-readpipeasync.md)
- [ReadPipeAsyncTO](./iousbinterfaceinterface197/api-1558769-readpipeasyncto.md)
- [ReadPipeTO](./iousbinterfaceinterface197/api-1559020-readpipeto.md)
- [Release](./iousbinterfaceinterface197/api-1559491-release.md)
- [ResetPipe](./iousbinterfaceinterface197/api-1558901-resetpipe.md)
- [SetAlternateInterface](./iousbinterfaceinterface197/api-1559212-setalternateinterface.md)
- [SetPipePolicy](./iousbinterfaceinterface197/api-1559326-setpipepolicy.md)
- [USBInterfaceClose](./iousbinterfaceinterface197/api-1559801-usbinterfaceclose.md)
- [USBInterfaceGetStringIndex](./iousbinterfaceinterface197/api-1559331-usbinterfacegetstringindex.md)
- [USBInterfaceOpen](./iousbinterfaceinterface197/api-1559275-usbinterfaceopen.md)
- [USBInterfaceOpenSeize](./iousbinterfaceinterface197/api-1559571-usbinterfaceopenseize.md)
- [WriteIsochPipeAsync](./iousbinterfaceinterface197/api-1558903-writeisochpipeasync.md)
- [WritePipe](./iousbinterfaceinterface197/api-1559286-writepipe.md)
- [WritePipeAsync](./iousbinterfaceinterface197/api-1559352-writepipeasync.md)
- [WritePipeAsyncTO](./iousbinterfaceinterface197/api-1559187-writepipeasyncto.md)
- [WritePipeTO](./iousbinterfaceinterface197/api-1559825-writepipeto.md)

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
- [IOUSBInterfaceInterface192](./iousbinterfaceinterface192.md)
  The object you use to access a USB device interface from user space, returned by the IOUSBFamily version 1.9.2 and above.
- [MMCDeviceInterface](./mmcdeviceinterface.md)
  Basic interface for an MMC-2 Compliant Device.
- [SCSITaskDeviceInterface](./scsitaskdeviceinterface.md)
  Basic interface for a SCSITask Device.
- [SCSITaskInterface](./scsitaskinterface.md)
  Basic interface for a SCSITask.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iousbinterfaceinterface197)*