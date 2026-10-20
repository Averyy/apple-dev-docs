# isReversed

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

A Boolean value indicating whether the animation is running in the reverse direction.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- tvOS
- visionOS

## Declaration

```swift
var isReversed: Bool { get set }
```

```objc
@property (nonatomic, getter=isReversed) BOOL reversed;
```

#### Discussion

When the value of this property is [`true`](../../Swift/true.md), animations run in the reverse direction—that is, view properties animate back to their original values. When the value is [`false`](../../Swift/false.md), view properties animate to their intended final values.

When implementing this property, changes should cause the animation to reverse direction. If you allow changes while the animation is running, it is best to pause the animation briefly and then start it again in the opposite direction. Once the animation transitions to the [`UIViewAnimatingState.stopped`](../uiviewanimatingstate/stopped.md) state, you can ignore changes to this property.

## See Also

### Getting the animator’s state
- [var fractionComplete: CGFloat](./fractioncomplete.md)
  The completion percentage of the animation.
- [var state: UIViewAnimatingState](./state.md)
  The current state of the animation.
- [var isRunning: Bool](./isrunning.md)
  A Boolean value indicating whether the animation is currently running.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiviewanimating/isreversed)*