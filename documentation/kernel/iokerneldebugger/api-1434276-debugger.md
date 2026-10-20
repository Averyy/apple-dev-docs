# debugger

**Framework**: Kernel  
**Kind**: clm  
**Role**: Type Method

**Availability**:
- macOS 10.11.4+

## Declaration

```c
static IOKernelDebugger * debugger(IOService *target, IODebuggerTxHandler txHandler, IODebuggerRxHandler rxHandler, IODebuggerLinkStatusHandler linkStatusHandler, IODebuggerSetModeHandler setModeHandler);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iokerneldebugger/1434276-debugger)*