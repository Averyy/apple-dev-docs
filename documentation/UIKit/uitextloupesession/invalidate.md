# invalidate()

**Framework**: UIKit  
**Kind**: method

Hides the loupe and cleans up any session-related state.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- tvOS 17.0+

## Declaration

```swift
@MainActor
func invalidate()
```

## Mentions

- [Adopting system selection UI in custom text views](adopting-system-selection-ui-in-custom-text-views.md)

#### Discussion

Call this method when you’re ready to hide the loupe. After calling this method, you can remove your reference to the session.

## See Also

- [func move(to: CGPoint, withCaretRect: CGRect, trackingCaret: Bool)](uitextloupesession/move(to:withcaretrect:trackingcaret:).md)
  Moves the loupe to the specified point in the session’s associated view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextloupesession/invalidate())*