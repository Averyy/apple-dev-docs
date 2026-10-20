# IOFWReadQuadCommand

**Framework**: Kernel  
**Kind**: cl  
**Role**: Class

An easier to use version of IOFWReadCommand for use when the data to be transferred is an integer number of quads. Note that block read requests will be used for transfers greater than one quad unless setMaxPacket(4) is called.

**Availability**:
- macOS 10.0+

## Declaration

```cpp
class IOFWReadQuadCommand : IOFWAsyncCommand
```

## Topics

### Instance Methods
- [- createMemberVariables](./iofwreadquadcommand/api-1563812-createmembervariables.md)
- [- destroyMemberVariables](./iofwreadquadcommand/api-1563779-destroymembervariables.md)
- [- execute](./iofwreadquadcommand/api-1563846-execute.md)
- [- free](./iofwreadquadcommand/api-1563855-free.md)
- [- getMetaClass](./iofwreadquadcommand/api-1563842-getmetaclass.md)
- [- gotPacket](./iofwreadquadcommand/api-1563835-gotpacket.md)
- [- initAll](./iofwreadquadcommand/api-1563850-initall.md)
- [- initAll](./iofwreadquadcommand/api-3516555-initall.md)
- [- reinit](./iofwreadquadcommand/api-1563902-reinit.md)
- [- reinit](./iofwreadquadcommand/api-3516556-reinit.md)
- [- setPingTime](./iofwreadquadcommand/api-1563873-setpingtime.md)

## Relationships

### Inherits From
- [IOFWAsyncCommand](./iofwasynccommand.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iofwreadquadcommand)*