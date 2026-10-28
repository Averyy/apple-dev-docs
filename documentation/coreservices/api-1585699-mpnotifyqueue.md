# MPNotifyQueue

**Framework**: Core Services  
**Kind**: func  
**Role**: Function

Sends a message to the specified message queue.

**Availability**:
- macOS 10.0+ - Deprecated in 10.7

## Declaration

```c
OSStatus MPNotifyQueue(MPQueueID queue, void *param1, void *param2, void *param3);
```

## Return Value

A result code. See [Result Codes](./carbon_core/multiprocessing_services.md#1663965).

## Discussion

This function sends a message to the specified queue, which consist of the three parameters, `param1`, `param2`, and `param3`. The system does not interpret the three values which comprise the text of the message. If tasks are waiting on the specified queue, the first waiting task is unblocked and the task’s  [`MPWaitOnQueue`](./api-1585762-mpwaitonqueue.md)  function completes.

Depending on the queue mode, the system either allocates messages dynamically or assigns them to memory reserved for the queue. In either case, if no more memory is available for messages `MPNotifyQueue` returns `kMPInsufficientResourcesErr`.

You can call this function from an interrupt handler if messages are reserved on the queue. For more information about queueing modes and reserving messages, see  [`MPSetQueueReserve`](./api-1585671-mpsetqueuereserve.md).

Also see the function  [`MPWaitOnQueue`](./api-1585762-mpwaitonqueue.md). 

## Parameters

- `queue`: The queue ID of the message queue you want to notify.
- `param1`: The first pointer-sized value of the message to send.
- `param2`: The second pointer-sized value of the message to send.
- `param3`: The third pointer-sized value of the message to send.

## See Also

### Creating and Handling Message Queues
- [MPCreateQueue](./api-1585694-mpcreatequeue.md)
  Creates a message queue.
- [MPDeleteQueue](./api-1585571-mpdeletequeue.md)
  Deletes a message queue.
- [MPSetQueueReserve](./api-1585671-mpsetqueuereserve.md)
  Reserves space for messages on a specified message queue. 
- [MPWaitOnQueue](./api-1585762-mpwaitonqueue.md)
  Obtains a message from a specified message queue. 


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1585699-mpnotifyqueue)*