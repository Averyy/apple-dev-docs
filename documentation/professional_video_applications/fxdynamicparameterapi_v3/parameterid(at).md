# parameterID(at:)

**Framework**: Professional Video Applications  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Returns the ID of the parameter at the given index.

**Availability**:
- FxPlug 4.0+

## Declaration

```swift
func parameterID(at index: UInt32) -> UInt32
```

```objc
- (UInt32) parameterIDAtIndex:(UInt32) index;
```

## Discussion

During `-addParameters:` your plugin tells the host to create parameters. Later, while running, your plugin can create new parameters using the FxParameterCreationAPI (just like in `-addParameters`), or it can remove them using the `-removeParameter:` method of this protocol. Each parameter must have a unique ID within the plugin. This method allows you to retrieve the ID of a parameter at a given index in the list of parameters. The IDs need not be sequential or even increasing. You could for example have the following:

| Index | ID | Parameter |
| --- | --- | --- |
| `0` | `1` | `slider` |
| `1` | `1000` | `checkbox` |
| `2` | `10` | `popup menu` |

## Parameters

- `index`: The 0-based index of the parameter whose ID you wish to get.

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
- [func removeParameter(UInt32) -> (any Error)!](./removeparameter%28_%29.md)
  Removes the parameter with the passed-in ID.
- [func setAsDefaultsAt(CMTime) throws](./setasdefaultsat%28_%29.md)
  Tell the host app that the settings at the given time should be considered the default settings for every parameter in the plug-in.
- [func setParameter(UInt32, floatMinimum: Double, maximum: Double, sliderMinimum: Double, sliderMaximum: Double) -> (any Error)!](./setparameter%28_,floatminimum,maximum,sliderminimum,slidermaximum%29.md)
  Set a parameter’s bounds using floating point values.
- [func setParameter(UInt32, intMinimum: Int32, maximum: Int32, sliderMinimum: Int32, sliderMaximum: Int32) -> (any Error)!](./setparameter%28_,intminimum,maximum,sliderminimum,slidermaximum%29.md)
  Set a parameter’s bounds using integer values.
- [func setParameter(UInt32, name: String!) -> (any Error)!](./setparameter%28_,name%29.md)
  Set a parameter with a name.
- [func setPopupMenuParameter(UInt32, entries: [Any]!, defaultValue: UInt32) -> (any Error)!](./setpopupmenuparameter%28_,entries,defaultvalue%29.md)
  Set the menu entries in a pop-up menu.


---

*[View on Apple Developer](https://developer.apple.com/documentation/professional_video_applications/fxdynamicparameterapi_v3/parameterid(at:))*