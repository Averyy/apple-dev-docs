# MPWaitForEvent

**Framework**: Core Services  
**Kind**: func  
**Role**: Function

Retrieves event flags from a specified event group. 

**Availability**:
- macOS 10.0+ - Deprecated in 10.7

## Declaration

```c
OSStatus MPWaitForEvent(MPEventID event, MPEventFlags *flags, Duration timeout);
```

#### Return Value

A result code. See [Result Codes](./carbon_core/multiprocessing_services.md#1663965).

#### Discussion

This function obtains event flags from the specified event group. The timeout specifies how long to wait for events if none are present when the call is made. If any flags are set when this function is called, all the flags in the event group are moved to the `flag` field and the event group is cleared. This obtaining and clearing action is an atomic operation to ensure that no updates are lost. If multiple tasks are waiting on an event group, only one can obtain any particular set of flags. 

If you call this function from a cooperative task, you should specify only `kDurationImmediate` for the timeout length; other waits will cause the task to block. 

Also see the function  [`MPSetEvent`](./api-1585752-mpsetevent.md). 

## Parameters

- `event`: The event group whose flags you want to retrieve. 
- `flags`: On return, `flags` contains the flags of the specified event group. Pass `NULL` if you do not need any flag information. 
- `timeout`: The maximum time to wait for events before timing out. See [Timer Duration Constants](./api-1585641-timer_duration_constants.md) for a list of constants you can use to specify the wait interval. 

## See Also

### Handling Event Groups
- [MPCreateEvent](./api-1585702-mpcreateevent.md)
  Creates an event group.
- [MPDeleteEvent](./api-1585691-mpdeleteevent.md)
  Removes an event group. 
- [MPSetEvent](./api-1585752-mpsetevent.md)
  Merges event flags into a specified event group. 


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1585656-mpwaitforevent)*