# commandGate

**Framework**: Kernel  
**Kind**: instm

Factory method to create and initialise an IOCommandGate, See $link init.

## Declaration

```c
static IOCommandGate *commandGate(
 OSObject *owner,
 Action action = 0);
```

#### Return Value

Returns a pointer to the new command gate if sucessful, 0 otherwise.

## See Also

### Miscellaneous
- [attemptAction](./api-1811105-attemptaction.md)
  Single thread a call to an action with the target work-loop.
- [attemptCommand](./api-1811141-attemptcommand.md)
  Single thread a command with the target work-loop.
- [commandSleep(void *, AbsoluteTime, UInt32)](./api-1811482-commandsleep.md)
  Put a thread that is currently holding the command gate to sleep.
- [commandSleep(void *, UInt32)](./api-1811498-commandsleep.md)
  Put a thread that is currently holding the command gate to sleep.
- [commandWakeup](./api-1811517-commandwakeup.md)
  Wakeup one or more threads that are asleep on an event.
- [disable](./api-1811531-disable.md)
  Disable the command gate
- [enable](./api-1811547-enable.md)
  Enable command gate, this will unblock any blocked Commands and Actions.
- [init](./api-1811560-init.md)
  Class initialiser.
- [runAction](./api-1811576-runaction.md)
  Single thread a call to an action with the target work-loop.
- [runCommand](./api-1811585-runcommand.md)
  Single thread a command with the target work-loop.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iocommandgate/1811293-commandgate)*