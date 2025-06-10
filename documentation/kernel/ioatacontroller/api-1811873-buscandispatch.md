# busCanDispatch

**Framework**: Kernel  
**Kind**: instm

answers whether the bus is in state such that the next command can be dispatched.

## Declaration

```swift
virtual bool busCanDispatch(
 void );
```

#### Return_value

true - bus is free to issue commands. false - bus cannot issue commands at this time.

## See Also

- [dispatchNext](ioatacontroller/1811887-dispatchnext.md)
  Causes the command at the front of the queue to dequeue, made the current command and begin execution.
- [handleCommand](ioatacontroller/1811902-handlecommand.md)
  Called by executeCommand() to handle the client command from the workloop context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/ioatacontroller/1811873-buscandispatch)*