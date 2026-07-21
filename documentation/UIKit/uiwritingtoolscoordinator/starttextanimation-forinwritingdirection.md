# startTextAnimation(_:for:in:writingDirection:)

**Framework**: UIKit  
**Kind**: method

Used to support the presentation of grammar issues in text. When an issue is first identified and indicated, call this to have it animated.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
func startTextAnimation(_ textAnimation: UIWritingToolsCoordinator.TextAnimation, for range: NSRange, in context: UIWritingToolsCoordinator.Context, writingDirection: NSWritingDirection) -> UUID?
```

#### Discussion

The context should be large enough to contain the range being indicated, and the range should be the range of the issue within the context. Returns a UUID that can be used to cancel the animation, or nil if the animation cannot be performed. Calls delegate methods to prepare for the animation (which should hide the text), request previews (with and without underlines), and finish the animation (which should show the text).


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiwritingtoolscoordinator/starttextanimation(_:for:in:writingdirection:))*