# SendDataServiced

**Framework**: Kernel  
**Kind**: instm  
**Role**: Instance Method

Notifies interested parties that you removed data from the queue. 

**Availability**:
- DriverKit 19.0+
- macOS 10.15.2+

## Declaration

```c
void SendDataServiced(void);
```

## Discussion

Use this method to send a single notification after dequeueing multiple entries with the [`DequeueWithCoalesce`](./api-3438179-dequeuewithcoalesce.md) method. The [`DequeueWithCoalesce`](./api-3438179-dequeuewithcoalesce.md) method doesn't call the [`DataServiced`](../../DriverKit/iodataqueuedispatchsource/dataserviced.md) handler automatically after removing an entry. Instead, you call this method after the successful removal of entries from the queue.

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
- [- Dequeue](./api-3438178-dequeue.md)
  Removes the next entry from the queue.
- [- DequeueWithCoalesce](./api-3438179-dequeuewithcoalesce.md)
  Removes the next queue entry, but doesn't automatically send notifications.
- [IODataQueueClientDequeueEntryBlock](../../DriverKit/iodataqueueclientdequeueentryblock.md)
  The handler block you use to remove data from a queue. 


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iodataqueuedispatchsource/3438185-senddataserviced)*