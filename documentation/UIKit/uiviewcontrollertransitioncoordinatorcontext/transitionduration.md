# transitionDuration

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

Returns the noninteractive duration of a transition.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- tvOS
- visionOS

## Declaration

```swift
var transitionDuration: TimeInterval { get }
```

```objc
@property (nonatomic, readonly) NSTimeInterval transitionDuration;
```

## Return Value

The expected duration, in seconds, of the view controller transition, if it proceeds noninteractively.

## Discussion

The transition duration defines the time for the main transition to finish. Use this value when configuring your own animations if you want them to end at the same time as the main transition.

## See Also

### Getting the behavior attributes
- [var presentationStyle: UIModalPresentationStyle](./presentationstyle.md)
  The presentation style to use for the transition.
- [var completionCurve: UIView.AnimationCurve](./completioncurve.md)
  Returns the completion curve associated with the transition.
- [var completionVelocity: CGFloat](./completionvelocity.md)
  Returns the starting velocity to use for any final animations.
- [var percentComplete: CGFloat](./percentcomplete.md)
  Returns the percentage of completion for an interactive transition when it moves to its noninteractive phase.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiviewcontrollertransitioncoordinatorcontext/transitionduration)*