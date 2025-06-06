# IODataQueueDispatchSource

**Framework**: Kernel  
**Kind**: cl

**Availability**:
- macOS 10.15+

## Declaration

```swift
class IODataQueueDispatchSource : IODispatchSource, IODataQueueDispatchSourceInterface
```

## Topics

### Instance Methods
- [- CanEnqueueData](../driverkit/iodataqueuedispatchsource/canenqueuedata-4tug8.md)
- [- CanEnqueueData](../driverkit/iodataqueuedispatchsource/canenqueuedata-3yyz2.md)
- [- Cancel_Impl](iodataqueuedispatchsource/3223201-cancel_impl.md)
- [- CheckForWork_Impl](iodataqueuedispatchsource/3223202-checkforwork_impl.md)
- [- CopyDataAvailableHandler](iodataqueuedispatchsource/3223203-copydataavailablehandler.md)
- [- CopyDataAvailableHandler_Impl](iodataqueuedispatchsource/3223204-copydataavailablehandler_impl.md)
- [- CopyDataServicedHandler](iodataqueuedispatchsource/3223206-copydataservicedhandler.md)
- [- CopyDataServicedHandler_Impl](iodataqueuedispatchsource/3223207-copydataservicedhandler_impl.md)
- [- CopyMemory](iodataqueuedispatchsource/3223209-copymemory.md)
- [- CopyMemory_Impl](iodataqueuedispatchsource/3223210-copymemory_impl.md)
- [- DataAvailable](iodataqueuedispatchsource/3223215-dataavailable.md)
- [- DataServiced](iodataqueuedispatchsource/3223217-dataserviced.md)
- [- Dequeue](iodataqueuedispatchsource/3438178-dequeue.md)
  Removes the next entry from the queue.
- [- DequeueWithCoalesce](iodataqueuedispatchsource/3438179-dequeuewithcoalesce.md)
  Removes the next queue entry, but doesn't automatically send notifications.
- [- Dispatch](iodataqueuedispatchsource/3223220-dispatch.md)
- [- Enqueue](iodataqueuedispatchsource/3438180-enqueue.md)
  Adds a single entry to the shared data queue.
- [- EnqueueWithCoalesce](iodataqueuedispatchsource/3438181-enqueuewithcoalesce.md)
  Adds an entry to the queue, but doesn't automatically send a data-available notification.
- [- IsDataAvailable](iodataqueuedispatchsource/3438182-isdataavailable.md)
  Checks whether the data queue contains data to process.
- [- Peek](iodataqueuedispatchsource/3438183-peek.md)
  Returns the next queue entry without removing it from the queue.
- [- SendDataAvailable](iodataqueuedispatchsource/3438184-senddataavailable.md)
  Sends a notification to observers that indicates more data is available for processing.
- [- SendDataServiced](iodataqueuedispatchsource/3438185-senddataserviced.md)
  Notifies interested parties that you removed data from the queue. 
- [- SetDataAvailableHandler](iodataqueuedispatchsource/3223226-setdataavailablehandler.md)
- [- SetDataAvailableHandler_Impl](iodataqueuedispatchsource/3223227-setdataavailablehandler_impl.md)
- [- SetDataServicedHandler](iodataqueuedispatchsource/3223229-setdataservicedhandler.md)
- [- SetDataServicedHandler_Impl](iodataqueuedispatchsource/3223230-setdataservicedhandler_impl.md)
- [- SetEnableWithCompletion_Impl](iodataqueuedispatchsource/3325695-setenablewithcompletion_impl.md)
- [- free](iodataqueuedispatchsource/3438186-free.md)
  Performs any final cleanup for the data-queue dispatch source.
- [- getMetaClass](iodataqueuedispatchsource/3223234-getmetaclass.md)
- [- init](iodataqueuedispatchsource/3438187-init.md)
  Handles the basic initialization of the dispatch source.
### Type Methods
- [+ CopyDataAvailableHandler_Invoke](iodataqueuedispatchsource/3223205-copydataavailablehandler_invoke.md)
- [+ CopyDataServicedHandler_Invoke](iodataqueuedispatchsource/3223208-copydataservicedhandler_invoke.md)
- [+ CopyMemory_Invoke](iodataqueuedispatchsource/3223211-copymemory_invoke.md)
- [+ Create](iodataqueuedispatchsource/3438177-create.md)
  Creates a dispatch source that you use as a shared-memory data queue.
- [+ Create_Impl](iodataqueuedispatchsource/3223213-create_impl.md)
- [+ Create_Invoke](iodataqueuedispatchsource/3223214-create_invoke.md)
- [+ DataAvailable_Invoke](iodataqueuedispatchsource/4519990-dataavailable_invoke.md)
- [+ DataAvailable_Invoke](iodataqueuedispatchsource/4519991-dataavailable_invoke.md)
- [+ DataServiced_Invoke](iodataqueuedispatchsource/4519992-dataserviced_invoke.md)
- [+ DataServiced_Invoke](iodataqueuedispatchsource/4519993-dataserviced_invoke.md)
- [+ GetDataQueueEntryHeaderSize](../driverkit/iodataqueuedispatchsource/getdataqueueentryheadersize.md)
- [+ SetDataAvailableHandler_Invoke](iodataqueuedispatchsource/3223228-setdataavailablehandler_invoke.md)
- [+ SetDataServicedHandler_Invoke](iodataqueuedispatchsource/3223231-setdataservicedhandler_invoke.md)

## Relationships

### Inherits From
- [IODataQueueDispatchSourceInterface](iodataqueuedispatchsourceinterface.md)
- [IODispatchSource](iodispatchsource.md)

## See Also

- [IODataQueueDispatchSourceInterface](iodataqueuedispatchsourceinterface.md)
- [IODataQueue](iodataqueue.md)
  A generic queue designed to pass data from the kernel to a user process.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iodataqueuedispatchsource)*