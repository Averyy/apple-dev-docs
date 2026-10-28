# drawingCoordinates()

**Framework**: Professional Video Applications  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Defines the coordinate space for an event.

**Availability**:
- FxPlug 4.0+

## Declaration

```swift
func drawingCoordinates() -> FxDrawingCoordinates
```

```objc
- (FxDrawingCoordinates) drawingCoordinates;
```

## Mentions

- [Adding onscreen controls to plug-ins](../../Professional-Video-Applications/adding-onscreen-controls-to-plug-ins.md)

## Return Value

Returns the appropriate coordinate space.

## See Also

### Instance Methods
- [func drawOSC(withWidth: Int, height: Int, activePart: Int, destinationImage: FxImageTile!, at: CMTime)](./drawosc%28withwidth,height,activepart,destinationimage,at%29.md)
  Draws a control on an image. This is the main method the host application calls to draw a plug-in parameter control.
- [func hitTestOSC(atMousePositionX: Double, mousePositionY: Double, activePart: UnsafeMutablePointer<Int>!, at: CMTime)](./hittestosc%28atmousepositionx,mousepositiony,activepart,at%29.md)
  Figures out which part of the onscreen control was hit.
- [func keyDown(atPositionX: Double, positionY: Double, keyPressed: UInt16, modifiers: FxModifierKeys, forceUpdate: UnsafeMutablePointer<ObjCBool>!, didHandle: UnsafeMutablePointer<ObjCBool>!, at: CMTime)](./keydown%28atpositionx,positiony,keypressed,modifiers,forceupdate,didhandle,at%29.md)
  Provides information when a key is pressed.
- [func keyUp(atPositionX: Double, positionY: Double, keyPressed: UInt16, modifiers: FxModifierKeys, forceUpdate: UnsafeMutablePointer<ObjCBool>!, didHandle: UnsafeMutablePointer<ObjCBool>!, at: CMTime)](./keyup%28atpositionx,positiony,keypressed,modifiers,forceupdate,didhandle,at%29.md)
  Provides information when a key is released.
- [func mouseDown(atPositionX: Double, positionY: Double, activePart: Int, modifiers: FxModifierKeys, forceUpdate: UnsafeMutablePointer<ObjCBool>!, at: CMTime)](./mousedown%28atpositionx,positiony,activepart,modifiers,forceupdate,at%29.md)
  Provides information when the left mouse button is pressed and the pointer is on an image with an active plug-in control.
- [func mouseDragged(atPositionX: Double, positionY: Double, activePart: Int, modifiers: FxModifierKeys, forceUpdate: UnsafeMutablePointer<ObjCBool>!, at: CMTime)](./mousedragged%28atpositionx,positiony,activepart,modifiers,forceupdate,at%29.md)
  Provides information when the left mouse button is pressed and the pointer is moved with the mouse button still down.
- [func mouseEntered(atPositionX: Double, positionY: Double, modifiers: FxModifierKeys, forceUpdate: UnsafeMutablePointer<ObjCBool>!, at: CMTime)](./mouseentered%28atpositionx,positiony,modifiers,forceupdate,at%29.md)
  Provides information when the mouse pointer enters the view.
- [func mouseExited(atPositionX: Double, positionY: Double, modifiers: FxModifierKeys, forceUpdate: UnsafeMutablePointer<ObjCBool>!, at: CMTime)](./mouseexited%28atpositionx,positiony,modifiers,forceupdate,at%29.md)
  Provides information when the mouse pointer leaves the view.
- [func mouseMoved(atPositionX: Double, positionY: Double, activePart: Int, modifiers: FxModifierKeys, forceUpdate: UnsafeMutablePointer<ObjCBool>!, at: CMTime)](./mousemoved%28atpositionx,positiony,activepart,modifiers,forceupdate,at%29.md)
  Provides information when the mouse pointer changes location.
- [func mouseUp(atPositionX: Double, positionY: Double, activePart: Int, modifiers: FxModifierKeys, forceUpdate: UnsafeMutablePointer<ObjCBool>!, at: CMTime)](./mouseup%28atpositionx,positiony,activepart,modifiers,forceupdate,at%29.md)
  Provides information when the left mouse button is released.


---

*[View on Apple Developer](https://developer.apple.com/documentation/professional_video_applications/fxonscreencontrol_v4/drawingcoordinates())*