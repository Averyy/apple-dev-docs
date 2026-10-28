# IOFireWirePCRSpace

**Framework**: Kernel  
**Kind**: cl  
**Role**: Class

object to multiplex users of the PCR plug registers

**Availability**:
- macOS 10.2+

## Declaration

```cpp
class IOFireWirePCRSpace : IOFWPseudoAddressSpace
```

## Overview

## Topics

### Miscellaneous
- [allocateInputPlug](./iofirewirepcrspace/api-1813120-allocateinputplug.md)
  allocates an input plug.
- [allocateOutputPlug](./iofirewirepcrspace/api-1813128-allocateoutputplug.md)
  allocates an output plug.
- [clearAllP2PConnections](./iofirewirepcrspace/api-1813138-clearallp2pconnections.md)
- [freeInputPlug](./iofirewirepcrspace/api-1813150-freeinputplug.md)
  deallocates an input plug.
- [freeOutputPlug](./iofirewirepcrspace/api-1813163-freeoutputplug.md)
  deallocates an output plug.
- [getPCRAddressSpace](./iofirewirepcrspace/api-1813173-getpcraddressspace.md)
  returns the IOFireWirePCRSpace object for the given FireWire bus
- [init](./iofirewirepcrspace/api-1813189-init.md)
  initializes the IOFireWirePCRSpace object
- [readInputMasterPlug](./iofirewirepcrspace/api-1813201-readinputmasterplug.md)
  Returns the current value of the primary input plug.
- [readInputPlug](./iofirewirepcrspace/api-1813218-readinputplug.md)
  returns the current value of an input plug.
- [readOutputMasterPlug](./iofirewirepcrspace/api-1813228-readoutputmasterplug.md)
  Returns the current value of the primary output plug.
- [readOutputPlug](./iofirewirepcrspace/api-1813239-readoutputplug.md)
  returns the current value of an output plug.
- [setAVCTargetSpacePointer](./iofirewirepcrspace/api-1813255-setavctargetspacepointer.md)
- [updateInputMasterPlug](./iofirewirepcrspace/api-1813265-updateinputmasterplug.md)
  Updates the value of the primary input plug (simulating a lock transaction).
- [updateInputPlug](./iofirewirepcrspace/api-1813280-updateinputplug.md)
  updates the value of an input plug (simulating a lock transaction).
- [updateOutputMasterPlug](./iofirewirepcrspace/api-1813299-updateoutputmasterplug.md)
  Updates the value of the primary output plug (simulating a lock transaction).
- [updateOutputPlug](./iofirewirepcrspace/api-1813322-updateoutputplug.md)
  updates the value of an output plug (simulating a lock transaction).
### DataTypes
- [ExpansionData](./ioservice/expansiondata.md)
### Instance Variables
- [reserved](./iofirewirepcrspace/reserved.md)
### Instance Methods
- [- activate](./iofirewirepcrspace/api-1556243-activate.md)
- [- allocateInputPlug](./iofirewirepcrspace/api-1556227-allocateinputplug.md)
- [- allocateOutputPlug](./iofirewirepcrspace/api-1556239-allocateoutputplug.md)
- [- allocatePlug](./iofirewirepcrspace/api-1556233-allocateplug.md)
- [- clearAllP2PConnections](./iofirewirepcrspace/api-1556238-clearallp2pconnections.md)
- [- deactivate](./iofirewirepcrspace/api-1556235-deactivate.md)
- [- doWrite](./iofirewirepcrspace/api-1556240-dowrite.md)
- [- freeInputPlug](./iofirewirepcrspace/api-1556226-freeinputplug.md)
- [- freeOutputPlug](./iofirewirepcrspace/api-1556237-freeoutputplug.md)
- [- freePlug](./iofirewirepcrspace/api-1556224-freeplug.md)
- [- getMetaClass](./iofirewirepcrspace/api-1556245-getmetaclass.md)
- [- init](./iofirewirepcrspace/api-1556236-init.md)
- [- readInputMasterPlug](./iofirewirepcrspace/api-1556248-readinputmasterplug.md)
- [- readInputPlug](./iofirewirepcrspace/api-1556225-readinputplug.md)
- [- readOutputMasterPlug](./iofirewirepcrspace/api-1556234-readoutputmasterplug.md)
- [- readOutputPlug](./iofirewirepcrspace/api-1556242-readoutputplug.md)
- [- readPlug](./iofirewirepcrspace/api-1556228-readplug.md)
- [- setAVCTargetSpacePointer](./iofirewirepcrspace/api-1556247-setavctargetspacepointer.md)
- [- updateInputMasterPlug](./iofirewirepcrspace/api-1556232-updateinputmasterplug.md)
- [- updateInputPlug](./iofirewirepcrspace/api-1556246-updateinputplug.md)
- [- updateOutputMasterPlug](./iofirewirepcrspace/api-1556241-updateoutputmasterplug.md)
- [- updateOutputPlug](./iofirewirepcrspace/api-1556229-updateoutputplug.md)
- [- updatePlug](./iofirewirepcrspace/api-1556231-updateplug.md)
### Type Methods
- [+ getPCRAddressSpace](./iofirewirepcrspace/api-1556230-getpcraddressspace.md)

## Relationships

### Inherits From
- [IOFWPseudoAddressSpace](./iofwpseudoaddressspace.md)

## See Also

### Address Spaces
- [IOFWAddressSpaceAux](./iofwaddressspaceaux.md)
- [IOFWPhysicalAddressSpaceAux](./iofwphysicaladdressspaceaux.md)
- [IOFWPseudoAddressSpaceAux](./iofwpseudoaddressspaceaux.md)
- [IOFWSimpleContiguousPhysicalAddressSpace](./iofwsimplecontiguousphysicaladdressspace.md)
- [IOFWPseudoAddressSpace](./iofwpseudoaddressspace.md)
- [IOFWSimplePhysicalAddressSpace](./iofwsimplephysicaladdressspace.md)
- [IOFWPhysicalAddressSpace](./iofwphysicaladdressspace.md)
- [IOFWAddressSpace](./iofwaddressspace.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iofirewirepcrspace)*