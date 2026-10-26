# FxParameterSettingAPI_v6

**Framework**: Professional Video Applications  
**Kind**: protocol  
**Role**: Protocol

Defines the functions the application provides to set parameter flags.

**Availability**:
- FxPlug 4.2.2+

## Declaration

```swift
protocol FxParameterSettingAPI_v6 : FxParameterSettingAPI_v5
```

```objc
@protocol FxParameterSettingAPI_v6 <FxParameterSettingAPI_v5>
```

## Topics

### Instance Methods
- [func addFlags(FxParameterFlags, toParameter: UInt32) -> Bool](./fxparametersettingapi_v6/addflags%28_,toparameter%29.md)
  Add new parameter flags to the current flags for a parameter.
- [func removeFlags(FxParameterFlags, fromParameter: UInt32) -> Bool](./fxparametersettingapi_v6/removeflags%28_,fromparameter%29.md)
  Remove parameter flags from the current flags for a parameter.

## Relationships

### Inherits From
- [FxParameterSettingAPI_v5](./fxparametersettingapi_v5.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Parameter APIs
- [protocol FxParameterCreationAPI_v5](./fxparametercreationapi_v5.md)
  Defines the methods provided by the host application to create parameters.
- [protocol FxParameterRetrievalAPI_v6](./fxparameterretrievalapi_v6.md)
  Defines the functions the application provides to retrieve parameter values.
- [protocol FxParameterRetrievalAPI_v7](./fxparameterretrievalapi_v7.md)
  Adds a method to retrieve the image information about an image parameter.
- [protocol FxParameterSettingAPI_v5](./fxparametersettingapi_v5.md)
  Defines the functions the application provides to set parameter values.
- [protocol FxDynamicParameterAPI_v3](./fxdynamicparameterapi_v3.md)
  Allows your plugin to create parameters on-the-fly.


---

*[View on Apple Developer](https://developer.apple.com/documentation/professional_video_applications/fxparametersettingapi_v6)*