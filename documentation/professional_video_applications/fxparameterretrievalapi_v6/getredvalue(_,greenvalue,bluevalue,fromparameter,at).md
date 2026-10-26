# getRedValue(_:greenValue:blueValue:fromParameter:at:)

**Framework**: Professional Video Applications  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Gets RGB color values (in 0.0 - 1.0 floating point) from a parameter.

**Availability**:
- FxPlug 4.0+

## Declaration

```swift
func getRedValue(_ red: UnsafeMutablePointer<Double>, greenValue green: UnsafeMutablePointer<Double>, blueValue blue: UnsafeMutablePointer<Double>, fromParameter parameterID: UInt32, at time: CMTime) -> Bool
```

```objc
- (BOOL) getRedValue:(double *) red greenValue:(double *) green blueValue:(double *) blue fromParameter:(UInt32) parameterID atTime:(CMTime) time;
```

#### Return Value

Returns `YES` if the values are retrieved successfully; otherwise `NO`.

#### Discussion

The returned color values are in the project working color space, unless the parameter has the [`kFxParameterFlag_DONT_REMAP_COLORS`](../kfxparameterflag_dont_remap_colors.md) flag set. If this flag is set, the color values are copied verbatim from the parameter with no conversion.

Depending on the host application, the time value may be relative to the start of the timeline or to the start of the clip. See [Understanding time in FxPlug](../../Professional-Video-Applications/understanding-time-in-fxplug.md).

## Parameters

- `red`: The pointer to the plug-in variable for the red value.
- `green`: The pointer to the plug-in variable for the green value.
- `blue`: The pointer to the plug-in variable for the blue value.
- `parameterID`: The unique identifier for the parameter.
- `time`: The specified time to get the values.

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
- [func getHistogramBlack(in: UnsafeMutablePointer<Double>, blackOut: UnsafeMutablePointer<Double>, whiteIn: UnsafeMutablePointer<Double>, whiteOut: UnsafeMutablePointer<Double>, gamma: UnsafeMutablePointer<Double>, forChannel: FxHistogramChannel, fromParameter: UInt32, at: CMTime) -> Bool](./gethistogramblack%28in,blackout,whitein,whiteout,gamma,forchannel,fromparameter,at%29.md)
  Gets the Histogram parameter settings.
- [func getIntValue(UnsafeMutablePointer<Int32>, fromParameter: UInt32, at: CMTime) -> Bool](./getintvalue%28_,fromparameter,at%29.md)
  Gets an integer value from a parameter.
- [func getParameterFlags(UnsafeMutablePointer<FxParameterFlags>, fromParameter: UInt32) -> Bool](./getparameterflags%28_,fromparameter%29.md)
  Gets current state of a parameter.
- [func getPathID(UnsafeMutablePointer<FxPathID?>, fromParameter: UInt32, at: CMTime) -> Bool](./getpathid%28_,fromparameter,at%29.md)
  Retrieves the (possibly keyframed) value of a pathID parameter at a given time.
- [func getRedValue(UnsafeMutablePointer<Double>, greenValue: UnsafeMutablePointer<Double>, blueValue: UnsafeMutablePointer<Double>, alphaValue: UnsafeMutablePointer<Double>, fromParameter: UInt32, at: CMTime) -> Bool](./getredvalue%28_,greenvalue,bluevalue,alphavalue,fromparameter,at%29.md)
  Gets RGBA color value (in 0.0 - 1.0 floating point) from a parameter.
- [func getStringParameterValue(AutoreleasingUnsafeMutablePointer<NSString>?, fromParameter: UInt32) -> Bool](./getstringparametervalue%28_,fromparameter%29.md)
  Gets a string value from a string parameter.
- [func getXValue(UnsafeMutablePointer<Double>, yValue: UnsafeMutablePointer<Double>, fromParameter: UInt32, at: CMTime) -> Bool](./getxvalue%28_,yvalue,fromparameter,at%29.md)
  Gets the xy position value (in 0.0 - 1.0 floating point) from a parameter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/professional_video_applications/fxparameterretrievalapi_v6/getredvalue(_:greenvalue:bluevalue:fromparameter:at:))*