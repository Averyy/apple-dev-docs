# WidgetAccentedRenderingMode

**Framework**: Widgetkit  
**Kind**: struct

Constants that indicate the rendering mode for an `Image` in when displayed in a widget in [`accented`](widgetrenderingmode/accented.md) mode.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- watchOS 11.0+

## Declaration

```swift
struct WidgetAccentedRenderingMode
```

## Topics

### Type Properties
- [static let accented: WidgetAccentedRenderingMode](widgetaccentedrenderingmode/accented.md)
  Specifies that the `Image` should be included as part of the accented widget group.
- [static let accentedDesaturated: WidgetAccentedRenderingMode](widgetaccentedrenderingmode/accenteddesaturated.md)
  Maps the luminance of the `Image` in to the alpha channel, replacing color channels with the color applied to the accent group.
- [static let desaturated: WidgetAccentedRenderingMode](widgetaccentedrenderingmode/desaturated.md)
  Maps the luminance of the `Image` in to the alpha channel, replacing color channels with the color applied to the default group.
- [static let fullColor: WidgetAccentedRenderingMode](widgetaccentedrenderingmode/fullcolor.md)
  Specifies that the `Image` should be rendered at full color with no other color modifications. Only applies to iOS.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)

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
- [struct WidgetRenderingMode](widgetrenderingmode.md)
  Constants that indicate the rendering mode for a widget.


---

*[View on Apple Developer](https://developer.apple.com/documentation/widgetkit/widgetaccentedrenderingmode)*