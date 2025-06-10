# token

**Framework**: WidgetKit  
**Kind**: property

A unique push token that may be used to deliver updates for widgets and widget relevances.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst ?+
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)
- watchOS 26.0+ (Beta)

## Declaration

```swift
let token: Data
```

#### Discussion

This token is valid until told otherwise through the `WidgetPushHandler/pushTokenDidChange(_:)` method on your push handler.


---

*[View on Apple Developer](https://developer.apple.com/documentation/widgetkit/widgetpushinfo/token)*