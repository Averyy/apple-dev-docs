# setStringParameterValue(_:toParameter:)

**Framework**: Professional Video Applications  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Sets a string value for a string parameter.

**Availability**:
- FxPlug 4.0+

## Declaration

```swift
func setStringParameterValue(_ string: String, toParameter parameterID: UInt32) -> Bool
```

```objc
- (BOOL) setStringParameterValue:(NSString *) string toParameter:(UInt32) parameterID;
```

#### Return Value

Returns `YES` if the value is set successfully; `NO` otherwise.

## Parameters

- `string`: Specified string value for the parameter
- `parameterID`: Unique identifier for the parameter.

## See Also

### Instance Methods
- [func setBoolValue(Bool, toParameter: UInt32, at: CMTime) -> Bool](./setboolvalue%28_,toparameter,at%29.md)
  Sets the value of a Boolean parameter.
- [func setCustomParameterValue(any NSCopying & NSSecureCoding & NSObjectProtocol, toParameter: UInt32, at: CMTime) -> Bool](./setcustomparametervalue%28_,toparameter,at%29.md)
  Sets a custom value for a custom parameter.
- [func setFloatValue(Double, toParameter: UInt32, at: CMTime) -> Bool](./setfloatvalue%28_,toparameter,at%29.md)
  Sets the value of a floating point parameter.
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
- [func setXValue(Double, yValue: Double, toParameter: UInt32, at: CMTime) -> Bool](./setxvalue%28_,yvalue,toparameter,at%29.md)
  Sets the xy values for a position parameter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/professional_video_applications/fxparametersettingapi_v5/setstringparametervalue(_:toparameter:))*