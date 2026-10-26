# Anonymous

**Framework**: Core Services  
**Kind**: enum  
**Role**: Enumeration

**Availability**:
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.0+ - Deprecated in 10.7

## Declaration

```c
enum : unsigned int {
    ...
};
```

## Topics

### Constants
- [kMPAnyRemoteContext](./api-1585592-anonymous/kmpanyremotecontext.md)
  Any cooperative context can execute the function. Note that the called function may not have access to any of the owning context’s process-specific low-memory values. 
- [kMPAsyncInterruptRemoteContext](./api-1585592-anonymous/kmpasyncinterruptremotecontext.md)
- [kMPInterruptRemoteContext](./api-1585592-anonymous/kmpinterruptremotecontext.md)
- [kMPOwningProcessRemoteContext](./api-1585592-anonymous/kmpowningprocessremotecontext.md)
  Only the context that owns the task can execute the function.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1585592-anonymous)*