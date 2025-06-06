# IOCommandPool

**Framework**: Kernel  
**Kind**: cl

Manipulates a pool of commands which inherit from IOCommand.

**Availability**:
- DriverKit 21.0+
- macOS 10.6+

## Declaration

```swift
class IOCommandPool : OSObject
```

#### Overview

The IOCommandPool class is used to manipulate a pool of commands which inherit from IOCommand. It includes a factory method to create a pool of a certain size. Once the factory method is invoked, the semaphore is set to zero. The caller must then put commands in the pool by creating the command (via the controller's factory method or a memory allocation) and calling the returnCommand method with the newly created command as its argument.

## Topics

### Miscellaneous
- [commandPool](iocommandpool/1811017-commandpool.md)
  Should never be used, obsolete. See IOCommandPool::withWorkLoop.
- [gatedGetCommand](iocommandpool/1811028-gatedgetcommand.md)
- [gatedReturnCommand](iocommandpool/1811045-gatedreturncommand.md)
- [getCommand](iocommandpool/1811062-getcommand.md)
- [init](iocommandpool/1811075-init.md)
  Should never be used, obsolete. See initWithWorkLoop.
- [initWithWorkLoop](iocommandpool/1811086-initwithworkloop.md)
  Primary initializer for an IOCommandPool object.
- [returnCommand](iocommandpool/1811102-returncommand.md)
- [withWorkLoop(IOService *, IOWorkLoop *, UInt32)](iocommandpool/1811120-withworkloop.md)
  Should never be used, obsolete. See IOCommandPool::withWorkLoop.
- [withWorkLoop(IOWorkLoop *)](iocommandpool/1811136-withworkloop.md)
  Primary factory method for the IOCommandPool class
### Constants
- [kIOCommandPoolDefaultSize](iocommandpool/kiocommandpooldefaultsize.md)
  The default size of any command pool.
### DataTypes
- [ExpansionData](ioservice/expansiondata.md)
### Instance Variables
- [reserved](iocommandpool/reserved.md)
### Instance Methods
- [- free](iocommandpool/1560748-free.md)
- [- gatedGetCommand](iocommandpool/1560742-gatedgetcommand.md)
- [- gatedReturnCommand](iocommandpool/1560738-gatedreturncommand.md)
- [- getCommand](iocommandpool/1560741-getcommand.md)
- [- getMetaClass](iocommandpool/1560745-getmetaclass.md)
- [- init](iocommandpool/1560739-init.md)
- [- init](../driverkit/iocommandpool/3758242-init.md)
- [- initWithQueue](../driverkit/iocommandpool/3758243-initwithqueue.md)
- [- initWithWorkLoop](iocommandpool/1560744-initwithworkloop.md)
- [- returnCommand](iocommandpool/1560740-returncommand.md)
### Type Methods
- [+ commandPool](iocommandpool/1560747-commandpool.md)
- [+ withQueue](../driverkit/iocommandpool/3758244-withqueue.md)
- [+ withWorkLoop](iocommandpool/1560746-withworkloop.md)

## Relationships

### Inherits From
- [OSObject](../driverkit/osobject.md)
- [OSObject](osobject.md)

## See Also

- [IOCommandGate](iocommandgate.md)
  Single-threaded work-loop client request mechanism.
- [IOCommand](iocommand.md)
  This class is an abstract class which represents an I/O command.
- [IODispatchSource](iodispatchsource.md)
- [IOEventSource](ioeventsource.md)
  Abstract class for all work-loop event sources.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iocommandpool)*