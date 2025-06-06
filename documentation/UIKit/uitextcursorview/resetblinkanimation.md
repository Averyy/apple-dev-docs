# resetBlinkAnimation()

**Framework**: UIKit  
**Kind**: method  
**Required**: Yes

Resets the blink animation to avoid glitches while someone is typing.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func resetBlinkAnimation()
```

#### Discussion

When the cursor is moving in your text view, call this method to prevent the insertion point from blinking.

## See Also

- [var isBlinking: Bool](uitextcursorview/isblinking.md)
  A Boolean value that determines whether the blink animation is running.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextcursorview/resetblinkanimation())*