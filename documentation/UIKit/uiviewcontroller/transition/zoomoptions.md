# UIViewController.Transition.ZoomOptions

**Framework**: UIKit  
**Kind**: class

Options for a zoom transition.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
class ZoomOptions
```

## Topics

### Setting options
- [var alignmentRectProvider: ((UIViewController.Transition.ZoomOptions.AlignmentRectContext) -> CGRect?)?](uiviewcontroller/transition/zoomoptions/alignmentrectprovider.md)
  A closure that returns the alignment rectangle for the starting and ending views.
- [UIViewController.Transition.ZoomOptions.AlignmentRectContext](uiviewcontroller/transition/zoomoptions/alignmentrectcontext.md)
  An object that contains a zoom transition’s starting and ending views.
- [var dimmingColor: UIColor?](uiviewcontroller/transition/zoomoptions/dimmingcolor.md)
  The dimming color.
- [var dimmingVisualEffect: UIBlurEffect?](uiviewcontroller/transition/zoomoptions/dimmingvisualeffect.md)
  The dimming visual effect.
### Accessing the animation state
- [var interactiveDismissShouldBegin: ((UIViewController.Transition.ZoomOptions.InteractionContext) -> Bool)?](uiviewcontroller/transition/zoomoptions/interactivedismissshouldbegin.md)
  A closure that determines whether an interactive dismissal can begin.
- [UIViewController.Transition.ZoomOptions.InteractionContext](uiviewcontroller/transition/zoomoptions/interactioncontext.md)
  Data you can use to determine whether an interactive dismissal can begin.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [static func zoom(options: UIViewController.Transition.ZoomOptions?, sourceViewProvider: (UIViewController.Transition.ZoomSourceViewProviderContext) -> UIView?) -> Self](uiviewcontroller/transition/zoom(options:sourceviewprovider:).md)
  Creates a zoom transition from the view that the source provider specifies.
- [UIViewController.Transition.ZoomSourceViewProviderContext](uiviewcontroller/transition/zoomsourceviewprovidercontext.md)
  A context object that contains references to the view controllers from a zoom transition.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiviewcontroller/transition/zoomoptions)*