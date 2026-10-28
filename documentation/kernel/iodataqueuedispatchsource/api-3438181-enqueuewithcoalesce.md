# EnqueueWithCoalesce

**Framework**: Kernel  
**Kind**: instm  
**Role**: Instance Method

Adds an entry to the queue, but doesn't automatically send a data-available notification.

**Availability**:
- DriverKit 19.0+
- macOS 10.15.2+

## Declaration

```c
kern_return_t EnqueueWithCoalesce(uint32_t dataSize, bool *sendDataAvailable, IODataQueueClientEnqueueEntryBlock callback);
```

## Return Value

[`kIOReturnSuccess`](../../DriverKit/kioreturnsuccess.md) on success, [`kIOReturnOverrun`](../../DriverKit/kioreturnoverrun.md) if the queue was full, or [`kIOReturnError`](../../DriverKit/kioreturnerror.md) if the queue is corrupt. See [Error Codes](../../DriverKit/error-codes.md). 

## Parameters

- `dataSize`: The size of the data to enqueue.
- `sendDataAvailable`: A Boolean value that indicates that this method would have sent a notification. Initialize the value to `false`, and then make one or more calls to this method. If the value is `true` after all of those calls, call the [`SendDataAvailable`](./api-3438184-senddataavailable.md) method yourself to deliver the notification.
- `callback`: The callback to execute when there is enough space to enqueue the data. 

## See Also

### Adding Work to the Queue
- [- SetDataServicedHandler](../../DriverKit/iodataqueuedispatchsource/setdataservicedhandler.md)
  Installs the handler block to execute when data is removed from the queue.
- [- DataServiced](../../DriverKit/iodataqueuedispatchsource/dataserviced.md)
  Responds to the removal of data from the queue.  
- [- Enqueue](./api-3438180-enqueue.md)
  Adds a single entry to the shared data queue.
- [- SendDataAvailable](./api-3438184-senddataavailable.md)
  Sends a notification to observers that indicates more data is available for processing.
- [IODataQueueClientEnqueueEntryBlock](../../DriverKit/iodataqueueclientenqueueentryblock.md)
  The handler block you use to add data to a queue. 


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iodataqueuedispatchsource/3438181-enqueuewithcoalesce)*