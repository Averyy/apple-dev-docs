# FxLight

**Framework**: Professional Video Applications  
**Kind**: struct  
**Role**: Structure

A structure that contains lighting information.

**Availability**:
- FxPlug 4.0+

## Declaration

```swift
struct FxLight
```

```c
typedef struct FxLight { ... } FxLight;
```

#### Overview

Note that the FxLight structure uses [`CMTime`](../CoreMedia/cmtime.md) in FxPlug 4, and replaces `FxLightInfo` from `FxLightingAPI` and `FxLightInfo_V1` from `FxLightingAPI_v2`.

## Topics

### Properties
- [var version: Int](./fxlight/version.md)
  The version of a lighting information structure.
- [var time: CMTime](./fxlight/time.md)
  The time of the lighting information.
- [var lightType: FxLightType](./fxlight/lighttype.md)
  The type of light, whether ambient, directional, point, or spot.
- [var color: Unmanaged<NSColor>!](./fxlight/color.md)
  The color of the light.
- [var intensity: Float](./fxlight/intensity.md)
  The brightness with which the light illuminates objects.
- [var constantAttenuation: Float](./fxlight/constantattenuation.md)
  The constant term of the lighting falloff equation.
- [var linearAttenuation: Float](./fxlight/linearattenuation.md)
  The linear component of the lighting falloff equation.
- [var quadraticAttenuation: Float](./fxlight/quadraticattenuation.md)
  The quadratic component of the lighting falloff equation.
- [var castsShadows: ObjCBool](./fxlight/castsshadows.md)
  A Boolean value that indicates whether a light casts shadows.
- [var spotCutoff: Float](./fxlight/spotcutoff.md)
  The angle, in radians, of the cone cutoff for spotlights.
- [var spotPenumbraCutoff: Float](./fxlight/spotpenumbracutoff.md)
  The angle, in radians, of the cone penumbra cutoff for spotlights.
- [var position: FxPoint3D](./fxlight/position.md)
  The location of the light.
- [var direction: FxPoint3D](./fxlight/direction.md)
  The direction in which the light points.
### Initializers
- [init()](./fxlight/init%28%29.md)
  Initializes an FxLight lighting information structure.
- [init(version: Int, time: CMTime, lightType: FxLightType, color: Unmanaged<NSColor>!, intensity: Float, constantAttenuation: Float, linearAttenuation: Float, quadraticAttenuation: Float, castsShadows: ObjCBool, spotCutoff: Float, spotPenumbraCutoff: Float, position: FxPoint3D, direction: FxPoint3D)](./fxlight/init%28version,time,lighttype,color,intensity,constantattenuation,linearattenuation,quadraticattenuation,castsshadows,spotcutoff,spotpenumbracutoff,position,direction%29.md)
  Initializes an FxLight lighting information structure with parameters.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Sendable](../Swift/sendable.md)

## See Also

### Getting Lighting Information
- [func lightInfo(UnsafeMutablePointer<FxLight>!, forLight: Int, at: CMTime) throws](./fxlightingapi_v3/lightinfo%28_,forlight,at%29.md)
  Provides information about a light at a particular time.
- [func numberOfLights(at: CMTime) -> Int](./fxlightingapi_v3/numberoflights%28at%29.md)
  Retrieves the number of lights at the passed-in time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/professional_video_applications/fxlight)*