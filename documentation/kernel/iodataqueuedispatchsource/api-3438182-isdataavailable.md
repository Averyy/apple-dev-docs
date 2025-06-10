# IsDataAvailable

**Framework**: Kernel  
**Kind**: instm

Checks whether the data queue contains data to process.

**Availability**:
- DriverKit 19.0+
- macOS 10.15.2+

## Declaration

```swift
bool IsDataAvailable(void);
```

#### Return_value

`true` if the queue contains data to process, or `false` if it is empty. 

## See Also

- [- SetDataAvailableHandler](../driverkit/iodataqueuedispatchsource/setdataavailablehandler.md)
  Sets the handler block to run when another object adds data to the queue.
- [- DataAvailable](../driverkit/iodataqueuedispatchsource/dataavailable.md)
  Responds to the addition of new data to the queue.
- [IODataQueueClientDequeueEntryBlock](../driverkit/iodataqueueclientdequeueentryblock.md)
  The handler block you use to remove data from a queue.
- [- Peek](iodataqueuedispatchsource/3438183-peek.md)
  Returns the next queue entry without removing it from the queue.
- [- Dequeue](iodataqueuedispatchsource/3438178-dequeue.md)
  Removes the next entry from the queue.
- [- DequeueWithCoalesce](iodataqueuedispatchsource/3438179-dequeuewithcoalesce.md)
  Removes the next queue entry, but doesn't automatically send notifications.
- [- SendDataServiced](iodataqueuedispatchsource/3438185-senddataserviced.md)
  Notifies interested parties that you removed data from the queue. 


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iodataqueuedispatchsource/3438182-isdataavailable)*