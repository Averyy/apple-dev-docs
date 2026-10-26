# keyframeCount(_:forParameter:andChannel:)

**Framework**: Professional Video Applications  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Returns the number of keyframes for a parameter’s channel.

**Availability**:
- FxPlug 4.0+

## Declaration

```swift
func keyframeCount(_ count: UnsafeMutablePointer<Int>, forParameter parameterID: Int, andChannel channelIndex: Int) -> (any Error)?
```

```objc
- (NSError *) keyframeCount:(NSUInteger *) count forParameter:(NSUInteger) parameterID andChannel:(NSUInteger) channelIndex;
```

#### Return Value

If any errors occur while getting the keyframe count, the return value will be a pointer to an `NSError` describing the problem. Otherwise, the return value is `nil`.

#### Discussion

Given a parameter, you can get the number of keyframes for any one of its channels. For a slider, toggle button (checkbox), or angle parameter, there will be only 1 channel (indexed starting at `0`), whereas a point parameter will have 2 channels (x and y), and a color channel will have 4 (R, G, B, and A).

## Parameters

- `count`: Receives the number of keyframes in the given channel.
- `parameterID`: The ID of the parameter you want to get the keyframe count for.
- `channelIndex`: The index of the channel within the parameter that you want to retrieve the keyframe count from.

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
- [func keyframe(UnsafeMutablePointer<FxKeyframe>, forParameter: Int, channel: Int, andIndex: Int) -> (any Error)?](./keyframe%28_,forparameter,channel,andindex%29.md)
  Returns the keyframe info for the keyframe at a given index.
- [func parameter(Int, channel: Int, hasKeyframe: UnsafeMutablePointer<ObjCBool>, at: CMTime) -> (any Error)?](./parameter%28_,channel,haskeyframe,at%29.md)
  Tells whether there is a keyframe at a given time.
- [func removeAllKeyframes(forParameter: Int, andChannel: Int) -> (any Error)?](./removeallkeyframes%28forparameter,andchannel%29.md)
  Remove all keyframes from the given parameter’s channel.
- [func removeKeyframe(at: Int, fromParameter: Int, andChannel: Int) -> (any Error)?](./removekeyframe%28at,fromparameter,andchannel%29.md)
  Removes the keyframe at the given index.
- [func setKeyframeIndex(Int, with: UnsafePointer<FxKeyframe>, forParameter: Int, andChannel: Int) -> (any Error)?](./setkeyframeindex%28_,with,forparameter,andchannel%29.md)
  Sets the keyframe at the given index to have the given info.


---

*[View on Apple Developer](https://developer.apple.com/documentation/professional_video_applications/fxkeyframeapi_v3/keyframecount(_:forparameter:andchannel:))*