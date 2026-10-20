# invalidate()

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Hides the loupe and cleans up any session-related state.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- tvOS 17.0+

## Declaration

```swift
func invalidate()
```

```objc
- (void) invalidate;
```

## Mentions

- [Adopting system selection UI in custom text views](../adopting-system-selection-ui-in-custom-text-views.md)

#### Discussion

Call this method when you’re ready to hide the loupe. After calling this method, you can remove your reference to the session.

## See Also

### Updating the loupe during the session
- [func move(to: CGPoint, withCaretRect: CGRect, trackingCaret: Bool)](./move%28to,withcaretrect,trackingcaret%29.md)
  Moves the loupe to the specified point in the session’s associated view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextloupesession/invalidate())*