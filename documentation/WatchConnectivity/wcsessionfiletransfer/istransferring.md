# isTransferring

**Framework**: Watchconnectivity  
**Kind**: property

A Boolean value indicating whether the file is still being transferred.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var isTransferring: Bool { get }
```

#### Discussion

The value of this property is [`true`](https://developer.apple.com/documentation/swift/true) if the file transfer is not yet complete or [`false`](https://developer.apple.com/documentation/swift/false) if the transfer is complete.

## See Also

- [var progress: Progress](wcsessionfiletransfer/progress.md)
  An object that tracks the progress of the file transfer.
- [func cancel()](wcsessionfiletransfer/cancel.md)
  Cancels the file transfer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchconnectivity/wcsessionfiletransfer/istransferring)*