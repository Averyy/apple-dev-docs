# FxCustomParameterViewHost_v2

**Framework**: Professional Video Applications  
**Kind**: protocol  
**Role**: Protocol

Defines the methods a plug-in needs to implement to associate a custom NSView with one of its parameters.

**Availability**:
- FxPlug 4.0+

## Declaration

```swift
protocol FxCustomParameterViewHost_v2
```

```objc
@protocol FxCustomParameterViewHost_v2
```

## Mentions

- [Adding parameters to plug-ins](../Professional-Video-Applications/adding-parameters-to-plug-ins.md)

## Overview

An FxPlug that wants to present custom UI for one or more of its parameters must conform to the FxCustomParmeterViewHost protocol. This protocol allows the plug-in to provide a subclass of NSView. It is up to the plug-in to handle NSEvents in its custom view(s). When an event in a custom view necessitates a change to the value of the associated parameter, the plug-in then uses methods in the host API FxCustomParameterActionAPI to tell the host application to change the parameter value.

## Topics

### Instance Methods
- [func createView(forParameterID: UInt32) -> NSView!](./fxcustomparameterviewhost_v2/createview%28forparameterid%29.md)
  Provides an NSView to be associated with the given parameter.

## See Also

### Custom Parameter APIs
- [protocol FxCustomParameterActionAPI_v4](./fxcustomparameteractionapi_v4.md)
  Defines the methods the host application provides to support a custom parameter view.
- [protocol FxCustomParameterInterpolation_v2](./fxcustomparameterinterpolation_v2.md)
  Defines the methods a plug-in needs to implement to support keyframing custom parameters.


---

*[View on Apple Developer](https://developer.apple.com/documentation/professional_video_applications/fxcustomparameterviewhost_v2)*