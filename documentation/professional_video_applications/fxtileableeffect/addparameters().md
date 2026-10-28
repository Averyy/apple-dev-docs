# addParameters()

**Framework**: Professional Video Applications  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Tells the host application what parameters your plug-in requires.

**Availability**:
- FxPlug 4.0+

## Declaration

```swift
func addParameters() throws
```

```objc
- (BOOL) addParametersWithError:(NSError * *) error;
```

## Mentions

- [Adding parameters to plug-ins](../../Professional-Video-Applications/adding-parameters-to-plug-ins.md)
- [Analyzing media](../../Professional-Video-Applications/analyzing-media.md)
- [Building an FxPlug plug-in manually](../../Professional-Video-Applications/building-an-fxplug-plug-in-manually.md)
- [Using FxPlug APIs](../../Professional-Video-Applications/using-fxplug-apis.md)

## Discussion

Use the `apiManager` object that was passed to your [`init(apiManager:)`](./init%28apimanager%29-6vvaz.md) method to obtain an `FxParameterCreation*` object. Tell the parameter creation API object which types of parameters your plug-in needs. This method is only called at most once per instance of your plug-in. It will not be called when loading a document which contains your plug-in.

## See Also

### Adding and setting parameters
- [func `class`(forCustomParameterID: UInt32) -> AnyClass](./class%28forcustomparameterid%29.md)
  Returns the class of the object contained in the custom parameter with the given ID.
- [func classes(forCustomParameterID: UInt32) -> Set<AnyHashable>](./classes%28forcustomparameterid%29.md)
  Returns the classes of the objects contained in the custom parameter with the given ID.
- [func parameterChanged(UInt32, at: CMTime) throws](./parameterchanged%28_,at%29.md)
  Executes when the host detects that a parameter has changed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/professional_video_applications/fxtileableeffect/addparameters())*