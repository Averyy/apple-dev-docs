# AccessoryWidgetGroup

**Framework**: WidgetKit  
**Kind**: struct

A view type that has a label at the top and three content views masked with a circle or rounded square.

**Availability**:
- watchOS 11.0+

## Declaration

```swift
@MainActor
@preconcurrency struct AccessoryWidgetGroup<Label, Content> where Label : View, Content : View
```

#### Overview

You can use this view on `.accessoryRectangular` family widgets on watchOS to lay out three content views horizontally inside of a rectangular widget.

Example usage:

```swift
struct WeatherGroupView: View {
   var entry: Provider.Entry

   var body: some View {
       AccessoryWidgetGroup("Weather", systemImage: "cloud.sun.fill") {
           TemperatureWidgetView(entry.temperature)
           ConditionsWidgetView(entry.conditions)
           UVIndexWidgetView(entry.UVIndex)
       }
       .accessoryWidgetGroupStyle(.circular)
   }
}
```

The above example creates an `.accessoryRectangular` widget that has a `SwiftUI.Label` as its label and has three content views: temperature, conditions, and UVIndex; all of which are circular. If fewer than three views are provided, the content views are centered within the available space.

You can change the shape with which the content views are masked using the `.accessoryWidgetGroupStyle(_:)` view modifier.

## Topics

### Creating an accessory widget group
- [init(some StringProtocol, content: () -> Content)](accessorywidgetgroup/init(_:content:)-3ij0e.md)
  Creates an `AccessoryWidgetGroup` that generates its label from a string.
- [init(LocalizedStringResource, content: () -> Content)](accessorywidgetgroup/init(_:content:)-75rkg.md)
  Creates an `AccessoryWidgetGroup` that generates its label from a localized string resource.
- [init(LocalizedStringKey, content: () -> Content)](accessorywidgetgroup/init(_:content:)-nb0.md)
  Creates an `AccessoryWidgetGroup` that generates its label from a localized string key.
- [init(LocalizedStringResource, image: ImageResource, content: () -> Content)](accessorywidgetgroup/init(_:image:content:)-385rt.md)
  Creates an `AccessoryWidgetGroup` that generates its label from a localized string resource and image resource.
- [init(LocalizedStringKey, image: ImageResource, content: () -> Content)](accessorywidgetgroup/init(_:image:content:)-50iyk.md)
  Creates an `AccessoryWidgetGroup` that generates its label from a localized string key and image resource.
- [init(some StringProtocol, image: ImageResource, content: () -> Content)](accessorywidgetgroup/init(_:image:content:)-66iys.md)
  Creates an `AccessoryWidgetGroup` that generates its label from a string and image resource.
- [init(LocalizedStringResource, systemImage: String, content: () -> Content)](accessorywidgetgroup/init(_:systemimage:content:)-3mynu.md)
  Creates an `AccessoryWidgetGroup` that generates its label from a localized string resource and a system image name.
- [init(LocalizedStringKey, systemImage: String, content: () -> Content)](accessorywidgetgroup/init(_:systemimage:content:)-54h9w.md)
  Creates an `AccessoryWidgetGroup` that generates its label from a localized string key and a system image name.
- [init(some StringProtocol, systemImage: String, content: () -> Content)](accessorywidgetgroup/init(_:systemimage:content:)-7rnqc.md)
  Creates an `AccessoryWidgetGroup` that generates its label from a string and system image name.
- [init(label: () -> Label, content: () -> Content)](accessorywidgetgroup/init(label:content:).md)
  Creates an AccessoryWidgetGroup composed of a label and three circular or rounded square contents with equal spacing and vertical alignment.
### Styling an accessory widget group
- [struct AccessoryWidgetGroupStyle](accessorywidgetgroupstyle.md)
  The style for an accessory widget group view.

## Relationships

### Conforms To
- [View](../swiftui/view.md)

## See Also

- [Creating accessory widgets and watch complications](creating-accessory-widgets-and-watch-complications.md)
  Support accessory widgets that appear on the Lock Screen and as complications on Apple Watch.
- [struct AccessoryWidgetGroupStyle](accessorywidgetgroupstyle.md)
  The style for an accessory widget group view.
- [Migrating ClockKit complications to WidgetKit](converting-a-clockkit-app.md)
  Leverage WidgetKit’s API to create watchOS complications using SwiftUI.
- [func widgetCurvesContent(Bool) -> some View
](../swiftui/view/widgetcurvescontent(_:).md)
  Displays the widget’s content along a curve if the context allows it.
- [func widgetLabel(_:)](../swiftui/view/widgetlabel(_:).md)
  Returns a localized text label that displays additional content outside the accessory family widget’s main SwiftUI view.
- [func widgetLabel<Label>(label: () -> Label) -> some View
](../swiftui/view/widgetlabel(label:).md)
  Creates a label for displaying additional content outside an accessory family widget’s main SwiftUI view.
- [var showsWidgetLabel: Bool](../swiftui/environmentvalues/showswidgetlabel.md)
  A Boolean value that indicates whether an accessory family widget can display an accessory label.
- [func accessoryWidgetGroupStyle(AccessoryWidgetGroupStyle) -> some View
](../swiftui/view/accessorywidgetgroupstyle(_:).md)
  The view modifier that can be applied to `AccessoryWidgetGroup` to specify the shape the three content views will be masked with. The value of `style` is set to `.automatic`, which is `.circular` by default.


---

*[View on Apple Developer](https://developer.apple.com/documentation/widgetkit/accessorywidgetgroup)*