# disable

**Framework**: Kernel  
**Kind**: instm

Disable the command gate

## Declaration

```swift
virtual void disable();
```

#### Overview

When a command gate is disabled all future calls to runAction and runCommand will stall until the gate is enable()d later. This can be used to block client threads when a system sleep is requested. The IOWorkLoop thread itself will never stall, even when making runAction/runCommand calls. This call must be made from a gated context, to clear potential race conditions.

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
- [enable](iocommandgate/1811547-enable.md)
  Enable command gate, this will unblock any blocked Commands and Actions.
- [init](iocommandgate/1811560-init.md)
  Class initialiser.
- [runAction](iocommandgate/1811576-runaction.md)
  Single thread a call to an action with the target work-loop.
- [runCommand](iocommandgate/1811585-runcommand.md)
  Single thread a command with the target work-loop.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iocommandgate/1811531-disable)*