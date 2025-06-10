# setNotificationPort

**Framework**: Kernel  
**Kind**: instm

Creates a simple mach message targeting the mach port specified in port.

## Declaration

```swift
virtual void setNotificationPort(
 mach_port_tport);
```

#### Overview

This message is sent when data is added to an empty queue. It is to notify a user process that new data has become available.

## Parameters

- `port`: The mach port to target with the notification message.

## See Also

- [enqueue](iodataqueue/1810927-enqueue.md)
  Enqueues a new entry on the queue.
- [getMemoryDescriptor](iodataqueue/1810939-getmemorydescriptor.md)
  Returns a memory descriptor covering the IODataQueueMemory region.
- [initWithCapacity](iodataqueue/1810950-initwithcapacity.md)
  Initializes an IODataQueue instance with the capacity specified in the size parameter.
- [initWithEntries](iodataqueue/1810963-initwithentries.md)
  Initializes an IODataQueue instance with the specified number of entries of the given size.
- [sendDataAvailableNotification](iodataqueue/1810980-senddataavailablenotification.md)
  Sends a dataAvailableNotification message to the specified mach port.
- [withCapacity](iodataqueue/1811001-withcapacity.md)
  Static method that creates a new IODataQueue instance with the capacity specified in the size parameter.
- [withEntries](iodataqueue/1811020-withentries.md)
  Static method that creates a new IODataQueue instance with the specified number of entries of the given size.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iodataqueue/1810994-setnotificationport)*