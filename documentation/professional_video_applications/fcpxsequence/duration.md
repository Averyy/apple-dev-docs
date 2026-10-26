# duration

**Framework**: Professional Video Applications  
**Kind**: property  
**Role**: Instance Property

The duration of a sequence opened in the Final Cut Pro timeline.

**Availability**:
- ProVideo Workflow Extensions 1.0+

## Declaration

```swift
var duration: CMTime { get }
```

```objc
@property (nonatomic, readonly) CMTime duration;
```

## See Also

### Getting Details of an Active Sequence
- [var frameDuration: CMTime](./frameduration.md)
  The amount of time to play a frame in a sequence.
- [var startTime: CMTime](./starttime.md)
  The start time of a sequence opened in the Final Cut Pro timeline.
- [var timecodeFormat: FCPXSequenceTimecodeFormat](./timecodeformat.md)
  The timecode format of the frames in a sequence.
- [var name: String](./name.md)
  The name of the active sequence in the Final Cut Pro timeline.


---

*[View on Apple Developer](https://developer.apple.com/documentation/professional_video_applications/fcpxsequence/duration)*