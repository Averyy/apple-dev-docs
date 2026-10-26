# IOFireWireLib.h

**Framework**: IOKit  
**Role**: API Collection

#### Overview

IOFireWireLib is the software used by user space software to communicate with FireWire devices and control the FireWire bus. IOFireWireLib is the lowest-level FireWire interface available in user space.

To communicate with a device on the FireWire bus, an instance of IOFireWireDeviceInterface (a struct which is defined below) is created. The methods of IOFireWireDeviceInterface allow you to communicate with the device and create instances of other interfaces which provide extended functionality (for example, creation of unit directories on the local machine).

References to interfaces should be kept using the interface reference typedefs defined herein. For example, you should use IOFireWireLibDeviceRef to refer to instances of IOFireWireDeviceInterface, IOFireWireLibCommandRef to refer to instances of IOFireWireCommandInterface, and so on.

To obtain an IOFireWireDeviceInterface for a device on the FireWire bus, use the function IOCreatePlugInInterfaceForService() defined in IOKit/IOCFPlugIn.h. (Note the "i" in "PlugIn" is always upper-case.) Quick usage reference:

- 'service' is a reference to the IOKit registry entry of the kernel object (usually of type IOFireWireDevice) representing the device of interest. This reference can be obtained using the functions defined in IOKit/IOKitLib.h.
- 'plugInType' should be CFUUIDGetUUIDBytes(kIOCFPlugInInterfaceID)
- 'interfaceType' should be CFUUIDGetUUIDBytes(kIOFireWireLibTypeID) when using IOFireWireLib

The interface returned by IOCreatePlugInInterfaceForService() should be deallocated using IODestroyPlugInInterface(). Do not call Release() on it.

##### Included Headers

- <CoreFoundation/CoreFoundation.h>
- <IOKit/IOCFPlugIn.h>
- <IOKit/firewire/IOFireWireFamilyCommon.h>

## Topics

### Miscellaneous
- [IOVirtualRangeMake](./api-1555660-iovirtualrangemake.md)
### Callbacks
- [IOFireWireBusResetDoneHandler](./iofirewirebusresetdonehandler.md)
  Called when a bus reset has occured and FireWire has completed configuring the bus.
- [IOFireWireBusResetHandler](./iofirewirebusresethandler.md)
  Called when a bus reset has occured, but before FireWire has completed configuring the bus.
- [IOFireWireLibCommandCallback](./iofirewirelibcommandcallback.md)
  Callback called when an asynchronous command has completed executing
- [IOFireWireLibIRMAllocationLostNotificationProc](./iofirewirelibirmallocationlostnotificationproc.md)
  Callback called when an IOFireWireLibIRMAllocationRef fails to reclaim IRM resources after a bus-reset
- [IOFireWireLibPHYPacketCallback](./iofirewirelibphypacketcallback.md)
  Callback called to handle incoming PHY packets
- [IOFireWireLibPHYPacketSkippedCallback](./iofirewirelibphypacketskippedcallback.md)
  Callback called when incoming packets have been dropped from the internal queue
- [IOFireWirePseudoAddressSpaceReadHandler](./iofirewirepseudoaddressspacereadhandler.md)
  This callback is called to handle read requests to pseudo address spaces. This function should fill in the specified area in the pseudo address space backing store and call ClientCommandIsComplete with the specified command ID
- [IOFireWirePseudoAddressSpaceSkippedPacketHandler](./iofirewirepseudoaddressspaceskippedpackethandler.md)
  Callback called when incoming packets have been dropped from the internal queue
- [IOFireWirePseudoAddressSpaceWriteHandler](./iofirewirepseudoaddressspacewritehandler.md)
  Callback called to handle write requests to a pseudo address space.
- [IOFWAsyncStreamListenerHandler](./iofwasyncstreamlistenerhandler.md)
  Callback called to handle Async Stream packets.
- [IOFWAsyncStreamListenerSkippedPacketHandler](./iofwasyncstreamlistenerskippedpackethandler.md)
  Callback called when incoming packets have been dropped from the internal queue
### Data Types
- [FWAddressSpaceFlags](./fwaddressspaceflags.md)
### Constants
- [IOFireWireLib Additional Command Flags](./api-1555858-iofirewirelib_additional_command.md)
  Flags for IOFireWireLib commands
- [IOFireWireLib Command Flags](./api-1556109-iofirewirelib_command_flags.md)
  Flags for IOFireWireLib command objects
- [IOFireWireLib failOnReset Flags](./api-1556012-iofirewirelib_failonreset_flags.md)
  Flags for IOFireWireLib commands


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iofirewirelib_h)*