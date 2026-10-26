# properties(_:)

**Framework**: Professional Video Applications  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Tells the host application about what the plug-in needs and supports, such as whether it renders in a gamma-corrected color space or a linear one.

**Availability**:
- FxPlug 4.0+

## Declaration

```swift
func properties(_ properties: AutoreleasingUnsafeMutablePointer<NSDictionary>?) throws
```

```objc
- (BOOL) properties:(NSDictionary * *) properties error:(NSError * *) error;
```

## Mentions

- [Optimizing FxPlug plug-ins](https://developer.apple.com/documentation/professional-video-applications/optimizing-fxplug-plug-ins)

#### Discussion

This method is called once per plug-in instantiation and the result is cached for later use by the host application. The dictionary returned by this method should contain various `kFxPropertyKeys` and their corresponding values.

## Parameters

- `properties`: An [`NSDictionary`](../../Foundation/nsdictionary.md) containing the values of any properties you want to tell the host you support or don’t support.

## Topics

### Property Keys
- [var kFxPropertyKey_NeedsFullBuffer: String](../kfxpropertykey_needsfullbuffer.md)
  A key that determines whether the plug-in needs the entire image to do its processing, and can’t tile its rendering.
- [var kFxPropertyKey_VariesWhenParamsAreStatic: String](../kfxpropertykey_varieswhenparamsarestatic.md)
  A key that determines whether your rendering varies even when the parameters remain the same.
- [var kFxPropertyKey_ChangesOutputSize: String](../kfxpropertykey_changesoutputsize.md)
  A key that determines whether your filter has the ability to change the size of its output to be different than the size of its input.
- [var kFxPropertyKey_DesiredProcessingColorInfo: String](../kfxpropertykey_desiredprocessingcolorinfo.md)
  A key that determines whether your plug-in renders in linear or gamma-corrected color space.

## See Also

### Setting up your plug-in
- [init?(apiManager: any PROAPIAccessing)](./init%28apimanager%29-6vvaz.md)
  Initializes the API manager for your plug-in.
- [protocol PROAPIAccessing](../proapiaccessing.md)
- [func finishInitialSetup() throws](./finishinitialsetup%28%29.md)
  Finishes the initial setup and is called exactly once on first application of your plug-in to allow it to do anything else it needs to in order to finish setting itself up.
- [func pluginInstanceAddedToDocument()](./plugininstanceaddedtodocument%28%29.md)
  Notifies your plug-in when it becomes part of user’s document.


---

*[View on Apple Developer](https://developer.apple.com/documentation/professional_video_applications/fxtileableeffect/properties(_:))*