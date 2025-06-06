# IOServiceInterestCallback

**Framework**: IOKit  
**Kind**: tdef

Callback function to be notified of changes in state of an IOService.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 13.0+
- macOS 10.0+
- visionOS 2.4+

## Declaration

```swift
typealias IOServiceInterestCallback = (UnsafeMutableRawPointer?, io_service_t, UInt32, UnsafeMutableRawPointer?) -> Void
```

## Parameters

- `refcon`: The refcon passed when the notification was installed.
- `service`: The IOService whose state has changed.
- `messageType`: A messageType enum, defined by IOKit/IOMessage.h or by the IOService's family.
- `messageArgument`: An argument for the message, dependent on the messageType. If the message data is larger than sizeof(void*), then messageArgument contains a pointer to the message data; otherwise, messageArgument contains the message data.

## See Also

- [typealias IOAsyncCallback](ioasynccallback.md)
  standard callback function for asynchronous I/O requests with lots of extra arguments beyond a refcon and result code.
- [typealias IOAsyncCallback0](ioasynccallback0.md)
  standard callback function for asynchronous I/O requests with no extra arguments beyond a refcon and result code.
- [typealias IOAsyncCallback1](ioasynccallback1.md)
  standard callback function for asynchronous I/O requests with one extra argument beyond a refcon and result code. This is often a count of the number of bytes transferred
- [typealias IOAsyncCallback2](ioasynccallback2.md)
  standard callback function for asynchronous I/O requests with two extra arguments beyond a refcon and result code.
- [typealias IOServiceMatchingCallback](ioservicematchingcallback.md)
  Callback function to be notified of IOService publication.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/ioserviceinterestcallback)*