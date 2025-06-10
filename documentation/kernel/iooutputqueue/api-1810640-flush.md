# flush

**Framework**: Kernel  
**Kind**: instm

Drops and frees all packets currently held by the queue.

## Declaration

```swift
virtual UInt32 flush() = 0;
```

#### Return_value

Returns the number of packets that were dropped and freed.

## See Also

- [cancelServiceThread](iooutputqueue/1810578-cancelservicethread.md)
  Cancels any pending service thread callout.
- [enqueue](iooutputqueue/1810610-enqueue.md)
  Adds a packet, or a chain of packets, to the queue.
- [free](iooutputqueue/1810666-free.md)
  Frees the IOOutputQueue object.
- [getCapacity](iooutputqueue/1810689-getcapacity.md)
  Gets the number of packets that the queue can hold.
- [getMbufPriority](iooutputqueue/1810719-getmbufpriority.md)
  Determines an mbuf's traffic priority. The highest priority is 0.
- [getOutputHandler](iooutputqueue/1810744-getoutputhandler.md)
  Returns the address of a function that is designated to handle incoming packets sent to the queue object.
- [getSize](iooutputqueue/1810788-getsize.md)
  Gets the number of packets currently held in the queue.
- [getStatisticsData](iooutputqueue/1810822-getstatisticsdata.md)
  Returns an IONetworkData object containing statistics counters updated by the queue.
- [init](iooutputqueue/1810854-init.md)
  Initializes an IOOutputQueue object.
- [scheduleServiceThread](iooutputqueue/1810887-scheduleservicethread.md)
  Schedules a service thread callout.
- [service](iooutputqueue/1810919-service.md)
  Services the queue.
- [serviceThread](iooutputqueue/1810947-servicethread.md)
  Method called by the scheduled service thread when it starts to run.
- [setCapacity](iooutputqueue/1810969-setcapacity.md)
  Changes the number of packets that the queue can hold before it begins to drop excess packets.
- [start](iooutputqueue/1810993-start.md)
  Starts up the queue.
- [stop](iooutputqueue/1811022-stop.md)
  Stops the queue.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iooutputqueue/1810640-flush)*