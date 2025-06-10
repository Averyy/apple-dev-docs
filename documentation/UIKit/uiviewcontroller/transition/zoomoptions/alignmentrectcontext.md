# UIViewController.Transition.ZoomOptions.AlignmentRectContext

**Framework**: UIKit  
**Kind**: class

An object that contains a zoom transition’s starting and ending views.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
class AlignmentRectContext
```

## Topics

### Accessing views
- [var sourceView: UIView](uiviewcontroller/transition/zoomoptions/alignmentrectcontext/sourceview.md)
  The zoomed-out view, for example a thumbnail image.
- [var zoomedViewController: UIViewController](uiviewcontroller/transition/zoomoptions/alignmentrectcontext/zoomedviewcontroller.md)
  The zoomed in view.

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

- [var alignmentRectProvider: ((UIViewController.Transition.ZoomOptions.AlignmentRectContext) -> CGRect?)?](uiviewcontroller/transition/zoomoptions/alignmentrectprovider.md)
  A closure that returns the alignment rectangle for the starting and ending views.
- [var dimmingColor: UIColor?](uiviewcontroller/transition/zoomoptions/dimmingcolor.md)
  The dimming color.
- [var dimmingVisualEffect: UIBlurEffect?](uiviewcontroller/transition/zoomoptions/dimmingvisualeffect.md)
  The dimming visual effect.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiviewcontroller/transition/zoomoptions/alignmentrectcontext)*