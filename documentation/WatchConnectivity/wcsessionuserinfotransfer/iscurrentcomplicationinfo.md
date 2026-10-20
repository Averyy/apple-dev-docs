# isCurrentComplicationInfo

**Framework**: Watch Connectivity  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (nonatomic, readonly, getter=isCurrentComplicationInfo) BOOL currentComplicationInfo;
```

#### Discussion

This property is set to [`true`](../../Swift/true.md) if you initiated the transfer using the [`transferCurrentComplicationUserInfo(_:)`](../wcsession/transfercurrentcomplicationuserinfo%28_%29.md) method of the [`WCSession`](../wcsession.md) object or [`false`](../../Swift/false.md) otherwise.

## See Also

### Getting the Transfer Information
- [var userInfo: [String : Any]](./userinfo.md)
  The data being transferred.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchconnectivity/wcsessionuserinfotransfer/iscurrentcomplicationinfo)*