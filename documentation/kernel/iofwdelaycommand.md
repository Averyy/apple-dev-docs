# IOFWDelayCommand

**Framework**: Kernel  
**Kind**: cl  
**Role**: Class

Command to execute some code after a specified delay (in microseconds) All it does is timeout after the specified delay, hence calling the completion callback.

**Availability**:
- macOS 10.0+

## Declaration

```cpp
class IOFWDelayCommand : IOFWBusCommand
```

## Topics

### DataTypes
- [ExpansionData](./ioservice/expansiondata.md)
### Instance Variables
- [reserved](./iofwdelaycommand/reserved.md)
### Instance Methods
- [- execute](./iofwdelaycommand/api-1563818-execute.md)
- [- getMetaClass](./iofwdelaycommand/api-1563819-getmetaclass.md)
- [- initWithDelay](./iofwdelaycommand/api-1563783-initwithdelay.md)
- [- reinit](./iofwdelaycommand/api-1563823-reinit.md)

## Relationships

### Inherits From
- [IOFWBusCommand](./iofwbuscommand.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iofwdelaycommand)*