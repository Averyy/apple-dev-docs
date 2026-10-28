# GetCommandCount

**Framework**: IOKit  
**Kind**: structp  
**Role**: Instance Property

Returns the number of commands currently in this vector.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.5+

## Declaration

```c
UInt32 (*GetCommandCount)(IOFireWireLibVectorCommandRef self);
```

## Return Value

UInt32 The number of commands in this vector

## Parameters

- `self`: A reference to the vector command object

## See Also

### Miscellaneous
- [AddCommand](./api-1555740-addcommand.md)
  Adds a command to the vector command.
- [EnsureCapacity](./api-1555615-ensurecapacity.md)
  Sets the number of commands this vector can hold.
- [GetCommandAtIndex](./api-1556052-getcommandatindex.md)
  Returns the command at a given index.
- [GetFlags](./api-1555608-getflags.md)
  Get the flags currently set for this command.
- [GetIndexOfCommand](./api-1555861-getindexofcommand.md)
  Returns the index of the specified command.
- [GetRefCon](./api-1555688-getrefcon.md)
  Get the reference constant for this command.
- [InsertCommandAtIndex](./api-1556014-insertcommandatindex.md)
  Inserts a command at a given index. Commands at and after this index will be moved to their next sequential index.
- [IsExecuting](./api-1555674-isexecuting.md)
  Checks if the vector command is currently executing.
- [RemoveAllCommands](./api-1555889-removeallcommands.md)
  Removes all commands from the vector.
- [RemoveCommand](./api-1556118-removecommand.md)
  Removes a command to the vector command.
- [RemoveCommandAtIndex](./api-1556038-removecommandatindex.md)
  Removes the command at a give index. Commands at and afte this index will be moved to their previous sequential index.
- [SetCallback](./api-1556100-setcallback.md)
  Set the callback routine for this command.
- [SetFlags](./api-1556107-setflags.md)
  Set flags governing this command's execution.
- [SetRefCon](./api-1555654-setrefcon.md)
  Set the reference constant for this command.
- [Submit(IOFireWireLibVectorCommandRef)](./submit_iofirewirelibvectorcommandref.md)
  Submit this command object to FireWire for execution.
- [Submit(IOFireWireLibVectorCommandRef, void *, IOFireWireLibCommandCallback)](./submit_iofirewirelibvectorcommandref_void_iofirewirelibcommandcallback.md)
  Submit this command object to FireWire for execution.
- [SubmitWithRefconAndCallback](./api-1555731-submitwithrefconandcallback.md)
  Submit this command object to FireWire for execution.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iofirewirelibvectorcommandinterface/1555752-getcommandcount)*