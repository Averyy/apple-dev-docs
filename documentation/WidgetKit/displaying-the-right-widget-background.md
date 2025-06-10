# Displaying the right widget background

**Framework**: WidgetKit

Group your widget’s background views and mark them as removable to ensure your widget appears correctly for each context and platform.

#### Overview

Widgets appear differently based on their context, including their background view, for example:

- In the [`vibrant`](widgetrenderingmode/vibrant.md) appearance, the system removes the background of your widget or renders it with semi-translucent appearance.
- In StandBy on iPhone, the system removes the background of your widget.

To make sure your widget appears correctly, mark your background views as removable for every widget size.

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

Marking background views as removable by defining a background container so you can use the same layout and views for your widget across contexts. For example, if you support the rectangular accessory widget size as shown in the code snippet above, WidgetKit renders it with a rich, full-color background in the Smart Stack on Apple Watch and without a background as a watch complication or on the Lock Screen of iPhone and iPad.

On Apple Watch, rectangular widgets in the Smart Stack use a default dark material background. By adding a container background, the widget renders with a background that visually ties it to your app and makes it more recognizable to people.

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

## See Also

- [Preparing widgets for additional platforms, contexts, and appearances](preparing-widgets-for-additional-contexts-and-appearances.md)
  Create widgets that support additional platforms and adapt to their context.
- [Optimizing your widget for accented rendering mode and Liquid Glass](optimizing-your-widget-for-accented-rendering-mode-and-liquid-glass.md)
  Make your widget feel at home on Apple platforms and Liquid Glass by using accented rendering mode.
- [Adding StandBy and CarPlay support to your widget](adding-standby-and-carplay-support-to-your-widget.md)
  Ensure that your small system family widget works well in StandBy and CarPlay.
- [Creating views for widgets, Live Activities, and watch complications](creating-views-for-widgets-live-activities-and-watch-complications.md)
  Implement glanceable views with WidgetKit and SwiftUI.
- [SwiftUI views for widgets](swiftui-views.md)
  Present your app’s content in widgets with SwiftUI views.
- [Introducing SwiftUI](https://developer.apple.com/tutorials/SwiftUI)
  SwiftUI is a modern way to declare user interfaces for any Apple platform. Create beautiful, dynamic apps faster than ever before.
- [struct WidgetRenderingMode](widgetrenderingmode.md)
  Constants that indicate the rendering mode for a widget.
- [struct WidgetAccentedRenderingMode](widgetaccentedrenderingmode.md)
  Constants that indicate the rendering mode for an `Image` in when displayed in a widget in [`accented`](widgetrenderingmode/accented.md) mode.
- [struct AccessoryWidgetBackground](accessorywidgetbackground.md)
  An adaptive background view that provides a standard appearance based on the the widget’s environment.
- [struct WidgetLocation](widgetlocation.md)
  Values that indicate different widget locations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/widgetkit/displaying-the-right-widget-background)*