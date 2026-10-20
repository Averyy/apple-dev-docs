# isRunning

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

A Boolean value indicating whether the animation is currently running.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- tvOS
- visionOS

## Declaration

```swift
var isRunning: Bool { get }
```

```objc
@property (nonatomic, readonly, getter=isRunning) BOOL running;
```

#### Discussion

This property reflects whether the animation is running either in the forward or reverse direction. The value of this property is [`true`](../../Swift/true.md) only after a call to the [`startAnimation()`](./startanimation%28%29.md) method. The value is [`false`](../../Swift/false.md) when the animator is paused or stopped.

## See Also

### Getting the animator’s state
- [var fractionComplete: CGFloat](./fractioncomplete.md)
  The completion percentage of the animation.
- [var isReversed: Bool](./isreversed.md)
  A Boolean value indicating whether the animation is running in the reverse direction.
- [var state: UIViewAnimatingState](./state.md)
  The current state of the animation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiviewanimating/isrunning)*