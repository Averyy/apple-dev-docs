# getMbufPriority

**Framework**: Kernel  
**Kind**: instm

Determines an mbuf's traffic priority. The highest priority is 0.

## Declaration

```cpp
virtual UInt32 getMbufPriority(
 mbuf_tm);
```

#### Return Value

Returns a UInt32 representing the priority of the packet. 0 is the highest priority.

#### Overview

A queue can prioritize certain classes of traffic. This method facilitates that by evaluating an mbuf and returning its priority.

## Parameters

- `m`: An mbuf to analyze.

## See Also

### Miscellaneous
- [cancelServiceThread](./api-1810578-cancelservicethread.md)
  Cancels any pending service thread callout.
- [enqueue](./api-1810610-enqueue.md)
  Adds a packet, or a chain of packets, to the queue.
- [flush](./api-1810640-flush.md)
  Drops and frees all packets currently held by the queue.
- [free](./api-1810666-free.md)
  Frees the IOOutputQueue object.
- [getCapacity](./api-1810689-getcapacity.md)
  Gets the number of packets that the queue can hold.
- [getOutputHandler](./api-1810744-getoutputhandler.md)
  Returns the address of a function that is designated to handle incoming packets sent to the queue object.
- [getSize](./api-1810788-getsize.md)
  Gets the number of packets currently held in the queue.
- [getStatisticsData](./api-1810822-getstatisticsdata.md)
  Returns an IONetworkData object containing statistics counters updated by the queue.
- [init](./api-1810854-init.md)
  Initializes an IOOutputQueue object.
- [scheduleServiceThread](./api-1810887-scheduleservicethread.md)
  Schedules a service thread callout.
- [service](./api-1810919-service.md)
  Services the queue.
- [serviceThread](./api-1810947-servicethread.md)
  Method called by the scheduled service thread when it starts to run.
- [setCapacity](./api-1810969-setcapacity.md)
  Changes the number of packets that the queue can hold before it begins to drop excess packets.
- [start](./api-1810993-start.md)
  Starts up the queue.
- [stop](./api-1811022-stop.md)
  Stops the queue.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iooutputqueue/1810719-getmbufpriority)*