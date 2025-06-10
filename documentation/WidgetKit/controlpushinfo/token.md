# token

**Framework**: WidgetKit  
**Kind**: property

A unique push token that may be used to deliver updates for this control.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst ?+
- macOS 26.0+ (Beta)
- watchOS 26.0+ (Beta)

## Declaration

```swift
let token: Data
```

#### Discussion

This token is valid until told otherwise through the [`pushTokensDidChange(controls:)`](controlpushhandler/pushtokensdidchange(controls:).md) method on your push handler.


---

*[View on Apple Developer](https://developer.apple.com/documentation/widgetkit/controlpushinfo/token)*