# MPRegisterDebugger

**Framework**: Core Services  
**Kind**: func  
**Role**: Function

Registers a debugger. 

**Availability**:
- macOS 10.0+ - Deprecated in 10.7

## Declaration

```c
OSStatus MPRegisterDebugger(MPQueueID queue, MPDebuggerLevel level);
```

#### Return Value

A result code. See [Result Codes](./carbon_core/multiprocessing_services.md#1663965).

#### Discussion

In macOS, this function is available but is not implemented. Use system debugging services to write a debugger for macOS.

## Parameters

- `queue`: The ID of the queue to which you want exception messages and other information to be sent. 
- `level`: The level of this debugger with respect to other debuggers. Exceptions and informational messages are sent first to the debugger with the highest level. If more than one debugger attempts to register at a particular level, only the first debugger is registered. Other attempts return an error. 

## See Also

### Debugger Support Functions
- [MPUnregisterDebugger](./api-1585598-mpunregisterdebugger.md)
  Unregisters a debugger. 


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1585573-mpregisterdebugger)*