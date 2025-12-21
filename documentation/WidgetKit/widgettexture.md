# WidgetTexture

**Framework**: WidgetKit  
**Kind**: struct

Values that define the texture of the widget’s coating layer.

**Availability**:
- visionOS 26.0+

## Declaration

```swift
struct WidgetTexture
```

## Topics

### Textures
- [static let glass: WidgetTexture](widgettexture/glass.md)
  A reflective, clear glass-like texture for the widget’s coating layer.
- [static let paper: WidgetTexture](widgettexture/paper.md)
  A matte, paper-like texture for the widget’s coating layer.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [Updating your widgets for visionOS](updating-your-widgets-for-visionos.md)
  Choose widget styles specific to visionOS, support recessed and elevated appearances, and add proximity awareness to your widget.
- [func widgetTexture(WidgetTexture) -> some WidgetConfiguration](../SwiftUI/WidgetConfiguration/widgetTexture(_:).md)
  Specifies the widget texture for this widget.
- [func supportedMountingStyles([WidgetMountingStyle]) -> some WidgetConfiguration](../SwiftUI/WidgetConfiguration/supportedMountingStyles(_:).md)
  Specifies the mounting style for this widget.
- [struct WidgetMountingStyle](widgetmountingstyle.md)
  Values that define the widget’s supported mounting style.
- [struct LevelOfDetail](levelofdetail.md)
  The level of detail the view is recommended to have.


---

*[View on Apple Developer](https://developer.apple.com/documentation/widgetkit/widgettexture)*