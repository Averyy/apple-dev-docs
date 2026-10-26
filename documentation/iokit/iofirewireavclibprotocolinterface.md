# IOFireWireAVCLibProtocolInterface

**Framework**: IOKit  
**Kind**: struct  
**Role**: Structure

Initial interface discovered for all AVC protocol drivers.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.2+

## Declaration

```c
typedef struct _IOFireWireAVCLibProtocolInterface {
    ...
} IOFireWireAVCLibProtocolInterface;
```

#### Overview

The IOFireWireAVCLibProtocolInterface is used to set up local plug control registers and to receive AVC requests.

## Topics

### Instance Properties
- [AddRef](./iofirewireavclibprotocolinterface/api-1508856-addref.md)
- [QueryInterface](./iofirewireavclibprotocolinterface/api-1508784-queryinterface.md)
- [Release](./iofirewireavclibprotocolinterface/api-1508829-release.md)
- [addCallbackDispatcherToRunLoop](./iofirewireavclibprotocolinterface/api-1508773-addcallbackdispatchertorunloop.md)
  Adds a dispatcher for kernel callbacks to the specified run loop.
- [addSubunit](./iofirewireavclibprotocolinterface/api-1508740-addsubunit.md)
  Installs a virtual AVC subunit.
- [allocateInputPlug](./iofirewireavclibprotocolinterface/api-1508762-allocateinputplug.md)
  Allocates an input plug.
- [allocateOutputPlug](./iofirewireavclibprotocolinterface/api-1508776-allocateoutputplug.md)
  Allocates an output plug.
- [connectTargetPlugs](./iofirewireavclibprotocolinterface/api-1508771-connecttargetplugs.md)
  Establishes an internal AVC plug connection between subunit/unit plugs.
- [disconnectTargetPlugs](./iofirewireavclibprotocolinterface/api-1508815-disconnecttargetplugs.md)
  Breaks an internal AVC plug connection between subunit/unit plugs.
- [freeInputPlug](./iofirewireavclibprotocolinterface/api-1508863-freeinputplug.md)
  Deallocates an input plug.
- [freeOutputPlug](./iofirewireavclibprotocolinterface/api-1508753-freeoutputplug.md)
  Deallocates an output plug.
- [getSubunitPlugSignalFormat](./iofirewireavclibprotocolinterface/api-1508742-getsubunitplugsignalformat.md)
  Gets the signal format of the specifed plug.
- [getTargetPlugConnection](./iofirewireavclibprotocolinterface/api-1508823-gettargetplugconnection.md)
  Gets the connection details for a specific plug.
- [installAVCCommandHandler](./iofirewireavclibprotocolinterface/api-1508800-installavccommandhandler.md)
  Installs a command handler for handling specific incoming AVC commands.
- [publishAVCUnitDirectory](./iofirewireavclibprotocolinterface/api-1508772-publishavcunitdirectory.md)
  Publishes an AVC unit directory in the config ROM.
- [readInputMasterPlug](./iofirewireavclibprotocolinterface/api-1508765-readinputmasterplug.md)
  Returns the current value of the input primary plug.
- [readInputPlug](./iofirewireavclibprotocolinterface/api-1508758-readinputplug.md)
  Returns the current value of an input plug.
- [readOutputMasterPlug](./iofirewireavclibprotocolinterface/api-1508810-readoutputmasterplug.md)
  Returns the current value of the output primary plug.
- [readOutputPlug](./iofirewireavclibprotocolinterface/api-1508847-readoutputplug.md)
  Returns the current value of an output plug.
- [removeCallbackDispatcherFromRunLoop](./iofirewireavclibprotocolinterface/api-1508824-removecallbackdispatcherfromrunl.md)
  Removes a dispatcher for kernel callbacks to the specified run loop.
- [revision](./iofirewireavclibprotocolinterface/api-1508855-revision.md)
- [sendAVCResponse](./iofirewireavclibprotocolinterface/api-1508835-sendavcresponse.md)
  Sends an AVC response packet.
- [setAVCRequestCallback](./iofirewireavclibprotocolinterface/api-1508881-setavcrequestcallback.md)
  This function has been deprecated. Use installAVCCommandHandler instead.
- [setMessageCallback](./iofirewireavclibprotocolinterface/api-1508849-setmessagecallback.md)
  Sets callback for user space message routine.
- [setSubunitPlugSignalFormat](./iofirewireavclibprotocolinterface/api-1508809-setsubunitplugsignalformat.md)
  Sets the signal format of the specifed plug.
- [updateInputMasterPlug](./iofirewireavclibprotocolinterface/api-1508884-updateinputmasterplug.md)
  Updates the value of the primary input plug (simulating a lock transaction).
- [updateInputPlug](./iofirewireavclibprotocolinterface/api-1508858-updateinputplug.md)
  Updates the value of an input plug (simulating a lock transaction).
- [updateOutputMasterPlug](./iofirewireavclibprotocolinterface/api-1508827-updateoutputmasterplug.md)
  Updates the value of the primary output plug (simulating a lock transaction).
- [updateOutputPlug](./iofirewireavclibprotocolinterface/api-1508878-updateoutputplug.md)
  Updates the value of an output plug (simulating a lock transaction).
- [version](./iofirewireavclibprotocolinterface/api-1508877-version.md)

## See Also

### COM Interfaces
- [IOATASMARTInterface](./ioatasmartinterface.md)
  Self-Monitoring, Analysis, and Reporting Technology Interface.
- [IOFireWireAsyncStreamCommandInterface](./iofirewireasyncstreamcommandinterface.md)
- [IOFireWireAVCLibConsumerInterface](./iofirewireavclibconsumerinterface.md)
  Interface for an asynchronous connection consumer.
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
- [IOUSBInterfaceInterface197](./iousbinterfaceinterface197.md)
  The object you use to access a USB device interface from user space, returned by the IOUSBFamily version 1.9.7 and above.
- [MMCDeviceInterface](./mmcdeviceinterface.md)
  Basic interface for an MMC-2 Compliant Device.
- [SCSITaskDeviceInterface](./scsitaskdeviceinterface.md)
  Basic interface for a SCSITask Device.
- [SCSITaskInterface](./scsitaskinterface.md)
  Basic interface for a SCSITask.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iofirewireavclibprotocolinterface)*