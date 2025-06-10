# cancel()

**Framework**: Watch Connectivity  
**Kind**: method

Cancels the file transfer.

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

Use this method to cancel a file transfer before it completes. If the file has already been transferred, calling this method has no effect.

## See Also

- [var isTransferring: Bool](wcsessionfiletransfer/istransferring.md)
  A Boolean value indicating whether the file is still being transferred.
- [var progress: Progress](wcsessionfiletransfer/progress.md)
  An object that tracks the progress of the file transfer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchconnectivity/wcsessionfiletransfer/cancel())*