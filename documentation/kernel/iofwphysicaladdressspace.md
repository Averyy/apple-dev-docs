# IOFWPhysicalAddressSpace

**Framework**: Kernel  
**Kind**: cl  
**Role**: Class

**Availability**:
- macOS 10.0+

## Declaration

```cpp
class IOFWPhysicalAddressSpace : IOFWAddressSpace
```

## Topics

### Miscellaneous
- [checkMemoryInRange](./iofwphysicaladdressspace/api-1812923-checkmemoryinrange.md)
  Validates the IOMemoryDescriptor, which is used to initialize the PhysicalAddressSpace.
- [complete](./iofwphysicaladdressspace/api-1812928-complete.md)
  complete the IODMACommand used by this PhysicalAddressSpace.
- [doRead](./iofwphysicaladdressspace/api-1812935-doread.md)
  A method for processing an address space read request
- [doWrite](./iofwphysicaladdressspace/api-1812940-dowrite.md)
  A method for processing an address space write request
- [getDMACommand](./iofwphysicaladdressspace/api-1812943-getdmacommand.md)
  Get the DMACommand from this PhysicalAddressSpace.
- [getLength](./iofwphysicaladdressspace/api-1812947-getlength.md)
  Get the length of the memory backed by PhysicalAddressSpace.
- [getMemoryDescriptor](./iofwphysicaladdressspace/api-1812953-getmemorydescriptor.md)
  Gets the memory descriptor, which is associated to this PhysicalAddressSpace.
- [getSegments](./iofwphysicaladdressspace/api-1812956-getsegments.md)
  Returns the scatter gather list of memory segments from the IODMACommand used in this PhysicalAddressSpace.
- [init](./iofwphysicaladdressspace/api-1812960-init.md)
  Initialize physical address space.
- [initWithDesc](./iofwphysicaladdressspace/api-1812962-initwithdesc.md)
  Initialize physical address space with IOMemoryDescriptor.
- [initWithDMACommand](./iofwphysicaladdressspace/api-1812968-initwithdmacommand.md)
  Initialize physical address space with IODMACommand.
- [isPrepared](./iofwphysicaladdressspace/api-1812974-isprepared.md)
  Inspects whether the IODMACommand was prepared in this PhysicalAddressSpace.
- [prepare](./iofwphysicaladdressspace/api-1812981-prepare.md)
  Prepare the IODMACommand used by this PhysicalAddressSpace.
- [setDMACommand](./iofwphysicaladdressspace/api-1812990-setdmacommand.md)
  Set the DMACommand for this PhysicalAddressSpace.
- [setMemoryDescriptor](./iofwphysicaladdressspace/api-1813001-setmemorydescriptor.md)
  Sets the memory descriptor, which will be associated to this PhysicalAddressSpace.
- [synchronize](./iofwphysicaladdressspace/api-1813014-synchronize.md)
  synchronize the IODMACommand used by this PhysicalAddressSpace.
### Instance Methods
- [- checkMemoryInRange](./iofwphysicaladdressspace/api-1535960-checkmemoryinrange.md)
- [- complete](./iofwphysicaladdressspace/api-1536019-complete.md)
- [- createAuxiliary](./iofwphysicaladdressspace/api-1535962-createauxiliary.md)
- [- doRead](./iofwphysicaladdressspace/api-1535988-doread.md)
- [- doWrite](./iofwphysicaladdressspace/api-1535956-dowrite.md)
- [- free](./iofwphysicaladdressspace/api-1535978-free.md)
- [- getDMACommand](./iofwphysicaladdressspace/api-1535972-getdmacommand.md)
- [- getLength](./iofwphysicaladdressspace/api-1536002-getlength.md)
- [- getMemoryDescriptor](./iofwphysicaladdressspace/api-1536014-getmemorydescriptor.md)
- [- getMetaClass](./iofwphysicaladdressspace/api-1536012-getmetaclass.md)
- [- getPhysicalSegment](./iofwphysicaladdressspace/api-1536008-getphysicalsegment.md)
- [- getSegments](./iofwphysicaladdressspace/api-1536006-getsegments.md)
- [- init](./iofwphysicaladdressspace/api-1535997-init.md)
- [- initWithDMACommand](./iofwphysicaladdressspace/api-1535990-initwithdmacommand.md)
- [- initWithDesc](./iofwphysicaladdressspace/api-1536017-initwithdesc.md)
- [- isPrepared](./iofwphysicaladdressspace/api-1535970-isprepared.md)
- [- prepare](./iofwphysicaladdressspace/api-1535964-prepare.md)
- [- setDMACommand](./iofwphysicaladdressspace/api-1536004-setdmacommand.md)
- [- setMemoryDescriptor](./iofwphysicaladdressspace/api-1536010-setmemorydescriptor.md)
- [- synchronize](./iofwphysicaladdressspace/api-1535995-synchronize.md)

## Relationships

### Inherits From
- [IOFWAddressSpace](./iofwaddressspace.md)

## See Also

### Address Spaces
- [IOFWAddressSpaceAux](./iofwaddressspaceaux.md)
- [IOFWPhysicalAddressSpaceAux](./iofwphysicaladdressspaceaux.md)
- [IOFWPseudoAddressSpaceAux](./iofwpseudoaddressspaceaux.md)
- [IOFWSimpleContiguousPhysicalAddressSpace](./iofwsimplecontiguousphysicaladdressspace.md)
- [IOFireWirePCRSpace](./iofirewirepcrspace.md)
  object to multiplex users of the PCR plug registers
- [IOFWPseudoAddressSpace](./iofwpseudoaddressspace.md)
- [IOFWSimplePhysicalAddressSpace](./iofwsimplephysicaladdressspace.md)
- [IOFWAddressSpace](./iofwaddressspace.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iofwphysicaladdressspace)*