# IOFireWireSBP2LibLoginInterface

**Framework**: IOKit  
**Kind**: struct  
**Role**: Structure

Supplies the login maintenance and Normal Command ORB execution portions of the API.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```c
typedef struct IOFireWireSBP2LibLoginInterface {
    ...
} IOFireWireSBP2LibLoginInterface;
```

#### Overview

Supplies APIs for login maintenance and command execution. Drivers can use this object to create IOFireWireSBP2LibORBInterface objects and execute them. Solicited and unsolicited status callback routines can be registered and the SBP2 services will notify the driver when the appropriate status arrives. This class also handles login maintenance. Supplies APIs for logging in and logging out and attempts to reconnect to the LUN after bus resets. The base FireWire services deliver bus reset notification via the IOKit message routine. The SBP2 services build on this behavior and deliver reconnectFailed and reconnectComplete through the message routine as well.

## Topics

### Instance Properties
- [AddRef](./iofirewiresbp2liblogininterface/api-1590571-addref.md)
- [QueryInterface](./iofirewiresbp2liblogininterface/api-1590543-queryinterface.md)
- [Release](./iofirewiresbp2liblogininterface/api-1590441-release.md)
- [createORB](./iofirewiresbp2liblogininterface/api-1590437-createorb.md)
  Creates a new IOFireWireSBP2ORB for this login.
- [enableUnsolicitedStatus](./iofirewiresbp2liblogininterface/api-1590454-enableunsolicitedstatus.md)
  Enables unsolicited status.
- [getLoginID](./iofirewiresbp2liblogininterface/api-1590456-getloginid.md)
  Returns the current login ID.
- [getMaxCommandBlockSize](./iofirewiresbp2liblogininterface/api-1590447-getmaxcommandblocksize.md)
  Returns the maximum command block size.
- [getRefCon](./iofirewiresbp2liblogininterface/api-1590546-getrefcon.md)
  Returns the refCon set with setRefCon.
- [revision](./iofirewiresbp2liblogininterface/api-1590449-revision.md)
- [ringDoorbell](./iofirewiresbp2liblogininterface/api-1590504-ringdoorbell.md)
  Rings the doorbell on the LUN.
- [setBusyTimeoutRegisterValue](./iofirewiresbp2liblogininterface/api-1590478-setbusytimeoutregistervalue.md)
  Sets the value to be written to the BUSY_TIMEOUT register.
- [setFetchAgentResetCallback](./iofirewiresbp2liblogininterface/api-1590513-setfetchagentresetcallback.md)
  Sets the callback to be called when a fetch agent reset completes.
- [setFetchAgentWriteCallback](./iofirewiresbp2liblogininterface/api-1590505-setfetchagentwritecallback.md)
  Sets the callback to be called when the fetch agent write completes.
- [setLoginCallback](./iofirewiresbp2liblogininterface/api-1590540-setlogincallback.md)
  Sets the callback to be called when a login attempt is complete.
- [setLoginFlags](./iofirewiresbp2liblogininterface/api-1590531-setloginflags.md)
  Sets login configuration flags.
- [setLogoutCallback](./iofirewiresbp2liblogininterface/api-1590492-setlogoutcallback.md)
  Sets the callback to be called when a logout attempt is complete.
- [setMaxPayloadSize](./iofirewiresbp2liblogininterface/api-1590576-setmaxpayloadsize.md)
  Sets the maximum data transfer length for a normal command ORB.
- [setPassword](./iofirewiresbp2liblogininterface/api-1590488-setpassword.md)
  Sets the login password.
- [setReconnectTime](./iofirewiresbp2liblogininterface/api-1590547-setreconnecttime.md)
  Sets the desired reconnect duration.
- [setRefCon](./iofirewiresbp2liblogininterface/api-1590544-setrefcon.md)
  Sets the login refCon.
- [setStatusNotify](./iofirewiresbp2liblogininterface/api-1590419-setstatusnotify.md)
  Sets the callback to be called on normal command status.
- [setUnsolicitedStatusNotify](./iofirewiresbp2liblogininterface/api-1590568-setunsolicitedstatusnotify.md)
  Sets the callback to be called on normal command status.
- [submitFetchAgentReset](./iofirewiresbp2liblogininterface/api-1590541-submitfetchagentreset.md)
  Resets the LUN's fetch agent.
- [submitLogin](./iofirewiresbp2liblogininterface/api-1590431-submitlogin.md)
  Attempts to login to the LUN.
- [submitLogout](./iofirewiresbp2liblogininterface/api-1590484-submitlogout.md)
  Attempts to logout of the LUN.
- [submitORB](./iofirewiresbp2liblogininterface/api-1590476-submitorb.md)
  Submits the given orb
- [version](./iofirewiresbp2liblogininterface/api-1590515-version.md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iofirewiresbp2liblogininterface)*