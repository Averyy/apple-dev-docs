# WidgetPushHandler

**Framework**: WidgetKit  
**Kind**: protocol

A type that can receive push information about widget refreshes and relevance refreshes.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst ?+
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)
- watchOS 26.0+ (Beta)

## Declaration

```swift
protocol WidgetPushHandler
```

## Mentions

- [Updating widgets with WidgetKit push notifications](updating-widgets-with-widgetkit-push-notifications.md)

#### Overview

Register a type conforming to this protocol to receive push information using the `WidgetConfiguration/pushHandler(_:)` modifier on your widgets’ configurations.

## Topics

### Initializers
- [init()](widgetpushhandler/init.md)
  Creates a push handler.
### Instance Methods
- [func pushTokenDidChange(WidgetPushInfo, widgets: [WidgetInfo])](widgetpushhandler/pushtokendidchange(_:widgets:).md)
  Handle push tokens changing for widgets reloads and relevance refreshes.

## See Also

- [Updating widgets with WidgetKit push notifications](updating-widgets-with-widgetkit-push-notifications.md)
  Use WidgetKit to receive push tokens and reload your widgets with remote push notifications.
- [struct WidgetPushInfo](widgetpushinfo.md)
  A structure that contains information about the push token for updating widgets and widget relevances.


---

*[View on Apple Developer](https://developer.apple.com/documentation/widgetkit/widgetpushhandler)*