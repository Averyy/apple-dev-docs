# SendDataAvailable

**Framework**: Kernel  
**Kind**: instm  
**Role**: Instance Method

Sends a notification to observers that indicates more data is available for processing.

**Availability**:
- DriverKit 19.0+
- macOS 10.15.2+

## Declaration

```c
void SendDataAvailable(void);
```

## See Also

### Adding Work to the Queue
- [- SetDataServicedHandler](../../DriverKit/iodataqueuedispatchsource/setdataservicedhandler.md)
  Installs the handler block to execute when data is removed from the queue.
- [- DataServiced](../../DriverKit/iodataqueuedispatchsource/dataserviced.md)
  Responds to the removal of data from the queue.  
- [- Enqueue](./api-3438180-enqueue.md)
  Adds a single entry to the shared data queue.
- [- EnqueueWithCoalesce](./api-3438181-enqueuewithcoalesce.md)
  Adds an entry to the queue, but doesn't automatically send a data-available notification.
- [IODataQueueClientEnqueueEntryBlock](../../DriverKit/iodataqueueclientenqueueentryblock.md)
  The handler block you use to add data to a queue. 


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iodataqueuedispatchsource/3438184-senddataavailable)*