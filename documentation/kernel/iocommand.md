# IOCommand

**Framework**: Kernel  
**Kind**: cl

This class is an abstract class which represents an I/O command.

**Availability**:
- DriverKit 21.0+
- macOS 10.6+

## Declaration

```swift
class IOCommand : OSObject
```

#### Overview

This class is an abstract class which represents an I/O command passed from a device driver to a controller. All controller commands (e.g. IOATACommand) should inherit from this class.

## Topics

### Instance Variables
- [fCommandChain](iocommand/fcommandchain.md)
### Instance Methods
- [- CommandChain](../driverkit/iocommand/3758238-commandchain.md)
- [- free](../driverkit/iocommand/3758240-free.md)
- [- getMetaClass](iocommand/1528522-getmetaclass.md)
- [- init](iocommand/1528524-init.md)
### Type Methods
- [+ FromChain](../driverkit/iocommand/3758239-fromchain.md)

## Relationships

### Inherits From
- [OSObject](../driverkit/osobject.md)
- [OSObject](osobject.md)

## See Also

- [IOCommandPool](iocommandpool.md)
  Manipulates a pool of commands which inherit from IOCommand.
- [IOCommandGate](iocommandgate.md)
  Single-threaded work-loop client request mechanism.
- [IODispatchSource](iodispatchsource.md)
- [IOEventSource](ioeventsource.md)
  Abstract class for all work-loop event sources.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iocommand)*