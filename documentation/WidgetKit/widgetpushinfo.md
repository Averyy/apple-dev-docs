# WidgetPushInfo

**Framework**: WidgetKit  
**Kind**: struct

A structure that contains information about the push token for updating widgets and widget relevances.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst ?+
- macOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
struct WidgetPushInfo
```

## Mentions

- [Updating widgets with WidgetKit push notifications](updating-widgets-with-widgetkit-push-notifications.md)

## Topics

### Instance Properties
- [let token: Data](widgetpushinfo/token.md)
  A unique push token that may be used to deliver updates for widgets and widget relevances.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [Updating widgets with WidgetKit push notifications](updating-widgets-with-widgetkit-push-notifications.md)
  Use WidgetKit to receive push tokens and reload your widgets with remote push notifications.
- [protocol WidgetPushHandler](widgetpushhandler.md)
  A type that can receive push information about widget refreshes and relevance refreshes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/widgetkit/widgetpushinfo)*