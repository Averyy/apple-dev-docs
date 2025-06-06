# IOAsyncCallback2

**Framework**: IOKit  
**Kind**: tdef

standard callback function for asynchronous I/O requests with two extra arguments beyond a refcon and result code.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 13.0+
- macOS 10.0+
- visionOS 2.4+

## Declaration

```swift
typealias IOAsyncCallback2 = (UnsafeMutableRawPointer?, IOReturn, UnsafeMutableRawPointer?, UnsafeMutableRawPointer?) -> Void
```

## Parameters

- `refcon`: The refcon passed into the original I/O request
- `result`: The result of the I/O operation
- `arg0`: Extra argument
- `arg1`: Extra argument

## See Also

- [typealias IOAsyncCallback](ioasynccallback.md)
  standard callback function for asynchronous I/O requests with lots of extra arguments beyond a refcon and result code.
- [typealias IOAsyncCallback0](ioasynccallback0.md)
  standard callback function for asynchronous I/O requests with no extra arguments beyond a refcon and result code.
- [typealias IOAsyncCallback1](ioasynccallback1.md)
  standard callback function for asynchronous I/O requests with one extra argument beyond a refcon and result code. This is often a count of the number of bytes transferred
- [typealias IOServiceInterestCallback](ioserviceinterestcallback.md)
  Callback function to be notified of changes in state of an IOService.
- [typealias IOServiceMatchingCallback](ioservicematchingcallback.md)
  Callback function to be notified of IOService publication.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/ioasynccallback2)*