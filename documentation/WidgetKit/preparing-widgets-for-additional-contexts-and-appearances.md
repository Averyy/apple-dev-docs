# Preparing widgets for additional platforms, contexts, and appearances

**Framework**: WidgetKit

Create widgets that support additional platforms and adapt to their context.

#### Overview

Widgets change their appearance to best fit their context. For example, widgets on the Home Screen, Today View, and on Mac use accented colors and a clear glass presentation with a specific tint color, or they appear in a full color rendering. In CarPlay, small widgets appear scaled up and in full color, while Lock Screen widgets and WidgetKit complications use more restrained colors because they’re smaller, always visible, and support tinted modes for each platform. Because all widgets appear in more than one context, make sure your widgets and their SwiftUI views support all applicable rendering modes.

WidgetKit uses three different rendering modes:

The following table shows the rendering modes for each widget you need to support:

| Widget size | [`fullColor`](widgetrenderingmode/fullcolor.md) | [`accented`](widgetrenderingmode/accented.md) | [`vibrant`](widgetrenderingmode/vibrant.md) |
| --- | --- | --- | --- |
| [`WidgetFamily.systemSmall`](widgetfamily/systemsmall.md) | Yes | Yes | Yes |
| [`WidgetFamily.systemMedium`](widgetfamily/systemmedium.md) | Yes | Yes | Yes |
| [`WidgetFamily.systemLarge`](widgetfamily/systemlarge.md) | Yes | Yes | Yes |
| [`WidgetFamily.systemExtraLarge`](widgetfamily/systemextralarge.md) | Yes | Yes | Yes |
| [`WidgetFamily.systemExtraLargePortrait`](widgetfamily/systemextralargeportrait.md) | Yes | Yes | Yes |
| [`WidgetFamily.accessoryCircular`](widgetfamily/accessorycircular.md) | No | Yes | Yes |
| [`WidgetFamily.accessoryCorner`](widgetfamily/accessorycorner.md) | No | Yes | Yes |
| [`WidgetFamily.accessoryRectangular`](widgetfamily/accessoryrectangular.md) | Yes | Yes | Yes |
| [`WidgetFamily.accessoryInline`](widgetfamily/accessoryinline.md) | No | Yes | Yes |

> **Note**: For design guidance, see [`Human Interface Guidelines > Complications`](https://developer.apple.comhttps://developer.apple.com/design/human-interface-guidelines/complications) and [`Human Interface Guidelines > Widgets`](https://developer.apple.comhttps://developer.apple.com/design/human-interface-guidelines/widgets).

In your code, read the [`widgetRenderingMode`](https://developer.apple.com/documentation/SwiftUI/EnvironmentValues/widgetRenderingMode) environment variable to create SwiftUI views for each applicable rendering mode, as shown in the following example:

```swift
// ...

@Environment(\.widgetRenderingMode) var renderingMode

var body: some View {
   ZStack {
       switch renderingMode {
       case .fullColor:
           // Create views for full-color widgets and watch complications.
       case .accented:
           // Create views and group applicable views in the accented group.
           VStack {
               // ...
           }
           .widgetAccentable()
           // Additional views that you don't group in the accented group.
       case .vibrant:
           // Create views for Lock Screen widgets on iPhone and iPad.
   }
}
```

##### Make Your Background Views Removable

In many contexts, the system removes your widget’s background views to match the system appearance. To control which components of your widget the system removes, group them into background containers and mark them as removable. For more information, refer to [`Displaying the right widget background`](displaying-the-right-widget-background.md).

##### Support Always on

If you create accessory widgets and WidgetKit complications, make sure to use SwiftUI’s [`isLuminanceReduced`](https://developer.apple.com/documentation/SwiftUI/EnvironmentValues/isLuminanceReduced) environment variable to detect Always On and color your views to look great with reduced luminance. For design guidance, see [`Human Interface Guidelines > Always On`](https://developer.apple.comhttps://developer.apple.com/design/human-interface-guidelines/always-on) and [`Human Interface Guidelines > Widgets`](https://developer.apple.comhttps://developer.apple.com/design/human-interface-guidelines/widgets).

##### Update Your Small Widget to Support Standby and Carplay

On iPhone in StandBy, the Lock Screen shows two widgets side by side on a dark background. In CarPlay, widgets appear on a dedicated Widgets screen. For both appearances, WidgetKit uses your [`WidgetFamily.systemSmall`](widgetfamily/systemsmall.md) widget and scales it to fit available space. For more information about supporting StandBy and CarPlay, refer to [`Adding StandBy and CarPlay support to your widget`](adding-standby-and-carplay-support-to-your-widget.md).

##### Indicate That a Widget Might Not Fit a Specific Context

By default, the system suggests widgets in many contexts, and people can choose widgets in the widget gallery to personalize their system experience. However, a widget might not be a good fit for a specific context. For example, a widget that relies on high-resolution photos and background colors for its functionality may not work well on the Lock Screen, where the system applies a vibrant treatment to the widget. To indicate that a widget doesn’t work well in a specific context, use [`disfavoredLocations(_:for:)`](https://developer.apple.com/documentation/SwiftUI/WidgetConfiguration/disfavoredLocations(_:for:)) and provide the applicable [`WidgetLocation`](widgetlocation.md). As a result, the widget appears in the widget gallery’s “Other” section for the disfavored location.

##### Verify Font Sizes in Macos

When people place an iPhone widget on a Mac desktop, the system renders it using iOS font metrics. However, a native Mac app’s widgets use macOS font sizing. If you’re sharing code across your iOS and macOS targets in your Xcode project, make sure to verify font sizing in macOS and adjust it for macOS as needed.

## See Also

- [Creating a widget extension](creating-a-widget-extension.md)
  Display your app’s content in a convenient, informative widget on various devices.
- [Developing a WidgetKit strategy](developing-a-widgetkit-strategy.md)
  Explore features, tasks, related frameworks, and constraints as you make a plan to implement widgets, controls, watch complications, and Live Activities.
- [Emoji Rangers: Supporting Live Activities, interactivity, and animations](emoji-rangers-supporting-live-activities-interactivity-and-animations.md)
  Offer Live Activities, controls, animate data updates, and add interactivity to widgets.
- [protocol Widget](../SwiftUI/Widget.md)
  The configuration and content of a widget to display on the Home screen or in Notification Center.
- [enum WidgetFamily](widgetfamily.md)
  Values that define the widget’s size and shape.
- [struct StaticConfiguration](staticconfiguration.md)
  An object describing the content of a widget that has no user-configurable options.


---

*[View on Apple Developer](https://developer.apple.com/documentation/widgetkit/preparing-widgets-for-additional-contexts-and-appearances)*