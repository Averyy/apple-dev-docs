# DequeueWithCoalesce

**Framework**: Kernel  
**Kind**: instm

Removes the next queue entry, but doesn't automatically send notifications.

**Availability**:
- DriverKit 19.0+
- macOS 10.15.2+

## Declaration

```swift
kern_return_t DequeueWithCoalesce(bool *sendDataServiced, IODataQueueClientDequeueEntryBlock callback);
```

#### Return_value

[`kIOReturnSuccess`](https://developer.apple.com/documentation/driverkit/kioreturnsuccess) on success, [`kIOReturnUnderrun`](https://developer.apple.com/documentation/driverkit/kioreturnunderrun) if the queue is empty, or [`kIOReturnError`](https://developer.apple.com/documentation/driverkit/kioreturnerror) if the queue is corrupt. See `Error Codes`. 

## Parameters

- `sendDataServiced`: A Boolean value that indicates that this method would have sent a notification. Initialize the value to  , and then make one or more calls to this method. If the value is   after all of those calls, call the   method yourself to deliver the notification.
- `callback`: The callback that you use to process the dequeued data.

## See Also

- [- SetDataAvailableHandler](../driverkit/iodataqueuedispatchsource/setdataavailablehandler.md)
  Sets the handler block to run when another object adds data to the queue.
- [- DataAvailable](../driverkit/iodataqueuedispatchsource/dataavailable.md)
  Responds to the addition of new data to the queue.
- [IODataQueueClientDequeueEntryBlock](../driverkit/iodataqueueclientdequeueentryblock.md)
  The handler block you use to remove data from a queue.
- [- IsDataAvailable](iodataqueuedispatchsource/3438182-isdataavailable.md)
  Checks whether the data queue contains data to process.
- [- Peek](iodataqueuedispatchsource/3438183-peek.md)
  Returns the next queue entry without removing it from the queue.
- [- Dequeue](iodataqueuedispatchsource/3438178-dequeue.md)
  Removes the next entry from the queue.
- [- SendDataServiced](iodataqueuedispatchsource/3438185-senddataserviced.md)
  Notifies interested parties that you removed data from the queue. 


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iodataqueuedispatchsource/3438179-dequeuewithcoalesce)*