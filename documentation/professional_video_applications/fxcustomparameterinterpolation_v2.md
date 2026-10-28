# FxCustomParameterInterpolation_v2

**Framework**: Professional Video Applications  
**Kind**: protocol  
**Role**: Protocol

Defines the methods a plug-in needs to implement to support keyframing custom parameters.

**Availability**:
- FxPlug 4.0+

## Declaration

```swift
protocol FxCustomParameterInterpolation_v2
```

```objc
@protocol FxCustomParameterInterpolation_v2
```

## Overview

An FxPlug 4 or later plug-in that wants to support keyframing custom parameters must conform to the `FxCustomParameterInterpolation_v2` or later protocol. This protocol allows the plug-in to generate interpolated (in-between) values between keyframes.

Note that this protocol intentionally does not inherit from the `FxCustomParameterInterpolation` protocol, which is for older-style plug-ins.

## Topics

### Instance Methods
- [func interpolateBetween(any NSCopying & NSSecureCoding & NSObjectProtocol, withWeight: Float) -> any NSCopying & NSSecureCoding & NSObjectProtocol](./fxcustomparameterinterpolation_v2/interpolatebetween%28_,withweight%29.md)
  Returns a new parameter value which has been calculated by interpolating between                 two key values.
- [func isEqual(any NSCopying & NSSecureCoding & NSObjectProtocol) -> Bool](./fxcustomparameterinterpolation_v2/isequal%28_%29.md)
  Returns whether one custom parameter value is equal to another.

## See Also

### Custom Parameter APIs
- [protocol FxCustomParameterViewHost_v2](./fxcustomparameterviewhost_v2.md)
  Defines the methods a plug-in needs to implement to associate a custom NSView with one of its parameters.
- [protocol FxCustomParameterActionAPI_v4](./fxcustomparameteractionapi_v4.md)
  Defines the methods the host application provides to support a custom parameter view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/professional_video_applications/fxcustomparameterinterpolation_v2)*