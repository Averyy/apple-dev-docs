# isUserInteractionEnabled

**Framework**: UIKit  
**Kind**: property

A Boolean value that determines whether user events are ignored and removed from the event queue.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var isUserInteractionEnabled: Bool { get set }
```

## Mentions

- [Handling swipe gestures](handling-swipe-gestures.md)
- [Handling pan gestures](handling-pan-gestures.md)
- [Handling pinch gestures](handling-pinch-gestures.md)
- [Handling tap gestures](handling-tap-gestures.md)
- [Handling long-press gestures](handling-long-press-gestures.md)
- [Handling rotation gestures](handling-rotation-gestures.md)

#### Discussion

When set to [`false`](https://developer.apple.com/documentation/swift/false), touch, press, keyboard, and focus events intended for the view are ignored and removed from the event queue. When set to [`true`](https://developer.apple.com/documentation/swift/true), events are delivered to the view normally. The default value of this property is [`true`](https://developer.apple.com/documentation/swift/true).

During an animation, user interactions are temporarily disabled for all views involved in the animation, regardless of the value in this property. You can disable this behavior by specifying the [`allowUserInteraction`](uiview/animationoptions/allowuserinteraction.md) option when configuring the animation.

> **Note**:  Some UIKit subclasses override this property and return a different default value. See the documentation for that class to determine if it returns a different value.

 Some UIKit subclasses override this property and return a different default value. See the documentation for that class to determine if it returns a different value.

## See Also

- [var isMultipleTouchEnabled: Bool](uiview/ismultipletouchenabled.md)
  A Boolean value that indicates whether the view receives more than one touch at a time.
- [var isExclusiveTouch: Bool](uiview/isexclusivetouch.md)
  A Boolean value that indicates whether the receiver handles touch events exclusively.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiview/isuserinteractionenabled)*