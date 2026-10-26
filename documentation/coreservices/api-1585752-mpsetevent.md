# MPSetEvent

**Framework**: Core Services  
**Kind**: func  
**Role**: Function

Merges event flags into a specified event group. 

**Availability**:
- macOS 10.0+ - Deprecated in 10.7

## Declaration

```c
OSStatus MPSetEvent(MPEventID event, MPEventFlags flags);
```

#### Return Value

A result code. See [Result Codes](./carbon_core/multiprocessing_services.md#1663965).

#### Discussion

The flags are logically ORed with the current flags in the event group. This procedure is an atomic operation to ensure that multiple updates do not get lost. If tasks are waiting on this event group, the first waiting task is unblocked.

Note that you can call this function from an interrupt handler.

Also see the function  [`MPWaitForEvent`](./api-1585656-mpwaitforevent.md). 

## Parameters

- `event`: The ID of the event group you want to set. 
- `flags`: The flags you want to merge into the event group. 

## See Also

### Handling Event Groups
- [MPCreateEvent](./api-1585702-mpcreateevent.md)
  Creates an event group.
- [MPDeleteEvent](./api-1585691-mpdeleteevent.md)
  Removes an event group. 
- [MPWaitForEvent](./api-1585656-mpwaitforevent.md)
  Retrieves event flags from a specified event group. 


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1585752-mpsetevent)*