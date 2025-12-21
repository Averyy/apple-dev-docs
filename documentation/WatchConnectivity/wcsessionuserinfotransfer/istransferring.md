# isTransferring

**Framework**: Watch Connectivity  
**Kind**: property

A Boolean value indicating whether the data is still being transferred.

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

The value of this property is [`true`](https://developer.apple.com/documentation/Swift/true) if the data has not yet been transferred or [`false`](https://developer.apple.com/documentation/Swift/false) if the transfer is complete.

## See Also

- [func cancel()](wcsessionuserinfotransfer/cancel.md)
  Cancels the data transfer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchconnectivity/wcsessionuserinfotransfer/istransferring)*