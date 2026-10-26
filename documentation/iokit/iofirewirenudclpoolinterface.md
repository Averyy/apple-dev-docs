# IOFireWireNuDCLPoolInterface

**Framework**: IOKit  
**Kind**: struct  
**Role**: Structure

Use this interface to build NuDCL-based DCL programs.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.3+

## Declaration

```c
typedef struct IOFireWireNuDCLPoolInterface_t {
    ...
} IOFireWireNuDCLPoolInterface;
```

## Topics

### Miscellaneous
- [AllocateReceivePacket](./iofirewirenudclpoolinterface/api-1569189-allocatereceivepacket.md)
  Allocate a ReceivePacket NuDCL and append it to the program
- [AllocateReceivePacket_v](./iofirewirenudclpoolinterface/api-1569299-allocatereceivepacket_v.md)
  Allocate a ReceivePacket NuDCL and append it to the program
- [AllocateSendPacket](./iofirewirenudclpoolinterface/api-1569297-allocatesendpacket.md)
  Allocate a SendPacket NuDCL and append it to the program.
- [AllocateSendPacket_v](./iofirewirenudclpoolinterface/api-1569323-allocatesendpacket_v.md)
  Allocate a SendPacket NuDCL and append it to the program.
- [AllocateSkipCycle](./iofirewirenudclpoolinterface/api-1569236-allocateskipcycle.md)
  Allocate a SkipCycle NuDCL and append it to the program.
- [AppendDCLRanges](./iofirewirenudclpoolinterface/api-1569263-appenddclranges.md)
  Add a memory range to the scatter gather list of a NuDCL
- [AppendDCLUpdateList](./iofirewirenudclpoolinterface/api-1569230-appenddclupdatelist.md)
- [CopyDCLUpdateList](./iofirewirenudclpoolinterface/api-1569302-copydclupdatelist.md)
- [CountDCLRanges](./iofirewirenudclpoolinterface/api-1569365-countdclranges.md)
  Returns number of buffers for a NuDCL
- [FindDCLNextDCL](./iofirewirenudclpoolinterface/api-1569217-finddclnextdcl.md)
  Get the next pointer for a NuDCL
- [GetDCLBranch](./iofirewirenudclpoolinterface/api-1569274-getdclbranch.md)
  Get the branch pointer for a NuDCL
- [GetDCLCallback](./iofirewirenudclpoolinterface/api-1569314-getdclcallback.md)
  Get callback for a NuDCL
- [GetDCLFlags](./iofirewirenudclpoolinterface/api-1569338-getdclflags.md)
- [GetDCLRanges](./iofirewirenudclpoolinterface/api-1569226-getdclranges.md)
  Get the scatter-gather list for a NuDCL
- [GetDCLRefcon](./iofirewirenudclpoolinterface/api-1569337-getdclrefcon.md)
- [GetDCLs](./iofirewirenudclpoolinterface/api-1569203-getdcls.md)
  Returns the pool's DCL program as a CFArray of NuDCLRef's.
- [GetDCLSize](./iofirewirenudclpoolinterface/api-1569253-getdclsize.md)
  Returns number of bytes to be transferred by a NuDCL
- [GetDCLSkipBranch](./iofirewirenudclpoolinterface/api-1569220-getdclskipbranch.md)
- [GetDCLSkipCallback](./iofirewirenudclpoolinterface/api-1569350-getdclskipcallback.md)
- [GetDCLSkipRefcon](./iofirewirenudclpoolinterface/api-1569331-getdclskiprefcon.md)
- [GetDCLSpan](./iofirewirenudclpoolinterface/api-1569262-getdclspan.md)
  Returns a virtual range spanning lowest referenced buffer address to highest
- [GetDCLStatusPtr](./iofirewirenudclpoolinterface/api-1569185-getdclstatusptr.md)
  Get the status pointer for a NuDCL.
- [GetDCLSyncBits](./iofirewirenudclpoolinterface/api-1569280-getdclsyncbits.md)
- [GetDCLTagBits](./iofirewirenudclpoolinterface/api-1569209-getdcltagbits.md)
- [GetDCLTimeStampPtr](./iofirewirenudclpoolinterface/api-1569218-getdcltimestampptr.md)
  Get the time stamp pointer for a NuDCL.
- [GetDCLUserHeaderPtr](./iofirewirenudclpoolinterface/api-1569294-getdcluserheaderptr.md)
- [GetProgram](./iofirewirenudclpoolinterface/api-1569183-getprogram.md)
  Finds the first DCL in the pool not preceeded by any other DCL.
- [GetUserHeaderMaskPtr](./iofirewirenudclpoolinterface/api-1569211-getuserheadermaskptr.md)
- [PrintDCL](./iofirewirenudclpoolinterface/api-1569336-printdcl.md)
- [PrintProgram](./iofirewirenudclpoolinterface/api-1569279-printprogram.md)
- [RemoveDCLUpdateList](./iofirewirenudclpoolinterface/api-1569281-removedclupdatelist.md)
- [SetCurrentTagAndSync](./iofirewirenudclpoolinterface/api-1569304-setcurrenttagandsync.md)
  Set current tag and sync bits
- [SetDCLBranch](./iofirewirenudclpoolinterface/api-1569290-setdclbranch.md)
  Set the branch pointer for a NuDCL
- [SetDCLCallback](./iofirewirenudclpoolinterface/api-1569248-setdclcallback.md)
  Set the callback for a NuDCL
- [SetDCLFlags](./iofirewirenudclpoolinterface/api-1569321-setdclflags.md)
- [SetDCLRanges](./iofirewirenudclpoolinterface/api-1569310-setdclranges.md)
  Set the scatter gather list for a NuDCL
- [SetDCLRefcon](./iofirewirenudclpoolinterface/api-1569363-setdclrefcon.md)
- [SetDCLSkipBranch](./iofirewirenudclpoolinterface/api-1569198-setdclskipbranch.md)
- [SetDCLSkipCallback](./iofirewirenudclpoolinterface/api-1569352-setdclskipcallback.md)
- [SetDCLSkipRefcon](./iofirewirenudclpoolinterface/api-1569313-setdclskiprefcon.md)
- [SetDCLStatusPtr](./iofirewirenudclpoolinterface/api-1569282-setdclstatusptr.md)
  Set the status pointer for a NuDCL
- [SetDCLSyncBits](./iofirewirenudclpoolinterface/api-1569275-setdclsyncbits.md)
- [SetDCLTagBits](./iofirewirenudclpoolinterface/api-1569229-setdcltagbits.md)
- [SetDCLTimeStampPtr](./iofirewirenudclpoolinterface/api-1569346-setdcltimestampptr.md)
  Set the time stamp pointer for a NuDCL
- [SetDCLUpdateList](./iofirewirenudclpoolinterface/api-1569340-setdclupdatelist.md)
- [SetDCLUserHeaderPtr](./iofirewirenudclpoolinterface/api-1569249-setdcluserheaderptr.md)
  Set a user specified header for a send NuDCL
- [SetDCLWaitControl](./iofirewirenudclpoolinterface/api-1569186-setdclwaitcontrol.md)
### Instance Variables
- [version](./iofirewirenudclpoolinterface/api-1569322-version.md)
- [revision](./iofirewirenudclpoolinterface/api-1569232-revision.md)
### Instance Properties
- [AddRef](./iofirewirenudclpoolinterface/api-1569234-addref.md)
- [QueryInterface](./iofirewirenudclpoolinterface/api-1569315-queryinterface.md)
- [Release](./iofirewirenudclpoolinterface/api-1569197-release.md)
- [SetDCLRanges_v](./iofirewirenudclpoolinterface/api-1569308-setdclranges_v.md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iofirewirenudclpoolinterface)*