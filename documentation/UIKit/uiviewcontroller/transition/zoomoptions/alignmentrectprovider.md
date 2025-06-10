# alignmentRectProvider

**Framework**: UIKit  
**Kind**: property

A closure that returns the alignment rectangle for the starting and ending views.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
var alignmentRectProvider: ((UIViewController.Transition.ZoomOptions.AlignmentRectContext) -> CGRect?)? { get set }
```

## See Also

- [UIViewController.Transition.ZoomOptions.AlignmentRectContext](uiviewcontroller/transition/zoomoptions/alignmentrectcontext.md)
  An object that contains a zoom transition’s starting and ending views.
- [var dimmingColor: UIColor?](uiviewcontroller/transition/zoomoptions/dimmingcolor.md)
  The dimming color.
- [var dimmingVisualEffect: UIBlurEffect?](uiviewcontroller/transition/zoomoptions/dimmingvisualeffect.md)
  The dimming visual effect.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiviewcontroller/transition/zoomoptions/alignmentrectprovider)*