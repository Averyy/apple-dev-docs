# FxParameterRetrievalAPI_v7

**Framework**: Professional Video Applications  
**Kind**: protocol  
**Role**: Protocol

Adds a method to retrieve the image information about an image parameter.

**Availability**:
- FxPlug 4.2+

## Declaration

```swift
protocol FxParameterRetrievalAPI_v7 : FxParameterRetrievalAPI_v6
```

```objc
@protocol FxParameterRetrievalAPI_v7 <FxParameterRetrievalAPI_v6>
```

## Mentions

- [Managing color space and gamut in plug-ins](../Professional-Video-Applications/managing-color-space-and-gamut-in-plug-ins.md)

## Topics

### Instance Methods
- [func imageSize(UnsafeMutablePointer<CGSize>, fromParameter: UInt32, at: CMTime) throws](./fxparameterretrievalapi_v7/imagesize%28_,fromparameter,at%29.md)
  Provides the dimensions of the image well image when it is at 100-percent scale and has square pixels.

## Relationships

### Inherits From
- [FxParameterRetrievalAPI_v6](./fxparameterretrievalapi_v6.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Parameter APIs
- [protocol FxParameterCreationAPI_v5](./fxparametercreationapi_v5.md)
  Defines the methods provided by the host application to create parameters.
- [protocol FxParameterRetrievalAPI_v6](./fxparameterretrievalapi_v6.md)
  Defines the functions the application provides to retrieve parameter values.
- [protocol FxParameterSettingAPI_v5](./fxparametersettingapi_v5.md)
  Defines the functions the application provides to set parameter values.
- [protocol FxParameterSettingAPI_v6](./fxparametersettingapi_v6.md)
  Defines the functions the application provides to set parameter flags.
- [protocol FxDynamicParameterAPI_v3](./fxdynamicparameterapi_v3.md)
  Allows your plugin to create parameters on-the-fly.


---

*[View on Apple Developer](https://developer.apple.com/documentation/professional_video_applications/fxparameterretrievalapi_v7)*