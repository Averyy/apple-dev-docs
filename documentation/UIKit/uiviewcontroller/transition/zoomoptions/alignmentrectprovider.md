# alignmentRectProvider

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

A closure that returns the alignment rectangle for the starting and ending views.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- tvOS
- visionOS

## Declaration

```swift
var alignmentRectProvider: ((UIViewController.Transition.ZoomOptions.AlignmentRectContext) -> CGRect?)? { get set }
```

## See Also

### Setting options
- [UIViewController.Transition.ZoomOptions.AlignmentRectContext](./alignmentrectcontext.md)
  An object that contains a zoom transition’s starting and ending views.
- [var dimmingColor: UIColor?](./dimmingcolor.md)
  The dimming color.
- [var dimmingVisualEffect: UIBlurEffect?](./dimmingvisualeffect.md)
  The dimming visual effect.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiviewcontroller/transition/zoomoptions/alignmentrectprovider)*