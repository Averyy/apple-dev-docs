# IODataQueue

**Framework**: Kernel  
**Kind**: cl

A generic queue designed to pass data from the kernel to a user process.

**Availability**:
- macOS 10.0+

## Declaration

```swift
class IODataQueue : OSObject
```

#### Overview

The IODataQueue class is designed to allow kernel code to queue data to a user process. IODataQueue objects are designed to be used in a single producer / single consumer situation. As such, there are no locks on the data itself. Because the kernel enqueue and user-space dequeue methods follow a strict set of guidelines, no locks are necessary to maintain the integrity of the data struct.

Each data entry can be variable sized, but the entire size of the queue data region (including overhead for each entry) must be specified up front.

In order for the IODataQueue instance to notify the user process that data is available, a notification mach port must be set. When the queue is empty and a new entry is added, a message is sent to the specified port.

User client code exists in the IOKit framework that facilitates the creation of the receive notification port as well as the listen process for new data available notifications.

In order to make the data queue memory available to a user process, the method getMemoryDescriptor() must be used to get an IOMemoryDescriptor instance that can be mapped into a user process. Typically, the clientMemoryForType() method on an IOUserClient instance will be used to request the IOMemoryDescriptor and then return it to be mapped into the user process.

## Topics

### Miscellaneous
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
- [setNotificationPort](iodataqueue/1810994-setnotificationport.md)
  Creates a simple mach message targeting the mach port specified in port.
- [withCapacity](iodataqueue/1811001-withcapacity.md)
  Static method that creates a new IODataQueue instance with the capacity specified in the size parameter.
- [withEntries](iodataqueue/1811020-withentries.md)
  Static method that creates a new IODataQueue instance with the specified number of entries of the given size.
### Instance Methods
- [- enqueue](iodataqueue/1586520-enqueue.md)
- [- free](iodataqueue/1586519-free.md)
- [- getMemoryDescriptor](iodataqueue/1586526-getmemorydescriptor.md)
- [- getMetaClass](iodataqueue/1586530-getmetaclass.md)
- [- initWithCapacity](iodataqueue/1586525-initwithcapacity.md)
- [- initWithEntries](iodataqueue/1586528-initwithentries.md)
- [- sendDataAvailableNotification](iodataqueue/1586529-senddataavailablenotification.md)
- [- setNotificationPort](iodataqueue/1586527-setnotificationport.md)
### Type Methods
- [+ withCapacity](iodataqueue/1586522-withcapacity.md)
- [+ withEntries](iodataqueue/1586523-withentries.md)

## Relationships

### Inherits From
- [OSObject](osobject.md)

## See Also

- [IODataQueueDispatchSource](iodataqueuedispatchsource.md)
- [IODataQueueDispatchSourceInterface](iodataqueuedispatchsourceinterface.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iodataqueue)*