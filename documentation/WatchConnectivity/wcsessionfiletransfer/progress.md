# progress

**Framework**: Watch Connectivity  
**Kind**: property  
**Role**: Instance Property

An object that tracks the progress of the file transfer.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 5.0+

## Declaration

```swift
var progress: Progress { get }
```

```objc
@property (nonatomic, readonly) NSProgress * progress;
```

## See Also

### Managing the File Transfer
- [var isTransferring: Bool](./istransferring.md)
  A Boolean value indicating whether the file is still being transferred.
- [func cancel()](./cancel%28%29.md)
  Cancels the file transfer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchconnectivity/wcsessionfiletransfer/progress)*