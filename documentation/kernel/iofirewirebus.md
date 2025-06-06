# IOFireWireBus

**Framework**: Kernel  
**Kind**: cl

IOFireWireBus is a public class the provides access to general FireWire functionality...

**Availability**:
- macOS 10.0+

## Declaration

```swift
class IOFireWireBus : IOService
```

#### Overview

## Topics

### Miscellaneous
- [createLocalIsochPort](iofirewirebus/1811054-createlocalisochport.md)
  Create a local isochronous port to run the given DCL program
### Instance Methods
- [- AddUnitDirectory](iofirewirebus/1571482-addunitdirectory.md)
- [- RemoveUnitDirectory](iofirewirebus/1571473-removeunitdirectory.md)
- [- createAsyncStreamCommand](iofirewirebus/1571461-createasyncstreamcommand.md)
- [- createAsyncStreamCommand](iofirewirebus/3516562-createasyncstreamcommand.md)
- [- createAuxiliary](iofirewirebus/1571483-createauxiliary.md)
- [- createDCLPool](iofirewirebus/1571491-createdclpool.md)
- [- createDelayedCmd](iofirewirebus/1571451-createdelayedcmd.md)
- [- createInitialAddressSpace](iofirewirebus/1571464-createinitialaddressspace.md)
- [- createIsochChannel](iofirewirebus/1571476-createisochchannel.md)
- [- createLocalIsochPort](iofirewirebus/1571438-createlocalisochport.md)
- [- createPhysicalAddressSpace](iofirewirebus/1571472-createphysicaladdressspace.md)
- [- createPseudoAddressSpace](iofirewirebus/1571440-createpseudoaddressspace.md)
- [- createSimpleContiguousPhysicalAddressSpace](iofirewirebus/1571456-createsimplecontiguousphysicalad.md)
- [- createSimplePhysicalAddressSpace](iofirewirebus/1571468-createsimplephysicaladdressspace.md)
- [- getAddressSpace](iofirewirebus/1571467-getaddressspace.md)
- [- getBusCycleTime](iofirewirebus/1571453-getbuscycletime.md)
- [- getBusPowerManager](iofirewirebus/1571489-getbuspowermanager.md)
- [- getCycleTime](iofirewirebus/1571485-getcycletime.md)
- [- getExtendedTCode](iofirewirebus/1571452-getextendedtcode.md)
- [- getFireWirePhysicalAddressBits](iofirewirebus/1571469-getfirewirephysicaladdressbits.md)
- [- getFireWirePhysicalAddressMask](iofirewirebus/1571475-getfirewirephysicaladdressmask.md)
- [- getFireWirePhysicalBufferBits](iofirewirebus/1571439-getfirewirephysicalbufferbits.md)
- [- getFireWirePhysicalBufferMask](iofirewirebus/1571448-getfirewirephysicalbuffermask.md)
- [- getMaxRec](iofirewirebus/1571454-getmaxrec.md)
- [- getMetaClass](iofirewirebus/1571487-getmetaclass.md)
- [- getSessionRefExporter](iofirewirebus/1571484-getsessionrefexporter.md)
- [- hopCount](iofirewirebus/1571474-hopcount.md)
- [- hopCount](iofirewirebus/3516563-hopcount.md)
- [- isCompleteRequest](iofirewirebus/1571437-iscompleterequest.md)
- [- isLockRequest](iofirewirebus/1571459-islockrequest.md)
- [- isQuadRequest](iofirewirebus/1571466-isquadrequest.md)
- [- makeRoot](iofirewirebus/1571445-makeroot.md)
- [- maxPackLog](iofirewirebus/1571465-maxpacklog.md)
- [- maxPackLog](iofirewirebus/3516564-maxpacklog.md)
- [- nodeIDtoDevice](iofirewirebus/1571492-nodeidtodevice.md)
- [- resetBus](iofirewirebus/1571479-resetbus.md)

## Relationships

### Inherits From
- [IOService](ioservice.md)

## See Also

- [IOFireWireSerialBusProtocolTransport](iofirewireserialbusprotocoltransport.md)
  SCSI Protocol Driver Family for FireWire SBP2 Devices.
- [IOFireWireSBP2Target](iofirewiresbp2target.md)
  Serves as bridge between IOFireWireUnit and IOFireWireLUN.
- [IOFireWireController](iofirewirecontroller.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iofirewirebus)*