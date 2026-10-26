# FxParameterSettingAPI_v5

**Framework**: Professional Video Applications  
**Kind**: protocol  
**Role**: Protocol

Defines the functions the application provides to set parameter values.

**Availability**:
- FxPlug 4.0+

## Declaration

```swift
protocol FxParameterSettingAPI_v5 : NSObjectProtocol
```

```objc
@protocol FxParameterSettingAPI_v5 <NSObject>
```

## Mentions

- [Analyzing media](https://developer.apple.com/documentation/professional-video-applications/analyzing-media)

## Topics

### Instance Methods
- [func setBoolValue(Bool, toParameter: UInt32, at: CMTime) -> Bool](./fxparametersettingapi_v5/setboolvalue%28_,toparameter,at%29.md)
  Sets the value of a Boolean parameter.
- [func setCustomParameterValue(any NSCopying & NSSecureCoding & NSObjectProtocol, toParameter: UInt32, at: CMTime) -> Bool](./fxparametersettingapi_v5/setcustomparametervalue%28_,toparameter,at%29.md)
  Sets a custom value for a custom parameter.
- [func setFloatValue(Double, toParameter: UInt32, at: CMTime) -> Bool](./fxparametersettingapi_v5/setfloatvalue%28_,toparameter,at%29.md)
  Sets the value of a floating point parameter.
- [func setHistogramBlackIn(Double, blackOut: Double, whiteIn: Double, whiteOut: Double, gamma: Double, forChannel: FxHistogramChannel, fromParameter: UInt32, at: CMTime) -> Bool](./fxparametersettingapi_v5/sethistogramblackin%28_,blackout,whitein,whiteout,gamma,forchannel,fromparameter,at%29.md)
  Sets the values in a histogram parameter group.
- [func setIntValue(Int32, toParameter: UInt32, at: CMTime) -> Bool](./fxparametersettingapi_v5/setintvalue%28_,toparameter,at%29.md)
  Sets the value of an integer parameter.
- [func setParameterFlags(FxParameterFlags, toParameter: UInt32) -> Bool](./fxparametersettingapi_v5/setparameterflags%28_,toparameter%29.md)
  Sets the flags for the state of a parameter.
- [func setPathID(FxPathID, toParameter: UInt32, at: CMTime) -> Bool](./fxparametersettingapi_v5/setpathid%28_,toparameter,at%29.md)
  Sets a custom value for a custom parameter.
- [func setRedValue(Double, greenValue: Double, blueValue: Double, alphaValue: Double, toParameter: UInt32, at: CMTime) -> Bool](./fxparametersettingapi_v5/setredvalue%28_,greenvalue,bluevalue,alphavalue,toparameter,at%29.md)
  Sets the value of an RGBA color parameter.
- [func setRedValue(Double, greenValue: Double, blueValue: Double, toParameter: UInt32, at: CMTime) -> Bool](./fxparametersettingapi_v5/setredvalue%28_,greenvalue,bluevalue,toparameter,at%29.md)
  Set the values of an RGB color parameter.
- [func setStringParameterValue(String, toParameter: UInt32) -> Bool](./fxparametersettingapi_v5/setstringparametervalue%28_,toparameter%29.md)
  Sets a string value for a string parameter.
- [func setXValue(Double, yValue: Double, toParameter: UInt32, at: CMTime) -> Bool](./fxparametersettingapi_v5/setxvalue%28_,yvalue,toparameter,at%29.md)
  Sets the xy values for a position parameter.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
### Inherited By
- [FxParameterSettingAPI_v6](./fxparametersettingapi_v6.md)

## See Also

### Parameter APIs
- [protocol FxParameterCreationAPI_v5](./fxparametercreationapi_v5.md)
  Defines the methods provided by the host application to create parameters.
- [protocol FxParameterRetrievalAPI_v6](./fxparameterretrievalapi_v6.md)
  Defines the functions the application provides to retrieve parameter values.
- [protocol FxParameterRetrievalAPI_v7](./fxparameterretrievalapi_v7.md)
  Adds a method to retrieve the image information about an image parameter.
- [protocol FxParameterSettingAPI_v6](./fxparametersettingapi_v6.md)
  Defines the functions the application provides to set parameter flags.
- [protocol FxDynamicParameterAPI_v3](./fxdynamicparameterapi_v3.md)
  Allows your plugin to create parameters on-the-fly.


---

*[View on Apple Developer](https://developer.apple.com/documentation/professional_video_applications/fxparametersettingapi_v5)*