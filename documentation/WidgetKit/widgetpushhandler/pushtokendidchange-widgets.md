# pushTokenDidChange(_:widgets:)

**Framework**: WidgetKit  
**Kind**: method  
**Required**: Yes

Handle push tokens changing for widgets reloads and relevance refreshes.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst ?+
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)
- watchOS 26.0+ (Beta)

## Declaration

```swift
func pushTokenDidChange(_ pushInfo: WidgetPushInfo, widgets: [WidgetInfo])
```

## Mentions

- [Updating widgets with WidgetKit push notifications](updating-widgets-with-widgetkit-push-notifications.md)

## Parameters

- `pushInfo`: Provides information containing your push token to use.
- `widgets`: Information about widgets that support push   updates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/widgetkit/widgetpushhandler/pushtokendidchange(_:widgets:))*