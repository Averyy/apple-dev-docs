# WSMethodInvocationScheduleWithRunLoop

**Framework**: Core Services  
**Kind**: func  
**Role**: Function

Schedule a method invocation for asynchronous execution on a run loop.

**Availability**:
- macOS 10.2+ - Deprecated in 10.8

## Declaration

```c
void WSMethodInvocationScheduleWithRunLoop(WSMethodInvocationRef invocation, CFRunLoopRef runLoop, CFStringRef runLoopMode);
```

## Discussion

Schedules the invocation to execute on the run loop. You must also set a callback to handle the response, using `WSMethodInvocationSetCallBack`. This is the recommended way to invoke web services, due to the unpredictable network delays inherent in such operations.

## Parameters

- `invocation`: The method invocation reference.
- `runLoop`: The run loop upon which to schedule the invocation.
- `runLoopMode`: The run loop mode.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1576408-wsmethodinvocationschedulewithru)*