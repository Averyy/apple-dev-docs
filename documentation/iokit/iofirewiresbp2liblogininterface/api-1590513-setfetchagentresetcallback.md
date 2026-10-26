# setFetchAgentResetCallback

**Framework**: IOKit  
**Kind**: structp  
**Role**: Instance Property

Sets the callback to be called when a fetch agent reset completes.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```c
void (*setFetchAgentResetCallback)(void *self, void *refCon, IOFWSBP2StatusCallback callback);
```

#### Discussion

The fetch agent state machine on the device can be reset by a write to a specific register. The SBP2 services offer a utility method to reset the fetch agent. You can register a callback routine here to be notified when this rest write completes.

## Parameters

- `self`: Pointer to IOFireWireSBP2LibLoginInterface object.
- `refCon`: refCon passed to callback.
- `callback`: address of callback method of type FWSBP2FetchAgentWriteCallback.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iofirewiresbp2liblogininterface/1590513-setfetchagentresetcallback)*