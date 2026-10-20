# Dequeue

**Framework**: Kernel  
**Kind**: instm  
**Role**: Instance Method

Removes the next entry from the queue.

**Availability**:
- DriverKit 19.0+
- macOS 10.15.2+

## Declaration

```c
kern_return_t Dequeue(IODataQueueClientDequeueEntryBlock callback);
```

#### Return Value

[`kIOReturnSuccess`](../../DriverKit/kioreturnsuccess.md) on success, [`kIOReturnUnderrun`](../../DriverKit/kioreturnunderrun.md) if the queue is empty, or [`kIOReturnError`](../../DriverKit/kioreturnerror.md) if the queue is corrupt. See [Error Codes](../../DriverKit/error-codes.md). 

## Parameters

- `callback`: The callback you use to process the next entry in the queue. 

## See Also

### Removing Work from the Queue
- [- SetDataAvailableHandler](../../DriverKit/iodataqueuedispatchsource/setdataavailablehandler.md)
  Sets the handler block to run when another object adds data to the queue.
- [- DataAvailable](../../DriverKit/iodataqueuedispatchsource/dataavailable.md)
  Responds to the addition of new data to the queue. 
- [- IsDataAvailable](./api-3438182-isdataavailable.md)
  Checks whether the data queue contains data to process.
- [- Peek](./api-3438183-peek.md)
  Returns the next queue entry without removing it from the queue.
- [- DequeueWithCoalesce](./api-3438179-dequeuewithcoalesce.md)
  Removes the next queue entry, but doesn't automatically send notifications.
- [- SendDataServiced](./api-3438185-senddataserviced.md)
  Notifies interested parties that you removed data from the queue. 
- [IODataQueueClientDequeueEntryBlock](../../DriverKit/iodataqueueclientdequeueentryblock.md)
  The handler block you use to remove data from a queue. 


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iodataqueuedispatchsource/3438178-dequeue)*