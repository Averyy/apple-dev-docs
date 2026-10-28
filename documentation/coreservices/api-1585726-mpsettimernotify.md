# MPSetTimerNotify

**Framework**: Core Services  
**Kind**: func  
**Role**: Function

Sets the notification information associated with a timer. 

**Availability**:
- macOS 10.0+ - Deprecated in 10.7

## Declaration

```c
OSStatus MPSetTimerNotify(MPTimerID timerID, MPOpaqueID anID, void *notifyParam1, void *notifyParam2, void *notifyParam3);
```

## Return Value

A result code. See [Result Codes](./carbon_core/multiprocessing_services.md#1663965).

## Discussion

When the timer expires, Multiprocessing Services checks the notification ID, and if it is valid, notifies the related notification mechanisms (that is, event groups, queues, or semaphores) you had specified in your  [`MPSetTimerNotify`](./api-1585726-mpsettimernotify.md)  calls. 

You can specify multiple notification mechanisms by calling this function several times. For example, you can call `MPSetTimerNotify` to specify a message queue and then call it again to specify a semaphore. When the timer expires, a message is sent to the message queue and the appropriate semaphore is signaled. You cannot, however, specify more than one notification per notification mechanism (for example, if you call `MPSetTimerNotify` twice, specifying different messages or message queues in each call, the second call will overwrite the first). Note that if a call to `MPSetTimerNotify` returns an error, any previous calls specifying the same timer are still valid; previously set notifications will still be notified when the timer expires. 

You can set the notification information at any time. If the timer is armed, it will modify the notification parameters dynamically. If the timer is disarmed, it will modify the notification parameters to be used for the next  [`MPArmTimer`](./api-1585612-mparmtimer.md)  call.  

## Parameters

- `timerID`: The ID of the timer whose notification information you want to set. 
- `notificationID`: The ID of the notification mechanism to associate with the timer. This value should be the ID of an event group, a message queue, or a semaphore. 
- `notifyParam1`: If `anID` specifies an event group, this parameter should contain the flags to set in the event group when the timer expires. If `anID` specifies a message queue, this parameter should contain the first pointer-sized value of the message to be sent to the message queue when the timer expires. 
- `notifyParam2`: If `anID` specifies a message queue, this parameter should contain the second pointer-sized value of the message to be sent to the message queue when the timer expires. Pass `NULL` if you don’t need this parameter.
- `notifyParam3`: If `anID` specifies a message queue, this parameter should contain the third pointer-sized value of the message sent to the message queue when the timer expires. Pass `NULL` if you don’t need this parameter.

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
- [MPDeleteTimer](./api-1585761-mpdeletetimer.md)
  Removes a timer. 


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1585726-mpsettimernotify)*