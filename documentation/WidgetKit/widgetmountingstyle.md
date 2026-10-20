# WidgetMountingStyle

**Framework**: WidgetKit  
**Kind**: struct  
**Role**: Structure

Values that define the widget’s supported mounting style.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- visionOS 26.0+

## Declaration

```swift
struct WidgetMountingStyle
```

## Topics

### Type Properties
- [static let elevated: WidgetMountingStyle](./widgetmountingstyle/elevated.md)
  Mounting style surrounding the widget with a composite material
- [static let recessed: WidgetMountingStyle](./widgetmountingstyle/recessed.md)
  Mounting style where a widget is displayed within a recessed portal

## Relationships

### Conforms To
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### visionOS widgets
- [Updating your widgets for visionOS](./updating-your-widgets-for-visionos.md)
  Choose widget styles specific to visionOS, support recessed and elevated appearances, and add proximity awareness to your widget.
- [func widgetTexture(WidgetTexture) -> some WidgetConfiguration
](../SwiftUI/widgetconfiguration/widgettexture%28_%29.md)
  Specifies the widget texture for this widget.
- [struct WidgetTexture](./widgettexture.md)
  Values that define the texture of the widget’s coating layer.
- [func supportedMountingStyles([WidgetMountingStyle]) -> some WidgetConfiguration
](../SwiftUI/widgetconfiguration/supportedmountingstyles%28_%29.md)
  Specifies the mounting style for this widget.
- [struct LevelOfDetail](./levelofdetail.md)
  The level of detail the view is recommended to have.


---

*[View on Apple Developer](https://developer.apple.com/documentation/widgetkit/widgetmountingstyle)*