# IODataQueueEnqueue(_:_:_:)

**Framework**: IOKit  
**Kind**: func

Enqueues a new entry on the queue.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- visionOS 1.0+

## Declaration

```swift
func IODataQueueEnqueue(_ dataQueue: UnsafeMutablePointer<IODataQueueMemory>!, _ data: UnsafeMutableRawPointer!, _ dataSize: UInt32) -> IOReturn
```

#### Return_value

Returns kIOReturnSuccess on success. Other return values possible are: kIOReturnOverrun - queue is full.

#### Discussion

This method adds a new data entry of dataSize to the queue. It sets the size parameter of the entry pointed to by the tail value and copies the memory pointed to by the data parameter in place in the queue. Once that is done, it moves the tail to the next available location. When attempting to add a new entry towards the end of the queue and there isn't enough space at the end, it wraps back to the beginning.

If the queue is empty when a new entry is added, the port specified in IODataQueueSetNotificationPort will be used to send a message to the client process that data is now available.

## Parameters

- `dataQueue`: The IODataQueueMemory region mapped from the kernel created from an IOSharedDataQueue.
- `data`: Pointer to the data to be added to the queue.
- `dataSize`: Size of the data pointed to by data.

## See Also

- [func IODataQueueAllocateNotificationPort() -> mach_port_t](1514495-iodataqueueallocatenotificationp.md)
  Allocates and returns a new mach port able to receive data available notifications from an IODataQueue.
- [func IODataQueueDataAvailable(UnsafeMutablePointer<IODataQueueMemory>!) -> Bool](1514386-iodataqueuedataavailable.md)
  Used to determine if more data is avilable on the queue.
- [func IODataQueueDequeue(UnsafeMutablePointer<IODataQueueMemory>!, UnsafeMutableRawPointer!, UnsafeMutablePointer<UInt32>!) -> IOReturn](1514287-iodataqueuedequeue.md)
  Dequeues the next available entry on the queue and copies it into the given data pointer.
- [func IODataQueuePeek(UnsafeMutablePointer<IODataQueueMemory>!) -> UnsafeMutablePointer<IODataQueueEntry>!](1514649-iodataqueuepeek.md)
  Used to peek at the next entry on the queue.
- [func IODataQueueSetNotificationPort(UnsafeMutablePointer<IODataQueueMemory>!, mach_port_t) -> IOReturn](1514301-iodataqueuesetnotificationport.md)
  Creates a simple mach message targeting the mach port specified in port.
- [func IODataQueueWaitForAvailableData(UnsafeMutablePointer<IODataQueueMemory>!, mach_port_t) -> IOReturn](1514696-iodataqueuewaitforavailabledata.md)
  Wait for an incoming dataAvailable message on the given notifyPort.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/1514482-iodataqueueenqueue)*