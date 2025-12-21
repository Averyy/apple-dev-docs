# isReversed

**Framework**: UIKit  
**Kind**: property  
**Required**: Yes

A Boolean value indicating whether the animation is running in the reverse direction.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
@MainActor
var isReversed: Bool { get set }
```

#### Discussion

When the value of this property is [`true`](https://developer.apple.com/documentation/Swift/true), animations run in the reverse direction—that is, view properties animate back to their original values. When the value is [`false`](https://developer.apple.com/documentation/Swift/false), view properties animate to their intended final values.

When implementing this property, changes should cause the animation to reverse direction. If you allow changes while the animation is running, it is best to pause the animation briefly and then start it again in the opposite direction. Once the animation transitions to the [`UIViewAnimatingState.stopped`](uiviewanimatingstate/stopped.md) state, you can ignore changes to this property.

## See Also

- [var fractionComplete: CGFloat](uiviewanimating/fractioncomplete.md)
  The completion percentage of the animation.
- [var state: UIViewAnimatingState](uiviewanimating/state.md)
  The current state of the animation.
- [var isRunning: Bool](uiviewanimating/isrunning.md)
  A Boolean value indicating whether the animation is currently running.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiviewanimating/isreversed)*