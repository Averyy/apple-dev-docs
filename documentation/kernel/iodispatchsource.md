# IODispatchSource

**Framework**: Kernel  
**Kind**: cl

**Availability**:
- macOS 10.15+

## Declaration

```swift
class IODispatchSource : OSObject, IODispatchSourceInterface
```

## Topics

### Instance Methods
- [- Cancel](iodispatchsource/3223291-cancel.md)
- [- CheckForWork](iodispatchsource/3223293-checkforwork.md)
- [- Dispatch](iodispatchsource/3223295-dispatch.md)
- [- SetEnable](iodispatchsource/3223296-setenable.md)
- [- SetEnableWithCompletion](iodispatchsource/3325697-setenablewithcompletion.md)
- [- SetEnable_Impl](iodispatchsource/3325699-setenable_impl.md)
- [- free](iodispatchsource/3438199-free.md)
  Performs any final cleanup for the dispatch source.
- [- getMetaClass](iodispatchsource/3223299-getmetaclass.md)
- [- init](iodispatchsource/3438200-init.md)
  Handles the basic initialization of the dispatch source.
### Type Methods
- [+ Cancel_Invoke](iodispatchsource/3223292-cancel_invoke.md)
- [+ CheckForWork_Invoke](iodispatchsource/3223294-checkforwork_invoke.md)
- [+ SetEnableWithCompletion_Invoke](iodispatchsource/3325698-setenablewithcompletion_invoke.md)
- [+ SetEnable_Invoke](iodispatchsource/3223297-setenable_invoke.md)

## Relationships

### Inherits From
- [IODispatchSourceInterface](iodispatchsourceinterface.md)
- [OSObject](osobject.md)

## See Also

- [IOCommandPool](iocommandpool.md)
  Manipulates a pool of commands which inherit from IOCommand.
- [IOCommandGate](iocommandgate.md)
  Single-threaded work-loop client request mechanism.
- [IOCommand](iocommand.md)
  This class is an abstract class which represents an I/O command.
- [IOEventSource](ioeventsource.md)
  Abstract class for all work-loop event sources.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iodispatchsource)*