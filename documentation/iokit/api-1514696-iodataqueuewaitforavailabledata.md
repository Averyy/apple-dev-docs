# IODataQueueWaitForAvailableData(_:_:)

**Framework**: IOKit  
**Kind**: func

Wait for an incoming dataAvailable message on the given notifyPort.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 13.0+
- macOS 10.0+
- visionOS 2.4+

## Declaration

```swift
func IODataQueueWaitForAvailableData(_ dataQueue: UnsafeMutablePointer<IODataQueueMemory>!, _ notificationPort: mach_port_t) -> IOReturn
```

#### Return_value

Returns kIOReturnSuccess on success. Returns kIOReturnBadArgument if either dataQueue is 0 (NULL) or notiryPort is MACH_PORT_NULL. Returns the result of the mach_msg() listen call on the given port.

#### Discussion

This method will simply wait for an incoming message on the given notifyPort. Once it is received, the return from mach_msg() is returned.

## Parameters

- `dataQueue`: The IODataQueueMemory region mapped from the kernel.
- `notifyPort`: Mach port on which to listen for incoming messages.

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
- [func IODataQueueSetNotificationPort(UnsafeMutablePointer<IODataQueueMemory>!, mach_port_t) -> IOReturn](1514301-iodataqueuesetnotificationport.md)
  Creates a simple mach message targeting the mach port specified in port.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/1514696-iodataqueuewaitforavailabledata)*