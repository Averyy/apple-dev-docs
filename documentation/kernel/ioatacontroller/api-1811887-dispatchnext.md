# dispatchNext

**Framework**: Kernel  
**Kind**: instm

Causes the command at the front of the queue to dequeue, made the current command and begin execution.

## Declaration

```cpp
virtual IOReturn dispatchNext(
 void );
```

## Return Value

noErr indicates successful dispatch.

## See Also

### Miscellaneous
- [busCanDispatch](./api-1811873-buscandispatch.md)
  answers whether the bus is in state such that the next command can be dispatched.
- [handleCommand](./api-1811902-handlecommand.md)
  Called by executeCommand() to handle the client command from the workloop context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/ioatacontroller/1811887-dispatchnext)*