# isTransferring

**Framework**: Watch Connectivity  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (nonatomic, readonly, getter=isTransferring) BOOL transferring;
```

#### Discussion

The value of this property is [`true`](../../Swift/true.md) if the data has not yet been transferred or [`false`](../../Swift/false.md) if the transfer is complete.

## See Also

### Managing the Transfer Operation
- [func cancel()](./cancel%28%29.md)
  Cancels the data transfer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchconnectivity/wcsessionuserinfotransfer/istransferring)*