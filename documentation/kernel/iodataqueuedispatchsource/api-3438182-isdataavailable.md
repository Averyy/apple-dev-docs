# IsDataAvailable

**Framework**: Kernel  
**Kind**: instm  
**Role**: Instance Method

Checks whether the data queue contains data to process.

**Availability**:
- DriverKit 19.0+
- macOS 10.15.2+

## Declaration

```c
bool IsDataAvailable(void);
```

#### Return Value

`true` if the queue contains data to process, or `false` if it is empty. 

## See Also

### Removing Work from the Queue
- [- SetDataAvailableHandler](../../DriverKit/iodataqueuedispatchsource/setdataavailablehandler.md)
  Sets the handler block to run when another object adds data to the queue.
- [- DataAvailable](../../DriverKit/iodataqueuedispatchsource/dataavailable.md)
  Responds to the addition of new data to the queue. 
- [- Peek](./api-3438183-peek.md)
  Returns the next queue entry without removing it from the queue.
- [- Dequeue](./api-3438178-dequeue.md)
  Removes the next entry from the queue.
- [- DequeueWithCoalesce](./api-3438179-dequeuewithcoalesce.md)
  Removes the next queue entry, but doesn't automatically send notifications.
- [- SendDataServiced](./api-3438185-senddataserviced.md)
  Notifies interested parties that you removed data from the queue. 
- [IODataQueueClientDequeueEntryBlock](../../DriverKit/iodataqueueclientdequeueentryblock.md)
  The handler block you use to remove data from a queue. 


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iodataqueuedispatchsource/3438182-isdataavailable)*