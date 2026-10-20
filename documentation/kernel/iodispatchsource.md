# IODispatchSource

**Framework**: Kernel  
**Kind**: cl  
**Role**: Class

**Availability**:
- macOS 10.15+

## Declaration

```cpp
class IODispatchSource : OSObject, IODispatchSourceInterface
```

## Topics

### Instance Methods
- [- Cancel](./iodispatchsource/api-3223291-cancel.md)
- [- CheckForWork](./iodispatchsource/api-3223293-checkforwork.md)
- [- Dispatch](./iodispatchsource/api-3223295-dispatch.md)
- [- SetEnable](./iodispatchsource/api-3223296-setenable.md)
- [- SetEnableWithCompletion](./iodispatchsource/api-3325697-setenablewithcompletion.md)
- [- SetEnable_Impl](./iodispatchsource/api-3325699-setenable_impl.md)
- [- free](./iodispatchsource/api-3438199-free.md)
  Performs any final cleanup for the dispatch source.
- [- getMetaClass](./iodispatchsource/api-3223299-getmetaclass.md)
- [- init](./iodispatchsource/api-3438200-init.md)
  Handles the basic initialization of the dispatch source.
### Type Methods
- [+ Cancel_Invoke](./iodispatchsource/api-3223292-cancel_invoke.md)
- [+ CheckForWork_Invoke](./iodispatchsource/api-3223294-checkforwork_invoke.md)
- [+ SetEnableWithCompletion_Invoke](./iodispatchsource/api-3325698-setenablewithcompletion_invoke.md)
- [+ SetEnable_Invoke](./iodispatchsource/api-3223297-setenable_invoke.md)

## Relationships

### Inherits From
- [IODispatchSourceInterface](./iodispatchsourceinterface.md)
- [OSObject](./osobject.md)

## See Also

### Base Types
- [IOCommandPool](./iocommandpool.md)
  Manipulates a pool of commands which inherit from IOCommand.
- [IOCommandGate](./iocommandgate.md)
  Single-threaded work-loop client request mechanism.
- [IOCommand](./iocommand.md)
  This class is an abstract class which represents an I/O command.
- [IOEventSource](./ioeventsource.md)
  Abstract class for all work-loop event sources.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iodispatchsource)*