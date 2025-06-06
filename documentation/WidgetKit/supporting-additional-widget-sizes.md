# Supporting additional widget sizes

**Framework**: Widgetkit

Offer widgets in additional contexts by adding support for various widget sizes.

#### Overview

After you add a widget extension to your app and create your first widget, add code to declare additional widgets your app supports using the [`supportedFamilies(_:)`](https://developer.apple.com/documentation/SwiftUI/WidgetConfiguration/supportedFamilies(_:)) property modifier. The sizes you use depend on the devices your app supports. If your app supports more than one platform, make sure to conditionally declare supported widget families.

The following example from the [`Emoji Rangers: Supporting Live Activities, interactivity, and animations`](emoji-rangers-supporting-live-activities-interactivity-and-animations.md) sample code project shows how you declare several widgets sizes in your [`Widget`](https://developer.apple.com/documentation/SwiftUI/Widget) implementation. The app supports accessory widgets in both watchOS and iOS and [`WidgetFamily.systemSmall`](widgetfamily/systemsmall.md) and [`WidgetFamily.systemMedium`](widgetfamily/systemmedium.md) widgets in iOS. Note the usage of the `#if os(watchOS)` macro to make sure you declare the correct supported widget families for each platform.

```swift
public var body: some WidgetConfiguration {
    makeWidgetConfiguration()
        .configurationDisplayName("Ranger Detail")
        .description("See your favorite ranger.")
#if os(watchOS)
        .supportedFamilies([.accessoryCircular,
                            .accessoryRectangular, .accessoryInline])
#else
        .supportedFamilies([.accessoryCircular,
                            .accessoryRectangular, .accessoryInline,
                            .systemSmall, .systemMedium, .systemLarge])
#endif
}
```

##### Update Swiftui Views to Support Additional Sizes

After you’ve declared support for additional widget sizes in your [`Widget`](https://developer.apple.com/documentation/SwiftUI/Widget), update the views of your widget to support the additional family sizes. In your view code:

1. Use the [`widgetFamily`](https://developer.apple.com/documentation/SwiftUI/EnvironmentValues/widgetFamily) environment variable to detect different widget families.
2. Construct the view for each size and include code to handle appearances like vibrant and Dark Mode, as applicable. To learn more, see [`Preparing widgets for additional platforms, contexts, and appearances`](preparing-widgets-for-additional-contexts-and-appearances.md).

The following example shows an abbreviated code snippet from the [`Emoji Rangers: Supporting Live Activities, interactivity, and animations`](emoji-rangers-supporting-live-activities-interactivity-and-animations.md) sample code project. It conditionally returns the right SwiftUI view for each widget family.

```swift
struct EmojiRangerWidgetEntryView: View {
    var entry: Provider.Entry
    
    @Environment(\.widgetFamily) var family

    @ViewBuilder
    var body: some View {
        switch family {
        case .accessoryCircular:
            // Code to construct the view for the circular accessory widget or watch complication.
        case .accessoryRectangular:
            // Code to construct the view for the rectangular accessory widget or watch complication.
        case .accessoryInline:
            // Code to construct the view for the inline accessory widget or watch complication.
        case .systemSmall:
            // Code to construct the view for the small widget.
        case .systemLarge:
            // Code to construct the view for the large widget.
        case .systemMedium
            // Code to construct the view for the medium widget.
        default:
            // Code to construct the view for other widgets, for example, the extra large widget.
        }
    }
}
```

> 💡 **Tip**: Use Xcode previews to view your widget designs without running your app in Simulator or on a device. For more information, see [`Preview widgets in Xcode`](creating-a-widget-extension#Preview-widgets-in-Xcode.md).

Use Xcode previews to view your widget designs without running your app in Simulator or on a device. For more information, see [`Preview widgets in Xcode`](creating-a-widget-extension#Preview-widgets-in-Xcode.md).

## See Also

- [Creating a widget extension](creating-a-widget-extension.md)
  Display your app’s content in a convenient, informative widget on various devices.
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
- [struct WidgetAccentedRenderingMode](widgetaccentedrenderingmode.md)
  Constants that indicate the rendering mode for an `Image` in when displayed in a widget in [`accented`](widgetrenderingmode/accented.md) mode.


---

*[View on Apple Developer](https://developer.apple.com/documentation/widgetkit/supporting-additional-widget-sizes)*