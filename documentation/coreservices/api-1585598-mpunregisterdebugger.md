# MPUnregisterDebugger

**Framework**: Core Services  
**Kind**: func  
**Role**: Function

Unregisters a debugger. 

**Availability**:
- macOS 10.0+ - Deprecated in 10.7

## Declaration

```c
OSStatus MPUnregisterDebugger(MPQueueID queue);
```

## Return Value

A result code. See [Result Codes](./carbon_core/multiprocessing_services.md#1663965).

## Discussion

In macOS, this function is available but is not implemented. Use system debugging services to write a debugger for macOS.

## Parameters

- `queue`: The ID of the queue whose debugger you want to unregister. 

## See Also

### Debugger Support Functions
- [MPRegisterDebugger](./api-1585573-mpregisterdebugger.md)
  Registers a debugger. 


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1585598-mpunregisterdebugger)*