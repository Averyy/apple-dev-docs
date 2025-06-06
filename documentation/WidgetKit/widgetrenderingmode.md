# WidgetRenderingMode

**Framework**: Widgetkit  
**Kind**: struct

Constants that indicate the rendering mode for a widget.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- watchOS 9.0+

## Declaration

```swift
struct WidgetRenderingMode
```

## Mentions

- [Migrating ClockKit complications to WidgetKit](converting-a-clockkit-app.md)

#### Overview

The system can modify the appearance of accessory family widgets. For example, it renders widgets on the Lock Screen on iPhone using the [`vibrant`](widgetrenderingmode/vibrant.md) mode, while it renders widget-based complications in watchOS using either the [`fullColor`](widgetrenderingmode/fullcolor.md) or [`accented`](widgetrenderingmode/accented.md) modes, depending on the watch face and the user’s settings.

You can read the rendering mode from the environment values using the `.widgetRenderingMode` key.

```swift
@Environment(\.widgetRenderingMode) var widgetRenderingMode
```

You can then customize your widget’s design based on the rendering mode.

## Topics

### Rendering modes
- [static let fullColor: WidgetRenderingMode](widgetrenderingmode/fullcolor.md)
  The system renders the widget in full color.
- [static let accented: WidgetRenderingMode](widgetrenderingmode/accented.md)
  The system divides the widget’s view hierarchy into an accent group and a default group, applying a different color to each group.
- [static let vibrant: WidgetRenderingMode](widgetrenderingmode/vibrant.md)
  The system desaturates the widget, making a monochrome version that it uses to create an adaptive, vibrant effect.

## Relationships

### Conforms To
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)

## See Also

- [Creating a widget extension](creating-a-widget-extension.md)
  Display your app’s content in a convenient, informative widget on various devices.
- [Supporting additional widget sizes](supporting-additional-widget-sizes.md)
  Offer widgets in additional contexts by adding support for various widget sizes.
- [Creating accessory widgets and watch complications](creating-accessory-widgets-and-watch-complications.md)
  Support accessory widgets that appear on the Lock Screen and as complications on Apple Watch.
- [Migrating ClockKit complications to WidgetKit](converting-a-clockkit-app.md)
  Leverage WidgetKit’s API to create watchOS complications using SwiftUI.
- [Building Widgets Using WidgetKit and SwiftUI](building_widgets_using_widgetkit_and_swiftui.md)
  Create widgets to show your app’s content on the Home screen, with custom intents for user-customizable settings.
- [Emoji Rangers: Supporting Live Activities, interactivity, and animations](emoji-rangers-supporting-live-activities-interactivity-and-animations.md)
  Offer Live Activities, controls, animate data updates, and add interactivity to widgets.
- [Backyard Birds: Building an app with SwiftData and widgets](../SwiftUI/Backyard-birds-sample.md)
  Create an app with persistent data, interactive widgets, and an all new in-app purchase experience.
- [Fruta: Building a Feature-Rich App with SwiftUI](../appclip/fruta_building_a_feature-rich_app_with_swiftui.md)
  Create a shared codebase to build a multiplatform app that offers widgets and an App Clip.
- [@MainActor @preconcurrency protocol Widget](../SwiftUI/Widget.md)
  The configuration and content of a widget to display on the Home screen or in Notification Center.
- [@MainActor @preconcurrency protocol WidgetBundle](../SwiftUI/WidgetBundle.md)
  A container used to expose multiple widgets from a single widget extension.
- [struct StaticConfiguration](staticconfiguration.md)
  An object describing the content of a widget that has no user-configurable options.
- [enum WidgetFamily](widgetfamily.md)
  Values that define the widget’s size and shape.
- [struct WidgetAccentedRenderingMode](widgetaccentedrenderingmode.md)
  Constants that indicate the rendering mode for an `Image` in when displayed in a widget in [`accented`](widgetrenderingmode/accented.md) mode.


---

*[View on Apple Developer](https://developer.apple.com/documentation/widgetkit/widgetrenderingmode)*