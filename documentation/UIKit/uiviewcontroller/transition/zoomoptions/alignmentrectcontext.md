# UIViewController.Transition.ZoomOptions.AlignmentRectContext

**Framework**: UIKit  
**Kind**: class  
**Role**: Class

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

```objc
@interface UIZoomTransitionAlignmentRectContext : NSObject
```

## Topics

### Accessing views
- [var sourceView: UIView](./alignmentrectcontext/sourceview.md)
  The zoomed-out view, for example a thumbnail image.
- [var zoomedViewController: UIViewController](./alignmentrectcontext/zoomedviewcontroller.md)
  The zoomed in view.

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

### Setting options
- [var alignmentRectProvider: ((UIViewController.Transition.ZoomOptions.AlignmentRectContext) -> CGRect?)?](./alignmentrectprovider.md)
  A closure that returns the alignment rectangle for the starting and ending views.
- [var dimmingColor: UIColor?](./dimmingcolor.md)
  The dimming color.
- [var dimmingVisualEffect: UIBlurEffect?](./dimmingvisualeffect.md)
  The dimming visual effect.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiviewcontroller/transition/zoomoptions/alignmentrectcontext)*