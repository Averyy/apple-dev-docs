# ControlPushHandler

**Framework**: WidgetKit  
**Kind**: protocol

A type that can receive push information about user-configured controls.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst ?+
- macOS 26.0+
- watchOS 26.0+

## Declaration

```swift
protocol ControlPushHandler
```

#### Overview

Register a type conforming to this protocol to receive push information using the [`pushHandler(_:)`](https://developer.apple.com/documentation/SwiftUI/ControlWidgetConfiguration/pushHandler(_:)) modifier on your controls’ configurations.

## Topics

### Initializers
- [init()](controlpushhandler/init.md)
  Creates a push handler.
### Instance Methods
- [func pushTokensDidChange(controls: [ControlInfo])](controlpushhandler/pushtokensdidchange(controls:).md)
  Handle push tokens changing for configured controls.

## See Also

- [Updating controls locally and remotely](updating-controls-locally-and-remotely.md)
  Update and reload controls from your app or using push notifications.
- [struct ControlPushInfo](controlpushinfo.md)
  A structure that contains information about the push token of a user-configured control.


---

*[View on Apple Developer](https://developer.apple.com/documentation/widgetkit/controlpushhandler)*