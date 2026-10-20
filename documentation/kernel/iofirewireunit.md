# IOFireWireUnit

**Framework**: Kernel  
**Kind**: cl  
**Role**: Class

**Availability**:
- macOS 10.0+

## Declaration

```cpp
class IOFireWireUnit : IOFireWireNub
```

## Topics

### Instance Methods
- [- attach](./iofirewireunit/api-1553358-attach.md)
- [- clearNodeFlags](./iofirewireunit/api-1553373-clearnodeflags.md)
- [- createAuxiliary](./iofirewireunit/api-1553359-createauxiliary.md)
- [- createPhysicalAddressSpace](./iofirewireunit/api-1553366-createphysicaladdressspace.md)
- [- createPseudoAddressSpace](./iofirewireunit/api-1553369-createpseudoaddressspace.md)
- [- free](./iofirewireunit/api-1553353-free.md)
- [- getMetaClass](./iofirewireunit/api-1553350-getmetaclass.md)
- [- getNodeFlags](./iofirewireunit/api-1553371-getnodeflags.md)
- [- handleClose](./iofirewireunit/api-1553372-handleclose.md)
- [- handleOpen](./iofirewireunit/api-1553364-handleopen.md)
- [- init](./iofirewireunit/api-1553356-init.md)
- [- matchPropertyTable](./iofirewireunit/api-1553357-matchpropertytable.md)
- [- message](./iofirewireunit/api-1553352-message.md)
- [- setConfigDirectory](./iofirewireunit/api-1553349-setconfigdirectory.md)
- [- setMaxSpeed](./iofirewireunit/api-1553368-setmaxspeed.md)
- [- setNodeFlags](./iofirewireunit/api-1553367-setnodeflags.md)
- [- terminateUnit](./iofirewireunit/api-1553370-terminateunit.md)
### Type Methods
- [+ terminateUnitThreadFunc](./iofirewireunit/api-1553354-terminateunitthreadfunc.md)

## Relationships

### Inherits From
- [IOFireWireNub](./iofirewirenub.md)

## See Also

### Nubs
- [IOFireWireLocalNode](./iofirewirelocalnode.md)
- [IOFireWireSBP2LUN](./iofirewiresbp2lun.md)
  Provider for most drivers.
- [IOFireWireAVCSubUnit](./iofirewireavcsubunit.md)
  nub for sub unit of AVC devices. Just for matching, calls the AVC unit for all functions.
- [IOFireWireAVCUnit](./iofirewireavcunit.md)
  nub for AVC devices
- [IOFireWireAVCNub](./iofirewireavcnub.md)
  nub for AVC devices
- [IOFireWireNub](./iofirewirenub.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iofirewireunit)*