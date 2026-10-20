# IOFireWireNub

**Framework**: Kernel  
**Kind**: cl  
**Role**: Class

**Availability**:
- macOS 10.0+

## Declaration

```cpp
class IOFireWireNub : IOService
```

## Topics

### Instance Methods
- [- FWSpeed](./iofirewirenub/api-1520891-fwspeed.md)
- [- FWSpeed](./iofirewirenub/api-3516576-fwspeed.md)
- [- clearNodeFlags](./iofirewirenub/api-1520937-clearnodeflags.md)
- [- createAuxiliary](./iofirewirenub/api-1520895-createauxiliary.md)
- [- createCompareAndSwapCommand](./iofirewirenub/api-1520925-createcompareandswapcommand.md)
- [- createPhysicalAddressSpace](./iofirewirenub/api-1520934-createphysicaladdressspace.md)
- [- createPseudoAddressSpace](./iofirewirenub/api-1520884-createpseudoaddressspace.md)
- [- createReadCommand](./iofirewirenub/api-1520876-createreadcommand.md)
- [- createReadQuadCommand](./iofirewirenub/api-1520931-createreadquadcommand.md)
- [- createSimpleContiguousPhysicalAddressSpace](./iofirewirenub/api-1520883-createsimplecontiguousphysicalad.md)
- [- createSimplePhysicalAddressSpace](./iofirewirenub/api-1520897-createsimplephysicaladdressspace.md)
- [- createWriteCommand](./iofirewirenub/api-1520893-createwritecommand.md)
- [- createWriteQuadCommand](./iofirewirenub/api-1520905-createwritequadcommand.md)
- [- free](./iofirewirenub/api-1520886-free.md)
- [- getBus](./iofirewirenub/api-1520865-getbus.md)
- [- getConfigDirectory](./iofirewirenub/api-1520889-getconfigdirectory.md)
- [- getConfigDirectoryRef](./iofirewirenub/api-1520922-getconfigdirectoryref.md)
- [- getController](./iofirewirenub/api-1520923-getcontroller.md)
- [- getMetaClass](./iofirewirenub/api-1520874-getmetaclass.md)
- [- getNodeFlags](./iofirewirenub/api-1520870-getnodeflags.md)
- [- getNodeIDGeneration](./iofirewirenub/api-1520902-getnodeidgeneration.md)
- [- getNodeIDGeneration](./iofirewirenub/api-3516577-getnodeidgeneration.md)
- [- getTerminationState](./iofirewirenub/api-1520878-getterminationstate.md)
- [- getUniqueID](./iofirewirenub/api-1520916-getuniqueid.md)
- [- hopCount](./iofirewirenub/api-1520863-hopcount.md)
- [- hopCount](./iofirewirenub/api-3516578-hopcount.md)
- [- init](./iofirewirenub/api-1520862-init.md)
- [- isPhysicalAccessEnabled](./iofirewirenub/api-1520933-isphysicalaccessenabled.md)
- [- maxPackLog](./iofirewirenub/api-1520859-maxpacklog.md)
- [- maxPackLog](./iofirewirenub/api-3516579-maxpacklog.md)
- [- maxPackLog](./iofirewirenub/api-3516580-maxpacklog.md)
- [- setConfigDirectory](./iofirewirenub/api-1520872-setconfigdirectory.md)
- [- setMaxPackLog](./iofirewirenub/api-1520898-setmaxpacklog.md)
- [- setNodeFlags](./iofirewirenub/api-1520919-setnodeflags.md)
- [- setTerminationState](./iofirewirenub/api-1520910-setterminationstate.md)

## Relationships

### Inherits From
- [IOService](./ioservice.md)

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
- [IOFireWireUnit](./iofirewireunit.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iofirewirenub)*