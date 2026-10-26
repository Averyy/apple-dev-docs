# MPRemoteCall

**Framework**: Core Services  
**Kind**: func  
**Role**: Function

Calls a non-reentrant function and blocks the current task. 

**Availability**:
- macOS 10.0+ - Deprecated in 10.7

## Declaration

```c
void * MPRemoteCall(MPRemoteProcedure remoteProc, void *parameter, MPRemoteContext context);
```

#### Return Value

The value that your remote procedure callback returned. 

#### Discussion

You use this function to execute code on your application’s main task. The `remoteProc` function is scheduled on the application’s main run loop and run in the default mode (`kCFRunloopDefaultMode`). If you call this function from your application’s main task, the `remoteProc` function is executed immediately in the current mode without blocking the task; otherwise, calling this function blocks the current task until the remote call completes.

## Parameters

- `remoteProc`: A pointer to the application-defined function you want to call. See [`MPRemoteProcedure`](./mpremoteprocedure.md) for more information about the form of this function. 
- `parameter`: A pointer to a parameter to pass to the application-defined function. For example, this value could point to a data structure or a memory location. 
- `context`: This parameter is ignored; specify `kMPOwningProcessRemoteContext`. 

## See Also

### Remote Calling Functions
- [MPRemoteCallCFM](./api-1585757-mpremotecallcfm.md)
  Calls a non-reentrant function and blocks the current task. 


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1585652-mpremotecall)*