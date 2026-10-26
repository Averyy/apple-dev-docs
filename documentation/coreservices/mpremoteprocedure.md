# MPRemoteProcedure

**Framework**: Core Services  
**Kind**: tdef  
**Role**: Type Alias

Defines a remote procedure call.

**Availability**:
- Mac Catalyst 17.0+
- macOS 10.0+

## Declaration

```c
typedef void *(*MPRemoteProcedure)(void *parameter);
```

#### Discussion

For example, this is how you would declare the application-defined function if you were to name the function `MyRemoteProcedure`:

## Parameters

- `parameter`: A pointer to the application-defined value you passed to the function [`MPRemoteCallCFM`](./api-1585757-mpremotecallcfm.md). For example, this value could point to a data structure or a memory location.

## See Also

### Callbacks
- [TaskProc](./taskproc.md)
  Defines the entry point of a task.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/mpremoteprocedure)*