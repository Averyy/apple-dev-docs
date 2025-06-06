# IOFWPhysicalAddressSpace

**Framework**: Kernel  
**Kind**: cl

**Availability**:
- macOS 10.0+

## Declaration

```swift
class IOFWPhysicalAddressSpace : IOFWAddressSpace
```

## Topics

### Miscellaneous
- [checkMemoryInRange](iofwphysicaladdressspace/1812923-checkmemoryinrange.md)
  Validates the IOMemoryDescriptor, which is used to initialize the PhysicalAddressSpace.
- [complete](iofwphysicaladdressspace/1812928-complete.md)
  complete the IODMACommand used by this PhysicalAddressSpace.
- [doRead](iofwphysicaladdressspace/1812935-doread.md)
  A method for processing an address space read request
- [doWrite](iofwphysicaladdressspace/1812940-dowrite.md)
  A method for processing an address space write request
- [getDMACommand](iofwphysicaladdressspace/1812943-getdmacommand.md)
  Get the DMACommand from this PhysicalAddressSpace.
- [getLength](iofwphysicaladdressspace/1812947-getlength.md)
  Get the length of the memory backed by PhysicalAddressSpace.
- [getMemoryDescriptor](iofwphysicaladdressspace/1812953-getmemorydescriptor.md)
  Gets the memory descriptor, which is associated to this PhysicalAddressSpace.
- [getSegments](iofwphysicaladdressspace/1812956-getsegments.md)
  Returns the scatter gather list of memory segments from the IODMACommand used in this PhysicalAddressSpace.
- [init](iofwphysicaladdressspace/1812960-init.md)
  Initialize physical address space.
- [initWithDesc](iofwphysicaladdressspace/1812962-initwithdesc.md)
  Initialize physical address space with IOMemoryDescriptor.
- [initWithDMACommand](iofwphysicaladdressspace/1812968-initwithdmacommand.md)
  Initialize physical address space with IODMACommand.
- [isPrepared](iofwphysicaladdressspace/1812974-isprepared.md)
  Inspects whether the IODMACommand was prepared in this PhysicalAddressSpace.
- [prepare](iofwphysicaladdressspace/1812981-prepare.md)
  Prepare the IODMACommand used by this PhysicalAddressSpace.
- [setDMACommand](iofwphysicaladdressspace/1812990-setdmacommand.md)
  Set the DMACommand for this PhysicalAddressSpace.
- [setMemoryDescriptor](iofwphysicaladdressspace/1813001-setmemorydescriptor.md)
  Sets the memory descriptor, which will be associated to this PhysicalAddressSpace.
- [synchronize](iofwphysicaladdressspace/1813014-synchronize.md)
  synchronize the IODMACommand used by this PhysicalAddressSpace.
### Instance Methods
- [- checkMemoryInRange](iofwphysicaladdressspace/1535960-checkmemoryinrange.md)
- [- complete](iofwphysicaladdressspace/1536019-complete.md)
- [- createAuxiliary](iofwphysicaladdressspace/1535962-createauxiliary.md)
- [- doRead](iofwphysicaladdressspace/1535988-doread.md)
- [- doWrite](iofwphysicaladdressspace/1535956-dowrite.md)
- [- free](iofwphysicaladdressspace/1535978-free.md)
- [- getDMACommand](iofwphysicaladdressspace/1535972-getdmacommand.md)
- [- getLength](iofwphysicaladdressspace/1536002-getlength.md)
- [- getMemoryDescriptor](iofwphysicaladdressspace/1536014-getmemorydescriptor.md)
- [- getMetaClass](iofwphysicaladdressspace/1536012-getmetaclass.md)
- [- getPhysicalSegment](iofwphysicaladdressspace/1536008-getphysicalsegment.md)
- [- getSegments](iofwphysicaladdressspace/1536006-getsegments.md)
- [- init](iofwphysicaladdressspace/1535997-init.md)
- [- initWithDMACommand](iofwphysicaladdressspace/1535990-initwithdmacommand.md)
- [- initWithDesc](iofwphysicaladdressspace/1536017-initwithdesc.md)
- [- isPrepared](iofwphysicaladdressspace/1535970-isprepared.md)
- [- prepare](iofwphysicaladdressspace/1535964-prepare.md)
- [- setDMACommand](iofwphysicaladdressspace/1536004-setdmacommand.md)
- [- setMemoryDescriptor](iofwphysicaladdressspace/1536010-setmemorydescriptor.md)
- [- synchronize](iofwphysicaladdressspace/1535995-synchronize.md)

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
- [IOFWPseudoAddressSpace](iofwpseudoaddressspace.md)
- [IOFWSimplePhysicalAddressSpace](iofwsimplephysicaladdressspace.md)
- [IOFWAddressSpace](iofwaddressspace.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iofwphysicaladdressspace)*