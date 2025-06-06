# UITextSelectionHighlightView

**Framework**: UIKit  
**Kind**: protocol

An interface you use to provide a custom highlight UI behind the selected text.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
protocol UITextSelectionHighlightView : UICoordinateSpace
```

#### Overview

Adopt the [`UITextSelectionHighlightView`](uitextselectionhighlightview.md) protocol in a custom view you use to draw the highlight behind text in one of your text views. Use your custom view in conjunction with a [`UITextSelectionDisplayInteraction`](uitextselectiondisplayinteraction.md) object to apply your custom selection UI to one of your text views. This protocol provides the rectangles for your view to fill with the highlight color and appearance. Use [`CALayer`](https://developer.apple.com/documentation/QuartzCore/CALayer) objects or your view’s [`draw(_:)`](uiview/draw(_:).md) method to draw these rectangles.

After adopting this protocol in your custom view, assign your view to the [`highlightView`](uitextselectiondisplayinteraction/highlightview.md) property of the interaction object you attached to your text view.

## Topics

### Getting the rectangles to draw
- [var selectionRects: [UITextSelectionRect]](uitextselectionhighlightview/selectionrects.md)
  The rectangles to draw with the selection highlight.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [UICoordinateSpace](uicoordinatespace.md)

## See Also

- [Adopting system selection UI in custom text views](adopting-system-selection-ui-in-custom-text-views.md)
  Incorporate the system text-selection experience into your custom text UI in UIKit.
- [class UITextSelectionDisplayInteraction](uitextselectiondisplayinteraction.md)
  An object that provides the system UI for displaying text selection.
- [protocol UITextSelectionHandleView](uitextselectionhandleview.md)
  An interface you use to draw custom the selection handles for ranges of text.
- [protocol UITextCursorView](uitextcursorview.md)
  An interface you use to draw the insertion point in a piece of text.
- [class UIStandardTextCursorView](uistandardtextcursorview.md)
  A view that draws the standard system insertion point in a piece of text.
- [class UITextCursorDropPositionAnimator](uitextcursordroppositionanimator.md)
- [class UITextLoupeSession](uitextloupesession.md)
  An object that manages the presentation of the system magnifier at the location you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextselectionhighlightview)*