# addStringParameter(withName:parameterID:defaultValue:parameterFlags:)

**Framework**: Professional Video Applications  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Creates a string parameter and adds it to the plug-in’s parameter list.

**Availability**:
- FxPlug 4.0+

## Declaration

```swift
func addStringParameter(withName name: String, parameterID: UInt32, defaultValue: String, parameterFlags flags: FxParameterFlags) -> Bool
```

```objc
- (BOOL) addStringParameterWithName:(NSString *) name parameterID:(UInt32) parameterID defaultValue:(NSString *) defaultValue parameterFlags:(FxParameterFlags) flags;
```

#### Return Value

Returns `YES` if the application successfully creates a string parameter; `NO` otherwise.

## Parameters

- `name`: Name of the parameter in the user interface.
- `parameterID`: Unique identifier for a parameter. Used to retrieve, set, or validate the parameter.
- `defaultValue`: Initial value for the parameter.
- `flags`: Flags that encode various state values for the parameter.

## See Also

### Instance Methods
- [func addAngleSlider(withName: String, parameterID: UInt32, defaultDegrees: Double, parameterMinDegrees: Double, parameterMaxDegrees: Double, parameterFlags: FxParameterFlags) -> Bool](./addangleslider%28withname,parameterid,defaultdegrees,parametermindegrees,parametermaxdegrees,parameterflags%29.md)
  Creates an angle slider parameter and adds it to the plug-in’s parameter list.
- [func addColorParameter(withName: String, parameterID: UInt32, defaultRed: Double, defaultGreen: Double, defaultBlue: Double, defaultAlpha: Double, parameterFlags: FxParameterFlags) -> Bool](./addcolorparameter%28withname,parameterid,defaultred,defaultgreen,defaultblue,defaultalpha,parameterflags%29.md)
  Creates an RGBA color value and adds it to the plug-in’s parameter list.
- [func addColorParameter(withName: String, parameterID: UInt32, defaultRed: Double, defaultGreen: Double, defaultBlue: Double, parameterFlags: FxParameterFlags) -> Bool](./addcolorparameter%28withname,parameterid,defaultred,defaultgreen,defaultblue,parameterflags%29.md)
  Creates an RGB color parameter and adds it to the plug-in’s parameter list.
- [func addCustomParameter(withName: String, parameterID: UInt32, defaultValue: any NSCopying & NSSecureCoding & NSObjectProtocol, parameterFlags: FxParameterFlags) -> Bool](./addcustomparameter%28withname,parameterid,defaultvalue,parameterflags%29.md)
  Creates a custom parameter and adds it to the plug-in’s parameter list.
- [func addFloatSlider(withName: String, parameterID: UInt32, defaultValue: Double, parameterMin: Double, parameterMax: Double, sliderMin: Double, sliderMax: Double, delta: Double, parameterFlags: FxParameterFlags) -> Bool](./addfloatslider%28withname,parameterid,defaultvalue,parametermin,parametermax,slidermin,slidermax,delta,parameterflags%29.md)
  Creates a floating point slider parameter and adds it to the plug-in’s parameter list.
- [func addFontMenu(withName: String, parameterID: UInt32, fontName: String, parameterFlags: FxParameterFlags) -> Bool](./addfontmenu%28withname,parameterid,fontname,parameterflags%29.md)
  Creates a font menu button parameter and adds it to the plug-in’s parameter.
- [func addGradient(withName: String, parameterID: UInt32, parameterFlags: FxParameterFlags) -> Bool](./addgradient%28withname,parameterid,parameterflags%29.md)
  Creates a gradient parameter.
- [func addHelpButton(withName: String, parameterID: UInt32, selector: Selector, parameterFlags: FxParameterFlags) -> Bool](./addhelpbutton%28withname,parameterid,selector,parameterflags%29.md)
  Creates a help push button parameter and adds it to the plug-in’s parameter.
- [func addHistogram(withName: String, parameterID: UInt32, parameterFlags: FxParameterFlags) -> Bool](./addhistogram%28withname,parameterid,parameterflags%29.md)
  Creates a histogram parameter.
- [func addImageReference(withName: String, parameterID: UInt32, parameterFlags: FxParameterFlags) -> Bool](./addimagereference%28withname,parameterid,parameterflags%29.md)
  Creates an image reference parameter and adds it to the plug-in’s parameter list.
- [func addIntSlider(withName: String, parameterID: UInt32, defaultValue: Int32, parameterMin: Int32, parameterMax: Int32, sliderMin: Int32, sliderMax: Int32, delta: Int32, parameterFlags: FxParameterFlags) -> Bool](./addintslider%28withname,parameterid,defaultvalue,parametermin,parametermax,slidermin,slidermax,delta,parameterflags%29.md)
  Creates an integer slider parameter and adds it to the plug-in’s parameter list.
- [func addPathPicker(withName: String, parameterID: UInt32, parameterFlags: FxParameterFlags) -> Bool](./addpathpicker%28withname,parameterid,parameterflags%29.md)
  Creates a parameter for choosing an image mask path.
- [func addPercentSlider(withName: String, parameterID: UInt32, defaultValue: Double, parameterMin: Double, parameterMax: Double, sliderMin: Double, sliderMax: Double, delta: Double, parameterFlags: FxParameterFlags) -> Bool](./addpercentslider%28withname,parameterid,defaultvalue,parametermin,parametermax,slidermin,slidermax,delta,parameterflags%29.md)
  Creates a percentage floating point slider parameter and adds it to the plug-in’s parameter list.  A parameter value of 1.0 corresponds to a slider value of 100%.
- [func addPointParameter(withName: String, parameterID: UInt32, defaultX: Double, defaultY: Double, parameterFlags: FxParameterFlags) -> Bool](./addpointparameter%28withname,parameterid,defaultx,defaulty,parameterflags%29.md)
  Creates a position point parameter and adds it to the plug-in’s parameter list.
- [func addPopupMenu(withName: String, parameterID: UInt32, defaultValue: UInt32, menuEntries: [Any], parameterFlags: FxParameterFlags) -> Bool](./addpopupmenu%28withname,parameterid,defaultvalue,menuentries,parameterflags%29.md)
  Creates a popup menu parameter and adds it to the plug-in’s parameter list.


---

*[View on Apple Developer](https://developer.apple.com/documentation/professional_video_applications/fxparametercreationapi_v5/addstringparameter(withname:parameterid:defaultvalue:parameterflags:))*