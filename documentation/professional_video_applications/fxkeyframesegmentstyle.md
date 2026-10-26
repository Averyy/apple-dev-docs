# FxKeyframeSegmentStyle

**Framework**: Professional Video Applications  
**Kind**: enum  
**Role**: Enumeration

Styles for the segment between keyframes.

**Availability**:
- FxPlug 4.1+

## Declaration

```swift
enum FxKeyframeSegmentStyle
```

```c
enum FxKeyframeSegmentStyle: NSUInteger;
```

#### Overview

Each style describes the segment between the keyframe you’re working with and the next keyframe.

## Topics

### Keyframe Segment Styles
- [FxKeyframeSegmentStyle.constant](./fxkeyframesegmentstyle/constant.md)
  A parameter value that is constant between this keyframe and the next one.
- [FxKeyframeSegmentStyle.linear](./fxkeyframesegmentstyle/linear.md)
  A parameter value that changes linearly between this keyframe and the next.
- [FxKeyframeSegmentStyle.bezier](./fxkeyframesegmentstyle/bezier.md)
  A parameter value that changes along a cubic Bézier curve defined by the keypoints and tangents in the FxKeyframe structure.
- [FxKeyframeSegmentStyle.continuous](./fxkeyframesegmentstyle/continuous.md)
  A parameter value that changes along a cubic Catmull-Rom spline defined by the the keypoints and tangents in the FxKeyframe structure.
- [FxKeyframeSegmentStyle.easeInNext](./fxkeyframesegmentstyle/easeinnext.md)
  A parameter value that performs a gentle ease-in interpolation to the next keyframe value.
- [FxKeyframeSegmentStyle.easeOutCurrent](./fxkeyframesegmentstyle/easeoutcurrent.md)
  A parameter value that performs a gentle ease-out interpolation from the current keyframe value.
- [FxKeyframeSegmentStyle.easeOutCurrentEaseInNext](./fxkeyframesegmentstyle/easeoutcurrenteaseinnext.md)
  A parameter value that performs a gentle ease-out interpolation from the current keyframe value and a gentle ease-in interpolation to the next keyframe value.
- [FxKeyframeSegmentStyle.exponential](./fxkeyframesegmentstyle/exponential.md)
  A parameter value that increases or decreases exponentially between the current keyframe and the next.
- [FxKeyframeSegmentStyle.logarithmic](./fxkeyframesegmentstyle/logarithmic.md)
  A parameter value that increases or decreases logarithmically between the current keyframe and the next.
### Initializers
- [init?(rawValue: UInt)](./fxkeyframesegmentstyle/init%28rawvalue%29.md)
### Default Implementations
- [Equatable Implementations](./fxkeyframesegmentstyle/equatable-implementations.md)
- [RawRepresentable Implementations](./fxkeyframesegmentstyle/rawrepresentable-implementations.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/professional_video_applications/fxkeyframesegmentstyle)*