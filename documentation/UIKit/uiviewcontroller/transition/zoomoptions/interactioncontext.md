# UIViewController.Transition.ZoomOptions.InteractionContext

**Framework**: UIKit  
**Kind**: class

Data you can use to determine whether an interactive dismissal can begin.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
class InteractionContext
```

## Topics

### Accessing the context
- [var location: CGPoint](uiviewcontroller/transition/zoomoptions/interactioncontext/location.md)
  The touch’s location.
- [var velocity: CGVector](uiviewcontroller/transition/zoomoptions/interactioncontext/velocity.md)
  The touch’s velocity.
- [var willBegin: Bool](uiviewcontroller/transition/zoomoptions/interactioncontext/willbegin.md)
  A Boolean value that indicates whether the transition is beginning.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [var interactiveDismissShouldBegin: ((UIViewController.Transition.ZoomOptions.InteractionContext) -> Bool)?](uiviewcontroller/transition/zoomoptions/interactivedismissshouldbegin.md)
  A closure that determines whether an interactive dismissal can begin.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiviewcontroller/transition/zoomoptions/interactioncontext)*