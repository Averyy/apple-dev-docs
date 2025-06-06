# IOCommandGate

**Framework**: Kernel  
**Kind**: cl

Single-threaded work-loop client request mechanism.

**Availability**:
- macOS 10.0+

## Declaration

```swift
class IOCommandGate : IOEventSource
```

#### Overview

An IOCommandGate instance is an extremely lightweight mechanism that executes an action on the driver's work-loop. 'On the work-loop' is actually a lie but the work-loop single threaded semantic is maintained for this event source. Using the work-loop gate rather than execution by the workloop. The command gate tests for a potential self dead lock by checking if the runCommand request is made from the work-loop's thread, it doesn't check for a mutual dead lock though where a pair of work loop's dead lock each other.

The IOCommandGate is a lighter weight version of the IOCommandQueue and should be used in preference. Generally use a command queue whenever you need a client to submit a request to a work loop. A typical command gate action would check if the hardware is active, if so it will add the request to a pending queue internal to the device or the device's family. Otherwise if the hardware is inactive then this request can be acted upon immediately.

CAUTION: The runAction, runCommand, and attemptCommand functions cannot be called from an interrupt context.

## Topics

### Miscellaneous
- [attemptAction](iocommandgate/1811105-attemptaction.md)
  Single thread a call to an action with the target work-loop.
- [attemptCommand](iocommandgate/1811141-attemptcommand.md)
  Single thread a command with the target work-loop.
- [commandGate](iocommandgate/1811293-commandgate.md)
  Factory method to create and initialise an IOCommandGate, See $link init.
- [commandSleep(void *, AbsoluteTime, UInt32)](iocommandgate/1811482-commandsleep.md)
  Put a thread that is currently holding the command gate to sleep.
- [commandSleep(void *, UInt32)](iocommandgate/1811498-commandsleep.md)
  Put a thread that is currently holding the command gate to sleep.
- [commandWakeup](iocommandgate/1811517-commandwakeup.md)
  Wakeup one or more threads that are asleep on an event.
- [disable](iocommandgate/1811531-disable.md)
  Disable the command gate
- [enable](iocommandgate/1811547-enable.md)
  Enable command gate, this will unblock any blocked Commands and Actions.
- [init](iocommandgate/1811560-init.md)
  Class initialiser.
- [runAction](iocommandgate/1811576-runaction.md)
  Single thread a call to an action with the target work-loop.
- [runCommand](iocommandgate/1811585-runcommand.md)
  Single thread a command with the target work-loop.
### Callbacks
- [Action](ioworkloop/action.md)
### DataTypes
- [ExpansionData](ioservice/expansiondata.md)
### Instance Variables
- [reserved](iocommandgate/reserved.md)
### Instance Methods
- [- attemptAction](iocommandgate/1573823-attemptaction.md)
- [- attemptCommand](iocommandgate/1573825-attemptcommand.md)
- [- commandSleep](iocommandgate/1573818-commandsleep.md)
- [- commandSleep](iocommandgate/3516447-commandsleep.md)
- [- commandWakeup](iocommandgate/1573826-commandwakeup.md)
- [- disable](iocommandgate/1573828-disable.md)
- [- enable](iocommandgate/1573822-enable.md)
- [- free](iocommandgate/1573821-free.md)
- [- getMetaClass](iocommandgate/1573820-getmetaclass.md)
- [- init](iocommandgate/1573817-init.md)
- [- runAction](iocommandgate/1573816-runaction.md)
- [- runActionBlock](iocommandgate/2967266-runactionblock.md)
- [- runCommand](iocommandgate/1573824-runcommand.md)
- [- setWorkLoop](iocommandgate/1573827-setworkloop.md)
### Type Methods
- [+ commandGate](iocommandgate/1573819-commandgate.md)

## Relationships

### Inherits From
- [IOEventSource](ioeventsource.md)

## See Also

- [IOCommandPool](iocommandpool.md)
  Manipulates a pool of commands which inherit from IOCommand.
- [IOCommand](iocommand.md)
  This class is an abstract class which represents an I/O command.
- [IODispatchSource](iodispatchsource.md)
- [IOEventSource](ioeventsource.md)
  Abstract class for all work-loop event sources.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iocommandgate)*