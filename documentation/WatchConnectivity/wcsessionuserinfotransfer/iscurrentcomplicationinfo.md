# isCurrentComplicationInfo

**Framework**: Watch Connectivity  
**Kind**: property

A Boolean indicating whether the data is related to the app’s complication.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
var isCurrentComplicationInfo: Bool { get }
```

#### Discussion

This property is set to [`true`](https://developer.apple.com/documentation/swift/true) if you initiated the transfer using the [`transferCurrentComplicationUserInfo(_:)`](wcsession/transfercurrentcomplicationuserinfo(_:).md) method of the [`WCSession`](wcsession.md) object or [`false`](https://developer.apple.com/documentation/swift/false) otherwise.

## See Also

- [var userInfo: [String : Any]](wcsessionuserinfotransfer/userinfo.md)
  The data being transferred.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchconnectivity/wcsessionuserinfotransfer/iscurrentcomplicationinfo)*