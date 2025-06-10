# IOPacketQueueDefaultCapacity

**Framework**: Kernel  
**Kind**: data

Describes the default capacity of the queue object.

## Declaration

```swift
static const UInt32 IOPacketQueueDefaultCapacity = 100;
```

#### Overview

The capacity is only observed by the enqueue() method. Therefore, it is possible for the size of the queue to exceed its capacity when other methods, such as prepend(), are used to add packets to the queue.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iopacketqueue/iopacketqueuedefaultcapacity)*