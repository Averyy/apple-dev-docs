# IODataQueueSetNotificationPort(_:_:)

**Framework**: IOKit  
**Kind**: func

Creates a simple mach message targeting the mach port specified in port.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- visionOS 1.0+

## Declaration

```swift
func IODataQueueSetNotificationPort(_ dataQueue: UnsafeMutablePointer<IODataQueueMemory>!, _ notifyPort: mach_port_t) -> IOReturn
```

#### Return_value

Returns kIOReturnSuccess on success. Returns kIOReturnBadArgument if either dataQueue is 0 (NULL).

#### Discussion

This message is sent when data is added to an empty queue. It is to notify another user process that new data has become available. 

## Parameters

- `dataQueue`: The IODataQueueMemory region mapped from the kernel created from an IOSharedDataQueue.
- `notifyPort`: The mach port to target with the notification message.

## See Also

- [func IODataQueueAllocateNotificationPort() -> mach_port_t](1514495-iodataqueueallocatenotificationp.md)
  Allocates and returns a new mach port able to receive data available notifications from an IODataQueue.
- [func IODataQueueDataAvailable(UnsafeMutablePointer<IODataQueueMemory>!) -> Bool](1514386-iodataqueuedataavailable.md)
  Used to determine if more data is avilable on the queue.
- [func IODataQueueDequeue(UnsafeMutablePointer<IODataQueueMemory>!, UnsafeMutableRawPointer!, UnsafeMutablePointer<UInt32>!) -> IOReturn](1514287-iodataqueuedequeue.md)
  Dequeues the next available entry on the queue and copies it into the given data pointer.
- [func IODataQueueEnqueue(UnsafeMutablePointer<IODataQueueMemory>!, UnsafeMutableRawPointer!, UInt32) -> IOReturn](1514482-iodataqueueenqueue.md)
  Enqueues a new entry on the queue.
- [func IODataQueuePeek(UnsafeMutablePointer<IODataQueueMemory>!) -> UnsafeMutablePointer<IODataQueueEntry>!](1514649-iodataqueuepeek.md)
  Used to peek at the next entry on the queue.
- [func IODataQueueWaitForAvailableData(UnsafeMutablePointer<IODataQueueMemory>!, mach_port_t) -> IOReturn](1514696-iodataqueuewaitforavailabledata.md)
  Wait for an incoming dataAvailable message on the given notifyPort.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/1514301-iodataqueuesetnotificationport)*