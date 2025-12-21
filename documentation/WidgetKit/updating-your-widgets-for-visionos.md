# Updating your widgets for visionOS

**Framework**: WidgetKit

Choose widget styles specific to visionOS, support recessed and elevated appearances, and add proximity awareness to your widget.

#### Overview

On Apple Vision Pro, people add widgets from your visionOS or compatible iPhone and iPad app to a room and permanently pin them to horizontal or vertical surfaces.

Widgets in visionOS work like widgets on other platforms, they:

- Have interaction, animation, networking, and location access capabilities
- Update their content with timelines and WidgetKit push notifications you send with the Apple Push Notification service (APNs)

visionOS supports all system family widget sizes, from [`WidgetFamily.systemSmall`](widgetfamily/systemsmall.md) to [`WidgetFamily.systemExtraLarge`](widgetfamily/systemextralarge.md) and [`WidgetFamily.systemExtraLargePortrait`](widgetfamily/systemextralargeportrait.md). However, supporting extra-large widgets in visionOS depends on whether your app is a visionOS app or a compatible iOS or iPadOS app:

- To add an extra-large widget to your visionOS app, use [`WidgetFamily.systemExtraLargePortrait`](widgetfamily/systemextralargeportrait.md).
- To add an extra-large visionOS widget to a compatible iOS and iPadOS app, use the `systemExtraLarge` widget family. The extra-large widget appears in a portrait orientation, similar to the [`WidgetFamily.systemExtraLargePortrait`](widgetfamily/systemextralargeportrait.md) widget of a visionOS app.

If your iPhone or iPad app already includes widgets and you enable visionOS compatibility mode, they automatically adopt new spatial and visual treatments for visionOS. However, widgets in visionOS are three-dimensional objects, and have additional capabilities that help them feel at home in a person’s surroundings, keeping information from your app ambient, relevant, and close by.

> **Note**: If you’re new to creating widgets or using WidgetKit, refer to [`Developing a WidgetKit strategy`](developing-a-widgetkit-strategy.md) and [`Creating a widget extension`](creating-a-widget-extension.md).

For design guidance, refer to [`Human Interface Guidelines > Widgets`](https://developer.apple.comhttps://developer.apple.com/design/human-interface-guidelines/components/system-experiences/widgets).

##### Support Recessed and Elevated Mounting Styles

People add widgets to a room and pin them to a surface. By default, widgets in visionOS sit directly on top of horizontal and vertical surfaces, taking on an elevated look. On horizontal surfaces, widgets always appear with this look. Additionally, widgets can appear recessed, directly embedded into a vertical surface like a wall. If one of these styles isn’t a good fit for your widget, use the [`supportedMountingStyles(_:)`](https://developer.apple.com/documentation/SwiftUI/WidgetConfiguration/supportedMountingStyles(_:)) view modifier to specify the [`WidgetMountingStyle`](WidgetMountingStyle.md) your visionOS or iOS and iPadOS widget supports:

- By default, widgets support both [`elevated`](WidgetMountingStyle/elevated.md) and [`recessed`](WidgetMountingStyle/recessed.md) mounting styles.
- If your widget only supports the [`recessed`](WidgetMountingStyle/recessed.md) mounting style, people can’t place it on horizontal surfaces.

For example, a widget might use a photo to create the illusion of a window into another part of the world. This widget would rely on a sense of depth and alignment that doesn’t make sense on a horizontal surface, and does not support the `elevated` mounting style as shown in the following example:

```swift
struct WeatherWidget: Widget {
    var body: some WidgetConfiguration {
        StaticConfiguration(
            // ...
        ) { entry in
            WeatherWidgetView(entry: entry)
        }
        .configurationDisplayName("Weather widget")
        .supportedMountingStyles([.recessed])
    }
}
```

##### Support Visionos Rendering Styles and Extra Large Widgets

By default, widgets in visionOS appear under a glass texture. For widgets that your visionOS app offers, choose between the default glass texture or an alternative paper texture that gives the widget a poster-like look. To specify your widget’s texture, use the [`widgetTexture(_:)`](https://developer.apple.com/documentation/SwiftUI/WidgetConfiguration/widgetTexture(_:)) view modifier and choose between [`glass`](widgettexture/glass.md) and [`paper`](widgettexture/paper.md).

Especially if your widgets uses a poster-like look, consider offering a [`WidgetFamily.systemExtraLargePortrait`](widgetfamily/systemextralargeportrait.md) or [`WidgetFamily.systemExtraLarge`](widgetfamily/systemextralarge.md) widget by including it in the array of [`supportedFamilies(_:)`](https://developer.apple.com/documentation/SwiftUI/WidgetConfiguration/supportedFamilies(_:)) as shown in the following example:

```swift
struct CaffeineTrackerWidget: Widget {
    var body: some WidgetConfiguration {
        StaticConfiguration(
            // ...
        ) { entry in
            CaffeineTrackerWidgetView(entry: entry)
        }
        .configurationDisplayName("Caffeine Tracker")
        .supportedMountingStyles([.elevated])
        .widgetTexture(.paper)
        .supportedFamilies([.systemExtraLarge])
    }
}
```

##### Support Full Color and Accented Rendering Modes

By default, widgets in visionOS appear in [`fullColor`](widgetrenderingmode/fullcolor.md), but people can also customize their widgets with a color theme that renders them in the [`accented`](widgetrenderingmode/accented.md) mode, removing the background, and replacing it with a solid color that complements the selected color theme. Supporting the accented rendering mode in visionOS works the same as on other platforms. For more information , refer to [`Preparing widgets for additional platforms, contexts, and appearances`](preparing-widgets-for-additional-contexts-and-appearances.md) and [`Optimizing your widget for accented rendering mode and Liquid Glass`](optimizing-your-widget-for-accented-rendering-mode-and-liquid-glass.md).

##### Add Proximity Awareness to Your Widget

While widgets in visionOS share a lot of similarities with widgets on other platforms, a key difference is the distance between a person and the widgets. People might look at your widget from a close distance or from further away. For example, someone might place a small widget on a desk and view it while sitting at the desk or from across the room. Widgets in visionOS behave like physical objects, appearing smaller as the distance between them and the person increases.

To make sure your widget remains glanceable, respond to a person’s proximity and update its layout accordingly:

1. Use the [`levelOfDetail`](https://developer.apple.com/documentation/SwiftUI/EnvironmentValues/levelOfDetail) environment variable to detect a person’s proximity.
2. Update your views to display a [`default`](levelofdetail/default.md) level of detail when a person is close to the widget.
3. Display a [`simplified`](levelofdetail/simplified.md) layout with fewer, larger elements that ensures the widget remains legible from a distance.

When a person’s distance to a widget changes to above or below the threshold for a simplified layout, the system animates the layout changes, similar to how it animates data changes between timeline entries.

This example shows how a view might respond to the level of detail environment variable by adjusting the text size:

```swift
struct TotalCaffeineView: View {
    @Environment(\.levelOfDetail) var levelOfDetail
    
    // ...

    var body: some View {
        VStack {
            Text("Total Caffeine")
                .font(.caption)
            Text(totalCaffeine.formatted())
                .font(caffeineFont)
       }
    }

    var caffeineFont: Font {
        if levelOfDetail == .simplified {
            .largeTitle
        } else {
            .title
        }
    }
}
```

## See Also

- [func widgetTexture(WidgetTexture) -> some WidgetConfiguration](../SwiftUI/WidgetConfiguration/widgetTexture(_:).md)
  Specifies the widget texture for this widget.
- [struct WidgetTexture](widgettexture.md)
  Values that define the texture of the widget’s coating layer.
- [func supportedMountingStyles([WidgetMountingStyle]) -> some WidgetConfiguration](../SwiftUI/WidgetConfiguration/supportedMountingStyles(_:).md)
  Specifies the mounting style for this widget.
- [struct WidgetMountingStyle](widgetmountingstyle.md)
  Values that define the widget’s supported mounting style.
- [struct LevelOfDetail](levelofdetail.md)
  The level of detail the view is recommended to have.


---

*[View on Apple Developer](https://developer.apple.com/documentation/widgetkit/updating-your-widgets-for-visionos)*