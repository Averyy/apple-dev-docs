# setAsDefaultsAt(_:)

**Framework**: Professional Video Applications  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Tell the host app that the settings at the given time should be considered the default settings for every parameter in the plug-in.

**Availability**:
- FxPlug 4.0+

## Declaration

```swift
func setAsDefaultsAt(_ time: CMTime) throws
```

```objc
- (BOOL) setAsDefaultsAtTime:(CMTime) time withError:(NSError * *) error;
```

## See Also

### Instance Methods
- [func parameter(UInt32, floatMinimum: UnsafeMutablePointer<Double>!, maximum: UnsafeMutablePointer<Double>!, sliderMinimum: UnsafeMutablePointer<Double>!, sliderMaximum: UnsafeMutablePointer<Double>!) -> (any Error)!](./parameter%28_,floatminimum,maximum,sliderminimum,slidermaximum%29.md)
  Get a parameter’s bounds as floating point values.
- [func parameter(UInt32, intMinimum: UnsafeMutablePointer<Int32>!, maximum: UnsafeMutablePointer<Int32>!, sliderMinimum: UnsafeMutablePointer<Int32>!, sliderMaximum: UnsafeMutablePointer<Int32>!) -> (any Error)!](./parameter%28_,intminimum,maximum,sliderminimum,slidermaximum%29.md)
  Get a parameter’s bounds as integer values.
- [func parameter(UInt32, name: AutoreleasingUnsafeMutablePointer<NSString?>!) -> (any Error)!](./parameter%28_,name%29.md)
  Get a parameter’s name.
- [func parameterCount() -> UInt32](./parametercount%28%29.md)
  Returns the number of parameters your plug-in currently has.
- [func parameterID(at: UInt32) -> UInt32](./parameterid%28at%29.md)
  Returns the ID of the parameter at the given index.
- [func removeParameter(UInt32) -> (any Error)!](./removeparameter%28_%29.md)
  Removes the parameter with the passed-in ID.
- [func setParameter(UInt32, floatMinimum: Double, maximum: Double, sliderMinimum: Double, sliderMaximum: Double) -> (any Error)!](./setparameter%28_,floatminimum,maximum,sliderminimum,slidermaximum%29.md)
  Set a parameter’s bounds using floating point values.
- [func setParameter(UInt32, intMinimum: Int32, maximum: Int32, sliderMinimum: Int32, sliderMaximum: Int32) -> (any Error)!](./setparameter%28_,intminimum,maximum,sliderminimum,slidermaximum%29.md)
  Set a parameter’s bounds using integer values.
- [func setParameter(UInt32, name: String!) -> (any Error)!](./setparameter%28_,name%29.md)
  Set a parameter with a name.
- [func setPopupMenuParameter(UInt32, entries: [Any]!, defaultValue: UInt32) -> (any Error)!](./setpopupmenuparameter%28_,entries,defaultvalue%29.md)
  Set the menu entries in a pop-up menu.


---

*[View on Apple Developer](https://developer.apple.com/documentation/professional_video_applications/fxdynamicparameterapi_v3/setasdefaultsat(_:))*