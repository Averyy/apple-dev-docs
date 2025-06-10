# getOutputCount

**Framework**: Kernel  
**Kind**: instm

Gets the number of packets accepted by the target.

## Declaration

```swift
virtual UInt32 getOutputCount();
```

#### Return_value

Returns the number of times that kIOOutputStatusAccepted is returned by the target.

## See Also

- [enqueue](iobasicoutputqueue/1811623-enqueue.md)
  Adds a packet, or a chain of packets, to the queue.
- [flush](iobasicoutputqueue/1811630-flush.md)
  Drops and frees all packets currently held by the queue.
- [free](iobasicoutputqueue/1811636-free.md)
  Frees the IOBasicOutputQueue object.
- [getCapacity](iobasicoutputqueue/1811642-getcapacity.md)
  Gets the number of packets that the queue can hold.
- [getDropCount](iobasicoutputqueue/1811646-getdropcount.md)
  Gets the number of packets dropped by the queue.
- [getRetryCount](iobasicoutputqueue/1811660-getretrycount.md)
  Gets the number of instances when the target has refused to accept the packet provided.
- [getSize](iobasicoutputqueue/1811664-getsize.md)
  Gets the number of packets currently held in the queue.
- [getStallCount](iobasicoutputqueue/1811671-getstallcount.md)
  Gets the number of instances when the target has stalled the queue.
- [getState](iobasicoutputqueue/1811677-getstate.md)
  Gets the state of the queue object.
- [getStatisticsData](iobasicoutputqueue/1811683-getstatisticsdata.md)
  Returns an IONetworkData object containing statistics counters updated by the queue.
- [handleNetworkDataAccess](iobasicoutputqueue/1811690-handlenetworkdataaccess.md)
  Handles an external access to the IONetworkData object returned by getStatisticsData().
- [init](iobasicoutputqueue/1811696-init.md)
  Initializes an IOBasicOutputQueue object.
- [output](iobasicoutputqueue/1811702-output.md)
  Transfers all packets in the mbuf queue to the target.
- [service](iobasicoutputqueue/1811708-service.md)
  Services a queue that was stalled by the target.
- [serviceThread](iobasicoutputqueue/1811713-servicethread.md)
  Provides an implementation for the serviceThread() method defined in IOOutputQueue.
- [setCapacity](iobasicoutputqueue/1811721-setcapacity.md)
  Changes the number of packets that the queue can hold before it begins to drop excess packets.
- [start](iobasicoutputqueue/1811726-start.md)
  Starts up the packet flow between the queue and its target.
- [stop](iobasicoutputqueue/1811734-stop.md)
  Stops the packet flow between the queue and its target.
- [withTarget(IONetworkController *, UInt32)](iobasicoutputqueue/1811748-withtarget.md)
  Factory method that constructs and initializes an IOBasicOutputQueue object.
- [withTarget(IONetworkController *, UInt32, UInt32)](iobasicoutputqueue/1811755-withtarget.md)
  Factory method that constructs and initializes an IOBasicOutputQueue object.
- [withTarget(OSObject *, IOOutputAction, UInt32)](iobasicoutputqueue/1811763-withtarget.md)
  Factory method that constructs and initializes an IOBasicOutputQueue object.
- [withTarget(OSObject *, IOOutputAction, UInt32, UInt32)](iobasicoutputqueue/1811770-withtarget.md)
  Factory method that constructs and initializes an IOBasicOutputQueue object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iobasicoutputqueue/1811651-getoutputcount)*