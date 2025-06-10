# cancel()

**Framework**: Watch Connectivity  
**Kind**: method

Cancels the data transfer.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func cancel()
```

#### Discussion

Use this method to cancel a transfer before it completes. If the data has already been transferred, calling this method has no effect.

## See Also

- [var isTransferring: Bool](wcsessionuserinfotransfer/istransferring.md)
  A Boolean value indicating whether the data is still being transferred.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchconnectivity/wcsessionuserinfotransfer/cancel())*