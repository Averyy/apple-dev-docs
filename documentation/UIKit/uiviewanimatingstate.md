# UIViewAnimatingState

**Framework**: UIKit  
**Kind**: enum  
**Role**: Enumeration

Constants indicating the current state of the animation.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
enum UIViewAnimatingState
```

```c
enum UIViewAnimatingState : NSInteger;
```

## Topics

### Constants
- [UIViewAnimatingState.inactive](./uiviewanimatingstate/inactive.md)
  The animations have not yet started executing. This is the initial state of the animator object.
- [UIViewAnimatingState.active](./uiviewanimatingstate/active.md)
  The animator object is active and animations are either running or paused. An animator moves to this state after the first call to [`startAnimation()`](./uiviewanimating/startanimation%28%29.md) or [`pauseAnimation()`](./uiviewanimating/pauseanimation%28%29.md). It stays in the active state until the animations finish naturally or until you call the [`stopAnimation(_:)`](./uiviewanimating/stopanimation%28_%29.md) method.
- [UIViewAnimatingState.stopped](./uiviewanimatingstate/stopped.md)
  The animation is stopped. Putting an animation into this state ends the animation and leaves any animatable properties at their current values, instead of updating them to their intended final values. An animation cannot be started while in this state.
### Initializers
- [init?(rawValue: Int)](./uiviewanimatingstate/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Constants
- [enum UIViewAnimatingPosition](./uiviewanimatingposition.md)
  Constants indicating positions within the animation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiviewanimatingstate)*