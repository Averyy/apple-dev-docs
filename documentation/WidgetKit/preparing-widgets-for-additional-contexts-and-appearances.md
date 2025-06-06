# Preparing widgets for additional platforms, contexts, and appearances

**Framework**: Widgetkit

Create widgets that support additional platforms and adapt to their context.

#### Overview

Widgets change their appearance to best fit their context. For example, widgets on the Home Screen, Today View, or the macOS Notification Center use full colors and rich images to represent your brand and encourage people to feature your widget on their devices. In contrast, Lock Screen widgets and WidgetKit complications use more restrained colors because they’re smaller, always visible, and support tinted modes for each platform. Since all widgets appear in more than one context, make sure your widgets and their SwiftUI views support all applicable rendering modes.

WidgetKit uses three different rendering modes:

The following table shows the rendering modes for each widget you need to support:

| Widget size | [`fullColor`](widgetrenderingmode/fullcolor.md) | [`accented`](widgetrenderingmode/accented.md) | [`vibrant`](widgetrenderingmode/vibrant.md) |
| --- | --- | --- | --- |
| [`WidgetFamily.systemSmall`](widgetfamily/systemsmall.md) | Yes | Yes | Yes |
| [`WidgetFamily.systemMedium`](widgetfamily/systemmedium.md) | Yes | Yes | Yes |
| [`WidgetFamily.systemLarge`](widgetfamily/systemlarge.md) | Yes | Yes | Yes |
| [`WidgetFamily.systemExtraLarge`](widgetfamily/systemextralarge.md) | Yes | Yes | Yes |
| [`WidgetFamily.accessoryCircular`](widgetfamily/accessorycircular.md) | No | Yes | Yes |
| [`WidgetFamily.accessoryCorner`](widgetfamily/accessorycorner.md) | No | Yes | Yes |
| [`WidgetFamily.accessoryRectangular`](widgetfamily/accessoryrectangular.md) | Yes | Yes | Yes |
| [`WidgetFamily.accessoryInline`](widgetfamily/accessoryinline.md) | No | Yes | Yes |

> **Note**: For design guidance, see [`Human Interface Guidelines > Complications`](https://developer.apple.comhttps://developer.apple.com/design/human-interface-guidelines/complications) and [`Human Interface Guidelines > Widgets`](https://developer.apple.comhttps://developer.apple.com/design/human-interface-guidelines/widgets).

In your code, read the [`widgetRenderingMode`](https://developer.apple.com/documentation/SwiftUI/EnvironmentValues/widgetRenderingMode) environment variable to create SwiftUI views for each applicable rendering mode, as shown in the following example:

```swift
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
           // Create views for Lock Screen widgets on iPhone and iPad, and for the receded appearance on the Mac desktop.
   }
}
```

##### Support Always on

If you create accessory widgets and WidgetKit complications, make sure to use SwiftUI’s [`isLuminanceReduced`](https://developer.apple.com/documentation/SwiftUI/EnvironmentValues/isLuminanceReduced) environment variable to detect Always On and color your views to look great with reduced luminance. For design guidance, see [`Human Interface Guidelines > Always On`](https://developer.apple.comhttps://developer.apple.com/design/human-interface-guidelines/always-on) and [`Human Interface Guidelines > Widgets`](https://developer.apple.comhttps://developer.apple.com/design/human-interface-guidelines/widgets).

##### Update Your Small Widget to Support Standby

On iPhone in StandBy, the Lock Screen shows two widgets side by side on a dark background. WidgetKit uses your [`WidgetFamily.systemSmall`](widgetfamily/systemsmall.md) widget and scales it to fit one half of the screen. To support this appearance:

- Make the widget’s background removable with a container background, as described below.
- Update the widget’s layout to take advantage of the larger appearance and smaller content margins and to make the widget easier to read from a larger distance.

##### Display the Correct Widget Background for Each Context

Widgets appear differently based on their context, including their background view, for example:

- In the [`vibrant`](widgetrenderingmode/vibrant.md) appearance, the system removes the background of your widget or renders it with semi-translucent appearance.
- In StandBy on iPhone, the system removes the background of your widget.
- On the Mac desktop, the system removes the background of your widget.

To make sure your widget appears correctly, mark your background views as removable for the following widget sizes:

- [`WidgetFamily.systemSmall`](widgetfamily/systemsmall.md)
- [`WidgetFamily.systemMedium`](widgetfamily/systemmedium.md)
- [`WidgetFamily.systemLarge`](widgetfamily/systemlarge.md)
- [`WidgetFamily.systemExtraLarge`](widgetfamily/systemextralarge.md)
- [`WidgetFamily.accessoryRectangular`](widgetfamily/accessoryrectangular.md)

> ❗ **Important**: If a widget doesn’t support removable background views or doesn’t explicitly mark a background as nonremovable, the system displays a warning message that overlays the widget during development with Xcode.

To mark your background views as removable:

1. Add the [`containerBackground(_:for:)`](https://developer.apple.com/documentation/SwiftUI/View/containerBackground(_:for:)) modifier to your background views to define the background appearance of your widget and tell WidgetKit that it can remove the view where applicable.
2. Move code that declares any background color or views inside the `containerBackground(for:)` view modifier and pass [`widget`](https://developer.apple.com/documentation/SwiftUI/ContainerBackgroundPlacement/widget) to it. This makes sure WidgetKit automatically removes the background as needed.

The following code snippet from the [`Emoji Rangers: Supporting Live Activities, interactivity, and animations`](emoji-rangers-supporting-live-activities-interactivity-and-animations.md) sample code project defines a `gameBackground` color for the widget’s container background to make sure WidgetKit renders it with or without the background color as applicable.

```swift
var body: some View {
    switch family {
    // Logic for additional widget sizes.
    case .accessoryRectangular:
        HStack(alignment: .center, spacing: 0) {
            VStack(alignment: .leading) {
                Text(entry.hero.name)
                    .font(.headline)
                    .widgetAccentable()
                Text("Level \(entry.hero.level)")
                Text(entry.hero.fullHealthDate, style: .timer)
            }.frame(maxWidth: .infinity, alignment: .leading)
            Avatar(hero: entry.hero, includeBackground: false)
        }
        .containerBackground(for: .widget) {
            Color.gameBackground
        }
		// Logic for additional widget sizes.
}
```

Marking background views as removable by defining a background container allows you to use the same layout and views for your widget across contexts. For example, if you support the rectangular accessory widget size as shown in the code snippet above, WidgetKit renders it with a rich, full-color background in the Smart Stack on Apple Watch and without a background as a watch complication or on the Lock Screen of iPhone and iPad.

> **Note**: On Apple Watch, rectangular widgets in the Smart Stack use a default dark material background. By adding a container background, the widget renders with a background that visually ties it to your app and makes it more recognizable to people.

To detect whether a widget appears with or without a background, use the [`showsWidgetContainerBackground`](https://developer.apple.com/documentation/SwiftUI/EnvironmentValues/showsWidgetContainerBackground) environment variable.

##### Explicitly Opt Out of Background Removal

Some widgets don’t have distinct foreground content, and background removal can negatively impact their functionality. For example, a widget might display a photo or map that takes up the entirety of the widget’s bounds. Removing the photo or map removes the functionality of the widget. If this case applies to your widget, set the [`containerBackgroundRemovable(_:)`](https://developer.apple.com/documentation/SwiftUI/WidgetConfiguration/containerBackgroundRemovable(_:)) modifier to `false` for your widget configuration.

> ❗ **Important**: Marking a background as nonremovable excludes your widget from the widget gallery in contexts that require a removable background; for example, on the iPad Lock Screen and in StandBy.

##### Set the Background Color of Accessory Widgets

Depending on your accessory widget or complication, you may need to set a consistent background for your accessory widget. Use [`AccessoryWidgetBackground`](accessorywidgetbackground.md) to draw a consistent background for your widget, as shown in the following example. It creates a view that’s similar to the circular Lock Screen widget that the Calendar app offers:

```swift
ZStack {
     AccessoryWidgetBackground()
     VStack {
        Text(“MON”)
        Text(“6”)
         .font(.title)
    }
}
```

##### Indicate That a Widget Might Not Fit a Specific Context

By default, the system suggests widgets in many contexts, and people can choose widgets in the widget gallery to personalize their system experience. However, a widget might not a good fit for a specific context. For example, a widget that relies on high-resolution photos and background colors for its functionality may not work well on the Lock Screen, where the system applies a vibrant treatment to the widget.  To indicate that a widget doesn’t work well in a specific context, use [`disfavoredLocations(_:for:)`](https://developer.apple.com/documentation/SwiftUI/WidgetConfiguration/disfavoredLocations(_:for:)) and provide the applicable [`WidgetLocation`](widgetlocation.md). As a result, the widget appears in the widget gallery’s “Other” section for the disfavored location.

##### Verify Font Sizes in Macos

When people place an iPhone widget on the Mac desktop, the system renders it using iOS font metrics. However, a native Mac app’s widgets use macOS font sizing. If you’re sharing code across your iOS and macOS targets in your Xcode project, make sure to verify font sizing in macOS and adjust it for macOS as needed.

## See Also

- [Creating views for widgets, Live Activities, and watch complications](creating-views-for-widgets-live-activities-and-watch-complications.md)
  Implement glanceable views with WidgetKit and SwiftUI.
- [SwiftUI views for widgets](swiftui-views.md)
  Present your app’s content in widgets with SwiftUI views.
- [Introducing SwiftUI](https://developer.apple.com/tutorials/SwiftUI)
  SwiftUI is a modern way to declare user interfaces for any Apple platform. Create beautiful, dynamic apps faster than ever before.
- [struct AccessoryWidgetBackground](accessorywidgetbackground.md)
  An adaptive background view that provides a standard appearance based on the the widget’s environment.
- [struct WidgetLocation](widgetlocation.md)
  Values that indicate different widget locations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/WidgetKit/preparing-widgets-for-additional-contexts-and-appearances)*