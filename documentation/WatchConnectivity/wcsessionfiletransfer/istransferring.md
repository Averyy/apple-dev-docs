# isTransferring

**Framework**: Watch Connectivity  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (nonatomic, readonly, getter=isTransferring) BOOL transferring;
```

## Discussion

The value of this property is [`true`](../../Swift/true.md) if the file transfer is not yet complete or [`false`](../../Swift/false.md) if the transfer is complete.

## See Also

### Managing the File Transfer
- [var progress: Progress](./progress.md)
  An object that tracks the progress of the file transfer.
- [func cancel()](./cancel%28%29.md)
  Cancels the file transfer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchconnectivity/wcsessionfiletransfer/istransferring)*