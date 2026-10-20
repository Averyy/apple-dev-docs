# completionCurve

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

Returns the completion curve associated with the transition.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
var completionCurve: UIView.AnimationCurve { get }
```

```objc
@property (nonatomic, readonly) UIViewAnimationCurve completionCurve;
```

#### Return Value

The completion curve for the view controller transition. For a list of possible values, see the [`UIView.AnimationCurve`](../uiview/animationcurve.md) type.

#### Discussion

The completion curve defines the timing of the animations. For interactive transitions, this value is usually obtained from the [`completionCurve`](../uiviewcontrollerinteractivetransitioning/completioncurve.md) property of the interactive animator object. Use this value when configuring your own animations if you want the same timing as the main transition.

## See Also

### Getting the behavior attributes
- [var presentationStyle: UIModalPresentationStyle](./presentationstyle.md)
  The presentation style to use for the transition.
- [var transitionDuration: TimeInterval](./transitionduration.md)
  Returns the noninteractive duration of a transition.
- [var completionVelocity: CGFloat](./completionvelocity.md)
  Returns the starting velocity to use for any final animations.
- [var percentComplete: CGFloat](./percentcomplete.md)
  Returns the percentage of completion for an interactive transition when it moves to its noninteractive phase.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiviewcontrollertransitioncoordinatorcontext/completioncurve)*