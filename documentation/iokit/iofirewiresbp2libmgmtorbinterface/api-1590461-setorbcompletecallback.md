# setORBCompleteCallback

**Framework**: IOKit  
**Kind**: structp  
**Role**: Instance Property

Sets the ORB completion routine.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```c
void (*setORBCompleteCallback)(void *self, void *refCon, IOFWSBP2ORBCompleteCallback callback);
```

#### Discussion

Sets the completion routine to be called when the ORB finishes execution. The refCon set with setRefCon will also be passed as the third argument to the completion handler.

## Parameters

- `self`: Pointer to a IOFireWireSBP2LibMgmtORBInterface.
- `refCon`: refCon passed as first argument to completion routine


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iofirewiresbp2libmgmtorbinterface/1590461-setorbcompletecallback)*