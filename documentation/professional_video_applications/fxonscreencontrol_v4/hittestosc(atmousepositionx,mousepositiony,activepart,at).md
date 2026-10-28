# hitTestOSC(atMousePositionX:mousePositionY:activePart:at:)

**Framework**: Professional Video Applications  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Figures out which part of the onscreen control was hit.

**Availability**:
- FxPlug 4.0+

## Declaration

```swift
func hitTestOSC(atMousePositionX mousePositionX: Double, mousePositionY: Double, activePart: UnsafeMutablePointer<Int>!, at time: CMTime)
```

```objc
- (void) hitTestOSCAtMousePositionX:(double) mousePositionX mousePositionY:(double) mousePositionY activePart:(NSInteger *) activePart atTime:(CMTime) time;
```

## Discussion

This method is called by the host to determine which part of your controls were hit by the mouse. Return a constant that represents a part number for your onscreen control in the activePart parameter. It will be sent to you in the `-draw`, `-mouse`, and `-key` methods so you can handle those events properly.

## Parameters

- `mousePositionX`: The x position of the mouse
- `mousePositionY`: The y position of the mouse
- `activePart`: The part that was hit - set to `0` if no part was hit
- `time`: The time at which we are checking for a hit

## See Also

### Instance Methods
- [func drawOSC(withWidth: Int, height: Int, activePart: Int, destinationImage: FxImageTile!, at: CMTime)](./drawosc%28withwidth,height,activepart,destinationimage,at%29.md)
  Draws a control on an image. This is the main method the host application calls to draw a plug-in parameter control.
- [func drawingCoordinates() -> FxDrawingCoordinates](./drawingcoordinates%28%29.md)
  Defines the coordinate space for an event.
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

*[View on Apple Developer](https://developer.apple.com/documentation/professional_video_applications/fxonscreencontrol_v4/hittestosc(atmousepositionx:mousepositiony:activepart:at:))*