# setCapacity

**Framework**: Kernel  
**Kind**: instm

Changes the capacity of the queue.

## Declaration

```swift
virtual bool setCapacity(
 UInt32capacity);
```

#### Return_value

Returns true if the new capacity was accepted, false otherwise.

## Parameters

- `capacity`: The new capacity.

## See Also

- [dequeue](iopacketqueue/1810464-dequeue.md)
  Removes a single packet from the head of the queue.
- [dequeueAll](iopacketqueue/1810493-dequeueall.md)
  Removes all packets from the queue and returns the head of the packet chain.
- [enqueue(IOPacketQueue *)](iopacketqueue/1810512-enqueue.md)
  Removes all packets from the specified queue, and adds them to the tail of this queue.
- [enqueue(mbuf_t)](iopacketqueue/1810538-enqueue.md)
  Adds a chain of packets to the tail of the queue.
- [enqueueWithDrop](iopacketqueue/1810567-enqueuewithdrop.md)
  Adds a chain of packets to the tail of the queue.
- [flush](iopacketqueue/1810584-flush.md)
  Frees all packets currently held in the queue and releases them back to the free mbuf pool.
- [free](iopacketqueue/1810608-free.md)
  Frees the IOPacketQueue object.
- [getCapacity](iopacketqueue/1810646-getcapacity.md)
  Gets the current capacity of the queue.
- [getSize](iopacketqueue/1810665-getsize.md)
  Gets the size of the queue.
- [initWithCapacity](iopacketqueue/1810679-initwithcapacity.md)
  Initializes an IOPacketQueue object.
- [lockDequeue](iopacketqueue/1810698-lockdequeue.md)
  Removes a single packet from the head of a synchronized queue.
- [lockDequeueAll](iopacketqueue/1810717-lockdequeueall.md)
  Removes all packets from a synchronized queue and returns the head of the packet chain.
- [lockEnqueue](iopacketqueue/1810734-lockenqueue.md)
  Adds a chain of packets to the tail of a synchronized queue.
- [lockEnqueueWithDrop](iopacketqueue/1810758-lockenqueuewithdrop.md)
  Adds a chain of packets to the tail of a synchronized queue.
- [lockFlush](iopacketqueue/1810785-lockflush.md)
  Frees all packets currently held in a synchronized queue and releases them back to the free mbuf pool.
- [lockPrepend](iopacketqueue/1810813-lockprepend.md)
  Adds a chain of packets to the head of a synchronized queue.
- [peek](iopacketqueue/1810837-peek.md)
  Examines the packet at the head of the queue without removing it from the queue.
- [prepend(IOPacketQueue *)](iopacketqueue/1810853-prepend.md)
  Removes all packets from the specified queue, and adds them to the head of this queue.
- [prepend(mbuf_t)](iopacketqueue/1810881-prepend.md)
  Adds a chain of packets to the head of the queue.
- [withCapacity](iopacketqueue/1810920-withcapacity.md)
  Factory method that constructs and initializes an IOPacketQueue object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iopacketqueue/1810899-setcapacity)*