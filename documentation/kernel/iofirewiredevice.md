# IOFireWireDevice

**Framework**: Kernel  
**Kind**: cl  
**Role**: Class

Represents a FireWire device.

**Availability**:
- macOS 10.0+

## Declaration

```cpp
class IOFireWireDevice : IOFireWireNub
```

#### Overview

The FireWire family tries to read the configuration ROM of each device on the FireWire bus. For each device that responds with its bus information block, the FireWire family publishes an `IOFireWireDevice` object in the I/O Registry. An `IOFireWireDevice` object keeps track of the device's node ID, copies config ROM properties into the object's property list, and scans the config ROM for unit directories, publishing an `IOFireWireUnit` object for each unit directory it finds.

## Topics

### Miscellaneous
- [clearNodeFlags](./iofirewiredevice/api-1810239-clearnodeflags.md)
  Resets the node's characteristics.
- [createPhysicalAddressSpace](./iofirewiredevice/api-1810254-createphysicaladdressspace.md)
  Creates local physical FireWire address spaces for the device to access.
- [createPseudoAddressSpace](./iofirewiredevice/api-1810271-createpseudoaddressspace.md)
  Creates local pseudo FireWire address spaces for the device to access.
- [getNodeFlags](./iofirewiredevice/api-1810283-getnodeflags.md)
  Retrieves the node's characteristics.
- [getUnitCount](./iofirewiredevice/api-1810297-getunitcount.md)
  Returns number of units attached to this device.
- [init](./iofirewiredevice/api-1810312-init.md)
  Initializes the nub.
- [setMaxSpeed](./iofirewiredevice/api-1810324-setmaxspeed.md)
  Sets the maximum speed for this node.
- [setNodeFlags](./iofirewiredevice/api-1810338-setnodeflags.md)
  Sets the node's characteristics.
### DataTypes
- [ExpansionData](./ioservice/expansiondata.md)
### Instance Variables
- [reserved](./iofirewiredevice/reserved.md)
### Instance Methods
- [- attach](./iofirewiredevice/api-1547573-attach.md)
- [- cacheROM](./iofirewiredevice/api-1547566-cacherom.md)
- [- clearNodeFlags](./iofirewiredevice/api-1547590-clearnodeflags.md)
- [- configureNode](./iofirewiredevice/api-1547569-configurenode.md)
- [- configurePhysicalFilter](./iofirewiredevice/api-1547578-configurephysicalfilter.md)
- [- createAuxiliary](./iofirewiredevice/api-1547564-createauxiliary.md)
- [- createPhysicalAddressSpace](./iofirewiredevice/api-1547571-createphysicaladdressspace.md)
- [- createPseudoAddressSpace](./iofirewiredevice/api-1547572-createpseudoaddressspace.md)
- [- finalize](./iofirewiredevice/api-1547568-finalize.md)
- [- free](./iofirewiredevice/api-1547588-free.md)
- [- getMetaClass](./iofirewiredevice/api-1547589-getmetaclass.md)
- [- getNodeFlags](./iofirewiredevice/api-1547586-getnodeflags.md)
- [- getOpenUnitSet](./iofirewiredevice/api-1547591-getopenunitset.md)
- [- getROMBase](./iofirewiredevice/api-1547570-getrombase.md)
- [- getResumeTime](./iofirewiredevice/api-1547603-getresumetime.md)
- [- getUnitCount](./iofirewiredevice/api-1547601-getunitcount.md)
- [- handleClose](./iofirewiredevice/api-1547554-handleclose.md)
- [- handleIsOpen](./iofirewiredevice/api-1547565-handleisopen.md)
- [- handleOpen](./iofirewiredevice/api-1547582-handleopen.md)
- [- init](./iofirewiredevice/api-1547561-init.md)
- [- isTerminated](./iofirewiredevice/api-1547600-isterminated.md)
- [- latchResumeTime](./iofirewiredevice/api-1547555-latchresumetime.md)
- [- matchPropertyTable](./iofirewiredevice/api-1547583-matchpropertytable.md)
- [- message](./iofirewiredevice/api-1547562-message.md)
- [- preprocessDirectories](./iofirewiredevice/api-1547575-preprocessdirectories.md)
- [- processROM](./iofirewiredevice/api-1547580-processrom.md)
- [- processRootDirectory](./iofirewiredevice/api-1547581-processrootdirectory.md)
- [- processUnitDirectories](./iofirewiredevice/api-1547594-processunitdirectories.md)
- [- readRootDirectory](./iofirewiredevice/api-1547602-readrootdirectory.md)
- [- readUnitDirectories](./iofirewiredevice/api-1547595-readunitdirectories.md)
- [- setMaxSpeed](./iofirewiredevice/api-1547557-setmaxspeed.md)
- [- setNodeFlags](./iofirewiredevice/api-1547593-setnodeflags.md)
- [- setNodeROM](./iofirewiredevice/api-1547567-setnoderom.md)
- [- setRegistrationState](./iofirewiredevice/api-1547574-setregistrationstate.md)
- [- setUnitCount](./iofirewiredevice/api-1547585-setunitcount.md)
### Type Methods
- [+ readROMDirGlue](./iofirewiredevice/api-1547552-readromdirglue.md)
- [+ readROMThreadFunc](./iofirewiredevice/api-1547584-readromthreadfunc.md)
- [+ terminateDevice](./iofirewiredevice/api-1547563-terminatedevice.md)

## Relationships

### Inherits From
- [IOFireWireNub](./iofirewirenub.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iofirewiredevice)*