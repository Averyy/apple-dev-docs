# fullColor

**Framework**: Widgetkit  
**Kind**: property

The system renders the widget in full color.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- watchOS 9.0+

## Declaration

```swift
static let fullColor: WidgetRenderingMode
```

## Mentions

- [Developing a WidgetKit strategy](developing-a-widgetkit-strategy.md)
- [Preparing widgets for additional platforms, contexts, and appearances](preparing-widgets-for-additional-contexts-and-appearances.md)

#### Discussion

In this mode, the system doesn’t alter or filter the widget’s colors.

The system displays full-color widget-based complications on some watch faces, such as the Infograph face, on the Home Screen or Today View in iOS or iPadOS, and in Notification Center on macOS.

> **Note**: The Infograph face only uses full-color rendering when the user sets the face to multicolor. If the user selects an accent color, the system uses [`accented`](widgetrenderingmode/accented.md) instead.

The Infograph face only uses full-color rendering when the user sets the face to multicolor. If the user selects an accent color, the system uses [`accented`](widgetrenderingmode/accented.md) instead.

## See Also

- [static let accented: WidgetRenderingMode](widgetrenderingmode/accented.md)
  The system divides the widget’s view hierarchy into an accent group and a default group, applying a different color to each group.
- [static let vibrant: WidgetRenderingMode](widgetrenderingmode/vibrant.md)
  The system desaturates the widget, making a monochrome version that it uses to create an adaptive, vibrant effect.


---

*[View on Apple Developer](https://developer.apple.com/documentation/widgetkit/widgetrenderingmode/fullcolor)*