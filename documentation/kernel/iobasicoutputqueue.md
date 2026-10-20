# IOBasicOutputQueue

**Framework**: Kernel  
**Kind**: cl  
**Role**: Class

A concrete implementation of an IOOutputQueue.

**Availability**:
- macOS 10.0+

## Declaration

```cpp
class IOBasicOutputQueue : IOOutputQueue
```

#### Overview

This object uses a mutex to protect the packet queue from multiple producers. A single producer is promoted to become a consumer when the queue is not active. Otherwise, the producer will simply queue the packet and return without blocking.

The flow of packets from the queue to its target can be controlled by calling methods such as start(), stop(), or service(). The target is expected to call those methods from a single threaded context, i.e. the work loop context in a network driver. In addition, the target must also return a status for every packet delivered by the consumer thread. This return value is the only mechanism that the target can use to manage the queue when it is running on the consumer thread.

## Topics

### Miscellaneous
- [enqueue](./iobasicoutputqueue/api-1811623-enqueue.md)
  Adds a packet, or a chain of packets, to the queue.
- [flush](./iobasicoutputqueue/api-1811630-flush.md)
  Drops and frees all packets currently held by the queue.
- [free](./iobasicoutputqueue/api-1811636-free.md)
  Frees the IOBasicOutputQueue object.
- [getCapacity](./iobasicoutputqueue/api-1811642-getcapacity.md)
  Gets the number of packets that the queue can hold.
- [getDropCount](./iobasicoutputqueue/api-1811646-getdropcount.md)
  Gets the number of packets dropped by the queue.
- [getOutputCount](./iobasicoutputqueue/api-1811651-getoutputcount.md)
  Gets the number of packets accepted by the target.
- [getRetryCount](./iobasicoutputqueue/api-1811660-getretrycount.md)
  Gets the number of instances when the target has refused to accept the packet provided.
- [getSize](./iobasicoutputqueue/api-1811664-getsize.md)
  Gets the number of packets currently held in the queue.
- [getStallCount](./iobasicoutputqueue/api-1811671-getstallcount.md)
  Gets the number of instances when the target has stalled the queue.
- [getState](./iobasicoutputqueue/api-1811677-getstate.md)
  Gets the state of the queue object.
- [getStatisticsData](./iobasicoutputqueue/api-1811683-getstatisticsdata.md)
  Returns an IONetworkData object containing statistics counters updated by the queue.
- [handleNetworkDataAccess](./iobasicoutputqueue/api-1811690-handlenetworkdataaccess.md)
  Handles an external access to the IONetworkData object returned by getStatisticsData().
- [init](./iobasicoutputqueue/api-1811696-init.md)
  Initializes an IOBasicOutputQueue object.
- [output](./iobasicoutputqueue/api-1811702-output.md)
  Transfers all packets in the mbuf queue to the target.
- [service](./iobasicoutputqueue/api-1811708-service.md)
  Services a queue that was stalled by the target.
- [serviceThread](./iobasicoutputqueue/api-1811713-servicethread.md)
  Provides an implementation for the serviceThread() method defined in IOOutputQueue.
- [setCapacity](./iobasicoutputqueue/api-1811721-setcapacity.md)
  Changes the number of packets that the queue can hold before it begins to drop excess packets.
- [start](./iobasicoutputqueue/api-1811726-start.md)
  Starts up the packet flow between the queue and its target.
- [stop](./iobasicoutputqueue/api-1811734-stop.md)
  Stops the packet flow between the queue and its target.
- [withTarget(IONetworkController *, UInt32)](./iobasicoutputqueue/api-1811748-withtarget.md)
  Factory method that constructs and initializes an IOBasicOutputQueue object.
- [withTarget(IONetworkController *, UInt32, UInt32)](./iobasicoutputqueue/api-1811755-withtarget.md)
  Factory method that constructs and initializes an IOBasicOutputQueue object.
- [withTarget(OSObject *, IOOutputAction, UInt32)](./iobasicoutputqueue/api-1811763-withtarget.md)
  Factory method that constructs and initializes an IOBasicOutputQueue object.
- [withTarget(OSObject *, IOOutputAction, UInt32, UInt32)](./iobasicoutputqueue/api-1811770-withtarget.md)
  Factory method that constructs and initializes an IOBasicOutputQueue object.
### Constants
- [GetStateBits](./iobasicoutputqueue/getstatebits.md)
  The bits in the value returned by getState().
- [ServiceAsync](./iobasicoutputqueue/serviceasync.md)
  The option bits recognized by service().
### Instance Methods
- [- dequeue](./iobasicoutputqueue/api-1567089-dequeue.md)
- [- enqueue](./iobasicoutputqueue/api-1567090-enqueue.md)
- [- flush](./iobasicoutputqueue/api-1567093-flush.md)
- [- free](./iobasicoutputqueue/api-1567099-free.md)
- [- getCapacity](./iobasicoutputqueue/api-1567102-getcapacity.md)
- [- getDropCount](./iobasicoutputqueue/api-1567083-getdropcount.md)
- [- getMetaClass](./iobasicoutputqueue/api-1567085-getmetaclass.md)
- [- getOutputCount](./iobasicoutputqueue/api-1567084-getoutputcount.md)
- [- getRetryCount](./iobasicoutputqueue/api-1567098-getretrycount.md)
- [- getSize](./iobasicoutputqueue/api-1567096-getsize.md)
- [- getStallCount](./iobasicoutputqueue/api-1567081-getstallcount.md)
- [- getState](./iobasicoutputqueue/api-1567095-getstate.md)
- [- getStatisticsData](./iobasicoutputqueue/api-1567086-getstatisticsdata.md)
- [- handleNetworkDataAccess](./iobasicoutputqueue/api-1567097-handlenetworkdataaccess.md)
- [- output](./iobasicoutputqueue/api-1567088-output.md)
- [- service](./iobasicoutputqueue/api-1567082-service.md)
- [- serviceThread](./iobasicoutputqueue/api-1567087-servicethread.md)
- [- setCapacity](./iobasicoutputqueue/api-1567103-setcapacity.md)
- [- start](./iobasicoutputqueue/api-1567094-start.md)
- [- stop](./iobasicoutputqueue/api-1567100-stop.md)
### Type Methods
- [+ dispatchNetworkDataNotification](./iobasicoutputqueue/api-1567091-dispatchnetworkdatanotification.md)
- [+ withTarget](./iobasicoutputqueue/api-1567101-withtarget.md)
- [+ withTarget](./iobasicoutputqueue/api-3516604-withtarget.md)

## Relationships

### Inherits From
- [IOOutputQueue](./iooutputqueue.md)

## See Also

### Output Queues
- [IOGatedOutputQueue](./iogatedoutputqueue.md)
  An extension of an IOBasicOutputQueue.
- [IOOutputQueue](./iooutputqueue.md)
  A packet queue that supports multiple producers and a single consumer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iobasicoutputqueue)*