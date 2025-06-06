# IOServiceMatchingCallback

**Framework**: IOKit  
**Kind**: tdef

Callback function to be notified of IOService publication.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 13.0+
- macOS 10.0+
- visionOS 2.4+

## Declaration

```swift
typealias IOServiceMatchingCallback = (UnsafeMutableRawPointer?, io_iterator_t) -> Void
```

## Parameters

- `refcon`: The refcon passed when the notification was installed.
- `iterator`: The notification iterator which now has new objects.

## See Also

- [typealias IOAsyncCallback](ioasynccallback.md)
  standard callback function for asynchronous I/O requests with lots of extra arguments beyond a refcon and result code.
- [typealias IOAsyncCallback0](ioasynccallback0.md)
  standard callback function for asynchronous I/O requests with no extra arguments beyond a refcon and result code.
- [typealias IOAsyncCallback1](ioasynccallback1.md)
  standard callback function for asynchronous I/O requests with one extra argument beyond a refcon and result code. This is often a count of the number of bytes transferred
- [typealias IOAsyncCallback2](ioasynccallback2.md)
  standard callback function for asynchronous I/O requests with two extra arguments beyond a refcon and result code.
- [typealias IOServiceInterestCallback](ioserviceinterestcallback.md)
  Callback function to be notified of changes in state of an IOService.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/ioservicematchingcallback)*