# FxOnScreenControlAPI_v3

**Framework**: Professional Video Applications  
**Kind**: protocol  
**Role**: Protocol

The `FxOnScreenControlAPI_v3` protocol specifies additions to the [`FxOnScreenControlAPI`](./fxonscreencontrolapi.md) protocol which defines the methods the host application provides to manage conversions between various on-screen coordinate spaces.

**Availability**:
- FxPlug 3.1+

## Declaration

```swift
protocol FxOnScreenControlAPI_v3 : FxOnScreenControlAPI_v2
```

```objc
@protocol FxOnScreenControlAPI_v3 <FxOnScreenControlAPI_v2>
```

## Overview

This protocol inherits from, and expands on, the [`FxOnScreenControlAPI_v2`](./fxonscreencontrolapi_v2.md) protocol. It can retrieve information about the scaling factor used to draw on screen controls to the screen.

## Topics

### Getting Scaling Factor
- [func backingScaleFactor() -> Double](./fxonscreencontrolapi_v3/backingscalefactor%28%29.md)
  Returns the scale factor for drawing the on-screen control to the current screen.

## Relationships

### Inherits From
- [FxOnScreenControlAPI](./fxonscreencontrolapi.md)
- [FxOnScreenControlAPI_v2](./fxonscreencontrolapi_v2.md)
### Inherited By
- [FxOnScreenControlAPI_v4](./fxonscreencontrolapi_v4.md)

## See Also

### Onscreen Control APIs
- [protocol FxOnScreenControl_v4](./fxonscreencontrol_v4.md)
  Defines the methods a plug-in must implement to create parameter controls.
- [protocol FxOnScreenControlAPI](./fxonscreencontrolapi.md)
  The `FxOnScreenControlAPI` protocol defines the methods the host application uses to draw controls and other user interface elements directly on the canvas where the user has applied the plug-in.
- [protocol FxOnScreenControlAPI_v2](./fxonscreencontrolapi_v2.md)
  The `FxOnScreenControlAPI_v2` protocol specifies additions to the `FxOnScreenControlAPI` protocol which defines the methods the host application provides to manage conversions between various on-screen coordinate spaces.
- [protocol FxOnScreenControlAPI_v4](./fxonscreencontrolapi_v4.md)
  The `FxOnScreenControlAPI_v4` protocol specifies additions to the [`FxOnScreenControlAPI`](./fxonscreencontrolapi.md) protocol which defines the methods the host application provides to manage conversions between various on-screen coordinate spaces.


---

*[View on Apple Developer](https://developer.apple.com/documentation/professional_video_applications/fxonscreencontrolapi_v3)*