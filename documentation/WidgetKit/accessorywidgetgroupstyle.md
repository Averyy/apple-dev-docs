# AccessoryWidgetGroupStyle

**Framework**: WidgetKit  
**Kind**: struct

The style for an accessory widget group view.

**Availability**:
- watchOS 11.0+

## Declaration

```swift
struct AccessoryWidgetGroupStyle
```

#### Discussion

Use the [`accessoryWidgetGroupStyle(_:)`](https://developer.apple.com/documentation/swiftui/view/accessorywidgetgroupstyle(_:)) modifier to set the desired style on an [`AccessoryWidgetGroup`](accessorywidgetgroup.md).

## Topics

### Getting styles
- [static let automatic: AccessoryWidgetGroupStyle](accessorywidgetgroupstyle/automatic.md)
  The default style that is set to circular.
- [static let circular: AccessoryWidgetGroupStyle](accessorywidgetgroupstyle/circular.md)
  Masks each content view with a circle.
- [static let roundedSquare: AccessoryWidgetGroupStyle](accessorywidgetgroupstyle/roundedsquare.md)
  Masks each content view with a rounded square.

## See Also

- [Creating accessory widgets and watch complications](creating-accessory-widgets-and-watch-complications.md)
  Support accessory widgets that appear on the Lock Screen and as complications on Apple Watch.
- [struct AccessoryWidgetGroup](accessorywidgetgroup.md)
  A view type that has a label at the top and three content views masked with a circle or rounded square.
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

*[View on Apple Developer](https://developer.apple.com/documentation/widgetkit/accessorywidgetgroupstyle)*