# drawOSC(withWidth:height:activePart:destinationImage:at:)

**Framework**: Professional Video Applications  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Draws a control on an image. This is the main method the host application calls to draw a plug-in parameter control.

**Availability**:
- FxPlug 4.0+

## Declaration

```swift
func drawOSC(withWidth width: Int, height: Int, activePart: Int, destinationImage: FxImageTile!, at time: CMTime)
```

```objc
- (void) drawOSCWithWidth:(NSInteger) width height:(NSInteger) height activePart:(NSInteger) activePart destinationImage:(FxImageTile *) destinationImage atTime:(CMTime) time;
```

## Discussion

This method is called when the host application wants you to draw your onscreen controls. You should draw them into the destination image. The `activePart` parameter tells which part of the control is currently selected so you can draw that control with proper highlighting.

## Parameters

- `width`: Width of the current image where the control will be drawn.
- `height`: Height of the current image where the control will be drawn.
- `activePart`: The active part of the control to draw.
- `destinationImage`: An [`ioSurface`](../fximagetile/iosurface.md) into which you should draw your OSCs.
- `time`: The time at which to draw the control.

## See Also

### Instance Methods
- [func drawingCoordinates() -> FxDrawingCoordinates](./drawingcoordinates%28%29.md)
  Defines the coordinate space for an event.
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

*[View on Apple Developer](https://developer.apple.com/documentation/professional_video_applications/fxonscreencontrol_v4/drawosc(withwidth:height:activepart:destinationimage:at:))*