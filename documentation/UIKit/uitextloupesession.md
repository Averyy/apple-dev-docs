# UITextLoupeSession

**Framework**: UIKit  
**Kind**: class

An object that manages the presentation of the system magnifier at the location you specify.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- tvOS 17.0+

## Declaration

```swift
@MainActor
class UITextLoupeSession
```

## Mentions

- [Adopting system selection UI in custom text views](adopting-system-selection-ui-in-custom-text-views.md)

#### Overview

A [`UITextLoupeSession`](uitextloupesession.md) object programmatically displays the system loupe in your view. You might display this view to allow someone to magnify your view’s content. Typically, you display the loupe from a [`UIPanGestureRecognizer`](uipangesturerecognizer.md) when someone interacts with your view. As the location in the gesture recognizer changes, use the loupe session object to update the position of the loupe.

## Topics

### Creating the loupe session
- [class func begin(at: CGPoint, fromSelectionWidgetView: UIView?, in: UIView) -> Self?](uitextloupesession/begin(at:fromselectionwidgetview:in:).md)
  Creates a new loupe session and displays the loupe at the specified location in your view.
### Updating the loupe during the session
- [func move(to: CGPoint, withCaretRect: CGRect, trackingCaret: Bool)](uitextloupesession/move(to:withcaretrect:trackingcaret:).md)
  Moves the loupe to the specified point in the session’s associated view.
- [func invalidate()](uitextloupesession/invalidate.md)
  Hides the loupe and cleans up any session-related state.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [Adopting system selection UI in custom text views](adopting-system-selection-ui-in-custom-text-views.md)
  Incorporate the system text-selection experience into your custom text UI in UIKit.
- [class UITextSelectionDisplayInteraction](uitextselectiondisplayinteraction.md)
  An object that provides the system UI for displaying text selection.
- [protocol UITextSelectionHighlightView](uitextselectionhighlightview.md)
  An interface you use to provide a custom highlight UI behind the selected text.
- [protocol UITextSelectionHandleView](uitextselectionhandleview.md)
  An interface you use to draw custom the selection handles for ranges of text.
- [protocol UITextCursorView](uitextcursorview.md)
  An interface you use to draw the insertion point in a piece of text.
- [class UIStandardTextCursorView](uistandardtextcursorview.md)
  A view that draws the standard system insertion point in a piece of text.
- [class UITextCursorDropPositionAnimator](uitextcursordroppositionanimator.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextloupesession)*