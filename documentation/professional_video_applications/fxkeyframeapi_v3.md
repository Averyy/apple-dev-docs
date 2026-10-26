# FxKeyframeAPI_v3

**Framework**: Professional Video Applications  
**Kind**: protocol  
**Role**: Protocol

A collection of methods for manipulating the keyframes of your FxPlug 4 plug-in.

**Availability**:
- FxPlug 4.0+

## Declaration

```swift
protocol FxKeyframeAPI_v3
```

```objc
@protocol FxKeyframeAPI_v3
```

#### Overview

These methods allow you to get keyframe information about any parameter your plug-in has. You can also set keyframes, which can be useful for creating presets and automating common uses of your plug-ins.

## Topics

### Instance Methods
- [func add(UnsafePointer<FxKeyframe>, toParameter: Int, andChannel: Int) -> (any Error)?](./fxkeyframeapi_v3/add%28_,toparameter,andchannel%29.md)
  Adds a keyframe at the given time.
- [func channelCount(UnsafeMutablePointer<Int>, forParameter: Int) -> (any Error)?](./fxkeyframeapi_v3/channelcount%28_,forparameter%29.md)
  Returns the number of channels in a parameter.
- [func keyframe(UnsafeMutablePointer<FxKeyframe>, atOrAfter: CMTime, fromParameter: Int, andChannel: Int) -> (any Error)?](./fxkeyframeapi_v3/keyframe%28_,atorafter,fromparameter,andchannel%29.md)
  Returns the info about the nearest next keyframe.
- [func keyframe(UnsafeMutablePointer<FxKeyframe>, atOrBefore: CMTime, fromParameter: Int, andChannel: Int) -> (any Error)?](./fxkeyframeapi_v3/keyframe%28_,atorbefore,fromparameter,andchannel%29.md)
  Returns the info about the nearest previous keyframe.
- [func keyframe(UnsafeMutablePointer<FxKeyframe>, forParameter: Int, channel: Int, andIndex: Int) -> (any Error)?](./fxkeyframeapi_v3/keyframe%28_,forparameter,channel,andindex%29.md)
  Returns the keyframe info for the keyframe at a given index.
- [func keyframeCount(UnsafeMutablePointer<Int>, forParameter: Int, andChannel: Int) -> (any Error)?](./fxkeyframeapi_v3/keyframecount%28_,forparameter,andchannel%29.md)
  Returns the number of keyframes for a parameter’s channel.
- [func parameter(Int, channel: Int, hasKeyframe: UnsafeMutablePointer<ObjCBool>, at: CMTime) -> (any Error)?](./fxkeyframeapi_v3/parameter%28_,channel,haskeyframe,at%29.md)
  Tells whether there is a keyframe at a given time.
- [func removeAllKeyframes(forParameter: Int, andChannel: Int) -> (any Error)?](./fxkeyframeapi_v3/removeallkeyframes%28forparameter,andchannel%29.md)
  Remove all keyframes from the given parameter’s channel.
- [func removeKeyframe(at: Int, fromParameter: Int, andChannel: Int) -> (any Error)?](./fxkeyframeapi_v3/removekeyframe%28at,fromparameter,andchannel%29.md)
  Removes the keyframe at the given index.
- [func setKeyframeIndex(Int, with: UnsafePointer<FxKeyframe>, forParameter: Int, andChannel: Int) -> (any Error)?](./fxkeyframeapi_v3/setkeyframeindex%28_,with,forparameter,andchannel%29.md)
  Sets the keyframe at the given index to have the given info.
### Structure
- [struct FxKeyframe](./fxkeyframe.md)
### Constants
- [typealias FxKeyframeStyle](./fxkeyframestyle.md)
  Constants for specifying the type of keyframe.
- [var kFxKeyframe_V3: Int32](./kfxkeyframe_v3.md)
- [var kFxKeyframe_CurrentVersion: Int32](./kfxkeyframe_currentversion.md)

## See Also

### Time and analysis
- [Understanding time in FxPlug](../Professional-Video-Applications/understanding-time-in-fxplug.md)
  Learn about time handling in host apps and plug-ins.
- [Scheduling media in plug-ins](../Professional-Video-Applications/scheduling-media-in-plug-ins.md)
  Use the scheduling APIs in FxPlug to retrieve frames from different times.
- [protocol FxTimingAPI_v4](./fxtimingapi_v4.md)
  A protocol that defines the methods provided by the host, so that a plug-in can query the timing properties of its input.
- [Analyzing media](../Professional-Video-Applications/analyzing-media.md)
  Use the FxPlug analysis API to analyze frames of source media before rendering them.
- [protocol FxAnalysisAPI](./fxanalysisapi.md)
  A protocol that host applications implement to provide information to plug-ins that support the FxAnalyzer protocol.
- [protocol FxAnalysisAPI_v2](./fxanalysisapi_v2.md)
  A protocol that host applications implement to provide information to plug-ins that support the FxAnalyzer protocol.
- [protocol FxAnalyzer](./fxanalyzer.md)
  A protocol you implement in your plug-in to analyze frames that the plug-in is applied to.


---

*[View on Apple Developer](https://developer.apple.com/documentation/professional_video_applications/fxkeyframeapi_v3)*