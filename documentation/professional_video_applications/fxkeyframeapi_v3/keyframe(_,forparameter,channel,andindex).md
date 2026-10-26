# keyframe(_:forParameter:channel:andIndex:)

**Framework**: Professional Video Applications  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Returns the keyframe info for the keyframe at a given index.

**Availability**:
- FxPlug 4.0+

## Declaration

```swift
func keyframe(_ keyframe: UnsafeMutablePointer<FxKeyframe>, forParameter parameterID: Int, channel channelIndex: Int, andIndex keyframeIndex: Int) -> (any Error)?
```

```objc
- (NSError *) keyframe:(FxKeyframe *) keyframe forParameter:(NSUInteger) parameterID channel:(NSUInteger) channelIndex andIndex:(NSUInteger) keyframeIndex;
```

## Parameters

- `keyframe`: A pointer to an FxKeyframeInfo structure to be filled out with the information about the keyframe in question.
- `parameterID`: The ID of the parameter you want info about.
- `channelIndex`: The index of the channel you want info about.
- `keyframeIndex`: The index of the keyframe you wish to retrieve.

## See Also

### Instance Methods
- [func add(UnsafePointer<FxKeyframe>, toParameter: Int, andChannel: Int) -> (any Error)?](./add%28_,toparameter,andchannel%29.md)
  Adds a keyframe at the given time.
- [func channelCount(UnsafeMutablePointer<Int>, forParameter: Int) -> (any Error)?](./channelcount%28_,forparameter%29.md)
  Returns the number of channels in a parameter.
- [func keyframe(UnsafeMutablePointer<FxKeyframe>, atOrAfter: CMTime, fromParameter: Int, andChannel: Int) -> (any Error)?](./keyframe%28_,atorafter,fromparameter,andchannel%29.md)
  Returns the info about the nearest next keyframe.
- [func keyframe(UnsafeMutablePointer<FxKeyframe>, atOrBefore: CMTime, fromParameter: Int, andChannel: Int) -> (any Error)?](./keyframe%28_,atorbefore,fromparameter,andchannel%29.md)
  Returns the info about the nearest previous keyframe.
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

*[View on Apple Developer](https://developer.apple.com/documentation/professional_video_applications/fxkeyframeapi_v3/keyframe(_:forparameter:channel:andindex:))*