# handleCommand

**Framework**: Kernel  
**Kind**: instm

Called by executeCommand() to handle the client command from the workloop context.

## Declaration

```swift
virtual IOReturn handleCommand(
 void *command, 
 void *param1 = 0, 
 void *param2 = 0, 
 void *param3 = 0);
```

#### Return_value

kIOReturnSuccess on success, or an error code otherwise.

## Parameters

- `command`: The command code.
- `param1`: Command parameter.
- `param2`: Command parameter.
- `param3`: Command parameter.

## See Also

- [busCanDispatch](ioatacontroller/1811873-buscandispatch.md)
  answers whether the bus is in state such that the next command can be dispatched.
- [dispatchNext](ioatacontroller/1811887-dispatchnext.md)
  Causes the command at the front of the queue to dequeue, made the current command and begin execution.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/ioatacontroller/1811902-handlecommand)*