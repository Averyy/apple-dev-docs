# IOCommand

**Framework**: Kernel  
**Kind**: cl  
**Role**: Class

This class is an abstract class which represents an I/O command.

**Availability**:
- DriverKit 21.0+
- macOS 10.6+

## Declaration

```cpp
class IOCommand : OSObject
```

## Overview

This class is an abstract class which represents an I/O command passed from a device driver to a controller. All controller commands (e.g. IOATACommand) should inherit from this class.

## Topics

### Instance Variables
- [fCommandChain](./iocommand/fcommandchain.md)
### Instance Methods
- [- CommandChain](../DriverKit/iocommand/commandchain.md)
- [- free](../DriverKit/iocommand/free.md)
- [- getMetaClass](./iocommand/api-1528522-getmetaclass.md)
- [- init](./iocommand/api-1528524-init.md)
### Type Methods
- [+ FromChain](../DriverKit/iocommand/fromchain.md)

## Relationships

### Inherits From
- [OSObject](../DriverKit/osobject.md)
- [OSObject](./osobject.md)

## See Also

### Base Types
- [IOCommandPool](./iocommandpool.md)
  Manipulates a pool of commands which inherit from IOCommand.
- [IOCommandGate](./iocommandgate.md)
  Single-threaded work-loop client request mechanism.
- [IODispatchSource](./iodispatchsource.md)
- [IOEventSource](./ioeventsource.md)
  Abstract class for all work-loop event sources.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iocommand)*