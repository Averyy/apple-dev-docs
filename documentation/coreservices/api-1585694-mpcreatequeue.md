# MPCreateQueue

**Framework**: Core Services  
**Kind**: func  
**Role**: Function

Creates a message queue.

**Availability**:
- macOS 10.0+ - Deprecated in 10.7

## Declaration

```c
OSStatus MPCreateQueue(MPQueueID *queue);
```

## Return Value

A result code. See [Result Codes](./carbon_core/multiprocessing_services.md#1663965). If a queue could not be created, `MPCreateQueue` returns `kMPInsufficientResourcesErr`.

## Discussion

This call creates a message queue, which can be used to notify (that is, send) and wait for (that is, receive) messages consisting of three pointer-sized values in a preemptively safe manner.

Message queues are created from dynamically allocated internal resources. Other tasks may be competing for these resources so it is possible this function may not be able to create a queue. 

See also the functions  [`MPDeleteQueue`](./api-1585571-mpdeletequeue.md)  and  [`MPSetQueueReserve`](./api-1585671-mpsetqueuereserve.md). 

## Parameters

- `queue`: On return, the variable contains the ID of the newly created message queue. 

## See Also

### Creating and Handling Message Queues
- [MPDeleteQueue](./api-1585571-mpdeletequeue.md)
  Deletes a message queue.
- [MPNotifyQueue](./api-1585699-mpnotifyqueue.md)
  Sends a message to the specified message queue.
- [MPSetQueueReserve](./api-1585671-mpsetqueuereserve.md)
  Reserves space for messages on a specified message queue. 
- [MPWaitOnQueue](./api-1585762-mpwaitonqueue.md)
  Obtains a message from a specified message queue. 


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1585694-mpcreatequeue)*