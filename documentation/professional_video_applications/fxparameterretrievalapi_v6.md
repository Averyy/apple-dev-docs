# FxParameterRetrievalAPI_v6

**Framework**: Professional Video Applications  
**Kind**: protocol  
**Role**: Protocol

Defines the functions the application provides to retrieve parameter values.

**Availability**:
- FxPlug 4.0+

## Declaration

```swift
protocol FxParameterRetrievalAPI_v6 : NSObjectProtocol
```

```objc
@protocol FxParameterRetrievalAPI_v6 <NSObject>
```

## Mentions

- [Adding onscreen controls to plug-ins](https://developer.apple.com/documentation/professional-video-applications/adding-onscreen-controls-to-plug-ins)
- [Communicating with the plug-in state](https://developer.apple.com/documentation/professional-video-applications/communicating-with-the-plug-in-state)
- [Using FxPlug APIs](https://developer.apple.com/documentation/professional-video-applications/using-fxplug-apis)

## Topics

### Instance Methods
- [func getBoolValue(UnsafeMutablePointer<ObjCBool>, fromParameter: UInt32, at: CMTime) -> Bool](./fxparameterretrievalapi_v6/getboolvalue%28_,fromparameter,at%29.md)
  Gets a Boolean value from a parameter.
- [func getCustomParameterValue(AutoreleasingUnsafeMutablePointer<(any NSCopying & NSSecureCoding & NSObjectProtocol)?>, fromParameter: UInt32, at: CMTime) -> Bool](./fxparameterretrievalapi_v6/getcustomparametervalue%28_,fromparameter,at%29.md)
  Retrieves the (possibly keyframed) value of a custom parameter at a given time.
- [func getFloatValue(UnsafeMutablePointer<Double>, fromParameter: UInt32, at: CMTime) -> Bool](./fxparameterretrievalapi_v6/getfloatvalue%28_,fromparameter,at%29.md)
  Gets a floating point value from a parameter.
- [func getFontName(AutoreleasingUnsafeMutablePointer<NSString?>, fromParameter: UInt32, at: CMTime) -> Bool](./fxparameterretrievalapi_v6/getfontname%28_,fromparameter,at%29.md)
  Retrieves the family and typeface of a given font.
- [func getGradientSamples(UnsafeMutableRawPointer, numSamples: Int, depth: FxDepth, fromParameter: UInt32, at: CMTime) -> Bool](./fxparameterretrievalapi_v6/getgradientsamples%28_,numsamples,depth,fromparameter,at%29.md)
  Gets the Gradient parameter settings.
- [func getHistogramBlack(in: UnsafeMutablePointer<Double>, blackOut: UnsafeMutablePointer<Double>, whiteIn: UnsafeMutablePointer<Double>, whiteOut: UnsafeMutablePointer<Double>, gamma: UnsafeMutablePointer<Double>, forChannel: FxHistogramChannel, fromParameter: UInt32, at: CMTime) -> Bool](./fxparameterretrievalapi_v6/gethistogramblack%28in,blackout,whitein,whiteout,gamma,forchannel,fromparameter,at%29.md)
  Gets the Histogram parameter settings.
- [func getIntValue(UnsafeMutablePointer<Int32>, fromParameter: UInt32, at: CMTime) -> Bool](./fxparameterretrievalapi_v6/getintvalue%28_,fromparameter,at%29.md)
  Gets an integer value from a parameter.
- [func getParameterFlags(UnsafeMutablePointer<FxParameterFlags>, fromParameter: UInt32) -> Bool](./fxparameterretrievalapi_v6/getparameterflags%28_,fromparameter%29.md)
  Gets current state of a parameter.
- [func getPathID(UnsafeMutablePointer<FxPathID?>, fromParameter: UInt32, at: CMTime) -> Bool](./fxparameterretrievalapi_v6/getpathid%28_,fromparameter,at%29.md)
  Retrieves the (possibly keyframed) value of a pathID parameter at a given time.
- [func getRedValue(UnsafeMutablePointer<Double>, greenValue: UnsafeMutablePointer<Double>, blueValue: UnsafeMutablePointer<Double>, alphaValue: UnsafeMutablePointer<Double>, fromParameter: UInt32, at: CMTime) -> Bool](./fxparameterretrievalapi_v6/getredvalue%28_,greenvalue,bluevalue,alphavalue,fromparameter,at%29.md)
  Gets RGBA color value (in 0.0 - 1.0 floating point) from a parameter.
- [func getRedValue(UnsafeMutablePointer<Double>, greenValue: UnsafeMutablePointer<Double>, blueValue: UnsafeMutablePointer<Double>, fromParameter: UInt32, at: CMTime) -> Bool](./fxparameterretrievalapi_v6/getredvalue%28_,greenvalue,bluevalue,fromparameter,at%29.md)
  Gets RGB color values (in 0.0 - 1.0 floating point) from a parameter.
- [func getStringParameterValue(AutoreleasingUnsafeMutablePointer<NSString>?, fromParameter: UInt32) -> Bool](./fxparameterretrievalapi_v6/getstringparametervalue%28_,fromparameter%29.md)
  Gets a string value from a string parameter.
- [func getXValue(UnsafeMutablePointer<Double>, yValue: UnsafeMutablePointer<Double>, fromParameter: UInt32, at: CMTime) -> Bool](./fxparameterretrievalapi_v6/getxvalue%28_,yvalue,fromparameter,at%29.md)
  Gets the xy position value (in 0.0 - 1.0 floating point) from a parameter.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
### Inherited By
- [FxParameterRetrievalAPI_v7](./fxparameterretrievalapi_v7.md)

## See Also

### Parameter APIs
- [protocol FxParameterCreationAPI_v5](./fxparametercreationapi_v5.md)
  Defines the methods provided by the host application to create parameters.
- [protocol FxParameterRetrievalAPI_v7](./fxparameterretrievalapi_v7.md)
  Adds a method to retrieve the image information about an image parameter.
- [protocol FxParameterSettingAPI_v5](./fxparametersettingapi_v5.md)
  Defines the functions the application provides to set parameter values.
- [protocol FxParameterSettingAPI_v6](./fxparametersettingapi_v6.md)
  Defines the functions the application provides to set parameter flags.
- [protocol FxDynamicParameterAPI_v3](./fxdynamicparameterapi_v3.md)
  Allows your plugin to create parameters on-the-fly.


---

*[View on Apple Developer](https://developer.apple.com/documentation/professional_video_applications/fxparameterretrievalapi_v6)*