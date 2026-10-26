# getBoolValue(_:fromParameter:at:)

**Framework**: Professional Video Applications  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Gets a Boolean value from a parameter.

**Availability**:
- FxPlug 4.0+

## Declaration

```swift
func getBoolValue(_ value: UnsafeMutablePointer<ObjCBool>, fromParameter parameterID: UInt32, at time: CMTime) -> Bool
```

```objc
- (BOOL) getBoolValue:(BOOL *) value fromParameter:(UInt32) parameterID atTime:(CMTime) time;
```

#### Return Value

Returns `YES` if the value is retrieved successfully; `NO` otherwise.

#### Discussion

Depending on the host application, the time value may be relative to the start of the timeline or to the start of the clip. See [Understanding time in FxPlug](https://developer.apple.com/documentation/professional-video-applications/understanding-time-in-fxplug).

## Parameters

- `value`: Pointer to the plug-in variable for the value.
- `parameterID`: Unique identifier for the parameter.
- `time`: Specified time to get the value.

## See Also

### Instance Methods
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
- [func getRedValue(UnsafeMutablePointer<Double>, greenValue: UnsafeMutablePointer<Double>, blueValue: UnsafeMutablePointer<Double>, fromParameter: UInt32, at: CMTime) -> Bool](./getredvalue%28_,greenvalue,bluevalue,fromparameter,at%29.md)
  Gets RGB color values (in 0.0 - 1.0 floating point) from a parameter.
- [func getStringParameterValue(AutoreleasingUnsafeMutablePointer<NSString>?, fromParameter: UInt32) -> Bool](./getstringparametervalue%28_,fromparameter%29.md)
  Gets a string value from a string parameter.
- [func getXValue(UnsafeMutablePointer<Double>, yValue: UnsafeMutablePointer<Double>, fromParameter: UInt32, at: CMTime) -> Bool](./getxvalue%28_,yvalue,fromparameter,at%29.md)
  Gets the xy position value (in 0.0 - 1.0 floating point) from a parameter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/professional_video_applications/fxparameterretrievalapi_v6/getboolvalue(_:fromparameter:at:))*