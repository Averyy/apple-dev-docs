# FxParameterCreationAPI_v5

**Framework**: Professional Video Applications  
**Kind**: protocol  
**Role**: Protocol

Defines the methods provided by the host application to create parameters.

**Availability**:
- FxPlug 3.1.1+

## Declaration

```swift
protocol FxParameterCreationAPI_v5
```

```objc
@protocol FxParameterCreationAPI_v5
```

## Mentions

- [Adding parameters to plug-ins](../Professional-Video-Applications/adding-parameters-to-plug-ins.md)
- [Managing color space and gamut in plug-ins](../Professional-Video-Applications/managing-color-space-and-gamut-in-plug-ins.md)
- [Using FxPlug APIs](../Professional-Video-Applications/using-fxplug-apis.md)

## Overview

A plug-in uses the methods defined in this protocol (along with those defined in `FxOptionalParameterAPI.h`) to populate its parameter list. Each parameter is created with a unique numeric parameter ID. The host application uses this parameter ID to identify a parameter, and stores the parameter ID in a saved project file. If a new version of a plug-in removes a parameter, the host application will then ignore any saved parameter data for that obsolete parameter in a project that was saved while using the old version of the plug-in. This implies that a new version plug-in should never change the ID of a given parameter unless it intentionally wants to obsolesce old value data in saved projects. Similarly, it should not introduce a new parameter with an ID that has already been obsolesced.

This is version 5 of the Parameter Creation API. This version 5 protocol is not a superset of version 4.

> ❗ **Important**:  Parameter IDs must be in the range of `[1, 9998]`. IDs outside of this range are invalid.

## Topics

### Instance Methods
- [func addAngleSlider(withName: String, parameterID: UInt32, defaultDegrees: Double, parameterMinDegrees: Double, parameterMaxDegrees: Double, parameterFlags: FxParameterFlags) -> Bool](./fxparametercreationapi_v5/addangleslider%28withname,parameterid,defaultdegrees,parametermindegrees,parametermaxdegrees,parameterflags%29.md)
  Creates an angle slider parameter and adds it to the plug-in’s parameter list.
- [func addColorParameter(withName: String, parameterID: UInt32, defaultRed: Double, defaultGreen: Double, defaultBlue: Double, defaultAlpha: Double, parameterFlags: FxParameterFlags) -> Bool](./fxparametercreationapi_v5/addcolorparameter%28withname,parameterid,defaultred,defaultgreen,defaultblue,defaultalpha,parameterflags%29.md)
  Creates an RGBA color value and adds it to the plug-in’s parameter list.
- [func addColorParameter(withName: String, parameterID: UInt32, defaultRed: Double, defaultGreen: Double, defaultBlue: Double, parameterFlags: FxParameterFlags) -> Bool](./fxparametercreationapi_v5/addcolorparameter%28withname,parameterid,defaultred,defaultgreen,defaultblue,parameterflags%29.md)
  Creates an RGB color parameter and adds it to the plug-in’s parameter list.
- [func addCustomParameter(withName: String, parameterID: UInt32, defaultValue: any NSCopying & NSSecureCoding & NSObjectProtocol, parameterFlags: FxParameterFlags) -> Bool](./fxparametercreationapi_v5/addcustomparameter%28withname,parameterid,defaultvalue,parameterflags%29.md)
  Creates a custom parameter and adds it to the plug-in’s parameter list.
- [func addFloatSlider(withName: String, parameterID: UInt32, defaultValue: Double, parameterMin: Double, parameterMax: Double, sliderMin: Double, sliderMax: Double, delta: Double, parameterFlags: FxParameterFlags) -> Bool](./fxparametercreationapi_v5/addfloatslider%28withname,parameterid,defaultvalue,parametermin,parametermax,slidermin,slidermax,delta,parameterflags%29.md)
  Creates a floating point slider parameter and adds it to the plug-in’s parameter list.
- [func addFontMenu(withName: String, parameterID: UInt32, fontName: String, parameterFlags: FxParameterFlags) -> Bool](./fxparametercreationapi_v5/addfontmenu%28withname,parameterid,fontname,parameterflags%29.md)
  Creates a font menu button parameter and adds it to the plug-in’s parameter.
- [func addGradient(withName: String, parameterID: UInt32, parameterFlags: FxParameterFlags) -> Bool](./fxparametercreationapi_v5/addgradient%28withname,parameterid,parameterflags%29.md)
  Creates a gradient parameter.
- [func addHelpButton(withName: String, parameterID: UInt32, selector: Selector, parameterFlags: FxParameterFlags) -> Bool](./fxparametercreationapi_v5/addhelpbutton%28withname,parameterid,selector,parameterflags%29.md)
  Creates a help push button parameter and adds it to the plug-in’s parameter.
- [func addHistogram(withName: String, parameterID: UInt32, parameterFlags: FxParameterFlags) -> Bool](./fxparametercreationapi_v5/addhistogram%28withname,parameterid,parameterflags%29.md)
  Creates a histogram parameter.
- [func addImageReference(withName: String, parameterID: UInt32, parameterFlags: FxParameterFlags) -> Bool](./fxparametercreationapi_v5/addimagereference%28withname,parameterid,parameterflags%29.md)
  Creates an image reference parameter and adds it to the plug-in’s parameter list.
- [func addIntSlider(withName: String, parameterID: UInt32, defaultValue: Int32, parameterMin: Int32, parameterMax: Int32, sliderMin: Int32, sliderMax: Int32, delta: Int32, parameterFlags: FxParameterFlags) -> Bool](./fxparametercreationapi_v5/addintslider%28withname,parameterid,defaultvalue,parametermin,parametermax,slidermin,slidermax,delta,parameterflags%29.md)
  Creates an integer slider parameter and adds it to the plug-in’s parameter list.
- [func addPathPicker(withName: String, parameterID: UInt32, parameterFlags: FxParameterFlags) -> Bool](./fxparametercreationapi_v5/addpathpicker%28withname,parameterid,parameterflags%29.md)
  Creates a parameter for choosing an image mask path.
- [func addPercentSlider(withName: String, parameterID: UInt32, defaultValue: Double, parameterMin: Double, parameterMax: Double, sliderMin: Double, sliderMax: Double, delta: Double, parameterFlags: FxParameterFlags) -> Bool](./fxparametercreationapi_v5/addpercentslider%28withname,parameterid,defaultvalue,parametermin,parametermax,slidermin,slidermax,delta,parameterflags%29.md)
  Creates a percentage floating point slider parameter and adds it to the plug-in’s parameter list.  A parameter value of 1.0 corresponds to a slider value of 100%.
- [func addPointParameter(withName: String, parameterID: UInt32, defaultX: Double, defaultY: Double, parameterFlags: FxParameterFlags) -> Bool](./fxparametercreationapi_v5/addpointparameter%28withname,parameterid,defaultx,defaulty,parameterflags%29.md)
  Creates a position point parameter and adds it to the plug-in’s parameter list.
- [func addPopupMenu(withName: String, parameterID: UInt32, defaultValue: UInt32, menuEntries: [Any], parameterFlags: FxParameterFlags) -> Bool](./fxparametercreationapi_v5/addpopupmenu%28withname,parameterid,defaultvalue,menuentries,parameterflags%29.md)
  Creates a popup menu parameter and adds it to the plug-in’s parameter list.
- [func addPushButton(withName: String, parameterID: UInt32, selector: Selector, parameterFlags: FxParameterFlags) -> Bool](./fxparametercreationapi_v5/addpushbutton%28withname,parameterid,selector,parameterflags%29.md)
  Creates a push button parameter and adds it to the plug-in’s parameter list.
- [func addStringParameter(withName: String, parameterID: UInt32, defaultValue: String, parameterFlags: FxParameterFlags) -> Bool](./fxparametercreationapi_v5/addstringparameter%28withname,parameterid,defaultvalue,parameterflags%29.md)
  Creates a string parameter and adds it to the plug-in’s parameter list.
- [func addToggleButton(withName: String, parameterID: UInt32, defaultValue: Bool, parameterFlags: FxParameterFlags) -> Bool](./fxparametercreationapi_v5/addtogglebutton%28withname,parameterid,defaultvalue,parameterflags%29.md)
  Creates a checkbox toggle button parameter and adds it to the plug-in’s parameter.
- [func endParameterSubGroup() -> Bool](./fxparametercreationapi_v5/endparametersubgroup%28%29.md)
  Closes current parameter subgroup. You should always pair this with a preceding [`startParameterSubGroup(_:parameterID:parameterFlags:)`](./fxparametercreationapi_v5/startparametersubgroup%28_,parameterid,parameterflags%29.md) message.
- [func startParameterSubGroup(String, parameterID: UInt32, parameterFlags: FxParameterFlags) -> Bool](./fxparametercreationapi_v5/startparametersubgroup%28_,parameterid,parameterflags%29.md)
  Starts a new parameter subgroup. All subsequent parameter additions are placed in this group until you send an [`endParameterSubGroup()`](./fxparametercreationapi_v5/endparametersubgroup%28%29.md) message.

## See Also

### Parameter APIs
- [protocol FxParameterRetrievalAPI_v6](./fxparameterretrievalapi_v6.md)
  Defines the functions the application provides to retrieve parameter values.
- [protocol FxParameterRetrievalAPI_v7](./fxparameterretrievalapi_v7.md)
  Adds a method to retrieve the image information about an image parameter.
- [protocol FxParameterSettingAPI_v5](./fxparametersettingapi_v5.md)
  Defines the functions the application provides to set parameter values.
- [protocol FxParameterSettingAPI_v6](./fxparametersettingapi_v6.md)
  Defines the functions the application provides to set parameter flags.
- [protocol FxDynamicParameterAPI_v3](./fxdynamicparameterapi_v3.md)
  Allows your plugin to create parameters on-the-fly.


---

*[View on Apple Developer](https://developer.apple.com/documentation/professional_video_applications/fxparametercreationapi_v5)*