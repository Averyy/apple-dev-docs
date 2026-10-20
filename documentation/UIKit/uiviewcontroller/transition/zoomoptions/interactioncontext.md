# UIViewController.Transition.ZoomOptions.InteractionContext

**Framework**: UIKit  
**Kind**: class  
**Role**: Class

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

```objc
@interface UIZoomTransitionInteractionContext : NSObject
```

## Topics

### Accessing the context
- [var location: CGPoint](./interactioncontext/location.md)
  The touch’s location.
- [var velocity: CGVector](./interactioncontext/velocity.md)
  The touch’s velocity.
- [var willBegin: Bool](./interactioncontext/willbegin.md)
  A Boolean value that indicates whether the transition is beginning.

## Relationships

### Inherits From
- [NSObject](../../../../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../../../../Swift/cvararg.md)
- [CustomDebugStringConvertible](../../../../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../../../../Swift/customstringconvertible.md)
- [Equatable](../../../../Swift/equatable.md)
- [Hashable](../../../../Swift/hashable.md)
- [NSObjectProtocol](../../../../ObjectiveC/nsobjectprotocol.md)

## See Also

### Accessing the animation state
- [var interactiveDismissShouldBegin: ((UIViewController.Transition.ZoomOptions.InteractionContext) -> Bool)?](./interactivedismissshouldbegin.md)
  A closure that determines whether an interactive dismissal can begin.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiviewcontroller/transition/zoomoptions/interactioncontext)*