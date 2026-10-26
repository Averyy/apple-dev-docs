# startTimeOfInput(toFilter:)

**Framework**: Professional Video Applications  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Provides the start time of the filter’s image input clip.

**Availability**:
- FxPlug 4.0+

## Declaration

```swift
func startTimeOfInput(toFilter startTime: UnsafeMutablePointer<CMTime>!)
```

```objc
- (void) startTimeOfInputToFilter:(CMTime *) startTime;
```

## Mentions

- [Understanding time in FxPlug](../../Professional-Video-Applications/understanding-time-in-fxplug.md)

#### Discussion

In Motion, this value represents the start time of the clip to which the user applies the effect, relative to the timeline time. This start time accounts for any trimming or retiming. It is the start time on the timeline of the first visible frame of the object.

In Final Cut Pro, this value represents the start time of the object relative to its native start, after retiming or trimming. For example, if the user trimmed the clip’s head by 10 seconds, then the start time is 10 seconds. If the user then retimes the clip by 200-percent, the start time is 5 seconds.

## Parameters

- `startTime`: The time when the filter’s image input object starts, in `CMTime`.

## See Also

### Accessing Timing Values
- [func frameDuration(UnsafeMutablePointer<CMTime>!)](./frameduration%28_%29.md)
  Provides the native frame duration of the object to which the effect is applied.
- [func sampleDuration(UnsafeMutablePointer<CMTime>!)](./sampleduration%28_%29.md)
  Provides the native sample duration of the object to which the effect is applied.
- [func startTime(forEffect: UnsafeMutablePointer<CMTime>!)](./starttime%28foreffect%29.md)
  Provides the start time for the effect.
- [func durationTime(forEffect: UnsafeMutablePointer<CMTime>!)](./durationtime%28foreffect%29.md)
  Provides the duration time for the effect.
- [func durationTimeOfInput(toFilter: UnsafeMutablePointer<CMTime>!)](./durationtimeofinput%28tofilter%29.md)
  Provides the duration of the filter’s image input clip.
- [func start(UnsafeMutablePointer<CMTime>!, ofImageParameter: UInt32)](./start%28_,ofimageparameter%29.md)
  Provides the start time of the clip the user assigned to the given image parameter for the effect.
- [func durationTime(UnsafeMutablePointer<CMTime>!, ofImageParameter: UInt32)](./durationtime%28_,ofimageparameter%29.md)
  Provides the duration of the clip the user assigns to the given image parameter for the effect.
- [func inPointTimeOfTimeline(forEffect: UnsafeMutablePointer<CMTime>!)](./inpointtimeoftimeline%28foreffect%29.md)
  The in point of the timeline on which the user applies the effect.
- [func outPointTimeOfTimeline(forEffect: UnsafeMutablePointer<CMTime>!)](./outpointtimeoftimeline%28foreffect%29.md)
  The out point of the timeline on which the user applies the effect.
- [func timelineTime(UnsafeMutablePointer<CMTime>!, fromInputTime: CMTime)](./timelinetime%28_,frominputtime%29.md)
  Converts from input time of the filter’s image input to timeline time.
- [func timelineTime(UnsafeMutablePointer<CMTime>!, fromImageTime: CMTime, forParameterID: UInt32)](./timelinetime%28_,fromimagetime,forparameterid%29.md)
  Converts from image time of the given parameter to timeline time.
- [func inputTime(UnsafeMutablePointer<CMTime>!, fromTimelineTime: CMTime)](./inputtime%28_,fromtimelinetime%29.md)
  Converts from timeline time to time of the filter’s image input.
- [func imageTime(UnsafeMutablePointer<CMTime>!, forParameterID: UInt32, fromTimelineTime: CMTime)](./imagetime%28_,forparameterid,fromtimelinetime%29.md)
  Converts from timeline time of the given parameter to image time.
- [func fieldOrderForInput(toFilter: (any FxTileableEffect)!) -> FxFieldOrder](./fieldorderforinput%28tofilter%29.md)
  Returns the field order of the filter input.
- [func timelineFpsNumerator(for: (any FxTileableEffect)!) -> Int](./timelinefpsnumerator%28for%29.md)
  The numerator of the timeline’s frame rate where the user applies the effect.


---

*[View on Apple Developer](https://developer.apple.com/documentation/professional_video_applications/fxtimingapi_v4/starttimeofinput(tofilter:))*