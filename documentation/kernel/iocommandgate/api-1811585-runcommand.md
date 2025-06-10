# runCommand

**Framework**: Kernel  
**Kind**: instm

Single thread a command with the target work-loop.

## Declaration

```swift
virtual IOReturn runCommand(
 void *arg0 = 0,
 void *arg1 = 0, 
 void *arg2 = 0,
 void *arg3 = 0);
```

#### Return_value

kIOReturnSuccess if successful. kIOReturnAborted if a disabled command gate is free()ed before being reenabled, kIOReturnNoResources if no action available.

#### Overview

Client function that causes the current action to be called in a single threaded manner. Beware the work-loop's gate is recursive and command gates can cause direct or indirect re-entrancy. When the executing on a client's thread runCommand will sleep until the work-loop's gate opens for execution of client actions, the action is single threaded against all other work-loop event sources. If the command is disabled the attempt to run a command will be stalled until enable is called.

## Parameters

- `arg0`: Parameter for action of command gate, defaults to 0.
- `arg1`: Parameter for action of command gate, defaults to 0.
- `arg2`: Parameter for action of command gate, defaults to 0.
- `arg3`: Parameter for action of command gate, defaults to 0.

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iocommandgate/1811585-runcommand)*