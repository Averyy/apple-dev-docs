# WSMethodInvocationUnscheduleFromRunLoop

**Framework**: Core Services  
**Kind**: func  
**Role**: Function

Unschedules a method invocation from a run loop.

**Availability**:
- macOS 10.2+ - Deprecated in 10.8

## Declaration

```c
void WSMethodInvocationUnscheduleFromRunLoop(WSMethodInvocationRef invocation, CFRunLoopRef runLoop, CFStringRef runLoopMode);
```

## Discussion

Unschedules the invocation from a given run loop and mode.  If the invocation has not yet completed, its callback will not be called.

## Parameters

- `invocation`: The method invocation reeference.
- `runLoop`: The run loop from which to unschedule the invocation.
- `runLoopMode`: The run loop mode.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1576409-wsmethodinvocationunschedulefrom)*