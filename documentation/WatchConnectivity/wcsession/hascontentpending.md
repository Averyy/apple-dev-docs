# hasContentPending

**Framework**: Watch Connectivity  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the session has more content to deliver.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
var hasContentPending: Bool { get }
```

```objc
@property (nonatomic, readonly) BOOL hasContentPending;
```

## Discussion

[`true`](../../Swift/true.md) if the session has received data in the background but has not yet delivered that data to the session’s delegate. The following methods send data in the background:

- [`updateApplicationContext(_:)`](./updateapplicationcontext%28_%29.md)
- [`transferUserInfo(_:)`](./transferuserinfo%28_%29.md)
- [`transferCurrentComplicationUserInfo(_:)`](./transfercurrentcomplicationuserinfo%28_%29.md)
- [`transferFile(_:metadata:)`](./transferfile%28_,metadata%29.md)

## See Also

### Transferring Files in the Background
- [func transferFile(URL, metadata: [String : Any]?) -> WCSessionFileTransfer](./transferfile%28_,metadata%29.md)
  Sends the specified file and optional dictionary to the counterpart.
- [var outstandingFileTransfers: [WCSessionFileTransfer]](./outstandingfiletransfers.md)
  An array of in-progress file transfers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchconnectivity/wcsession/hascontentpending)*