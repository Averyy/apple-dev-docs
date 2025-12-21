# isRunning

**Framework**: UIKit  
**Kind**: property  
**Required**: Yes

A Boolean value indicating whether the animation is currently running.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
@MainActor
var isRunning: Bool { get }
```

#### Discussion

This property reflects whether the animation is running either in the forward or reverse direction. The value of this property is [`true`](https://developer.apple.com/documentation/Swift/true) only after a call to the [`startAnimation()`](uiviewanimating/startanimation().md) method. The value is [`false`](https://developer.apple.com/documentation/Swift/false) when the animator is paused or stopped.

## See Also

- [var fractionComplete: CGFloat](uiviewanimating/fractioncomplete.md)
  The completion percentage of the animation.
- [var isReversed: Bool](uiviewanimating/isreversed.md)
  A Boolean value indicating whether the animation is running in the reverse direction.
- [var state: UIViewAnimatingState](uiviewanimating/state.md)
  The current state of the animation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiviewanimating/isrunning)*