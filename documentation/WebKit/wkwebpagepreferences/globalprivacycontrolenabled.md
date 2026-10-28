# globalPrivacyControlEnabled

**Framework**: WebKit  
**Kind**: property  
**Role**: Instance Property

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+

## Declaration

```swift
var globalPrivacyControlEnabled: Bool { get set }
```

```objc
@property (nonatomic) BOOL globalPrivacyControlEnabled;
```

## Discussion

Whether the Global Privacy Control (GPC) signal is enabled for the navigation.

The default value is NO. When enabled, both navigator.globalPrivacyControl and the Sec-GPC: 1 request header are active for the main frame, its subframes, and their subresources.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebpagepreferences/globalprivacycontrolenabled)*