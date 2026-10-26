# init(version:time:lightType:color:intensity:constantAttenuation:linearAttenuation:quadraticAttenuation:castsShadows:spotCutoff:spotPenumbraCutoff:position:direction:)

**Framework**: Professional Video Applications  
**Kind**: init  
**Role**: Initializer

Initializes an FxLight lighting information structure with parameters.

**Availability**:
- FxPlug 4.1+

## Declaration

```swift
init(version: Int, time: CMTime, lightType: FxLightType, color: Unmanaged<NSColor>!, intensity: Float, constantAttenuation: Float, linearAttenuation: Float, quadraticAttenuation: Float, castsShadows: ObjCBool, spotCutoff: Float, spotPenumbraCutoff: Float, position: FxPoint3D, direction: FxPoint3D)
```

## Parameters

- `version`: The version of a lighting information structure.
- `time`: The time of the lighting information.
- `lightType`: The type of light, whether ambient, directional, point, or spot.
- `color`: The color of the light.
- `intensity`: The brightness with which the light illuminates objects.
- `constantAttenuation`: The constant term of the lighting falloff equation.
- `linearAttenuation`: The linear component of the lighting falloff equation.
- `quadraticAttenuation`: The quadratic component of the lighting falloff equation.
- `castsShadows`: A Boolean value that indicates whether a light casts shadows.
- `spotCutoff`: The angle, in radians, of the cone cutoff for spotlights.
- `spotPenumbraCutoff`: The angle, in radians, of the cone penumbra cutoff for spotlights.
- `position`: The location of the light.
- `direction`: The direction in which the light points.

## See Also

### Initializers
- [init()](./init%28%29.md)
  Initializes an FxLight lighting information structure.


---

*[View on Apple Developer](https://developer.apple.com/documentation/professional_video_applications/fxlight/init(version:time:lighttype:color:intensity:constantattenuation:linearattenuation:quadraticattenuation:castsshadows:spotcutoff:spotpenumbracutoff:position:direction:))*