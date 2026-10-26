# TaskProc

**Framework**: Core Services  
**Kind**: tdef  
**Role**: Type Alias

Defines the entry point of a task.

**Availability**:
- Mac Catalyst 17.0+
- macOS 10.0+

## Declaration

```c
typedef OSStatus (*TaskProc)(void *parameter);
```

#### Discussion

For example, this is how you would declare the application-defined function if you were to name the function `MyTaskProc`:

## Parameters

- `parameter`: A pointer to the application-defined value you passed to the function [`MPCreateTask`](./api-1585779-mpcreatetask.md). For example, this value could point to a data structure or a memory location.

## See Also

### Callbacks
- [MPRemoteProcedure](./mpremoteprocedure.md)
  Defines a remote procedure call.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/taskproc)*