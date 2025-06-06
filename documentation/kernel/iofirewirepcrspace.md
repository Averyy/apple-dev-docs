# IOFireWirePCRSpace

**Framework**: Kernel  
**Kind**: cl

object to multiplex users of the PCR plug registers

**Availability**:
- macOS 10.2+

## Declaration

```swift
class IOFireWirePCRSpace : IOFWPseudoAddressSpace
```

#### Overview

## Topics

### Miscellaneous
- [allocateInputPlug](iofirewirepcrspace/1813120-allocateinputplug.md)
  allocates an input plug.
- [allocateOutputPlug](iofirewirepcrspace/1813128-allocateoutputplug.md)
  allocates an output plug.
- [clearAllP2PConnections](iofirewirepcrspace/1813138-clearallp2pconnections.md)
- [freeInputPlug](iofirewirepcrspace/1813150-freeinputplug.md)
  deallocates an input plug.
- [freeOutputPlug](iofirewirepcrspace/1813163-freeoutputplug.md)
  deallocates an output plug.
- [getPCRAddressSpace](iofirewirepcrspace/1813173-getpcraddressspace.md)
  returns the IOFireWirePCRSpace object for the given FireWire bus
- [init](iofirewirepcrspace/1813189-init.md)
  initializes the IOFireWirePCRSpace object
- [readInputMasterPlug](iofirewirepcrspace/1813201-readinputmasterplug.md)
  Returns the current value of the primary input plug.
- [readInputPlug](iofirewirepcrspace/1813218-readinputplug.md)
  returns the current value of an input plug.
- [readOutputMasterPlug](iofirewirepcrspace/1813228-readoutputmasterplug.md)
  Returns the current value of the primary output plug.
- [readOutputPlug](iofirewirepcrspace/1813239-readoutputplug.md)
  returns the current value of an output plug.
- [setAVCTargetSpacePointer](iofirewirepcrspace/1813255-setavctargetspacepointer.md)
- [updateInputMasterPlug](iofirewirepcrspace/1813265-updateinputmasterplug.md)
  Updates the value of the primary input plug (simulating a lock transaction).
- [updateInputPlug](iofirewirepcrspace/1813280-updateinputplug.md)
  updates the value of an input plug (simulating a lock transaction).
- [updateOutputMasterPlug](iofirewirepcrspace/1813299-updateoutputmasterplug.md)
  Updates the value of the primary output plug (simulating a lock transaction).
- [updateOutputPlug](iofirewirepcrspace/1813322-updateoutputplug.md)
  updates the value of an output plug (simulating a lock transaction).
### DataTypes
- [ExpansionData](ioservice/expansiondata.md)
### Instance Variables
- [reserved](iofirewirepcrspace/reserved.md)
### Instance Methods
- [- activate](iofirewirepcrspace/1556243-activate.md)
- [- allocateInputPlug](iofirewirepcrspace/1556227-allocateinputplug.md)
- [- allocateOutputPlug](iofirewirepcrspace/1556239-allocateoutputplug.md)
- [- allocatePlug](iofirewirepcrspace/1556233-allocateplug.md)
- [- clearAllP2PConnections](iofirewirepcrspace/1556238-clearallp2pconnections.md)
- [- deactivate](iofirewirepcrspace/1556235-deactivate.md)
- [- doWrite](iofirewirepcrspace/1556240-dowrite.md)
- [- freeInputPlug](iofirewirepcrspace/1556226-freeinputplug.md)
- [- freeOutputPlug](iofirewirepcrspace/1556237-freeoutputplug.md)
- [- freePlug](iofirewirepcrspace/1556224-freeplug.md)
- [- getMetaClass](iofirewirepcrspace/1556245-getmetaclass.md)
- [- init](iofirewirepcrspace/1556236-init.md)
- [- readInputMasterPlug](iofirewirepcrspace/1556248-readinputmasterplug.md)
- [- readInputPlug](iofirewirepcrspace/1556225-readinputplug.md)
- [- readOutputMasterPlug](iofirewirepcrspace/1556234-readoutputmasterplug.md)
- [- readOutputPlug](iofirewirepcrspace/1556242-readoutputplug.md)
- [- readPlug](iofirewirepcrspace/1556228-readplug.md)
- [- setAVCTargetSpacePointer](iofirewirepcrspace/1556247-setavctargetspacepointer.md)
- [- updateInputMasterPlug](iofirewirepcrspace/1556232-updateinputmasterplug.md)
- [- updateInputPlug](iofirewirepcrspace/1556246-updateinputplug.md)
- [- updateOutputMasterPlug](iofirewirepcrspace/1556241-updateoutputmasterplug.md)
- [- updateOutputPlug](iofirewirepcrspace/1556229-updateoutputplug.md)
- [- updatePlug](iofirewirepcrspace/1556231-updateplug.md)
### Type Methods
- [+ getPCRAddressSpace](iofirewirepcrspace/1556230-getpcraddressspace.md)

## Relationships

### Inherits From
- [IOFWPseudoAddressSpace](iofwpseudoaddressspace.md)

## See Also

- [IOFWAddressSpaceAux](iofwaddressspaceaux.md)
- [IOFWPhysicalAddressSpaceAux](iofwphysicaladdressspaceaux.md)
- [IOFWPseudoAddressSpaceAux](iofwpseudoaddressspaceaux.md)
- [IOFWSimpleContiguousPhysicalAddressSpace](iofwsimplecontiguousphysicaladdressspace.md)
- [IOFWPseudoAddressSpace](iofwpseudoaddressspace.md)
- [IOFWSimplePhysicalAddressSpace](iofwsimplephysicaladdressspace.md)
- [IOFWPhysicalAddressSpace](iofwphysicaladdressspace.md)
- [IOFWAddressSpace](iofwaddressspace.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iofirewirepcrspace)*