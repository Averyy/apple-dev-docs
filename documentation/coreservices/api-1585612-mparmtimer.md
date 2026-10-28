# MPArmTimer

**Framework**: Core Services  
**Kind**: func  
**Role**: Function

Arms the timer to expire at a given time. 

**Availability**:
- macOS 10.0+ - Deprecated in 10.7

## Declaration

```c
OSStatus MPArmTimer(MPTimerID timerID, AbsoluteTime *expirationTime, OptionBits options);
```

## Return Value

A result code. See [Result Codes](./carbon_core/multiprocessing_services.md#1663965). If the timer has already expired, the reset does not take place and the function returns `kMPInsufficientResourcesErr`.

## Discussion

The expiration time is an absolute time, which you can generate by calling the Driver Services Library function `UpTime`. When the timer expires, a notification is sent to the notification mechanism specified in the last  [`MPSetTimerNotify`](./api-1585726-mpsettimernotify.md)  call. If the specified notification ID has become invalid, no action is taken when the timer expires. The timer itself is deleted when it expires unless you specified the `kMPPreserveTimerID` option in the options parameter.

Also see the function  [`MPCancelTimer`](./api-1585745-mpcanceltimer.md). 

## Parameters

- `timerID`: The ID of the timer you want to arm. 
- `expirationTime`: A pointer to a value that specifies when you want the timer to expire. Note that if you arm the timer with a time that has already passed, the timer expires immediately. 
- `options`: Any optional actions. See [Timer Option Masks](./api-1585611-timer_option_masks.md) for a list of possible values. 

## See Also

### Timer Services Functions
- [MPCancelTimer](./api-1585745-mpcanceltimer.md)
  Cancels an armed timer. 
- [MPCreateTimer](./api-1585748-mpcreatetimer.md)
  Creates a timer.
- [MPDelayUntil](./api-1585647-mpdelayuntil.md)
  Blocks the calling task until a specified time. 
- [MPDeleteTimer](./api-1585761-mpdeletetimer.md)
  Removes a timer. 
- [MPSetTimerNotify](./api-1585726-mpsettimernotify.md)
  Sets the notification information associated with a timer. 


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1585612-mparmtimer)*