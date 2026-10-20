# completionVelocity

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

Returns the starting velocity to use for any final animations.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var completionVelocity: CGFloat { get }
```

```objc
@property (nonatomic, readonly) CGFloat completionVelocity;
```

#### Return Value

The completion velocity for the view controller transition. A value of `1.0` corresponds to an animation that would complete in the duration returned by the [`transitionDuration`](./transitionduration.md) method. Higher values cause the animations to move faster by the corresponding factor and lower values cause it to move slower. The value of this property is always greater than `0.0`.

#### Discussion

The completion velocity provides the starting speed to use at the end of an interactive animation. Setting the initial speed of your animations ensures that views don’t change velocity abruptly. This value is usually obtained from the [`completionVelocity`](./completionvelocity.md) property of the interactive animator object.

## See Also

### Getting the behavior attributes
- [var presentationStyle: UIModalPresentationStyle](./presentationstyle.md)
  The presentation style to use for the transition.
- [var transitionDuration: TimeInterval](./transitionduration.md)
  Returns the noninteractive duration of a transition.
- [var completionCurve: UIView.AnimationCurve](./completioncurve.md)
  Returns the completion curve associated with the transition.
- [var percentComplete: CGFloat](./percentcomplete.md)
  Returns the percentage of completion for an interactive transition when it moves to its noninteractive phase.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiviewcontrollertransitioncoordinatorcontext/completionvelocity)*