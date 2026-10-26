# FxOnScreenControl_v4

**Framework**: Professional Video Applications  
**Kind**: protocol  
**Role**: Protocol

Defines the methods a plug-in must implement to create parameter controls.

**Availability**:
- FxPlug 4.0+

## Declaration

```swift
protocol FxOnScreenControl_v4
```

```objc
@protocol FxOnScreenControl_v4
```

## Topics

### Instance Methods
- [func drawOSC(withWidth: Int, height: Int, activePart: Int, destinationImage: FxImageTile!, at: CMTime)](./fxonscreencontrol_v4/drawosc%28withwidth,height,activepart,destinationimage,at%29.md)
  Draws a control on an image. This is the main method the host application calls to draw a plug-in parameter control.
- [func drawingCoordinates() -> FxDrawingCoordinates](./fxonscreencontrol_v4/drawingcoordinates%28%29.md)
  Defines the coordinate space for an event.
- [func hitTestOSC(atMousePositionX: Double, mousePositionY: Double, activePart: UnsafeMutablePointer<Int>!, at: CMTime)](./fxonscreencontrol_v4/hittestosc%28atmousepositionx,mousepositiony,activepart,at%29.md)
  Figures out which part of the onscreen control was hit.
- [func keyDown(atPositionX: Double, positionY: Double, keyPressed: UInt16, modifiers: FxModifierKeys, forceUpdate: UnsafeMutablePointer<ObjCBool>!, didHandle: UnsafeMutablePointer<ObjCBool>!, at: CMTime)](./fxonscreencontrol_v4/keydown%28atpositionx,positiony,keypressed,modifiers,forceupdate,didhandle,at%29.md)
  Provides information when a key is pressed.
- [func keyUp(atPositionX: Double, positionY: Double, keyPressed: UInt16, modifiers: FxModifierKeys, forceUpdate: UnsafeMutablePointer<ObjCBool>!, didHandle: UnsafeMutablePointer<ObjCBool>!, at: CMTime)](./fxonscreencontrol_v4/keyup%28atpositionx,positiony,keypressed,modifiers,forceupdate,didhandle,at%29.md)
  Provides information when a key is released.
- [func mouseDown(atPositionX: Double, positionY: Double, activePart: Int, modifiers: FxModifierKeys, forceUpdate: UnsafeMutablePointer<ObjCBool>!, at: CMTime)](./fxonscreencontrol_v4/mousedown%28atpositionx,positiony,activepart,modifiers,forceupdate,at%29.md)
  Provides information when the left mouse button is pressed and the pointer is on an image with an active plug-in control.
- [func mouseDragged(atPositionX: Double, positionY: Double, activePart: Int, modifiers: FxModifierKeys, forceUpdate: UnsafeMutablePointer<ObjCBool>!, at: CMTime)](./fxonscreencontrol_v4/mousedragged%28atpositionx,positiony,activepart,modifiers,forceupdate,at%29.md)
  Provides information when the left mouse button is pressed and the pointer is moved with the mouse button still down.
- [func mouseEntered(atPositionX: Double, positionY: Double, modifiers: FxModifierKeys, forceUpdate: UnsafeMutablePointer<ObjCBool>!, at: CMTime)](./fxonscreencontrol_v4/mouseentered%28atpositionx,positiony,modifiers,forceupdate,at%29.md)
  Provides information when the mouse pointer enters the view.
- [func mouseExited(atPositionX: Double, positionY: Double, modifiers: FxModifierKeys, forceUpdate: UnsafeMutablePointer<ObjCBool>!, at: CMTime)](./fxonscreencontrol_v4/mouseexited%28atpositionx,positiony,modifiers,forceupdate,at%29.md)
  Provides information when the mouse pointer leaves the view.
- [func mouseMoved(atPositionX: Double, positionY: Double, activePart: Int, modifiers: FxModifierKeys, forceUpdate: UnsafeMutablePointer<ObjCBool>!, at: CMTime)](./fxonscreencontrol_v4/mousemoved%28atpositionx,positiony,activepart,modifiers,forceupdate,at%29.md)
  Provides information when the mouse pointer changes location.
- [func mouseUp(atPositionX: Double, positionY: Double, activePart: Int, modifiers: FxModifierKeys, forceUpdate: UnsafeMutablePointer<ObjCBool>!, at: CMTime)](./fxonscreencontrol_v4/mouseup%28atpositionx,positiony,activepart,modifiers,forceupdate,at%29.md)
  Provides information when the left mouse button is released.

## See Also

### Onscreen Control APIs
- [protocol FxOnScreenControlAPI](./fxonscreencontrolapi.md)
  The `FxOnScreenControlAPI` protocol defines the methods the host application uses to draw controls and other user interface elements directly on the canvas where the user has applied the plug-in.
- [protocol FxOnScreenControlAPI_v2](./fxonscreencontrolapi_v2.md)
  The `FxOnScreenControlAPI_v2` protocol specifies additions to the `FxOnScreenControlAPI` protocol which defines the methods the host application provides to manage conversions between various on-screen coordinate spaces.
- [protocol FxOnScreenControlAPI_v3](./fxonscreencontrolapi_v3.md)
  The `FxOnScreenControlAPI_v3` protocol specifies additions to the [`FxOnScreenControlAPI`](./fxonscreencontrolapi.md) protocol which defines the methods the host application provides to manage conversions between various on-screen coordinate spaces.
- [protocol FxOnScreenControlAPI_v4](./fxonscreencontrolapi_v4.md)
  The `FxOnScreenControlAPI_v4` protocol specifies additions to the [`FxOnScreenControlAPI`](./fxonscreencontrolapi.md) protocol which defines the methods the host application provides to manage conversions between various on-screen coordinate spaces.


---

*[View on Apple Developer](https://developer.apple.com/documentation/professional_video_applications/fxonscreencontrol_v4)*