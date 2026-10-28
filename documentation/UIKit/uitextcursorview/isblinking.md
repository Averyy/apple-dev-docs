# isBlinking

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property  
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
var isBlinking: Bool { get set }
```

```objc
@property (nonatomic, readwrite, getter=isBlinking) BOOL blinking;
```

## Discussion

Set this property to [`true`](../../Swift/true.md) when you want the system to start animating the blink effect for the insertion point cursor. Set the property to [`false`](../../Swift/false.md) to stop the blink animation.

## See Also

### Determining the animation state
- [func resetBlinkAnimation()](./resetblinkanimation%28%29.md)
  Resets the blink animation to avoid glitches while someone is typing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextcursorview/isblinking)*