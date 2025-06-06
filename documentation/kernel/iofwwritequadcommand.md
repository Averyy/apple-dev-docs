# IOFWWriteQuadCommand

**Framework**: Kernel  
**Kind**: cl

An easier to use version of IOFWWriteCommand for use when the data to be transferred is small and an integer number of quads. Note that block read requests will be used for transfers greater than one quad unless setMaxPacket(4) is called. kMaxWriteQuads is the largest legal number of quads that this object can be asked to transfer (the data is copied into an internal buffer in init() and reinit()).

**Availability**:
- macOS 10.0+

## Declaration

```swift
class IOFWWriteQuadCommand : IOFWAsyncCommand
```

## Topics

### Instance Methods
- [- createMemberVariables](iofwwritequadcommand/1563773-createmembervariables.md)
- [- createMemoryDescriptor](iofwwritequadcommand/1563753-creatememorydescriptor.md)
- [- destroyMemberVariables](iofwwritequadcommand/1563848-destroymembervariables.md)
- [- destroyMemoryDescriptor](iofwwritequadcommand/1563815-destroymemorydescriptor.md)
- [- execute](iofwwritequadcommand/1563774-execute.md)
- [- free](iofwwritequadcommand/1563894-free.md)
- [- getMetaClass](iofwwritequadcommand/1563768-getmetaclass.md)
- [- gotPacket](iofwwritequadcommand/1563766-gotpacket.md)
- [- initAll](iofwwritequadcommand/1563825-initall.md)
- [- initAll](iofwwritequadcommand/3516559-initall.md)
- [- initWithController](iofwwritequadcommand/1563860-initwithcontroller.md)
- [- reinit](iofwwritequadcommand/1563808-reinit.md)
- [- reinit](iofwwritequadcommand/3516560-reinit.md)
- [- setDeferredNotify](iofwwritequadcommand/1563791-setdeferrednotify.md)
- [- setQuads](iofwwritequadcommand/1563869-setquads.md)

## Relationships

### Inherits From
- [IOFWAsyncCommand](iofwasynccommand.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iofwwritequadcommand)*