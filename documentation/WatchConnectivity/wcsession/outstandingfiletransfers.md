# outstandingFileTransfers

**Framework**: Watch Connectivity  
**Kind**: property  
**Role**: Instance Property

An array of in-progress file transfers.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var outstandingFileTransfers: [WCSessionFileTransfer] { get }
```

```objc
@property (nonatomic, copy, readonly) NSArray<WCSessionFileTransfer *> * outstandingFileTransfers;
```

## Discussion

This property contains the [`WCSessionFileTransfer`](../wcsessionfiletransfer.md) objects representing the files that are queued for delivery but have not yet been delivered to the counterpart. You can use the objects to cancel specific file transfers.

## See Also

### Transferring Files in the Background
- [func transferFile(URL, metadata: [String : Any]?) -> WCSessionFileTransfer](./transferfile%28_,metadata%29.md)
  Sends the specified file and optional dictionary to the counterpart.
- [var hasContentPending: Bool](./hascontentpending.md)
  A Boolean value that indicates whether the session has more content to deliver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchconnectivity/wcsession/outstandingfiletransfers)*