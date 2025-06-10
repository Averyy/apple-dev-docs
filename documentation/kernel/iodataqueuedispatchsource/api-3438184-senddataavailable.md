# SendDataAvailable

**Framework**: Kernel  
**Kind**: instm

Sends a notification to observers that indicates more data is available for processing.

**Availability**:
- DriverKit 19.0+
- macOS 10.15.2+

## Declaration

```swift
void SendDataAvailable(void);
```

## See Also

- [- SetDataServicedHandler](../driverkit/iodataqueuedispatchsource/setdataservicedhandler.md)
  Installs the handler block to execute when data is removed from the queue.
- [- DataServiced](../driverkit/iodataqueuedispatchsource/dataserviced.md)
  Responds to the removal of data from the queue.
- [IODataQueueClientEnqueueEntryBlock](../driverkit/iodataqueueclientenqueueentryblock.md)
  The handler block you use to add data to a queue.
- [- Enqueue](iodataqueuedispatchsource/3438180-enqueue.md)
  Adds a single entry to the shared data queue.
- [- EnqueueWithCoalesce](iodataqueuedispatchsource/3438181-enqueuewithcoalesce.md)
  Adds an entry to the queue, but doesn't automatically send a data-available notification.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iodataqueuedispatchsource/3438184-senddataavailable)*