# IOFWPseudoAddressSpaceAux

**Framework**: Kernel  
**Kind**: cl  
**Role**: Class

**Availability**:
- macOS 10.2+

## Declaration

```cpp
class IOFWPseudoAddressSpaceAux : IOFWAddressSpaceAux
```

## Topics

### Miscellaneous
- [setARxReqIntCompleteHandler](./iofwpseudoaddressspaceaux/api-1812922-setarxreqintcompletehandler.md)
  Installs a callback to receive notification, when FWIM has completed ARxReqInt processing and no incoming packets are left in the queue.
### Instance Methods
- [- createMemberVariables](./iofwpseudoaddressspaceaux/api-1584058-createmembervariables.md)
- [- destroyMemberVariables](./iofwpseudoaddressspaceaux/api-1584076-destroymembervariables.md)
- [- free](./iofwpseudoaddressspaceaux/api-1584080-free.md)
- [- getMetaClass](./iofwpseudoaddressspaceaux/api-1584065-getmetaclass.md)
- [- handleARxReqIntComplete](./iofwpseudoaddressspaceaux/api-1584071-handlearxreqintcomplete.md)
- [- init](./iofwpseudoaddressspaceaux/api-1584053-init.md)
- [- intersects](./iofwpseudoaddressspaceaux/api-1584078-intersects.md)
- [- setARxReqIntCompleteHandler](./iofwpseudoaddressspaceaux/api-1584069-setarxreqintcompletehandler.md)

## Relationships

### Inherits From
- [IOFWAddressSpaceAux](./iofwaddressspaceaux.md)

## See Also

### Address Spaces
- [IOFWAddressSpaceAux](./iofwaddressspaceaux.md)
- [IOFWPhysicalAddressSpaceAux](./iofwphysicaladdressspaceaux.md)
- [IOFWSimpleContiguousPhysicalAddressSpace](./iofwsimplecontiguousphysicaladdressspace.md)
- [IOFireWirePCRSpace](./iofirewirepcrspace.md)
  object to multiplex users of the PCR plug registers
- [IOFWPseudoAddressSpace](./iofwpseudoaddressspace.md)
- [IOFWSimplePhysicalAddressSpace](./iofwsimplephysicaladdressspace.md)
- [IOFWPhysicalAddressSpace](./iofwphysicaladdressspace.md)
- [IOFWAddressSpace](./iofwaddressspace.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iofwpseudoaddressspaceaux)*