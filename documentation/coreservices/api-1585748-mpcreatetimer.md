# MPCreateTimer

**Framework**: Core Services  
**Kind**: func  
**Role**: Function

Creates a timer.

**Availability**:
- macOS 10.0+ - Deprecated in 10.7

## Declaration

```c
OSStatus MPCreateTimer(MPTimerID *timerID);
```

#### Return Value

A result code. See [Result Codes](./carbon_core/multiprocessing_services.md#1663965).

#### Discussion

You can use a timer to notify an event, queue, or semaphore after a specified amount of time has elapsed. 

Timer objects are created from dynamically-allocated internal resources. Other tasks may be competing for these resources so it is possible this function may not be able to create one.

To specify the notification mechanism to signal, use the function  [`MPSetTimerNotify`](./api-1585726-mpsettimernotify.md).

Also see the functions  [`MPDeleteTimer`](./api-1585761-mpdeletetimer.md)  and  [`MPArmTimer`](./api-1585612-mparmtimer.md). 

## Parameters

- `timerID`: On return, the `timerID` contains the ID of the newly created timer. 

## See Also

### Timer Services Functions
- [MPArmTimer](./api-1585612-mparmtimer.md)
  Arms the timer to expire at a given time. 
- [MPCancelTimer](./api-1585745-mpcanceltimer.md)
  Cancels an armed timer. 
- [MPDelayUntil](./api-1585647-mpdelayuntil.md)
  Blocks the calling task until a specified time. 
- [MPDeleteTimer](./api-1585761-mpdeletetimer.md)
  Removes a timer. 
- [MPSetTimerNotify](./api-1585726-mpsettimernotify.md)
  Sets the notification information associated with a timer. 


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1585748-mpcreatetimer)*