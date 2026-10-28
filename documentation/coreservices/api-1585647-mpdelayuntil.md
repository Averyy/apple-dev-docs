# MPDelayUntil

**Framework**: Core Services  
**Kind**: func  
**Role**: Function

Blocks the calling task until a specified time. 

**Availability**:
- macOS 10.0+ - Deprecated in 10.7

## Declaration

```c
OSStatus MPDelayUntil(AbsoluteTime *expirationTime);
```

## Return Value

A result code. See [Result Codes](./carbon_core/multiprocessing_services.md#1663965).

## Discussion

You cannot call this function from a cooperative task.  

## Parameters

- `expirationTime`: The time to unblock the task. 

## See Also

### Timer Services Functions
- [MPArmTimer](./api-1585612-mparmtimer.md)
  Arms the timer to expire at a given time. 
- [MPCancelTimer](./api-1585745-mpcanceltimer.md)
  Cancels an armed timer. 
- [MPCreateTimer](./api-1585748-mpcreatetimer.md)
  Creates a timer.
- [MPDeleteTimer](./api-1585761-mpdeletetimer.md)
  Removes a timer. 
- [MPSetTimerNotify](./api-1585726-mpsettimernotify.md)
  Sets the notification information associated with a timer. 


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1585647-mpdelayuntil)*