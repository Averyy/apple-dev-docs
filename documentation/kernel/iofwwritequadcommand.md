# IOFWWriteQuadCommand

**Framework**: Kernel  
**Kind**: cl  
**Role**: Class

An easier to use version of IOFWWriteCommand for use when the data to be transferred is small and an integer number of quads. Note that block read requests will be used for transfers greater than one quad unless setMaxPacket(4) is called. kMaxWriteQuads is the largest legal number of quads that this object can be asked to transfer (the data is copied into an internal buffer in init() and reinit()).

**Availability**:
- macOS 10.0+

## Declaration

```cpp
class IOFWWriteQuadCommand : IOFWAsyncCommand
```

## Topics

### Instance Methods
- [- createMemberVariables](./iofwwritequadcommand/api-1563773-createmembervariables.md)
- [- createMemoryDescriptor](./iofwwritequadcommand/api-1563753-creatememorydescriptor.md)
- [- destroyMemberVariables](./iofwwritequadcommand/api-1563848-destroymembervariables.md)
- [- destroyMemoryDescriptor](./iofwwritequadcommand/api-1563815-destroymemorydescriptor.md)
- [- execute](./iofwwritequadcommand/api-1563774-execute.md)
- [- free](./iofwwritequadcommand/api-1563894-free.md)
- [- getMetaClass](./iofwwritequadcommand/api-1563768-getmetaclass.md)
- [- gotPacket](./iofwwritequadcommand/api-1563766-gotpacket.md)
- [- initAll](./iofwwritequadcommand/api-1563825-initall.md)
- [- initAll](./iofwwritequadcommand/api-3516559-initall.md)
- [- initWithController](./iofwwritequadcommand/api-1563860-initwithcontroller.md)
- [- reinit](./iofwwritequadcommand/api-1563808-reinit.md)
- [- reinit](./iofwwritequadcommand/api-3516560-reinit.md)
- [- setDeferredNotify](./iofwwritequadcommand/api-1563791-setdeferrednotify.md)
- [- setQuads](./iofwwritequadcommand/api-1563869-setquads.md)

## Relationships

### Inherits From
- [IOFWAsyncCommand](./iofwasynccommand.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iofwwritequadcommand)*