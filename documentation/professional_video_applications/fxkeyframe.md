# FxKeyframe

**Framework**: Professional Video Applications  
**Kind**: struct  
**Role**: Structure

**Availability**:
- FxPlug 4.0+

## Declaration

```swift
struct FxKeyframe
```

```c
typedef struct FxKeyframe { ... } FxKeyframe;
```

## Topics

### Properties
- [var version: Int](./fxkeyframe/version.md)
- [var time: CMTime](./fxkeyframe/time.md)
- [var segmentStyle: FxKeyframeSegmentStyle](./fxkeyframe/segmentstyle.md)
  The type of segment between this keyframe and the next.
- [var inTangentX: Double](./fxkeyframe/intangentx.md)
- [var inTangentY: Double](./fxkeyframe/intangenty.md)
- [var outTangentX: Double](./fxkeyframe/outtangentx.md)
- [var outTangentY: Double](./fxkeyframe/outtangenty.md)
### Initializers
- [init()](./fxkeyframe/init%28%29.md)
- [init(version: Int, time: CMTime, segmentStyle: FxKeyframeSegmentStyle, inTangentX: Double, inTangentY: Double, outTangentX: Double, outTangentY: Double)](./fxkeyframe/init%28version,time,segmentstyle,intangentx,intangenty,outtangentx,outtangenty%29.md)
  Contains information about a single keyframe.
### Enumerations
- [enum FxKeyframeSegmentStyle](./fxkeyframesegmentstyle.md)
  Styles for the segment between keyframes.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Sendable](../Swift/sendable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/professional_video_applications/fxkeyframe)*