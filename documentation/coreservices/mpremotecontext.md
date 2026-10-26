# MPRemoteContext

**Framework**: Core Services  
**Kind**: tdef  
**Role**: Type Alias

Specify which contexts are allowed to execute the callback function when using `MPRemoteCall`.

**Availability**:
- Mac Catalyst 17.0+
- macOS 10.0+

## Declaration

```c
typedef UInt8 MPRemoteContext;
```

#### Discussion

These constants are used to support older versions of Mac OS and are ignored in macOS.

## Topics

### Constants
- [kMPAnyRemoteContext](./api-1585592-anonymous/kmpanyremotecontext.md)
  Any cooperative context can execute the function. Note that the called function may not have access to any of the owning context’s process-specific low-memory values. 
- [kMPOwningProcessRemoteContext](./api-1585592-anonymous/kmpowningprocessremotecontext.md)
  Only the context that owns the task can execute the function.
- [kMPInterruptRemoteContext](./api-1585592-anonymous/kmpinterruptremotecontext.md)
- [kMPAsyncInterruptRemoteContext](./api-1585592-anonymous/kmpasyncinterruptremotecontext.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/mpremotecontext)*