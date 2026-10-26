# parameterChanged(_:at:)

**Framework**: Professional Video Applications  
**Kind**: method  
**Role**: Instance Method

Executes when the host detects that a parameter has changed.

**Availability**:
- FxPlug 4.0+

## Declaration

```swift
optional func parameterChanged(_ paramID: UInt32, at time: CMTime) throws
```

```objc
- (BOOL) parameterChanged:(UInt32) paramID atTime:(CMTime) time error:(NSError * *) error;
```

## Mentions

- [Adding parameters to plug-ins](https://developer.apple.com/documentation/professional-video-applications/adding-parameters-to-plug-ins)
- [Building an FxPlug plug-in manually](https://developer.apple.com/documentation/professional-video-applications/building-an-fxplug-plug-in-manually)
- [Thread safety in plug-ins](https://developer.apple.com/documentation/professional-video-applications/thread-safety-in-plug-ins)
- [Versioning and obsoleting old plug-ins](https://developer.apple.com/documentation/professional-video-applications/versioning-and-obsoleting-old-plug-ins)

#### Discussion

Use this method to change, enable, disable, hide, or show other parameters. This method is called each time the user changes a parameter. You can use this method to update other parameters (such as hiding or showing them). You have full access to the [`FxParameterCreationAPI_v5`](../fxparametercreationapi_v5.md) or later, [`FxParameterRetrievalAPI_v6`](../fxparameterretrievalapi_v6.md) or later, and [`FxParameterSettingAPI_v5`](../fxparametersettingapi_v5.md) or later, within this method.

## Parameters

- `paramID`: The ID of the parameter that changed.
- `time`: The rational time at which the parameter changed.

## See Also

### Adding and setting parameters
- [func addParameters() throws](./addparameters%28%29.md)
  Tells the host application what parameters your plug-in requires.
- [func `class`(forCustomParameterID: UInt32) -> AnyClass](./class%28forcustomparameterid%29.md)
  Returns the class of the object contained in the custom parameter with the given ID.
- [func classes(forCustomParameterID: UInt32) -> Set<AnyHashable>](./classes%28forcustomparameterid%29.md)
  Returns the classes of the objects contained in the custom parameter with the given ID.


---

*[View on Apple Developer](https://developer.apple.com/documentation/professional_video_applications/fxtileableeffect/parameterchanged(_:at:))*