# commandSleep(void *, AbsoluteTime, UInt32)

**Framework**: Kernel  
**Kind**: instm

Put a thread that is currently holding the command gate to sleep.

## Declaration

```swift
virtual IOReturn commandSleep(
 void *event, 
 AbsoluteTimedeadline, 
 UInt32interruptible);
```

#### Return_value

THREAD_AWAKENED - normal wakeup, THREAD_TIMED_OUT - timeout expired, THREAD_INTERRUPTED - interrupted, THREAD_RESTART - restart operation entirely, kIOReturnNotPermitted if the calling thread does not hold the command gate.

#### Overview

Put a thread to sleep waiting for an event but release the gate first. If the event occurs or timeout occurs then the commandGate is closed before the function returns.

## Parameters

- `event`: Pointer to an address.
- `deadline`: Clock deadline to timeout the sleep.
- `interruptible`: THREAD_UNINT, THREAD_INTERRUPTIBLE or THREAD_ABORTSAFE. THREAD_UNINT specifies that the sleep cannot be interrupted by a signal. THREAD_INTERRUPTIBLE specifies that the sleep may be interrupted by a "kill -9" signal. THREAD_ABORTSAFE specifies that the sleep may be interrupted by any user signal.

## See Also

- [attemptAction](iocommandgate/1811105-attemptaction.md)
  Single thread a call to an action with the target work-loop.
- [attemptCommand](iocommandgate/1811141-attemptcommand.md)
  Single thread a command with the target work-loop.
- [commandGate](iocommandgate/1811293-commandgate.md)
  Factory method to create and initialise an IOCommandGate, See $link init.
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

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iocommandgate/1811482-commandsleep)*