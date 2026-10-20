# interactiveDismissShouldBegin

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

A closure that determines whether an interactive dismissal can begin.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
var interactiveDismissShouldBegin: ((UIViewController.Transition.ZoomOptions.InteractionContext) -> Bool)? { get set }
```

```objc
@property (nonatomic, copy, nullable) BOOL (^interactiveDismissShouldBegin)(UIZoomTransitionInteractionContext *);
```

## See Also

### Accessing the animation state
- [UIViewController.Transition.ZoomOptions.InteractionContext](./interactioncontext.md)
  Data you can use to determine whether an interactive dismissal can begin.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiviewcontroller/transition/zoomoptions/interactivedismissshouldbegin)*