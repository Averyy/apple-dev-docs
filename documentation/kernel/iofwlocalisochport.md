# IOFWLocalIsochPort

**Framework**: Kernel  
**Kind**: cl  
**Role**: Class

**Availability**:
- macOS 10.0+

## Declaration

```cpp
class IOFWLocalIsochPort : IOFWIsochPort
```

## Topics

### Miscellaneous
- [notify](./iofwlocalisochport/api-1812964-notify.md)
  Informs hardware of a change to the DCL program.
### DataTypes
- [ExpansionData](./ioservice/expansiondata.md)
### Instance Methods
- [- allocatePort](./iofwlocalisochport/api-1521417-allocateport.md)
- [- free](./iofwlocalisochport/api-1521418-free.md)
- [- getMetaClass](./iofwlocalisochport/api-1521421-getmetaclass.md)
- [- getProgramRef](./iofwlocalisochport/api-1521420-getprogramref.md)
- [- getSupported](./iofwlocalisochport/api-1521424-getsupported.md)
- [- init](./iofwlocalisochport/api-1521425-init.md)
- [- notify](./iofwlocalisochport/api-1521429-notify.md)
- [- releasePort](./iofwlocalisochport/api-1521434-releaseport.md)
- [- setIsochResourceFlags](./iofwlocalisochport/api-1521437-setisochresourceflags.md)
- [- start](./iofwlocalisochport/api-1521435-start.md)
- [- stop](./iofwlocalisochport/api-1521427-stop.md)
- [- synchronizeWithIO](./iofwlocalisochport/api-1521422-synchronizewithio.md)
### Type Methods
- [+ printDCLProgram](./iofwlocalisochport/api-1521431-printdclprogram.md)

## Relationships

### Inherits From
- [IOFWIsochPort](./iofwisochport.md)

## See Also

### FireWire Types
- [UCInfo](./ucinfo.md)
- [IOLocalConfigDirectory](./iolocalconfigdirectory.md)
- [IOConfigDirectory](./ioconfigdirectory.md)
- [IOFireWireDuplicateGUIDList](./iofirewireduplicateguidlist.md)
- [IOFireWireIRMAllocation](./iofirewireirmallocation.md)
- [IOFireWireMultiIsochReceiveListener](./iofirewiremultiisochreceivelistener.md)
- [IOFWPHYPacketListener](./iofwphypacketlistener.md)
- [IOFireWireMultiIsochReceivePacket](./iofirewiremultiisochreceivepacket.md)
- [IOFireWirePowerManager](./iofirewirepowermanager.md)
- [IOFWIsochChannel](./iofwisochchannel.md)
- [IOFWIsochPort](./iofwisochport.md)
- [IOFWSyncer](./iofwsyncer.md)
- [IOFWUserObjectExporter](./iofwuserobjectexporter.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iofwlocalisochport)*