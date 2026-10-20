# dimmingVisualEffect

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The dimming visual effect.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
var dimmingVisualEffect: UIBlurEffect? { get set }
```

```objc
@property (nonatomic, strong, nullable) UIBlurEffect * dimmingVisualEffect;
```

## See Also

### Setting options
- [var alignmentRectProvider: ((UIViewController.Transition.ZoomOptions.AlignmentRectContext) -> CGRect?)?](./alignmentrectprovider.md)
  A closure that returns the alignment rectangle for the starting and ending views.
- [UIViewController.Transition.ZoomOptions.AlignmentRectContext](./alignmentrectcontext.md)
  An object that contains a zoom transition’s starting and ending views.
- [var dimmingColor: UIColor?](./dimmingcolor.md)
  The dimming color.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiviewcontroller/transition/zoomoptions/dimmingvisualeffect)*