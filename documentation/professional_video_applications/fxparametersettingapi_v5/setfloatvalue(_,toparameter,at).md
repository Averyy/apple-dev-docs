# setFloatValue(_:toParameter:at:)

**Framework**: Professional Video Applications  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Sets the value of a floating point parameter.

**Availability**:
- FxPlug 4.0+

## Declaration

```swift
func setFloatValue(_ value: Double, toParameter parameterID: UInt32, at time: CMTime) -> Bool
```

```objc
- (BOOL) setFloatValue:(double) value toParameter:(UInt32) parameterID atTime:(CMTime) time;
```

#### Return Value

Returns `YES` if the value is set successfully; `NO` otherwise.

#### Discussion

When used to set the value of an angle parameter, the result will be expressed in counter-clockwise degrees. Depending on the host application, the time value may be relative to the start of the timeline or to the start of the clip. See [Understanding time in FxPlug](https://developer.apple.com/documentation/professional-video-applications/understanding-time-in-fxplug).

## Parameters

- `value`: Specified value for the parameter.
- `parameterID`: Unique identifier for the parameter.
- `time`: Specified time to set the value.

## See Also

### Instance Methods
- [func setBoolValue(Bool, toParameter: UInt32, at: CMTime) -> Bool](./setboolvalue%28_,toparameter,at%29.md)
  Sets the value of a Boolean parameter.
- [func setCustomParameterValue(any NSCopying & NSSecureCoding & NSObjectProtocol, toParameter: UInt32, at: CMTime) -> Bool](./setcustomparametervalue%28_,toparameter,at%29.md)
  Sets a custom value for a custom parameter.
- [func setHistogramBlackIn(Double, blackOut: Double, whiteIn: Double, whiteOut: Double, gamma: Double, forChannel: FxHistogramChannel, fromParameter: UInt32, at: CMTime) -> Bool](./sethistogramblackin%28_,blackout,whitein,whiteout,gamma,forchannel,fromparameter,at%29.md)
  Sets the values in a histogram parameter group.
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

*[View on Apple Developer](https://developer.apple.com/documentation/professional_video_applications/fxparametersettingapi_v5/setfloatvalue(_:toparameter:at:))*