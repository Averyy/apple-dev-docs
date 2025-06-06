# isBlinking

**Framework**: UIKit  
**Kind**: property  
**Required**: Yes

A Boolean value that determines whether the blink animation is running.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var isBlinking: Bool { get set }
```

#### Discussion

Set this property to [`true`](https://developer.apple.com/documentation/swift/true) when you want the system to start animating the blink effect for the insertion point cursor. Set the property to [`false`](https://developer.apple.com/documentation/swift/false) to stop the blink animation.

## See Also

- [func resetBlinkAnimation()](uitextcursorview/resetblinkanimation.md)
  Resets the blink animation to avoid glitches while someone is typing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextcursorview/isblinking)*