# globalPrivacyControlStatus

**Framework**: WebKit  
**Kind**: property

Whether the Global Privacy Control (GPC) signal is enabled for the navigation.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
var globalPrivacyControlStatus: Bool
```

#### Discussion

The default value of this property is `false`. When enabled, both `navigator.globalPrivacyControl` and the `Sec-GPC: 1` request header are active for the main frame, its subframes, and their subresources.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webpage/navigationpreferences/globalprivacycontrolstatus)*