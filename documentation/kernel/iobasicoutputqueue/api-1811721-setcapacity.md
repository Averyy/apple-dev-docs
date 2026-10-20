# setCapacity

**Framework**: Kernel  
**Kind**: instm

Changes the number of packets that the queue can hold before it begins to drop excess packets.

## Declaration

```cpp
virtual bool setCapacity(
 UInt32capacity);
```

#### Return Value

Returns true if the new capacity was accepted, false otherwise.

## Parameters

- `capacity`: The new desired capacity.

## See Also

### Miscellaneous
- [enqueue](./api-1811623-enqueue.md)
  Adds a packet, or a chain of packets, to the queue.
- [flush](./api-1811630-flush.md)
  Drops and frees all packets currently held by the queue.
- [free](./api-1811636-free.md)
  Frees the IOBasicOutputQueue object.
- [getCapacity](./api-1811642-getcapacity.md)
  Gets the number of packets that the queue can hold.
- [getDropCount](./api-1811646-getdropcount.md)
  Gets the number of packets dropped by the queue.
- [getOutputCount](./api-1811651-getoutputcount.md)
  Gets the number of packets accepted by the target.
- [getRetryCount](./api-1811660-getretrycount.md)
  Gets the number of instances when the target has refused to accept the packet provided.
- [getSize](./api-1811664-getsize.md)
  Gets the number of packets currently held in the queue.
- [getStallCount](./api-1811671-getstallcount.md)
  Gets the number of instances when the target has stalled the queue.
- [getState](./api-1811677-getstate.md)
  Gets the state of the queue object.
- [getStatisticsData](./api-1811683-getstatisticsdata.md)
  Returns an IONetworkData object containing statistics counters updated by the queue.
- [handleNetworkDataAccess](./api-1811690-handlenetworkdataaccess.md)
  Handles an external access to the IONetworkData object returned by getStatisticsData().
- [init](./api-1811696-init.md)
  Initializes an IOBasicOutputQueue object.
- [output](./api-1811702-output.md)
  Transfers all packets in the mbuf queue to the target.
- [service](./api-1811708-service.md)
  Services a queue that was stalled by the target.
- [serviceThread](./api-1811713-servicethread.md)
  Provides an implementation for the serviceThread() method defined in IOOutputQueue.
- [start](./api-1811726-start.md)
  Starts up the packet flow between the queue and its target.
- [stop](./api-1811734-stop.md)
  Stops the packet flow between the queue and its target.
- [withTarget(IONetworkController *, UInt32)](./api-1811748-withtarget.md)
  Factory method that constructs and initializes an IOBasicOutputQueue object.
- [withTarget(IONetworkController *, UInt32, UInt32)](./api-1811755-withtarget.md)
  Factory method that constructs and initializes an IOBasicOutputQueue object.
- [withTarget(OSObject *, IOOutputAction, UInt32)](./api-1811763-withtarget.md)
  Factory method that constructs and initializes an IOBasicOutputQueue object.
- [withTarget(OSObject *, IOOutputAction, UInt32, UInt32)](./api-1811770-withtarget.md)
  Factory method that constructs and initializes an IOBasicOutputQueue object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iobasicoutputqueue/1811721-setcapacity)*