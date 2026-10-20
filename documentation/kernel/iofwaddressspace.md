# IOFWAddressSpace

**Framework**: Kernel  
**Kind**: cl  
**Role**: Class

**Availability**:
- macOS 10.0+

## Declaration

```cpp
class IOFWAddressSpace : OSObject
```

## Topics

### Miscellaneous
- [activate](./iofwaddressspace/api-1812970-activate.md)
  Address space is ready for handling requests.
- [addTrustedNode](./iofwaddressspace/api-1812980-addtrustednode.md)
  Add a trusted node.
- [contains](./iofwaddressspace/api-1812994-contains.md)
  returns number of bytes starting at addr in this space
- [deactivate](./iofwaddressspace/api-1813008-deactivate.md)
  Address space request handler is disabled.
- [doLock](./iofwaddressspace/api-1813019-dolock.md)
  A method for processing a lock request.
- [doRead](./iofwaddressspace/api-1813035-doread.md)
  An abstract method for processing an address space read request
- [doWrite](./iofwaddressspace/api-1813050-dowrite.md)
  An abstract method for processing an address space write request
- [intersects](./iofwaddressspace/api-1813068-intersects.md)
  Checks this address space intersects with the given address range. Currently only supports IOFWPsuedoAddressSpaces.
- [isExclusive](./iofwaddressspace/api-1813086-isexclusive.md)
  Checks if an address space wants exclusive control of its address range
- [isTrustedNode](./iofwaddressspace/api-1813105-istrustednode.md)
  returns true if the node is added as a trusted node
- [removeAllTrustedNodes](./iofwaddressspace/api-1813134-removealltrustednodes.md)
  Remove all trusted nodes.
- [removeTrustedNode](./iofwaddressspace/api-1813152-removetrustednode.md)
  Remove a trusted node.
- [setExclusive](./iofwaddressspace/api-1813180-setexclusive.md)
  Sets if this address space requires exclusive control of its address range. Exclusivity should be set before an address space is activated.
### DataTypes
- [ExpansionData](./ioservice/expansiondata.md)
### Instance Variables
- [fIOFWAddressSpaceExpansion](./iofwaddressspace/fiofwaddressspaceexpansion.md)
### Instance Methods
- [- activate](./iofwaddressspace/api-1388221-activate.md)
- [- addTrustedNode](./iofwaddressspace/api-1388279-addtrustednode.md)
- [- contains](./iofwaddressspace/api-1388217-contains.md)
- [- createAuxiliary](./iofwaddressspace/api-1388243-createauxiliary.md)
- [- deactivate](./iofwaddressspace/api-1388251-deactivate.md)
- [- doLock](./iofwaddressspace/api-1388225-dolock.md)
- [- doRead](./iofwaddressspace/api-1388271-doread.md)
- [- doWrite](./iofwaddressspace/api-1388227-dowrite.md)
- [- free](./iofwaddressspace/api-1388231-free.md)
- [- getMetaClass](./iofwaddressspace/api-1388223-getmetaclass.md)
- [- init](./iofwaddressspace/api-1388269-init.md)
- [- intersects](./iofwaddressspace/api-1388273-intersects.md)
- [- isExclusive](./iofwaddressspace/api-1388233-isexclusive.md)
- [- isTrustedNode](./iofwaddressspace/api-1388265-istrustednode.md)
- [- removeAllTrustedNodes](./iofwaddressspace/api-1388285-removealltrustednodes.md)
- [- removeTrustedNode](./iofwaddressspace/api-1388275-removetrustednode.md)
- [- setExclusive](./iofwaddressspace/api-1388249-setexclusive.md)

## Relationships

### Inherits From
- [OSObject](./osobject.md)

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
- [IOFWPhysicalAddressSpace](./iofwphysicaladdressspace.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iofwaddressspace)*