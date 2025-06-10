# IOPacketQueue

**Framework**: Kernel  
**Kind**: cl

Implements a bounded FIFO queue of mbuf packets.

**Availability**:
- macOS 10.0+

## Declaration

```swift
class IOPacketQueue : OSObject
```

#### Overview

Packets are removed from the head of the queue (dequeue), and new packets are added to the tail of the queue (enqueue). A spinlock is used to synchronize access to the queue between methods that have a "lock" prefix.

## Topics

### Miscellaneous
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
- [setCapacity](iopacketqueue/1810899-setcapacity.md)
  Changes the capacity of the queue.
- [withCapacity](iopacketqueue/1810920-withcapacity.md)
  Factory method that constructs and initializes an IOPacketQueue object.
### Constants
- [IOPacketQueueDefaultCapacity](iopacketqueue/iopacketqueuedefaultcapacity.md)
  Describes the default capacity of the queue object.
### Instance Variables
- [_reserved](iopacketqueue/reserved.md)
### Instance Methods
- [- dequeue](iopacketqueue/1526779-dequeue.md)
- [- dequeueAll](iopacketqueue/1526777-dequeueall.md)
- [- enqueue](iopacketqueue/1526775-enqueue.md)
- [- enqueue](iopacketqueue/3516617-enqueue.md)
- [- enqueueWithDrop](iopacketqueue/1526759-enqueuewithdrop.md)
- [- flush](iopacketqueue/1526772-flush.md)
- [- free](iopacketqueue/1526773-free.md)
- [- getCapacity](iopacketqueue/1526767-getcapacity.md)
- [- getMetaClass](iopacketqueue/1526784-getmetaclass.md)
- [- getSize](iopacketqueue/1526760-getsize.md)
- [- initWithCapacity](iopacketqueue/1526781-initwithcapacity.md)
- [- lockDequeue](iopacketqueue/1526764-lockdequeue.md)
- [- lockDequeueAll](iopacketqueue/1526757-lockdequeueall.md)
- [- lockEnqueue](iopacketqueue/1526762-lockenqueue.md)
- [- lockEnqueueWithDrop](iopacketqueue/1526765-lockenqueuewithdrop.md)
- [- lockFlush](iopacketqueue/1526776-lockflush.md)
- [- lockPrepend](iopacketqueue/1526755-lockprepend.md)
- [- peek](iopacketqueue/1526771-peek.md)
- [- prepend](iopacketqueue/1526770-prepend.md)
- [- prepend](iopacketqueue/3516618-prepend.md)
- [- setCapacity](iopacketqueue/1526786-setcapacity.md)
### Type Methods
- [+ withCapacity](iopacketqueue/1526783-withcapacity.md)

## Relationships

### Inherits From
- [OSObject](osobject.md)

## See Also

- [IONetworkData](ionetworkdata.md)
  An object that manages a fixed-size named buffer.
- [IONetworkMedium](ionetworkmedium.md)
  An object that encapsulates information about a network medium (i.e. 10Base-T, or 100Base-T Full Duplex).
- [IOPacketBufferConstraints](iopacketbufferconstraints.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iopacketqueue)*