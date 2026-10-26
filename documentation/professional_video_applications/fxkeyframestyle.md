# FxKeyframeStyle

**Framework**: Professional Video Applications  
**Kind**: typealias  
**Role**: Type Alias

Constants for specifying the type of keyframe.

**Availability**:
- FxPlug 3.1+

## Declaration

```swift
typealias FxKeyframeStyle = Int
```

```c
typedef NSUInteger FxKeyframeStyle;
```

## Topics

### Constants
- [var kFxKeyframeStyle_Constant: UInt32](./kfxkeyframestyle_constant.md)
  Also known as “Hold,” constant keyframes have a constant value between keyframes.
- [var kFxKeyframeStyle_Linear: UInt32](./kfxkeyframestyle_linear.md)
  The values are interpolated along a straight line between keyframes.
- [var kFxKeyframeStyle_Quadratic: UInt32](./kfxkeyframestyle_quadratic.md)
  The values are interpolated along a quadratic curve.
- [var kFxKeyframeStyle_Cubic: UInt32](./kfxkeyframestyle_cubic.md)
  The values are interpolated along a cubic curve.
- [var kFxKeyframeStyle_Bezier: UInt32](./kfxkeyframestyle_bezier.md)
  The values are interpolated along a cubic curve the user can control by varying the tangent handles.
- [var kFxKeyframeStyle_EaseIn: UInt32](./kfxkeyframestyle_easein.md)
  The values are interpolated along a pre-calculated cubic curve that smoothly transitions into the next value.
- [var kFxKeyframeStyle_EaseOut: UInt32](./kfxkeyframestyle_easeout.md)
  The values are interpolated along a pre-calculated cubic curve that smoothly transitions out of the previous value.
- [var kFxKeyframeStyle_BSpline: UInt32](./kfxkeyframestyle_bspline.md)
  The values are interpolated along a B-Spline.
- [var kFxKeyframeStyle_XSpline: UInt32](./kfxkeyframestyle_xspline.md)
  The values are interpolated along a weighted X-Spline.
- [var kFxKeyframeStyle_Exponential: UInt32](./kfxkeyframestyle_exponential.md)
  The values are interpolated along an exponential curve.
- [var kFxKeyframeStyle_Logarithmic: UInt32](./kfxkeyframestyle_logarithmic.md)
  The values are interpolated along a logarithmic curve.
- [var kFxKeyframeStyle_Mixed: UInt32](./kfxkeyframestyle_mixed.md)
  The keyframe is a mixture of two of the other style types.
- [var kFxKeyframeStyle_All: UInt32](./kfxkeyframestyle_all.md)
  A mask for all types.

## See Also

### Constants
- [var kFxKeyframe_V3: Int32](./kfxkeyframe_v3.md)
- [var kFxKeyframe_CurrentVersion: Int32](./kfxkeyframe_currentversion.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/professional_video_applications/fxkeyframestyle)*