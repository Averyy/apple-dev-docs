# interactiveDismissShouldBegin

**Framework**: UIKit  
**Kind**: property

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

## See Also

- [UIViewController.Transition.ZoomOptions.InteractionContext](uiviewcontroller/transition/zoomoptions/interactioncontext.md)
  Data you can use to determine whether an interactive dismissal can begin.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiviewcontroller/transition/zoomoptions/interactivedismissshouldbegin)*