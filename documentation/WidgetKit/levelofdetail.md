# LevelOfDetail

**Framework**: WidgetKit  
**Kind**: struct

The level of detail the view is recommended to have.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst ?+
- visionOS 26.0+

## Declaration

```swift
struct LevelOfDetail
```

#### Overview

The system can update the levelOfDetail value based on user proximity or other system specific factors and allow content customization adapting to show different levels of details.

> **Note**: The `levelOfDetail` can be determined by different factors depending on the platforms. On visionOS, it would be user proximity. On all non-visionOS platforms this will always be `default` LevelOfDetail

## Topics

### Type Properties
- [static let `default`: LevelOfDetail](levelofdetail/default.md)
  The default level of details.
- [static let simplified: LevelOfDetail](levelofdetail/simplified.md)
  The level of detail should be simplified.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)

## See Also

- [Updating your widgets for visionOS](updating-your-widgets-for-visionos.md)
  Choose widget styles specific to visionOS, support recessed and elevated appearances, and add proximity awareness to your widget.
- [func widgetTexture(WidgetTexture) -> some WidgetConfiguration](../SwiftUI/WidgetConfiguration/widgetTexture(_:).md)
  Specifies the widget texture for this widget.
- [struct WidgetTexture](widgettexture.md)
  Values that define the texture of the widget’s coating layer.
- [func supportedMountingStyles([WidgetMountingStyle]) -> some WidgetConfiguration](../SwiftUI/WidgetConfiguration/supportedMountingStyles(_:).md)
  Specifies the mounting style for this widget.
- [struct WidgetMountingStyle](widgetmountingstyle.md)
  Values that define the widget’s supported mounting style.


---

*[View on Apple Developer](https://developer.apple.com/documentation/widgetkit/levelofdetail)*