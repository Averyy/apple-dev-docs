# WidgetLocation

**Framework**: Widgetkit  
**Kind**: struct

Values that indicate different widget locations.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+

## Declaration

```swift
struct WidgetLocation
```

## Mentions

- [Preparing widgets for additional platforms, contexts, and appearances](preparing-widgets-for-additional-contexts-and-appearances.md)

## Topics

### Specifying a location style
- [static let iPhoneWidgetsOnMac: WidgetLocation](widgetlocation/iphonewidgetsonmac.md)
  The widget originates from another device and appears on the Mac.
- [static let homeScreen: WidgetLocation](widgetlocation/homescreen.md)
  The widget appears on the Home Screen or in Today View.
- [static let lockScreen: WidgetLocation](widgetlocation/lockscreen.md)
  The widget appears on the Lock Screen.
- [static let standBy: WidgetLocation](widgetlocation/standby.md)
  The widget appears in StandBy.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [Creating views for widgets, Live Activities, and watch complications](creating-views-for-widgets-live-activities-and-watch-complications.md)
  Implement glanceable views with WidgetKit and SwiftUI.
- [Preparing widgets for additional platforms, contexts, and appearances](preparing-widgets-for-additional-contexts-and-appearances.md)
  Create widgets that support additional platforms and adapt to their context.
- [SwiftUI views for widgets](swiftui-views.md)
  Present your app’s content in widgets with SwiftUI views.
- [Introducing SwiftUI](https://developer.apple.com/tutorials/SwiftUI)
  SwiftUI is a modern way to declare user interfaces for any Apple platform. Create beautiful, dynamic apps faster than ever before.
- [struct AccessoryWidgetBackground](accessorywidgetbackground.md)
  An adaptive background view that provides a standard appearance based on the the widget’s environment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/widgetkit/widgetlocation)*