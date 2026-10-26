# MPDeleteTimer

**Framework**: Core Services  
**Kind**: func  
**Role**: Function

Removes a timer. 

**Availability**:
- macOS 10.0+ - Deprecated in 10.7

## Declaration

```c
OSStatus MPDeleteTimer(MPTimerID timerID);
```

#### Return Value

A result code. See [Result Codes](./carbon_core/multiprocessing_services.md#1663965).

#### Discussion

After deletion, the timer ID becomes invalid, and all internal resources associated with the timer are reclaimed.

Also see the function  [`MPCreateTimer`](./api-1585748-mpcreatetimer.md). 

## Parameters

- `timerID`: The ID of the timer you want to remove. 

## See Also

### Timer Services Functions
- [MPArmTimer](./api-1585612-mparmtimer.md)
  Arms the timer to expire at a given time. 
- [MPCancelTimer](./api-1585745-mpcanceltimer.md)
  Cancels an armed timer. 
- [MPCreateTimer](./api-1585748-mpcreatetimer.md)
  Creates a timer.
- [MPDelayUntil](./api-1585647-mpdelayuntil.md)
  Blocks the calling task until a specified time. 
- [MPSetTimerNotify](./api-1585726-mpsettimernotify.md)
  Sets the notification information associated with a timer. 


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1585761-mpdeletetimer)*