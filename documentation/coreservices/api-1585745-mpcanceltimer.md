# MPCancelTimer

**Framework**: Core Services  
**Kind**: func  
**Role**: Function

Cancels an armed timer. 

**Availability**:
- macOS 10.0+ - Deprecated in 10.7

## Declaration

```c
OSStatus MPCancelTimer(MPTimerID timerID, AbsoluteTime *timeRemaining);
```

#### Return Value

A result code. See [Result Codes](./carbon_core/multiprocessing_services.md#1663965). If the timer has already expired, this function returns `kMPInsufficientResourcesErr`.

#### Discussion

Also see the function  [`MPArmTimer`](./api-1585612-mparmtimer.md). 

## Parameters

- `timerID`: The ID of the armed timer you want to cancel. 
- `timeRemaining`: On return, the `timeRemaining` contains the time remaining before the timer would have expired. 

## See Also

### Timer Services Functions
- [MPArmTimer](./api-1585612-mparmtimer.md)
  Arms the timer to expire at a given time. 
- [MPCreateTimer](./api-1585748-mpcreatetimer.md)
  Creates a timer.
- [MPDelayUntil](./api-1585647-mpdelayuntil.md)
  Blocks the calling task until a specified time. 
- [MPDeleteTimer](./api-1585761-mpdeletetimer.md)
  Removes a timer. 
- [MPSetTimerNotify](./api-1585726-mpsettimernotify.md)
  Sets the notification information associated with a timer. 


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1585745-mpcanceltimer)*