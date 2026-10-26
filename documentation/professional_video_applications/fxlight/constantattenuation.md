# constantAttenuation

**Framework**: Professional Video Applications  
**Kind**: property  
**Role**: Instance Property

The constant term of the lighting falloff equation.

**Availability**:
- FxPlug 4.0+

## Declaration

```swift
var constantAttenuation: Float
```

```c
float constantAttenuation;
```

#### Discussion

Lighting falloff is governed by an equation that contains constant, linear, and quadratic terms.

## See Also

### Properties
- [var version: Int](./version.md)
  The version of a lighting information structure.
- [var time: CMTime](./time.md)
  The time of the lighting information.
- [var lightType: FxLightType](./lighttype.md)
  The type of light, whether ambient, directional, point, or spot.
- [var color: Unmanaged<NSColor>!](./color.md)
  The color of the light.
- [var intensity: Float](./intensity.md)
  The brightness with which the light illuminates objects.
- [var linearAttenuation: Float](./linearattenuation.md)
  The linear component of the lighting falloff equation.
- [var quadraticAttenuation: Float](./quadraticattenuation.md)
  The quadratic component of the lighting falloff equation.
- [var castsShadows: ObjCBool](./castsshadows.md)
  A Boolean value that indicates whether a light casts shadows.
- [var spotCutoff: Float](./spotcutoff.md)
  The angle, in radians, of the cone cutoff for spotlights.
- [var spotPenumbraCutoff: Float](./spotpenumbracutoff.md)
  The angle, in radians, of the cone penumbra cutoff for spotlights.
- [var position: FxPoint3D](./position.md)
  The location of the light.
- [var direction: FxPoint3D](./direction.md)
  The direction in which the light points.


---

*[View on Apple Developer](https://developer.apple.com/documentation/professional_video_applications/fxlight/constantattenuation)*