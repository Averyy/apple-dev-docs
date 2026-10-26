# mouseExited(atPositionX:positionY:modifiers:forceUpdate:at:)

**Framework**: Professional Video Applications  
**Kind**: method  
**Role**: Instance Method

Provides information when the mouse pointer leaves the view.

**Availability**:
- FxPlug 4.0+

## Declaration

```swift
optional func mouseExited(atPositionX mousePositionX: Double, positionY mousePositionY: Double, modifiers: FxModifierKeys, forceUpdate: UnsafeMutablePointer<ObjCBool>!, at time: CMTime)
```

```objc
- (void) mouseExitedAtPositionX:(double) mousePositionX positionY:(double) mousePositionY modifiers:(FxModifierKeys) modifiers forceUpdate:(BOOL *) forceUpdate atTime:(CMTime) time;
```

## Mentions

- [Adding onscreen controls to plug-ins](https://developer.apple.com/documentation/professional-video-applications/adding-onscreen-controls-to-plug-ins)

## Parameters

- `mousePositionX`: X position of the pointer (in `drawingCoordinates` space).
- `mousePositionY`: Y position of the pointer (in `drawingCoordinates` space).
- `modifiers`: The keyboard modifiers currently pressed.
- `forceUpdate`: Set to `YES` if the filter/generator associated with this control needs to be re-calculated; `NO` otherwise.
- `time`: The current time when the mouse exits the OSC.

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
- [func mouseMoved(atPositionX: Double, positionY: Double, activePart: Int, modifiers: FxModifierKeys, forceUpdate: UnsafeMutablePointer<ObjCBool>!, at: CMTime)](./mousemoved%28atpositionx,positiony,activepart,modifiers,forceupdate,at%29.md)
  Provides information when the mouse pointer changes location.
- [func mouseUp(atPositionX: Double, positionY: Double, activePart: Int, modifiers: FxModifierKeys, forceUpdate: UnsafeMutablePointer<ObjCBool>!, at: CMTime)](./mouseup%28atpositionx,positiony,activepart,modifiers,forceupdate,at%29.md)
  Provides information when the left mouse button is released.


---

*[View on Apple Developer](https://developer.apple.com/documentation/professional_video_applications/fxonscreencontrol_v4/mouseexited(atpositionx:positiony:modifiers:forceupdate:at:))*