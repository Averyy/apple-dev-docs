# lockDequeue

**Framework**: Kernel  
**Kind**: instm

Removes a single packet from the head of a synchronized queue.

## Declaration

```cpp
virtual mbuf_t lockDequeue();
```

## Return Value

Returns a packet removed from the head of the queue, or NULL if the queue was empty.

## Overview

A spinlock is used to synchronize access to the queue.

## See Also

### Miscellaneous
- [dequeue](./api-1810464-dequeue.md)
  Removes a single packet from the head of the queue.
- [dequeueAll](./api-1810493-dequeueall.md)
  Removes all packets from the queue and returns the head of the packet chain.
- [enqueue(IOPacketQueue *)](./api-1810512-enqueue.md)
  Removes all packets from the specified queue, and adds them to the tail of this queue.
- [enqueue(mbuf_t)](./api-1810538-enqueue.md)
  Adds a chain of packets to the tail of the queue.
- [enqueueWithDrop](./api-1810567-enqueuewithdrop.md)
  Adds a chain of packets to the tail of the queue.
- [flush](./api-1810584-flush.md)
  Frees all packets currently held in the queue and releases them back to the free mbuf pool.
- [free](./api-1810608-free.md)
  Frees the IOPacketQueue object.
- [getCapacity](./api-1810646-getcapacity.md)
  Gets the current capacity of the queue.
- [getSize](./api-1810665-getsize.md)
  Gets the size of the queue.
- [initWithCapacity](./api-1810679-initwithcapacity.md)
  Initializes an IOPacketQueue object.
- [lockDequeueAll](./api-1810717-lockdequeueall.md)
  Removes all packets from a synchronized queue and returns the head of the packet chain.
- [lockEnqueue](./api-1810734-lockenqueue.md)
  Adds a chain of packets to the tail of a synchronized queue.
- [lockEnqueueWithDrop](./api-1810758-lockenqueuewithdrop.md)
  Adds a chain of packets to the tail of a synchronized queue.
- [lockFlush](./api-1810785-lockflush.md)
  Frees all packets currently held in a synchronized queue and releases them back to the free mbuf pool.
- [lockPrepend](./api-1810813-lockprepend.md)
  Adds a chain of packets to the head of a synchronized queue.
- [peek](./api-1810837-peek.md)
  Examines the packet at the head of the queue without removing it from the queue.
- [prepend(IOPacketQueue *)](./api-1810853-prepend.md)
  Removes all packets from the specified queue, and adds them to the head of this queue.
- [prepend(mbuf_t)](./api-1810881-prepend.md)
  Adds a chain of packets to the head of the queue.
- [setCapacity](./api-1810899-setcapacity.md)
  Changes the capacity of the queue.
- [withCapacity](./api-1810920-withcapacity.md)
  Factory method that constructs and initializes an IOPacketQueue object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iopacketqueue/1810698-lockdequeue)*