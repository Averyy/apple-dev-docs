# IOFireWireLocalIsochPortInterface

**Framework**: IOKit  
**Kind**: struct  
**Role**: Structure

FireWire user client local isochronous port object.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.1+

## Declaration

```c
typedef struct IOFireWireLocalIsochPortInterface_t {
    ...
} IOFireWireLocalIsochPortInterface;
```

## Overview

Represents a FireWire isochronous talker or listener within the local machine. Isochronous transfer is controlled by an associated DCL (Data Stream Control Language) program, which is similar to a hardware DMA program but is hardware agnostic. DCL programs can be written using the IOFireWireDCLCommandPoolInterface object.

This interface contains all methods of IOFireWireIsochPortInterface and IOFireWireLocalIsochPortInterface. This interface will contain all v2 methods of IOFireWireLocalIsochPortInterface when instantiated as v2 or newer.

Transfer buffers for the local isoch port must all come from a single allocation made with vm_allocate() or mmap(..., MAP_ANON ).

Calling vm_deallocate() on the buffers before deallocating a local isoch port object may result in a deadlock.

Note: Calling Release() on the local isoch port may not immediately release the isoch port; so it may not be safe to call vm_deallocate() on your transfer buffers. To guarantee the port has been release, run the isochronous runloop until the port is finalized (it has processed any pending callbacks). The finalize callback will be called when the port is finalized. Set the finalize callback using SetFinalizeCallback().

## Topics

### Miscellaneous
- [AllocatePort](./iofirewirelocalisochportinterface/api-1569283-allocateport.md)
  The method is called when the port should configure its associated hardware to prepare to send or receive isochronous data on the channel number and at the speed specified.
- [GetRefCon](./iofirewirelocalisochportinterface/api-1569219-getrefcon.md)
  Get reference value associated with this port.
- [GetSupported](./iofirewirelocalisochportinterface/api-1569242-getsupported.md)
  The method is called to determine which FireWire isochronous channels and speed this port supports.
- [ModifyJumpDCL](./iofirewirelocalisochportinterface/api-1569296-modifyjumpdcl.md)
  Change the jump target label of a jump DCL.
- [ModifyTransferPacketDCL](./iofirewirelocalisochportinterface/api-1569359-modifytransferpacketdcl.md)
  Modify the transfer size of a transfer packet DCL (send or receive)
- [ModifyTransferPacketDCLBuffer](./iofirewirelocalisochportinterface/api-1569193-modifytransferpacketdclbuffer.md)
  NOT IMPLEMENTED. Modify the transfer size of a transfer packet DCL (send or receive)
- [ModifyTransferPacketDCLSize](./iofirewirelocalisochportinterface/api-1569237-modifytransferpacketdclsize.md)
  Modify the transfer size of a transfer packet DCL (send or receive)
- [PrintDCLProgram](./iofirewirelocalisochportinterface/api-1569238-printdclprogram.md)
  Display the contents of a DCL program.
- [ReleasePort](./iofirewirelocalisochportinterface/api-1569332-releaseport.md)
  The method is called to release the hardware after the channel has been stopped.
- [SetFinalizeCallback](./iofirewirelocalisochportinterface/api-1569239-setfinalizecallback.md)
  Set the finalize callback for a local isoch port
- [SetRefCon](./iofirewirelocalisochportinterface/api-1569318-setrefcon.md)
  Set reference value associated with this port.
- [Start](./iofirewirelocalisochportinterface/api-1569339-start.md)
  The method is called when the port is to begin talking or listening.
- [Stop](./iofirewirelocalisochportinterface/api-1569247-stop.md)
  The method is called when the port is to stop talking or listening.
### Instance Variables
- [version](./iofirewirelocalisochportinterface/api-1569207-version.md)
- [revision](./iofirewirelocalisochportinterface/api-1569184-revision.md)
### Instance Properties
- [AddRef](./iofirewirelocalisochportinterface/api-1569293-addref.md)
- [Notify](./iofirewirelocalisochportinterface/api-1569231-notify.md)
- [QueryInterface](./iofirewirelocalisochportinterface/api-1569271-queryinterface.md)
- [Release](./iofirewirelocalisochportinterface/api-1569288-release.md)
- [SetResourceUsageFlags](./iofirewirelocalisochportinterface/api-1569228-setresourceusageflags.md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iofirewirelocalisochportinterface)*