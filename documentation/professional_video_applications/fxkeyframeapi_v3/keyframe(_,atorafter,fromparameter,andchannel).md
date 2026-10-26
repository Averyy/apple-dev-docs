# keyframe(_:atOrAfter:fromParameter:andChannel:)

**Framework**: Professional Video Applications  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Returns the info about the nearest next keyframe.

**Availability**:
- FxPlug 4.0+

## Declaration

```swift
func keyframe(_ keyframe: UnsafeMutablePointer<FxKeyframe>, atOrAfter time: CMTime, fromParameter parameterID: Int, andChannel channelIndex: Int) -> (any Error)?
```

```objc
- (NSError *) keyframe:(FxKeyframe *) keyframe atOrAfterTime:(CMTime) time fromParameter:(NSUInteger) parameterID andChannel:(NSUInteger) channelIndex;
```

## Parameters

- `keyframe`: A pointer to a struct which will receive information about the keyframe at or after the given time.
- `time`: The time ([`CMTime`](../../CoreMedia/cmtime.md)) you want a keyframe at or after.
- `parameterID`: The ID of the parameter for which you want the keyframe information.
- `channelIndex`: The index of the channel of the parameter for which you want the keyframe information.

## See Also

### Instance Methods
- [func add(UnsafePointer<FxKeyframe>, toParameter: Int, andChannel: Int) -> (any Error)?](./add%28_,toparameter,andchannel%29.md)
  Adds a keyframe at the given time.
- [func channelCount(UnsafeMutablePointer<Int>, forParameter: Int) -> (any Error)?](./channelcount%28_,forparameter%29.md)
  Returns the number of channels in a parameter.
- [func keyframe(UnsafeMutablePointer<FxKeyframe>, atOrBefore: CMTime, fromParameter: Int, andChannel: Int) -> (any Error)?](./keyframe%28_,atorbefore,fromparameter,andchannel%29.md)
  Returns the info about the nearest previous keyframe.
- [func keyframe(UnsafeMutablePointer<FxKeyframe>, forParameter: Int, channel: Int, andIndex: Int) -> (any Error)?](./keyframe%28_,forparameter,channel,andindex%29.md)
  Returns the keyframe info for the keyframe at a given index.
- [func keyframeCount(UnsafeMutablePointer<Int>, forParameter: Int, andChannel: Int) -> (any Error)?](./keyframecount%28_,forparameter,andchannel%29.md)
  Returns the number of keyframes for a parameter’s channel.
- [func parameter(Int, channel: Int, hasKeyframe: UnsafeMutablePointer<ObjCBool>, at: CMTime) -> (any Error)?](./parameter%28_,channel,haskeyframe,at%29.md)
  Tells whether there is a keyframe at a given time.
- [func removeAllKeyframes(forParameter: Int, andChannel: Int) -> (any Error)?](./removeallkeyframes%28forparameter,andchannel%29.md)
  Remove all keyframes from the given parameter’s channel.
- [func removeKeyframe(at: Int, fromParameter: Int, andChannel: Int) -> (any Error)?](./removekeyframe%28at,fromparameter,andchannel%29.md)
  Removes the keyframe at the given index.
- [func setKeyframeIndex(Int, with: UnsafePointer<FxKeyframe>, forParameter: Int, andChannel: Int) -> (any Error)?](./setkeyframeindex%28_,with,forparameter,andchannel%29.md)
  Sets the keyframe at the given index to have the given info.


---

*[View on Apple Developer](https://developer.apple.com/documentation/professional_video_applications/fxkeyframeapi_v3/keyframe(_:atorafter:fromparameter:andchannel:))*