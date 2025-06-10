# SendDataServiced

**Framework**: Kernel  
**Kind**: instm

Notifies interested parties that you removed data from the queue. 

**Availability**:
- DriverKit 19.0+
- macOS 10.15.2+

## Declaration

```swift
void SendDataServiced(void);
```

#### Discussion

Use this method to send a single notification after dequeueing multiple entries with the [`DequeueWithCoalesce`](iodataqueuedispatchsource/3438179-dequeuewithcoalesce.md) method. The [`DequeueWithCoalesce`](iodataqueuedispatchsource/3438179-dequeuewithcoalesce.md) method doesn't call the [`DataServiced`](https://developer.apple.com/documentation/driverkit/iodataqueuedispatchsource/dataserviced) handler automatically after removing an entry. Instead, you call this method after the successful removal of entries from the queue.

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
- [- DequeueWithCoalesce](iodataqueuedispatchsource/3438179-dequeuewithcoalesce.md)
  Removes the next queue entry, but doesn't automatically send notifications.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iodataqueuedispatchsource/3438185-senddataserviced)*