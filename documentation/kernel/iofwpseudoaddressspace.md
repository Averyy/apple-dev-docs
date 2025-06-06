# IOFWPseudoAddressSpace

**Framework**: Kernel  
**Kind**: cl

**Availability**:
- macOS 10.0+

## Declaration

```swift
class IOFWPseudoAddressSpace : IOFWAddressSpace
```

## Topics

### Miscellaneous
- [contains](iofwpseudoaddressspace/1813836-contains.md)
  returns number of bytes starting at addr in this space
- [doRead](iofwpseudoaddressspace/1813839-doread.md)
  A method for processing an address space read request
- [doWrite](iofwpseudoaddressspace/1813844-dowrite.md)
  A method for processing an address space write request
- [initAll](iofwpseudoaddressspace/1813848-initall.md)
  Initialize an address space object to handle r/w memory
- [initFixed](iofwpseudoaddressspace/1813852-initfixed.md)
  Initialize a fixed address space at top of kCSRRegisterSpaceBaseAddressHi
- [setARxReqIntCompleteHandler](iofwpseudoaddressspace/1813855-setarxreqintcompletehandler.md)
  Installs a callback to receive notification, when FWIM has completed ARxReqInt processing and no incoming packets are left in the queue.
- [simpleRead](iofwpseudoaddressspace/1813859-simpleread.md)
  Create an address space object to handle read-only memory (eg. the local ROM) handles everything itself
- [simpleReader](iofwpseudoaddressspace/1813862-simplereader.md)
  A method for processing an address space read request
- [simpleReadFixed](iofwpseudoaddressspace/1813866-simplereadfixed.md)
  Create an address space object to handle fixed read-only memory (eg. the local ROM) handles everything itself
- [simpleRW(IOFireWireBus *, FWAddress *, IOMemoryDescriptor *)](iofwpseudoaddressspace/1813868-simplerw.md)
  Create an address space object to handle r/w memory handles everything itself
- [simpleRW(IOFireWireBus *, FWAddress *, UInt32, void *)](iofwpseudoaddressspace/1813871-simplerw.md)
  Create an address space object to handle r/w memory handles everything itself
- [simpleRWFixed](iofwpseudoaddressspace/1813874-simplerwfixed.md)
  Create a Read/Write fixed address space at top of kCSRRegisterSpaceBaseAddressHi.
- [simpleWriter](iofwpseudoaddressspace/1813878-simplewriter.md)
  A method for processing an address space write request
### DataTypes
- [ExpansionData](ioservice/expansiondata.md)
### Instance Variables
- [reserved](iofwpseudoaddressspace/reserved.md)
### Instance Methods
- [- allocateAddress](iofwpseudoaddressspace/1584079-allocateaddress.md)
- [- contains](iofwpseudoaddressspace/1584054-contains.md)
- [- createAuxiliary](iofwpseudoaddressspace/1584057-createauxiliary.md)
- [- doRead](iofwpseudoaddressspace/1584056-doread.md)
- [- doWrite](iofwpseudoaddressspace/1584068-dowrite.md)
- [- free](iofwpseudoaddressspace/1584074-free.md)
- [- freeAddress](iofwpseudoaddressspace/1584070-freeaddress.md)
- [- getMetaClass](iofwpseudoaddressspace/1584059-getmetaclass.md)
- [- handleARxReqIntComplete](iofwpseudoaddressspace/1584073-handlearxreqintcomplete.md)
- [- initAll](iofwpseudoaddressspace/1584067-initall.md)
- [- initFixed](iofwpseudoaddressspace/1584052-initfixed.md)
- [- setARxReqIntCompleteHandler](iofwpseudoaddressspace/1584077-setarxreqintcompletehandler.md)
### Type Methods
- [+ readWrite](iofwpseudoaddressspace/1584061-readwrite.md)
- [+ simpleRW](iofwpseudoaddressspace/1584055-simplerw.md)
- [+ simpleRW](iofwpseudoaddressspace/3516561-simplerw.md)
- [+ simpleRWFixed](iofwpseudoaddressspace/1584060-simplerwfixed.md)
- [+ simpleRead](iofwpseudoaddressspace/1584064-simpleread.md)
- [+ simpleReadFixed](iofwpseudoaddressspace/1584072-simplereadfixed.md)
- [+ simpleReader](iofwpseudoaddressspace/1584063-simplereader.md)
- [+ simpleWriter](iofwpseudoaddressspace/1584062-simplewriter.md)

## Relationships

### Inherits From
- [IOFWAddressSpace](iofwaddressspace.md)

## See Also

- [IOFWAddressSpaceAux](iofwaddressspaceaux.md)
- [IOFWPhysicalAddressSpaceAux](iofwphysicaladdressspaceaux.md)
- [IOFWPseudoAddressSpaceAux](iofwpseudoaddressspaceaux.md)
- [IOFWSimpleContiguousPhysicalAddressSpace](iofwsimplecontiguousphysicaladdressspace.md)
- [IOFireWirePCRSpace](iofirewirepcrspace.md)
  object to multiplex users of the PCR plug registers
- [IOFWSimplePhysicalAddressSpace](iofwsimplephysicaladdressspace.md)
- [IOFWPhysicalAddressSpace](iofwphysicaladdressspace.md)
- [IOFWAddressSpace](iofwaddressspace.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iofwpseudoaddressspace)*