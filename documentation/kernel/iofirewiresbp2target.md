# IOFireWireSBP2Target

**Framework**: Kernel  
**Kind**: cl

Serves as bridge between IOFireWireUnit and IOFireWireLUN.

**Availability**:
- macOS 10.0+

## Declaration

```swift
class IOFireWireSBP2Target : IOService
```

#### Overview

Matches against IOFireWireUnits supporting the SBP2 protocol. Creates IOFireWireSBP2LUN nubs for matching. Most drivers will match against an IOFireWireSBP2LUN, but matching against an IOFireWireSBP2Target is also supported. This can be useful in cases where a single driver wishes to control all LUNs on a device. Support for this technique is minimal, however, and the driver will be required to discover it's LUNs through the registry.

## Topics

### Miscellaneous
- [getFireWireUnit](iofirewiresbp2target/1812999-getfirewireunit.md)
  Returns an IOFireWireUnit object.
- [handleClose](iofirewiresbp2target/1813009-handleclose.md)
  Overrideable method to control the open / close behaviour of an IOService.
- [handleIsOpen](iofirewiresbp2target/1813021-handleisopen.md)
  Overrideable method to control the open / close behaviour of an IOService.
- [handleOpen](iofirewiresbp2target/1813037-handleopen.md)
  Overrideable method to control the open / close behaviour of an IOService.
- [matchPropertyTable](iofirewiresbp2target/1813051-matchpropertytable.md)
  Implements SBP2 specific matching.
- [start](iofirewiresbp2target/1813074-start.md)
  During an IOService instantiation, the start method is called when the IOService has been selected to run on the provider.
- [stop](iofirewiresbp2target/1813099-stop.md)
  During an IOService termination, the stop method is called in its clients before they are detached & it is destroyed.
### Instance Methods
- [- beginIOCriticalSection](iofirewiresbp2target/1580295-beginiocriticalsection.md)
- [- cancelMgmtAgentAccess](iofirewiresbp2target/1580286-cancelmgmtagentaccess.md)
- [- clearMgmtAgentAccess](iofirewiresbp2target/1580304-clearmgmtagentaccess.md)
- [- clearTargetFlags](iofirewiresbp2target/1580300-cleartargetflags.md)
- [- completeMgmtAgentAccess](iofirewiresbp2target/1580289-completemgmtagentaccess.md)
- [- configurePhysicalFilter](iofirewiresbp2target/1580292-configurephysicalfilter.md)
- [- createLUN](iofirewiresbp2target/1580306-createlun.md)
- [- endIOCriticalSection](iofirewiresbp2target/1580287-endiocriticalsection.md)
- [- finalize](iofirewiresbp2target/1580291-finalize.md)
- [- free](iofirewiresbp2target/1580301-free.md)
- [- getFireWireUnit](iofirewiresbp2target/1580285-getfirewireunit.md)
- [- getMetaClass](iofirewiresbp2target/1580305-getmetaclass.md)
- [- getTargetFlags](iofirewiresbp2target/1580288-gettargetflags.md)
- [- handleClose](iofirewiresbp2target/1580302-handleclose.md)
- [- handleIsOpen](iofirewiresbp2target/1580299-handleisopen.md)
- [- handleOpen](iofirewiresbp2target/1580282-handleopen.md)
- [- matchPropertyTable](iofirewiresbp2target/1580293-matchpropertytable.md)
- [- message](iofirewiresbp2target/1580298-message.md)
- [- scanForLUNs](iofirewiresbp2target/1580303-scanforluns.md)
- [- setTargetFlags](iofirewiresbp2target/1580281-settargetflags.md)
- [- start](iofirewiresbp2target/1580284-start.md)
- [- stop](iofirewiresbp2target/1580294-stop.md)
- [- synchMgmtAgentAccess](iofirewiresbp2target/1580296-synchmgmtagentaccess.md)

## Relationships

### Inherits From
- [IOService](ioservice.md)

## See Also

- [IOFireWireSerialBusProtocolTransport](iofirewireserialbusprotocoltransport.md)
  SCSI Protocol Driver Family for FireWire SBP2 Devices.
- [IOFireWireController](iofirewirecontroller.md)
- [IOFireWireBus](iofirewirebus.md)
  IOFireWireBus is a public class the provides access to general FireWire functionality...


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iofirewiresbp2target)*