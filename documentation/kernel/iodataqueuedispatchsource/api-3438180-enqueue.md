# Enqueue

**Framework**: Kernel  
**Kind**: instm  
**Role**: Instance Method

Adds a single entry to the shared data queue.

**Availability**:
- DriverKit 19.0+
- macOS 10.15.2+

## Declaration

```c
kern_return_t Enqueue(uint32_t dataSize, IODataQueueClientEnqueueEntryBlock callback);
```

#### Return Value

[`kIOReturnSuccess`](../../DriverKit/kioreturnsuccess.md) on success, [`kIOReturnOverrun`](../../DriverKit/kioreturnoverrun.md) if the queue was full, or [`kIOReturnError`](../../DriverKit/kioreturnerror.md) if the queue is corrupt. See [Error Codes](../../DriverKit/error-codes.md). 

## Parameters

- `dataSize`: The size of the data to enqueue.
- `callback`: The callback to execute when there is enough space to enqueue the data.

## See Also

### Adding Work to the Queue
- [- SetDataServicedHandler](../../DriverKit/iodataqueuedispatchsource/setdataservicedhandler.md)
  Installs the handler block to execute when data is removed from the queue.
- [- DataServiced](../../DriverKit/iodataqueuedispatchsource/dataserviced.md)
  Responds to the removal of data from the queue.  
- [- EnqueueWithCoalesce](./api-3438181-enqueuewithcoalesce.md)
  Adds an entry to the queue, but doesn't automatically send a data-available notification.
- [- SendDataAvailable](./api-3438184-senddataavailable.md)
  Sends a notification to observers that indicates more data is available for processing.
- [IODataQueueClientEnqueueEntryBlock](../../DriverKit/iodataqueueclientenqueueentryblock.md)
  The handler block you use to add data to a queue. 


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iodataqueuedispatchsource/3438180-enqueue)*