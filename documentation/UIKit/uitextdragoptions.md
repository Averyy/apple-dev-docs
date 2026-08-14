# UITextDragOptions

**Framework**: UIKit  
**Kind**: struct

A set of options that determine the behavior of a draggable text view.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
struct UITextDragOptions
```

## Topics

### Text drag options
- [static var stripTextColorFromPreviews: UITextDragOptions](uitextdragoptions/striptextcolorfrompreviews.md)
  Strips the foreground and background colors for a system-provided text drag preview.
### Initializers
- [init(rawValue: Int)](uitextdragoptions/init(rawvalue:).md)
  Creates a text-drag options structure with the specified raw value.

## Relationships

### Conforms To
- [BitwiseCopyable](../swift/bitwisecopyable.md)
- [Equatable](../swift/equatable.md)
- [ExpressibleByArrayLiteral](../swift/expressiblebyarrayliteral.md)
- [OptionSet](../swift/optionset.md)
- [RawRepresentable](../swift/rawrepresentable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)
- [SetAlgebra](../swift/setalgebra.md)

## See Also

- [protocol UITextDragDelegate](uitextdragdelegate.md)
  The interface for customizing the behavior of a drag activity for a text view.
- [protocol UITextDropDelegate](uitextdropdelegate.md)
  The interface for configuring a text view’s drop behavior.
- [protocol UITextDraggable](uitextdraggable.md)
  The interface that determines if a text view is a drag source.
- [protocol UITextDroppable](uitextdroppable.md)
  The interface that determines if a text view is a drop destination.
- [enum UITextDropEditability](uitextdropeditability.md)
  The text-drop editability styles for noneditable text views.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextdragoptions)*