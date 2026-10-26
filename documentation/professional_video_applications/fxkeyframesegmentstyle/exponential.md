# FxKeyframeSegmentStyle.exponential

**Framework**: Professional Video Applications  
**Kind**: case  
**Role**: Case

A parameter value that increases or decreases exponentially between the current keyframe and the next.

**Availability**:
- FxPlug 4.1+

## Declaration

```swift
case exponential
```

```c
kFxKeyframeSegmentStyle_Exponential
```

## See Also

### Keyframe Segment Styles
- [FxKeyframeSegmentStyle.constant](./constant.md)
  A parameter value that is constant between this keyframe and the next one.
- [FxKeyframeSegmentStyle.linear](./linear.md)
  A parameter value that changes linearly between this keyframe and the next.
- [FxKeyframeSegmentStyle.bezier](./bezier.md)
  A parameter value that changes along a cubic Bézier curve defined by the keypoints and tangents in the FxKeyframe structure.
- [FxKeyframeSegmentStyle.continuous](./continuous.md)
  A parameter value that changes along a cubic Catmull-Rom spline defined by the the keypoints and tangents in the FxKeyframe structure.
- [FxKeyframeSegmentStyle.easeInNext](./easeinnext.md)
  A parameter value that performs a gentle ease-in interpolation to the next keyframe value.
- [FxKeyframeSegmentStyle.easeOutCurrent](./easeoutcurrent.md)
  A parameter value that performs a gentle ease-out interpolation from the current keyframe value.
- [FxKeyframeSegmentStyle.easeOutCurrentEaseInNext](./easeoutcurrenteaseinnext.md)
  A parameter value that performs a gentle ease-out interpolation from the current keyframe value and a gentle ease-in interpolation to the next keyframe value.
- [FxKeyframeSegmentStyle.logarithmic](./logarithmic.md)
  A parameter value that increases or decreases logarithmically between the current keyframe and the next.


---

*[View on Apple Developer](https://developer.apple.com/documentation/professional_video_applications/fxkeyframesegmentstyle/exponential)*