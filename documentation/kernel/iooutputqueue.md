# IOOutputQueue

**Framework**: Kernel  
**Kind**: cl

A packet queue that supports multiple producers and a single consumer.

**Availability**:
- macOS 10.0+

## Declaration

```swift
class IOOutputQueue : OSObject
```

#### Overview

Each producer, or a client thread, will deliver a chain of packets to the queue. A single consumer will remove packets from the queue one at a time and forward it to the registered target/action. This object may be used by an IONetworkController on the output (transmit) side to handle the output packet flow downstream from an IONetworkInterface, and then call the driver's output function. IOOutputQueue is an abstract class that provides an interface for its subclasses. Concrete subclasses will complete the implementation, and specify the context that the target is called for packets removed from the queue.

## Topics

### Miscellaneous
- [cancelServiceThread](iooutputqueue/1810578-cancelservicethread.md)
  Cancels any pending service thread callout.
- [enqueue](iooutputqueue/1810610-enqueue.md)
  Adds a packet, or a chain of packets, to the queue.
- [flush](iooutputqueue/1810640-flush.md)
  Drops and frees all packets currently held by the queue.
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
### Instance Variables
- [_reserved](iooutputqueue/reserved.md)
### Instance Methods
- [- cancelServiceThread](iooutputqueue/1470208-cancelservicethread.md)
- [- enqueue](iooutputqueue/1470236-enqueue.md)
- [- flush](iooutputqueue/1470215-flush.md)
- [- free](iooutputqueue/1470280-free.md)
- [- getCapacity](iooutputqueue/1470212-getcapacity.md)
- [- getMbufPriority](iooutputqueue/1470277-getmbufpriority.md)
- [- getMetaClass](iooutputqueue/1470221-getmetaclass.md)
- [- getOutputHandler](iooutputqueue/1470270-getoutputhandler.md)
- [- getSize](iooutputqueue/1470261-getsize.md)
- [- getStatisticsData](iooutputqueue/1470205-getstatisticsdata.md)
- [- init](iooutputqueue/1470264-init.md)
- [- scheduleServiceThread](iooutputqueue/1470273-scheduleservicethread.md)
- [- service](iooutputqueue/1470199-service.md)
- [- serviceThread](iooutputqueue/1470251-servicethread.md)
- [- setCapacity](iooutputqueue/1470267-setcapacity.md)
- [- start](iooutputqueue/1470231-start.md)
- [- stop](iooutputqueue/1470225-stop.md)
### Type Methods
- [+ runServiceThread](iooutputqueue/1470245-runservicethread.md)

## Relationships

### Inherits From
- [OSObject](osobject.md)

## See Also

- [IOGatedOutputQueue](iogatedoutputqueue.md)
  An extension of an IOBasicOutputQueue.
- [IOBasicOutputQueue](iobasicoutputqueue.md)
  A concrete implementation of an IOOutputQueue.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iooutputqueue)*