# FxDynamicParameterAPI_v3

**Framework**: Professional Video Applications  
**Kind**: protocol  
**Role**: Protocol

Allows your plugin to create parameters on-the-fly.

**Availability**:
- FxPlug 4.0+

## Declaration

```swift
protocol FxDynamicParameterAPI_v3
```

```objc
@protocol FxDynamicParameterAPI_v3
```

## Overview

With this API your plugin can create and remove parameters outside of its `-addParameters` method. It can also get and set various properties of parameters during run-time, as well, such as the minimum and maximum allowable values.

## Topics

### Instance Methods
- [func parameter(UInt32, floatMinimum: UnsafeMutablePointer<Double>!, maximum: UnsafeMutablePointer<Double>!, sliderMinimum: UnsafeMutablePointer<Double>!, sliderMaximum: UnsafeMutablePointer<Double>!) -> (any Error)!](./fxdynamicparameterapi_v3/parameter%28_,floatminimum,maximum,sliderminimum,slidermaximum%29.md)
  Get a parameter’s bounds as floating point values.
- [func parameter(UInt32, intMinimum: UnsafeMutablePointer<Int32>!, maximum: UnsafeMutablePointer<Int32>!, sliderMinimum: UnsafeMutablePointer<Int32>!, sliderMaximum: UnsafeMutablePointer<Int32>!) -> (any Error)!](./fxdynamicparameterapi_v3/parameter%28_,intminimum,maximum,sliderminimum,slidermaximum%29.md)
  Get a parameter’s bounds as integer values.
- [func parameter(UInt32, name: AutoreleasingUnsafeMutablePointer<NSString?>!) -> (any Error)!](./fxdynamicparameterapi_v3/parameter%28_,name%29.md)
  Get a parameter’s name.
- [func parameterCount() -> UInt32](./fxdynamicparameterapi_v3/parametercount%28%29.md)
  Returns the number of parameters your plug-in currently has.
- [func parameterID(at: UInt32) -> UInt32](./fxdynamicparameterapi_v3/parameterid%28at%29.md)
  Returns the ID of the parameter at the given index.
- [func removeParameter(UInt32) -> (any Error)!](./fxdynamicparameterapi_v3/removeparameter%28_%29.md)
  Removes the parameter with the passed-in ID.
- [func setAsDefaultsAt(CMTime) throws](./fxdynamicparameterapi_v3/setasdefaultsat%28_%29.md)
  Tell the host app that the settings at the given time should be considered the default settings for every parameter in the plug-in.
- [func setParameter(UInt32, floatMinimum: Double, maximum: Double, sliderMinimum: Double, sliderMaximum: Double) -> (any Error)!](./fxdynamicparameterapi_v3/setparameter%28_,floatminimum,maximum,sliderminimum,slidermaximum%29.md)
  Set a parameter’s bounds using floating point values.
- [func setParameter(UInt32, intMinimum: Int32, maximum: Int32, sliderMinimum: Int32, sliderMaximum: Int32) -> (any Error)!](./fxdynamicparameterapi_v3/setparameter%28_,intminimum,maximum,sliderminimum,slidermaximum%29.md)
  Set a parameter’s bounds using integer values.
- [func setParameter(UInt32, name: String!) -> (any Error)!](./fxdynamicparameterapi_v3/setparameter%28_,name%29.md)
  Set a parameter with a name.
- [func setPopupMenuParameter(UInt32, entries: [Any]!, defaultValue: UInt32) -> (any Error)!](./fxdynamicparameterapi_v3/setpopupmenuparameter%28_,entries,defaultvalue%29.md)
  Set the menu entries in a pop-up menu.

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
- [protocol FxParameterSettingAPI_v6](./fxparametersettingapi_v6.md)
  Defines the functions the application provides to set parameter flags.


---

*[View on Apple Developer](https://developer.apple.com/documentation/professional_video_applications/fxdynamicparameterapi_v3)*