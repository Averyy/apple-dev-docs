# completionCurve

**Framework**: UIKit  
**Kind**: property

Called when the system needs the animation completion curve for an interactive view controller transition.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
optional var completionCurve: UIView.AnimationCurve { get }
```

#### Return Value

Default value is [`UIView.AnimationCurve.easeInOut`](uiview/animationcurve/easeinout.md), with other possible values described in the [`UIView.AnimationCurve`](uiview/animationcurve.md) type definition.

## See Also

- [var completionSpeed: CGFloat](uiviewcontrollerinteractivetransitioning/completionspeed.md)
  Called when the system needs the speed at which to complete an interactive transition, after the interactive portion is finished.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiviewcontrollerinteractivetransitioning/completioncurve)*