# getHistogramBlack(in:blackOut:whiteIn:whiteOut:gamma:forChannel:fromParameter:at:)

**Framework**: Professional Video Applications  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Gets the Histogram parameter settings.

**Availability**:
- FxPlug 4.0+

## Declaration

```swift
func getHistogramBlack(in blackIn: UnsafeMutablePointer<Double>, blackOut: UnsafeMutablePointer<Double>, whiteIn: UnsafeMutablePointer<Double>, whiteOut: UnsafeMutablePointer<Double>, gamma: UnsafeMutablePointer<Double>, forChannel channel: FxHistogramChannel, fromParameter parameterID: UInt32, at time: CMTime) -> Bool
```

```objc
- (BOOL) getHistogramBlackIn:(double *) blackIn BlackOut:(double *) blackOut WhiteIn:(double *) whiteIn WhiteOut:(double *) whiteOut Gamma:(double *) gamma forChannel:(FxHistogramChannel) channel fromParameter:(UInt32) parameterID atTime:(CMTime) time;
```

#### Return Value

Returns `YES` if the value is retrieved successfully; `NO` otherwise.

#### Discussion

Depending on the host application, the time value may be relative to the start of the timeline or to the start of the clip. See [Understanding time in FxPlug](../../Professional-Video-Applications/understanding-time-in-fxplug.md).

## Parameters

- `blackIn`: Pointer for the parameter black in level value.
- `blackOut`: Pointer for the parameter black out level value.
- `whiteIn`: Pointer for the parameter white in level value.
- `whiteOut`: Pointer for the parameter white out level value.
- `gamma`: Pointer for the parameter gamma level value.
- `channel`: Specified channel for the histogram information (RGB: `0`, Red: `1`, Green: `2`, Blue: `3`, Alpha: `4`).
- `parameterID`: Unique identifier for the parameter.
- `time`: Specified time to get the values.

## See Also

### Instance Methods
- [func getBoolValue(UnsafeMutablePointer<ObjCBool>, fromParameter: UInt32, at: CMTime) -> Bool](./getboolvalue%28_,fromparameter,at%29.md)
  Gets a Boolean value from a parameter.
- [func getCustomParameterValue(AutoreleasingUnsafeMutablePointer<(any NSCopying & NSSecureCoding & NSObjectProtocol)?>, fromParameter: UInt32, at: CMTime) -> Bool](./getcustomparametervalue%28_,fromparameter,at%29.md)
  Retrieves the (possibly keyframed) value of a custom parameter at a given time.
- [func getFloatValue(UnsafeMutablePointer<Double>, fromParameter: UInt32, at: CMTime) -> Bool](./getfloatvalue%28_,fromparameter,at%29.md)
  Gets a floating point value from a parameter.
- [func getFontName(AutoreleasingUnsafeMutablePointer<NSString?>, fromParameter: UInt32, at: CMTime) -> Bool](./getfontname%28_,fromparameter,at%29.md)
  Retrieves the family and typeface of a given font.
- [func getGradientSamples(UnsafeMutableRawPointer, numSamples: Int, depth: FxDepth, fromParameter: UInt32, at: CMTime) -> Bool](./getgradientsamples%28_,numsamples,depth,fromparameter,at%29.md)
  Gets the Gradient parameter settings.
- [func getIntValue(UnsafeMutablePointer<Int32>, fromParameter: UInt32, at: CMTime) -> Bool](./getintvalue%28_,fromparameter,at%29.md)
  Gets an integer value from a parameter.
- [func getParameterFlags(UnsafeMutablePointer<FxParameterFlags>, fromParameter: UInt32) -> Bool](./getparameterflags%28_,fromparameter%29.md)
  Gets current state of a parameter.
- [func getPathID(UnsafeMutablePointer<FxPathID?>, fromParameter: UInt32, at: CMTime) -> Bool](./getpathid%28_,fromparameter,at%29.md)
  Retrieves the (possibly keyframed) value of a pathID parameter at a given time.
- [func getRedValue(UnsafeMutablePointer<Double>, greenValue: UnsafeMutablePointer<Double>, blueValue: UnsafeMutablePointer<Double>, alphaValue: UnsafeMutablePointer<Double>, fromParameter: UInt32, at: CMTime) -> Bool](./getredvalue%28_,greenvalue,bluevalue,alphavalue,fromparameter,at%29.md)
  Gets RGBA color value (in 0.0 - 1.0 floating point) from a parameter.
- [func getRedValue(UnsafeMutablePointer<Double>, greenValue: UnsafeMutablePointer<Double>, blueValue: UnsafeMutablePointer<Double>, fromParameter: UInt32, at: CMTime) -> Bool](./getredvalue%28_,greenvalue,bluevalue,fromparameter,at%29.md)
  Gets RGB color values (in 0.0 - 1.0 floating point) from a parameter.
- [func getStringParameterValue(AutoreleasingUnsafeMutablePointer<NSString>?, fromParameter: UInt32) -> Bool](./getstringparametervalue%28_,fromparameter%29.md)
  Gets a string value from a string parameter.
- [func getXValue(UnsafeMutablePointer<Double>, yValue: UnsafeMutablePointer<Double>, fromParameter: UInt32, at: CMTime) -> Bool](./getxvalue%28_,yvalue,fromparameter,at%29.md)
  Gets the xy position value (in 0.0 - 1.0 floating point) from a parameter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/professional_video_applications/fxparameterretrievalapi_v6/gethistogramblack(in:blackout:whitein:whiteout:gamma:forchannel:fromparameter:at:))*