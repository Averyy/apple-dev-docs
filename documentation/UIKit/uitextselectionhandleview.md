# UITextSelectionHandleView

**Framework**: UIKit  
**Kind**: protocol

An interface you use to draw custom the selection handles for ranges of text.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
protocol UITextSelectionHandleView : UICoordinateSpace
```

#### Overview

Adopt the [`UITextSelectionHandleView`](uitextselectionhandleview.md) protocol in a custom view you use to draw text-selection handles in one of your text views. Use your custom view in conjunction with a [`UITextSelectionDisplayInteraction`](uitextselectiondisplayinteraction.md) object to apply your custom selection UI to one of your text views. This protocol provides the preferred frame for the selection handle, and you provide details about the handle back to the system. Use [`CALayer`](https://developer.apple.com/documentation/QuartzCore/CALayer) objects or your view’s [`draw(_:)`](uiview/draw(_:).md) method to draw the handles.

After adopting this protocol in your custom view, create exactly two instances and assign them to the [`handleViews`](uitextselectiondisplayinteraction/handleviews.md) property of the interaction object you attached to your text view. Configure one instance as the leading selection handle, and configure the other instance as the trailing selection handle.

## Topics

### Providing the preferred frame rectangle
- [func preferredFrame(for: CGRect) -> CGRect](uitextselectionhandleview/preferredframe(for:).md)
### Specifying the handle details
- [var direction: NSDirectionalRectEdge](uitextselectionhandleview/direction.md)
  The orientation of the selection handle.
- [var customShape: UIBezierPath?](uitextselectionhandleview/customshape.md)
  The custom shape to draw for the stem of the selection handle.
- [var isVertical: Bool](uitextselectionhandleview/isvertical.md)

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [UICoordinateSpace](uicoordinatespace.md)

## See Also

- [Adopting system selection UI in custom text views](adopting-system-selection-ui-in-custom-text-views.md)
  Incorporate the system text-selection experience into your custom text UI in UIKit.
- [class UITextSelectionDisplayInteraction](uitextselectiondisplayinteraction.md)
  An object that provides the system UI for displaying text selection.
- [protocol UITextSelectionHighlightView](uitextselectionhighlightview.md)
  An interface you use to provide a custom highlight UI behind the selected text.
- [protocol UITextCursorView](uitextcursorview.md)
  An interface you use to draw the insertion point in a piece of text.
- [class UIStandardTextCursorView](uistandardtextcursorview.md)
  A view that draws the standard system insertion point in a piece of text.
- [class UITextCursorDropPositionAnimator](uitextcursordroppositionanimator.md)
- [class UITextLoupeSession](uitextloupesession.md)
  An object that manages the presentation of the system magnifier at the location you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextselectionhandleview)*