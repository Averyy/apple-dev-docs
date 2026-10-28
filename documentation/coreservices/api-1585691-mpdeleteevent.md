# MPDeleteEvent

**Framework**: Core Services  
**Kind**: func  
**Role**: Function

Removes an event group. 

**Availability**:
- macOS 10.0+ - Deprecated in 10.7

## Declaration

```c
OSStatus MPDeleteEvent(MPEventID event);
```

## Return Value

A result code. See [Result Codes](./carbon_core/multiprocessing_services.md#1663965).

## Discussion

After deletion, the event ID becomes invalid, and all internal resources associated with the event group are reclaimed. Calling this function unblocks all tasks waiting on the event group and their respective  [`MPWaitForEvent`](./api-1585656-mpwaitforevent.md)  calls will return with the result code `kMPDeletedErr`.

Also see the function  [`MPCreateEvent`](./api-1585702-mpcreateevent.md). 

## Parameters

- `event`: The ID of the event group you want to remove. 

## See Also

### Handling Event Groups
- [MPCreateEvent](./api-1585702-mpcreateevent.md)
  Creates an event group.
- [MPSetEvent](./api-1585752-mpsetevent.md)
  Merges event flags into a specified event group. 
- [MPWaitForEvent](./api-1585656-mpwaitforevent.md)
  Retrieves event flags from a specified event group. 


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1585691-mpdeleteevent)*