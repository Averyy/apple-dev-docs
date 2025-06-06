# IOFireWireDevice

**Framework**: Kernel  
**Kind**: cl

Represents a FireWire device.

**Availability**:
- macOS 10.0+

## Declaration

```swift
class IOFireWireDevice : IOFireWireNub
```

#### Overview

The FireWire family tries to read the configuration ROM of each device on the FireWire bus. For each device that responds with its bus information block, the FireWire family publishes an `IOFireWireDevice` object in the I/O Registry. An `IOFireWireDevice` object keeps track of the device's node ID, copies config ROM properties into the object's property list, and scans the config ROM for unit directories, publishing an `IOFireWireUnit` object for each unit directory it finds.

## Topics

### Miscellaneous
- [clearNodeFlags](iofirewiredevice/1810239-clearnodeflags.md)
  Resets the node's characteristics.
- [createPhysicalAddressSpace](iofirewiredevice/1810254-createphysicaladdressspace.md)
  Creates local physical FireWire address spaces for the device to access.
- [createPseudoAddressSpace](iofirewiredevice/1810271-createpseudoaddressspace.md)
  Creates local pseudo FireWire address spaces for the device to access.
- [getNodeFlags](iofirewiredevice/1810283-getnodeflags.md)
  Retrieves the node's characteristics.
- [getUnitCount](iofirewiredevice/1810297-getunitcount.md)
  Returns number of units attached to this device.
- [init](iofirewiredevice/1810312-init.md)
  Initializes the nub.
- [setMaxSpeed](iofirewiredevice/1810324-setmaxspeed.md)
  Sets the maximum speed for this node.
- [setNodeFlags](iofirewiredevice/1810338-setnodeflags.md)
  Sets the node's characteristics.
### DataTypes
- [ExpansionData](ioservice/expansiondata.md)
### Instance Variables
- [reserved](iofirewiredevice/reserved.md)
### Instance Methods
- [- attach](iofirewiredevice/1547573-attach.md)
- [- cacheROM](iofirewiredevice/1547566-cacherom.md)
- [- clearNodeFlags](iofirewiredevice/1547590-clearnodeflags.md)
- [- configureNode](iofirewiredevice/1547569-configurenode.md)
- [- configurePhysicalFilter](iofirewiredevice/1547578-configurephysicalfilter.md)
- [- createAuxiliary](iofirewiredevice/1547564-createauxiliary.md)
- [- createPhysicalAddressSpace](iofirewiredevice/1547571-createphysicaladdressspace.md)
- [- createPseudoAddressSpace](iofirewiredevice/1547572-createpseudoaddressspace.md)
- [- finalize](iofirewiredevice/1547568-finalize.md)
- [- free](iofirewiredevice/1547588-free.md)
- [- getMetaClass](iofirewiredevice/1547589-getmetaclass.md)
- [- getNodeFlags](iofirewiredevice/1547586-getnodeflags.md)
- [- getOpenUnitSet](iofirewiredevice/1547591-getopenunitset.md)
- [- getROMBase](iofirewiredevice/1547570-getrombase.md)
- [- getResumeTime](iofirewiredevice/1547603-getresumetime.md)
- [- getUnitCount](iofirewiredevice/1547601-getunitcount.md)
- [- handleClose](iofirewiredevice/1547554-handleclose.md)
- [- handleIsOpen](iofirewiredevice/1547565-handleisopen.md)
- [- handleOpen](iofirewiredevice/1547582-handleopen.md)
- [- init](iofirewiredevice/1547561-init.md)
- [- isTerminated](iofirewiredevice/1547600-isterminated.md)
- [- latchResumeTime](iofirewiredevice/1547555-latchresumetime.md)
- [- matchPropertyTable](iofirewiredevice/1547583-matchpropertytable.md)
- [- message](iofirewiredevice/1547562-message.md)
- [- preprocessDirectories](iofirewiredevice/1547575-preprocessdirectories.md)
- [- processROM](iofirewiredevice/1547580-processrom.md)
- [- processRootDirectory](iofirewiredevice/1547581-processrootdirectory.md)
- [- processUnitDirectories](iofirewiredevice/1547594-processunitdirectories.md)
- [- readRootDirectory](iofirewiredevice/1547602-readrootdirectory.md)
- [- readUnitDirectories](iofirewiredevice/1547595-readunitdirectories.md)
- [- setMaxSpeed](iofirewiredevice/1547557-setmaxspeed.md)
- [- setNodeFlags](iofirewiredevice/1547593-setnodeflags.md)
- [- setNodeROM](iofirewiredevice/1547567-setnoderom.md)
- [- setRegistrationState](iofirewiredevice/1547574-setregistrationstate.md)
- [- setUnitCount](iofirewiredevice/1547585-setunitcount.md)
### Type Methods
- [+ readROMDirGlue](iofirewiredevice/1547552-readromdirglue.md)
- [+ readROMThreadFunc](iofirewiredevice/1547584-readromthreadfunc.md)
- [+ terminateDevice](iofirewiredevice/1547563-terminatedevice.md)

## Relationships

### Inherits From
- [IOFireWireNub](iofirewirenub.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iofirewiredevice)*