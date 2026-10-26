# convertPoint(fromSpace:fromX:fromY:toSpace:toX:toY:)

**Framework**: Professional Video Applications  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Converts a position from object space to canvas space.

**Availability**:
- FxPlug 3.1+

## Declaration

```swift
func convertPoint(fromSpace: FxDrawingCoordinates, fromX: Double, fromY: Double, toSpace: FxDrawingCoordinates, toX: UnsafeMutablePointer<Double>!, toY: UnsafeMutablePointer<Double>!)
```

```objc
- (void) convertPointFromSpace:(FxDrawingCoordinates) fromSpace fromX:(double) fromX fromY:(double) fromY toSpace:(FxDrawingCoordinates) toSpace toX:(double *) toX toY:(double *) toY;
```

## Mentions

- [Adding onscreen controls to plug-ins](../../Professional-Video-Applications/adding-onscreen-controls-to-plug-ins.md)

## Parameters

- `fromSpace`: The coordinate space to convert from.
- `fromX`: The X coordinate of the position to convert from.
- `fromY`: The Y coordinate of the position to convert from.
- `toSpace`: The coordinate space to convert to.
- `toX`: Returns, by-reference, the X coordinate of the computed position.
- `toY`: Returns, by-reference, the Y coordinate of the computed position.


---

*[View on Apple Developer](https://developer.apple.com/documentation/professional_video_applications/fxonscreencontrolapi/convertpoint(fromspace:fromx:fromy:tospace:tox:toy:))*