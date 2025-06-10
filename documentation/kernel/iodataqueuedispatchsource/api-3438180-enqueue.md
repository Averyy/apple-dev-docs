# Enqueue

**Framework**: Kernel  
**Kind**: instm

Adds a single entry to the shared data queue.

**Availability**:
- DriverKit 19.0+
- macOS 10.15.2+

## Declaration

```swift
kern_return_t Enqueue(uint32_t dataSize, IODataQueueClientEnqueueEntryBlock callback);
```

#### Return_value

[`kIOReturnSuccess`](https://developer.apple.com/documentation/driverkit/kioreturnsuccess) on success, [`kIOReturnOverrun`](https://developer.apple.com/documentation/driverkit/kioreturnoverrun) if the queue was full, or [`kIOReturnError`](https://developer.apple.com/documentation/driverkit/kioreturnerror) if the queue is corrupt. See `Error Codes`. 

## Parameters

- `dataSize`: The size of the data to enqueue.
- `callback`: The callback to execute when there is enough space to enqueue the data.

## See Also

- [- SetDataServicedHandler](../driverkit/iodataqueuedispatchsource/setdataservicedhandler.md)
  Installs the handler block to execute when data is removed from the queue.
- [- DataServiced](../driverkit/iodataqueuedispatchsource/dataserviced.md)
  Responds to the removal of data from the queue.
- [IODataQueueClientEnqueueEntryBlock](../driverkit/iodataqueueclientenqueueentryblock.md)
  The handler block you use to add data to a queue.
- [- EnqueueWithCoalesce](iodataqueuedispatchsource/3438181-enqueuewithcoalesce.md)
  Adds an entry to the queue, but doesn't automatically send a data-available notification.
- [- SendDataAvailable](iodataqueuedispatchsource/3438184-senddataavailable.md)
  Sends a notification to observers that indicates more data is available for processing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iodataqueuedispatchsource/3438180-enqueue)*