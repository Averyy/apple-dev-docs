# FxTimingAPI_v4

**Framework**: Professional Video Applications  
**Kind**: protocol  
**Role**: Protocol

A protocol that defines the methods provided by the host, so that a plug-in can query the timing properties of its input.

**Availability**:
- FxPlug 4.0+

## Declaration

```swift
protocol FxTimingAPI_v4
```

```objc
@protocol FxTimingAPI_v4
```

## Mentions

- [Understanding time in FxPlug](../Professional-Video-Applications/understanding-time-in-fxplug.md)

#### Overview

Using the FxTimingAPI, your plug-in can query the timing properties of its input image or images, image parameters, effect, timeline, and in or out points.

> **Note**:  This version of the API is only available to plug-ins built in the FxPlug 4 style and later, and it intentionally doesn’t inherit from previous versions.

## Topics

### Accessing Timing Values
- [func frameDuration(UnsafeMutablePointer<CMTime>!)](./fxtimingapi_v4/frameduration%28_%29.md)
  Provides the native frame duration of the object to which the effect is applied.
- [func sampleDuration(UnsafeMutablePointer<CMTime>!)](./fxtimingapi_v4/sampleduration%28_%29.md)
  Provides the native sample duration of the object to which the effect is applied.
- [func startTime(forEffect: UnsafeMutablePointer<CMTime>!)](./fxtimingapi_v4/starttime%28foreffect%29.md)
  Provides the start time for the effect.
- [func durationTime(forEffect: UnsafeMutablePointer<CMTime>!)](./fxtimingapi_v4/durationtime%28foreffect%29.md)
  Provides the duration time for the effect.
- [func startTimeOfInput(toFilter: UnsafeMutablePointer<CMTime>!)](./fxtimingapi_v4/starttimeofinput%28tofilter%29.md)
  Provides the start time of the filter’s image input clip.
- [func durationTimeOfInput(toFilter: UnsafeMutablePointer<CMTime>!)](./fxtimingapi_v4/durationtimeofinput%28tofilter%29.md)
  Provides the duration of the filter’s image input clip.
- [func start(UnsafeMutablePointer<CMTime>!, ofImageParameter: UInt32)](./fxtimingapi_v4/start%28_,ofimageparameter%29.md)
  Provides the start time of the clip the user assigned to the given image parameter for the effect.
- [func durationTime(UnsafeMutablePointer<CMTime>!, ofImageParameter: UInt32)](./fxtimingapi_v4/durationtime%28_,ofimageparameter%29.md)
  Provides the duration of the clip the user assigns to the given image parameter for the effect.
- [func inPointTimeOfTimeline(forEffect: UnsafeMutablePointer<CMTime>!)](./fxtimingapi_v4/inpointtimeoftimeline%28foreffect%29.md)
  The in point of the timeline on which the user applies the effect.
- [func outPointTimeOfTimeline(forEffect: UnsafeMutablePointer<CMTime>!)](./fxtimingapi_v4/outpointtimeoftimeline%28foreffect%29.md)
  The out point of the timeline on which the user applies the effect.
- [func timelineTime(UnsafeMutablePointer<CMTime>!, fromInputTime: CMTime)](./fxtimingapi_v4/timelinetime%28_,frominputtime%29.md)
  Converts from input time of the filter’s image input to timeline time.
- [func timelineTime(UnsafeMutablePointer<CMTime>!, fromImageTime: CMTime, forParameterID: UInt32)](./fxtimingapi_v4/timelinetime%28_,fromimagetime,forparameterid%29.md)
  Converts from image time of the given parameter to timeline time.
- [func inputTime(UnsafeMutablePointer<CMTime>!, fromTimelineTime: CMTime)](./fxtimingapi_v4/inputtime%28_,fromtimelinetime%29.md)
  Converts from timeline time to time of the filter’s image input.
- [func imageTime(UnsafeMutablePointer<CMTime>!, forParameterID: UInt32, fromTimelineTime: CMTime)](./fxtimingapi_v4/imagetime%28_,forparameterid,fromtimelinetime%29.md)
  Converts from timeline time of the given parameter to image time.
- [func fieldOrderForInput(toFilter: (any FxTileableEffect)!) -> FxFieldOrder](./fxtimingapi_v4/fieldorderforinput%28tofilter%29.md)
  Returns the field order of the filter input.
- [func timelineFpsNumerator(for: (any FxTileableEffect)!) -> Int](./fxtimingapi_v4/timelinefpsnumerator%28for%29.md)
  The numerator of the timeline’s frame rate where the user applies the effect.
- [func timelineFpsDenominator(for: (any FxTileableEffect)!) -> Int](./fxtimingapi_v4/timelinefpsdenominator%28for%29.md)
  The denominator of the timeline’s frame rate where the user applies the effect.

## See Also

### Time and analysis
- [Understanding time in FxPlug](../Professional-Video-Applications/understanding-time-in-fxplug.md)
  Learn about time handling in host apps and plug-ins.
- [Scheduling media in plug-ins](../Professional-Video-Applications/scheduling-media-in-plug-ins.md)
  Use the scheduling APIs in FxPlug to retrieve frames from different times.
- [protocol FxKeyframeAPI_v3](./fxkeyframeapi_v3.md)
  A collection of methods for manipulating the keyframes of your FxPlug 4 plug-in.
- [Analyzing media](../Professional-Video-Applications/analyzing-media.md)
  Use the FxPlug analysis API to analyze frames of source media before rendering them.
- [protocol FxAnalysisAPI](./fxanalysisapi.md)
  A protocol that host applications implement to provide information to plug-ins that support the FxAnalyzer protocol.
- [protocol FxAnalysisAPI_v2](./fxanalysisapi_v2.md)
  A protocol that host applications implement to provide information to plug-ins that support the FxAnalyzer protocol.
- [protocol FxAnalyzer](./fxanalyzer.md)
  A protocol you implement in your plug-in to analyze frames that the plug-in is applied to.


---

*[View on Apple Developer](https://developer.apple.com/documentation/professional_video_applications/fxtimingapi_v4)*