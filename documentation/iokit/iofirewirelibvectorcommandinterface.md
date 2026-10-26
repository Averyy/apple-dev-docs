# IOFireWireLibVectorCommandInterface

**Framework**: IOKit  
**Kind**: struct  
**Role**: Structure

IOFireWireLib command object for grouping commands execution.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.5+

## Declaration

```c
typedef struct IOFireWireLibVectorCommandInterface_t {
    ...
} IOFireWireLibVectorCommandInterface;
```

#### Overview

Read and Write commands can be attached in order to the vector command. When the vector command is submitted all the commands are sent to the kernel for execution. When all the commands in a vector command are complete the vector command's completion is called. The advantage over submitting and completeing each command simultaneously is that only one kernel transition will be used for submission and one for completion, regardless of the number of commands in the vector.

## Topics

### Miscellaneous
- [AddCommand](./iofirewirelibvectorcommandinterface/api-1555740-addcommand.md)
  Adds a command to the vector command.
- [EnsureCapacity](./iofirewirelibvectorcommandinterface/api-1555615-ensurecapacity.md)
  Sets the number of commands this vector can hold.
- [GetCommandAtIndex](./iofirewirelibvectorcommandinterface/api-1556052-getcommandatindex.md)
  Returns the command at a given index.
- [GetCommandCount](./iofirewirelibvectorcommandinterface/api-1555752-getcommandcount.md)
  Returns the number of commands currently in this vector.
- [GetFlags](./iofirewirelibvectorcommandinterface/api-1555608-getflags.md)
  Get the flags currently set for this command.
- [GetIndexOfCommand](./iofirewirelibvectorcommandinterface/api-1555861-getindexofcommand.md)
  Returns the index of the specified command.
- [GetRefCon](./iofirewirelibvectorcommandinterface/api-1555688-getrefcon.md)
  Get the reference constant for this command.
- [InsertCommandAtIndex](./iofirewirelibvectorcommandinterface/api-1556014-insertcommandatindex.md)
  Inserts a command at a given index. Commands at and after this index will be moved to their next sequential index.
- [IsExecuting](./iofirewirelibvectorcommandinterface/api-1555674-isexecuting.md)
  Checks if the vector command is currently executing.
- [RemoveAllCommands](./iofirewirelibvectorcommandinterface/api-1555889-removeallcommands.md)
  Removes all commands from the vector.
- [RemoveCommand](./iofirewirelibvectorcommandinterface/api-1556118-removecommand.md)
  Removes a command to the vector command.
- [RemoveCommandAtIndex](./iofirewirelibvectorcommandinterface/api-1556038-removecommandatindex.md)
  Removes the command at a give index. Commands at and afte this index will be moved to their previous sequential index.
- [SetCallback](./iofirewirelibvectorcommandinterface/api-1556100-setcallback.md)
  Set the callback routine for this command.
- [SetFlags](./iofirewirelibvectorcommandinterface/api-1556107-setflags.md)
  Set flags governing this command's execution.
- [SetRefCon](./iofirewirelibvectorcommandinterface/api-1555654-setrefcon.md)
  Set the reference constant for this command.
- [Submit(IOFireWireLibVectorCommandRef)](./iofirewirelibvectorcommandinterface/submit_iofirewirelibvectorcommandref.md)
  Submit this command object to FireWire for execution.
- [Submit(IOFireWireLibVectorCommandRef, void *, IOFireWireLibCommandCallback)](./iofirewirelibvectorcommandinterface/submit_iofirewirelibvectorcommandref_void_iofirewirelibcommandcallback.md)
  Submit this command object to FireWire for execution.
- [SubmitWithRefconAndCallback](./iofirewirelibvectorcommandinterface/api-1555731-submitwithrefconandcallback.md)
  Submit this command object to FireWire for execution.
### Instance Variables
- [version](./iofirewirelibvectorcommandinterface/api-1555613-version.md)
- [revision](./iofirewirelibvectorcommandinterface/api-1555650-revision.md)
### Instance Properties
- [AddRef](./iofirewirelibvectorcommandinterface/api-1556066-addref.md)
- [QueryInterface](./iofirewirelibvectorcommandinterface/api-1555621-queryinterface.md)
- [Release](./iofirewirelibvectorcommandinterface/api-1555709-release.md)
- [Submit](./iofirewirelibvectorcommandinterface/api-1555700-submit.md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iofirewirelibvectorcommandinterface)*