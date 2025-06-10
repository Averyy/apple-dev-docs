# attemptCommand

**Framework**: Kernel  
**Kind**: instm

Single thread a command with the target work-loop.

## Declaration

```swift
virtual IOReturn attemptCommand(
 void *arg0 = 0,
 void *arg1 = 0, 
 void *arg2 = 0,
 void *arg3 = 0);
```

#### Return_value

kIOReturnSuccess if successful. kIOReturnNotPermitted if this event source is currently disabled, kIOReturnNoResources if no action available, kIOReturnCannotLock if lock attempt fails.

#### Overview

Client function that causes the current action to be called in a single threaded manner. When the executing on a client's thread attemptCommand will fail if the work-loop's gate is closed.

## Parameters

- `arg0`: Parameter for action of command gate, defaults to 0.
- `arg1`: Parameter for action of command gate, defaults to 0.
- `arg2`: Parameter for action of command gate, defaults to 0.
- `arg3`: Parameter for action of command gate, defaults to 0.

## See Also

- [attemptAction](iocommandgate/1811105-attemptaction.md)
  Single thread a call to an action with the target work-loop.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iocommandgate/1811141-attemptcommand)*