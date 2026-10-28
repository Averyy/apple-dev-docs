# MPDeleteQueue

**Framework**: Core Services  
**Kind**: func  
**Role**: Function

Deletes a message queue.

**Availability**:
- macOS 10.0+ - Deprecated in 10.7

## Declaration

```c
OSStatus MPDeleteQueue(MPQueueID queue);
```

## Return Value

A result code. See [Result Codes](./carbon_core/multiprocessing_services.md#1663965).

## Discussion

After calling `MPDeleteQueue`, the specified queue ID becomes invalid, and all internal resources associated with the queue (including queued messages) are reclaimed. Any tasks waiting on the queue are unblocked and their respective  [`MPWaitOnQueue`](./api-1585762-mpwaitonqueue.md)  calls will return with the result code `kMPDeletedErr`.

Also see the function  [`MPCreateQueue`](./api-1585694-mpcreatequeue.md). 

## Parameters

- `queue`: The ID of the message queue you want to delete. 

## See Also

### Creating and Handling Message Queues
- [MPCreateQueue](./api-1585694-mpcreatequeue.md)
  Creates a message queue.
- [MPNotifyQueue](./api-1585699-mpnotifyqueue.md)
  Sends a message to the specified message queue.
- [MPSetQueueReserve](./api-1585671-mpsetqueuereserve.md)
  Reserves space for messages on a specified message queue. 
- [MPWaitOnQueue](./api-1585762-mpwaitonqueue.md)
  Obtains a message from a specified message queue. 


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1585571-mpdeletequeue)*