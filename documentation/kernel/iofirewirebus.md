# IOFireWireBus

**Framework**: Kernel  
**Kind**: cl  
**Role**: Class

IOFireWireBus is a public class the provides access to general FireWire functionality...

**Availability**:
- macOS 10.0+

## Declaration

```cpp
class IOFireWireBus : IOService
```

## Overview

## Topics

### Miscellaneous
- [createLocalIsochPort](./iofirewirebus/api-1811054-createlocalisochport.md)
  Create a local isochronous port to run the given DCL program
### Instance Methods
- [- AddUnitDirectory](./iofirewirebus/api-1571482-addunitdirectory.md)
- [- RemoveUnitDirectory](./iofirewirebus/api-1571473-removeunitdirectory.md)
- [- createAsyncStreamCommand](./iofirewirebus/api-1571461-createasyncstreamcommand.md)
- [- createAsyncStreamCommand](./iofirewirebus/api-3516562-createasyncstreamcommand.md)
- [- createAuxiliary](./iofirewirebus/api-1571483-createauxiliary.md)
- [- createDCLPool](./iofirewirebus/api-1571491-createdclpool.md)
- [- createDelayedCmd](./iofirewirebus/api-1571451-createdelayedcmd.md)
- [- createInitialAddressSpace](./iofirewirebus/api-1571464-createinitialaddressspace.md)
- [- createIsochChannel](./iofirewirebus/api-1571476-createisochchannel.md)
- [- createLocalIsochPort](./iofirewirebus/api-1571438-createlocalisochport.md)
- [- createPhysicalAddressSpace](./iofirewirebus/api-1571472-createphysicaladdressspace.md)
- [- createPseudoAddressSpace](./iofirewirebus/api-1571440-createpseudoaddressspace.md)
- [- createSimpleContiguousPhysicalAddressSpace](./iofirewirebus/api-1571456-createsimplecontiguousphysicalad.md)
- [- createSimplePhysicalAddressSpace](./iofirewirebus/api-1571468-createsimplephysicaladdressspace.md)
- [- getAddressSpace](./iofirewirebus/api-1571467-getaddressspace.md)
- [- getBusCycleTime](./iofirewirebus/api-1571453-getbuscycletime.md)
- [- getBusPowerManager](./iofirewirebus/api-1571489-getbuspowermanager.md)
- [- getCycleTime](./iofirewirebus/api-1571485-getcycletime.md)
- [- getExtendedTCode](./iofirewirebus/api-1571452-getextendedtcode.md)
- [- getFireWirePhysicalAddressBits](./iofirewirebus/api-1571469-getfirewirephysicaladdressbits.md)
- [- getFireWirePhysicalAddressMask](./iofirewirebus/api-1571475-getfirewirephysicaladdressmask.md)
- [- getFireWirePhysicalBufferBits](./iofirewirebus/api-1571439-getfirewirephysicalbufferbits.md)
- [- getFireWirePhysicalBufferMask](./iofirewirebus/api-1571448-getfirewirephysicalbuffermask.md)
- [- getMaxRec](./iofirewirebus/api-1571454-getmaxrec.md)
- [- getMetaClass](./iofirewirebus/api-1571487-getmetaclass.md)
- [- getSessionRefExporter](./iofirewirebus/api-1571484-getsessionrefexporter.md)
- [- hopCount](./iofirewirebus/api-1571474-hopcount.md)
- [- hopCount](./iofirewirebus/api-3516563-hopcount.md)
- [- isCompleteRequest](./iofirewirebus/api-1571437-iscompleterequest.md)
- [- isLockRequest](./iofirewirebus/api-1571459-islockrequest.md)
- [- isQuadRequest](./iofirewirebus/api-1571466-isquadrequest.md)
- [- makeRoot](./iofirewirebus/api-1571445-makeroot.md)
- [- maxPackLog](./iofirewirebus/api-1571465-maxpacklog.md)
- [- maxPackLog](./iofirewirebus/api-3516564-maxpacklog.md)
- [- nodeIDtoDevice](./iofirewirebus/api-1571492-nodeidtodevice.md)
- [- resetBus](./iofirewirebus/api-1571479-resetbus.md)

## Relationships

### Inherits From
- [IOService](./ioservice.md)

## See Also

### Interfaces
- [IOFireWireSerialBusProtocolTransport](./iofirewireserialbusprotocoltransport.md)
  SCSI Protocol Driver Family for FireWire SBP2 Devices.
- [IOFireWireSBP2Target](./iofirewiresbp2target.md)
  Serves as bridge between IOFireWireUnit and IOFireWireLUN.
- [IOFireWireController](./iofirewirecontroller.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iofirewirebus)*