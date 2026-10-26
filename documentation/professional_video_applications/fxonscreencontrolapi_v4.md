# FxOnScreenControlAPI_v4

**Framework**: Professional Video Applications  
**Kind**: protocol  
**Role**: Protocol

The `FxOnScreenControlAPI_v4` protocol specifies additions to the [`FxOnScreenControlAPI`](./fxonscreencontrolapi.md) protocol which defines the methods the host application provides to manage conversions between various on-screen coordinate spaces.

**Availability**:
- FxPlug 3.1.1+

## Declaration

```swift
protocol FxOnScreenControlAPI_v4 : FxOnScreenControlAPI_v3
```

```objc
@protocol FxOnScreenControlAPI_v4 <FxOnScreenControlAPI_v3>
```

## Mentions

- [Adding onscreen controls to plug-ins](https://developer.apple.com/documentation/professional-video-applications/adding-onscreen-controls-to-plug-ins)

#### Overview

This protocol inherits from, and expands on, the `FxOnScreenControlAPI_v3` protocol. It allows an FxPlug plug-in to set the cursor the users sees in the canvas.

## Topics

### Setting Canvas Cursor
- [func setCursor(NSCursor!)](./fxonscreencontrolapi_v4/setcursor%28_%29.md)
  Sets the cursor the user sees in the canvas.

## Relationships

### Inherits From
- [FxOnScreenControlAPI](./fxonscreencontrolapi.md)
- [FxOnScreenControlAPI_v2](./fxonscreencontrolapi_v2.md)
- [FxOnScreenControlAPI_v3](./fxonscreencontrolapi_v3.md)

## See Also

### Onscreen Control APIs
- [protocol FxOnScreenControl_v4](./fxonscreencontrol_v4.md)
  Defines the methods a plug-in must implement to create parameter controls.
- [protocol FxOnScreenControlAPI](./fxonscreencontrolapi.md)
  The `FxOnScreenControlAPI` protocol defines the methods the host application uses to draw controls and other user interface elements directly on the canvas where the user has applied the plug-in.
- [protocol FxOnScreenControlAPI_v2](./fxonscreencontrolapi_v2.md)
  The `FxOnScreenControlAPI_v2` protocol specifies additions to the `FxOnScreenControlAPI` protocol which defines the methods the host application provides to manage conversions between various on-screen coordinate spaces.
- [protocol FxOnScreenControlAPI_v3](./fxonscreencontrolapi_v3.md)
  The `FxOnScreenControlAPI_v3` protocol specifies additions to the [`FxOnScreenControlAPI`](./fxonscreencontrolapi.md) protocol which defines the methods the host application provides to manage conversions between various on-screen coordinate spaces.


---

*[View on Apple Developer](https://developer.apple.com/documentation/professional_video_applications/fxonscreencontrolapi_v4)*