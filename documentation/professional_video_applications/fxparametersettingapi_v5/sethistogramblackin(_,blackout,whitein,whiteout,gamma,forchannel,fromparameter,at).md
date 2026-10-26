# setHistogramBlackIn(_:blackOut:whiteIn:whiteOut:gamma:forChannel:fromParameter:at:)

**Framework**: Professional Video Applications  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Sets the values in a histogram parameter group.

**Availability**:
- FxPlug 4.0+

## Declaration

```swift
func setHistogramBlackIn(_ blackIn: Double, blackOut: Double, whiteIn: Double, whiteOut: Double, gamma: Double, forChannel channel: FxHistogramChannel, fromParameter parameterID: UInt32, at time: CMTime) -> Bool
```

```objc
- (BOOL) setHistogramBlackIn:(double) blackIn blackOut:(double) blackOut whiteIn:(double) whiteIn whiteOut:(double) whiteOut gamma:(double) gamma forChannel:(FxHistogramChannel) channel fromParameter:(UInt32) parameterID atTime:(CMTime) time;
```

#### Return Value

Returns `YES` if the values are set successfully; `NO` otherwise.

#### Discussion

Depending on the host application, the time value may be relative to the start of the timeline or to the start of the clip. See [Understanding time in FxPlug](https://developer.apple.com/documentation/professional-video-applications/understanding-time-in-fxplug).

## Parameters

- `blackIn`: The new black in level value.
- `blackOut`: The new black out level value.
- `whiteIn`: The new white in level value.
- `whiteOut`: The new white out level value.
- `gamma`: The new gamma level value.
- `channel`: Specified channel for new histogram values (RGB: `0`, Red: `1`, Green: `2`, Blue: `3`, Alpha: `4`).
- `parameterID`: Parameter identifier assigned upon creation.
- `time`: Specified time to set the values.

## See Also

### Instance Methods
- [func setBoolValue(Bool, toParameter: UInt32, at: CMTime) -> Bool](./setboolvalue%28_,toparameter,at%29.md)
  Sets the value of a Boolean parameter.
- [func setCustomParameterValue(any NSCopying & NSSecureCoding & NSObjectProtocol, toParameter: UInt32, at: CMTime) -> Bool](./setcustomparametervalue%28_,toparameter,at%29.md)
  Sets a custom value for a custom parameter.
- [func setFloatValue(Double, toParameter: UInt32, at: CMTime) -> Bool](./setfloatvalue%28_,toparameter,at%29.md)
  Sets the value of a floating point parameter.
- [func setIntValue(Int32, toParameter: UInt32, at: CMTime) -> Bool](./setintvalue%28_,toparameter,at%29.md)
  Sets the value of an integer parameter.
- [func setParameterFlags(FxParameterFlags, toParameter: UInt32) -> Bool](./setparameterflags%28_,toparameter%29.md)
  Sets the flags for the state of a parameter.
- [func setPathID(FxPathID, toParameter: UInt32, at: CMTime) -> Bool](./setpathid%28_,toparameter,at%29.md)
  Sets a custom value for a custom parameter.
- [func setRedValue(Double, greenValue: Double, blueValue: Double, alphaValue: Double, toParameter: UInt32, at: CMTime) -> Bool](./setredvalue%28_,greenvalue,bluevalue,alphavalue,toparameter,at%29.md)
  Sets the value of an RGBA color parameter.
- [func setRedValue(Double, greenValue: Double, blueValue: Double, toParameter: UInt32, at: CMTime) -> Bool](./setredvalue%28_,greenvalue,bluevalue,toparameter,at%29.md)
  Set the values of an RGB color parameter.
- [func setStringParameterValue(String, toParameter: UInt32) -> Bool](./setstringparametervalue%28_,toparameter%29.md)
  Sets a string value for a string parameter.
- [func setXValue(Double, yValue: Double, toParameter: UInt32, at: CMTime) -> Bool](./setxvalue%28_,yvalue,toparameter,at%29.md)
  Sets the xy values for a position parameter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/professional_video_applications/fxparametersettingapi_v5/sethistogramblackin(_:blackout:whitein:whiteout:gamma:forchannel:fromparameter:at:))*