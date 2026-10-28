# FxOnScreenControlAPI

**Framework**: Professional Video Applications  
**Kind**: protocol  
**Role**: Protocol

The `FxOnScreenControlAPI` protocol defines the methods the host application uses to draw controls and other user interface elements directly on the canvas where the user has applied the plug-in.

**Availability**:
- FxPlug 3.1+

## Declaration

```swift
protocol FxOnScreenControlAPI
```

```objc
@protocol FxOnScreenControlAPI
```

## Mentions

- [Adding onscreen controls to plug-ins](../Professional-Video-Applications/adding-onscreen-controls-to-plug-ins.md)

## Overview

Plug-ins use protocol to direct manipulation of the object and is an intuitive means for users to interact with a plug-in.

Use this API to transform points from the drawing space of the canvas or document to the pixel space of the object the user wants to manipulate, and vice-versa.

## Topics

### Converting Points Between Coordinate Spaces
- [func convertPoint(fromSpace: FxDrawingCoordinates, fromX: Double, fromY: Double, toSpace: FxDrawingCoordinates, toX: UnsafeMutablePointer<Double>!, toY: UnsafeMutablePointer<Double>!)](./fxonscreencontrolapi/convertpoint%28fromspace,fromx,fromy,tospace,tox,toy%29.md)
  Converts a position from object space to canvas space.

## Relationships

### Inherited By
- [FxOnScreenControlAPI_v2](./fxonscreencontrolapi_v2.md)
- [FxOnScreenControlAPI_v3](./fxonscreencontrolapi_v3.md)
- [FxOnScreenControlAPI_v4](./fxonscreencontrolapi_v4.md)

## See Also

### Onscreen Control APIs
- [protocol FxOnScreenControl_v4](./fxonscreencontrol_v4.md)
  Defines the methods a plug-in must implement to create parameter controls.
- [protocol FxOnScreenControlAPI_v2](./fxonscreencontrolapi_v2.md)
  The `FxOnScreenControlAPI_v2` protocol specifies additions to the `FxOnScreenControlAPI` protocol which defines the methods the host application provides to manage conversions between various on-screen coordinate spaces.
- [protocol FxOnScreenControlAPI_v3](./fxonscreencontrolapi_v3.md)
  The `FxOnScreenControlAPI_v3` protocol specifies additions to the [`FxOnScreenControlAPI`](./fxonscreencontrolapi.md) protocol which defines the methods the host application provides to manage conversions between various on-screen coordinate spaces.
- [protocol FxOnScreenControlAPI_v4](./fxonscreencontrolapi_v4.md)
  The `FxOnScreenControlAPI_v4` protocol specifies additions to the [`FxOnScreenControlAPI`](./fxonscreencontrolapi.md) protocol which defines the methods the host application provides to manage conversions between various on-screen coordinate spaces.


---

*[View on Apple Developer](https://developer.apple.com/documentation/professional_video_applications/fxonscreencontrolapi)*