# mouseMoved(atPositionX:positionY:activePart:modifiers:forceUpdate:at:)

**Framework**: Professional Video Applications  
**Kind**: method  
**Role**: Instance Method

Provides information when the mouse pointer changes location.

**Availability**:
- FxPlug 4.0+

## Declaration

```swift
optional func mouseMoved(atPositionX mousePositionX: Double, positionY mousePositionY: Double, activePart: Int, modifiers: FxModifierKeys, forceUpdate: UnsafeMutablePointer<ObjCBool>!, at time: CMTime)
```

```objc
- (void) mouseMovedAtPositionX:(double) mousePositionX positionY:(double) mousePositionY activePart:(NSInteger) activePart modifiers:(FxModifierKeys) modifiers forceUpdate:(BOOL *) forceUpdate atTime:(CMTime) time;
```

## Mentions

- [Adding onscreen controls to plug-ins](../../Professional-Video-Applications/adding-onscreen-controls-to-plug-ins.md)

## Parameters

- `mousePositionX`: X position of the pointer (in `drawingCoordinates` space).
- `mousePositionY`: Y position of the pointer (in `drawingCoordinates` space).
- `activePart`: The active part of the control that currently contains the pointer.
- `modifiers`: The keyboard modifiers currently pressed.
- `forceUpdate`: Set to `YES` if the filter/generator associated with this control needs to be re-calculated; `NO` otherwise.
- `time`: The current time when the mouse moved.

## See Also

### Instance Methods
- [func drawOSC(withWidth: Int, height: Int, activePart: Int, destinationImage: FxImageTile!, at: CMTime)](./drawosc%28withwidth,height,activepart,destinationimage,at%29.md)
  Draws a control on an image. This is the main method the host application calls to draw a plug-in parameter control.
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
- [func mouseUp(atPositionX: Double, positionY: Double, activePart: Int, modifiers: FxModifierKeys, forceUpdate: UnsafeMutablePointer<ObjCBool>!, at: CMTime)](./mouseup%28atpositionx,positiony,activepart,modifiers,forceupdate,at%29.md)
  Provides information when the left mouse button is released.


---

*[View on Apple Developer](https://developer.apple.com/documentation/professional_video_applications/fxonscreencontrol_v4/mousemoved(atpositionx:positiony:activepart:modifiers:forceupdate:at:))*