# move(to:withCaretRect:trackingCaret:)

**Framework**: UIKit  
**Kind**: method

Moves the loupe to the specified point in the session’s associated view.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- tvOS 17.0+

## Declaration

```swift
@MainActor
func move(to point: CGPoint, withCaretRect caretRect: CGRect, trackingCaret tracksCaret: Bool)
```

## Mentions

- [Adopting system selection UI in custom text views](adopting-system-selection-ui-in-custom-text-views.md)

#### Discussion

Call this method repeatedly from a gesture recognizer when the touch location changes.

## Parameters

- `point`: The new location you want to magnify with the loupe. When creating the loupe with a gesture recognizer, specify the location of the gesture.
- `caretRect`: The current position of the caret handle. Specify   if the view doesn’t contain a selection or the caret isn’t visible.
- `tracksCaret`:   if you want the loupe to track the movements of the caret. If you specify  , provide a valid rectangle in the   parameter. Specify   to continue tracking the location of touch events.

## See Also

- [func invalidate()](uitextloupesession/invalidate.md)
  Hides the loupe and cleans up any session-related state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextloupesession/move(to:withcaretrect:trackingcaret:))*