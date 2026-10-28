# MPCreateEvent

**Framework**: Core Services  
**Kind**: func  
**Role**: Function

Creates an event group.

**Availability**:
- macOS 10.0+ - Deprecated in 10.7

## Declaration

```c
OSStatus MPCreateEvent(MPEventID *event);
```

## Return Value

A result code. See [Result Codes](./carbon_core/multiprocessing_services.md#1663965).

## Discussion

Event groups are created from dynamically allocated internal resources. Other tasks may be competing for these resources so it is possible that this function will not be able to create an event group.

Also see the function  [`MPDeleteEvent`](./api-1585691-mpdeleteevent.md). 

## Parameters

- `event`: On return, `event` contains the ID of the newly created event group. 

## See Also

### Handling Event Groups
- [MPDeleteEvent](./api-1585691-mpdeleteevent.md)
  Removes an event group. 
- [MPSetEvent](./api-1585752-mpsetevent.md)
  Merges event flags into a specified event group. 
- [MPWaitForEvent](./api-1585656-mpwaitforevent.md)
  Retrieves event flags from a specified event group. 


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1585702-mpcreateevent)*