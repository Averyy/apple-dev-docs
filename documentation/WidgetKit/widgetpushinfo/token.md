# token

**Framework**: WidgetKit  
**Kind**: property

A unique push token that may be used to deliver updates for widgets and widget relevances.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst ?+
- macOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
let token: Data
```

#### Discussion

This token is valid until told otherwise through the [`pushTokenDidChange(_:widgets:)`](widgetpushhandler/pushtokendidchange(_:widgets:).md) method on your push handler.


---

*[View on Apple Developer](https://developer.apple.com/documentation/widgetkit/widgetpushinfo/token)*