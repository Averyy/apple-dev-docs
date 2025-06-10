# dispatchNext

**Framework**: Kernel  
**Kind**: instm

Causes the command at the front of the queue to dequeue, made the current command and begin execution.

## Declaration

```swift
virtual IOReturn dispatchNext(
 void );
```

#### Return_value

noErr indicates successful dispatch.

## See Also

- [busCanDispatch](ioatacontroller/1811873-buscandispatch.md)
  answers whether the bus is in state such that the next command can be dispatched.
- [handleCommand](ioatacontroller/1811902-handlecommand.md)
  Called by executeCommand() to handle the client command from the workloop context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/ioatacontroller/1811887-dispatchnext)*