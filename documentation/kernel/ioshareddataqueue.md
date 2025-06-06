# IOSharedDataQueue

**Framework**: Kernel  
**Kind**: cl

A generic queue designed to pass data both from the kernel to a user process and from a user process to the kernel.

**Availability**:
- macOS 10.5+

## Declaration

```swift
class IOSharedDataQueue : IODataQueue
```

#### Overview

The IOSharedDataQueue class is designed to also allow a user process to queue data to kernel code. IOSharedDataQueue objects are designed to be used in a single producer / single consumer situation. As such, there are no locks on the data itself. Because the kernel enqueue and user-space dequeue methods follow a strict set of guidelines, no locks are necessary to maintain the integrity of the data struct.

Each data entry can be variable sized, but the entire size of the queue data region (including overhead for each entry) must be specified up front.

In order for the IODataQueue instance to notify the user process that data is available, a notification mach port must be set. When the queue is empty and a new entry is added, a message is sent to the specified port.

In order to make the data queue memory available to a user process, the method getMemoryDescriptor() must be used to get an IOMemoryDescriptor instance that can be mapped into a user process. Typically, the clientMemoryForType() method on an IOUserClient instance will be used to request the IOMemoryDescriptor and then return it to be mapped into the user process.

## Topics

### Miscellaneous
- [dequeue](ioshareddataqueue/1810190-dequeue.md)
  Dequeues the next available entry on the queue and copies it into the given data pointer.
- [getMemoryDescriptor](ioshareddataqueue/1810240-getmemorydescriptor.md)
  Returns a memory descriptor covering the IODataQueueMemory region.
- [initWithCapacity](ioshareddataqueue/1810293-initwithcapacity.md)
  Initializes an IOSharedDataQueue instance with the capacity specified in the size parameter.
- [peek](ioshareddataqueue/1810347-peek.md)
  Used to peek at the next entry on the queue.
- [withCapacity](ioshareddataqueue/1810400-withcapacity.md)
  Static method that creates a new IOSharedDataQueue instance with the capacity specified in the size parameter.
- [withEntries](ioshareddataqueue/1810447-withentries.md)
  Static method that creates a new IOSharedDataQueue instance with the specified number of entries of the given size.
### Instance Variables
- [_reserved](ioshareddataqueue/reserved.md)
### Instance Methods
- [- dequeue](ioshareddataqueue/1562870-dequeue.md)
- [- enqueue](ioshareddataqueue/1562880-enqueue.md)
- [- free](ioshareddataqueue/1562879-free.md)
- [- getMemoryDescriptor](ioshareddataqueue/1562877-getmemorydescriptor.md)
- [- getMetaClass](ioshareddataqueue/1562878-getmetaclass.md)
- [- getQueueSize](ioshareddataqueue/1562873-getqueuesize.md)
- [- initWithCapacity](ioshareddataqueue/1562876-initwithcapacity.md)
- [- peek](ioshareddataqueue/1562872-peek.md)
- [- setQueueSize](ioshareddataqueue/1562874-setqueuesize.md)
### Type Methods
- [+ withCapacity](ioshareddataqueue/1562871-withcapacity.md)
- [+ withEntries](ioshareddataqueue/1562881-withentries.md)

## Relationships

### Inherits From
- [IODataQueue](iodataqueue.md)

## See Also

- [IOSharedInterruptController](iosharedinterruptcontroller.md)
- [IOUserClient](iouserclient.md)
  Provides a basis for communication between client applications and I/O Kit objects.
- [IOStreamUserClient](iostreamuserclient.md)
- [IOStream](iostream.md)
  A class representing a stream of data buffers passed from kernel to user space and back again.
- [IOStreamBuffer](iostreambuffer.md)
  A class representing a data buffer that is part of an IOStream.
- [OSAction_IOUserClient_KernelCompletion](osaction_iouserclient_kernelcompletion.md)
- [OSAction_IOUserClient_KernelCompletionInterface](osaction_iouserclient_kernelcompletioninterface.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/ioshareddataqueue)*