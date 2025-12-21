# hasContentPending

**Framework**: Watch Connectivity  
**Kind**: property

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

#### Discussion

[`true`](https://developer.apple.com/documentation/Swift/true) if the session has received data in the background but has not yet delivered that data to the session’s delegate. The following methods send data in the background:

- [`updateApplicationContext(_:)`](wcsession/updateapplicationcontext(_:).md)
- [`transferUserInfo(_:)`](wcsession/transferuserinfo(_:).md)
- [`transferCurrentComplicationUserInfo(_:)`](wcsession/transfercurrentcomplicationuserinfo(_:).md)
- [`transferFile(_:metadata:)`](wcsession/transferfile(_:metadata:).md)

## See Also

- [func transferFile(URL, metadata: [String : Any]?) -> WCSessionFileTransfer](wcsession/transferfile(_:metadata:).md)
  Sends the specified file and optional dictionary to the counterpart.
- [var outstandingFileTransfers: [WCSessionFileTransfer]](wcsession/outstandingfiletransfers.md)
  An array of in-progress file transfers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchconnectivity/wcsession/hascontentpending)*