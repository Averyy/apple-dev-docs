# alignmentRectProvider

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

A block that returns the alignment rectangle for the starting and ending views.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```objc
@property (nonatomic, copy, nullable) struct CGRect (^)(UIZoomTransitionAlignmentRectContext *) alignmentRectProvider;
```

## See Also

### Setting options
- [UIViewController.Transition.ZoomOptions.AlignmentRectContext](../uiviewcontroller/transition/zoomoptions/alignmentrectcontext.md)
  An object that contains a zoom transition’s starting and ending views.
- [var dimmingColor: UIColor?](../uiviewcontroller/transition/zoomoptions/dimmingcolor.md)
  The dimming color.
- [var dimmingVisualEffect: UIBlurEffect?](../uiviewcontroller/transition/zoomoptions/dimmingvisualeffect.md)
  The dimming visual effect.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uizoomtransitionoptions/alignmentrectprovider)*