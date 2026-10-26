# kFxLightType_Directional

**Framework**: Professional Video Applications  
**Kind**: var  
**Role**: Global Variable

Light that comes from a particular direction, but which is infinitely far away.

**Availability**:
- FxPlug 3.1+

## Declaration

```swift
var kFxLightType_Directional: Int { get }
```

```c
kFxLightType_Directional
```

#### Discussion

This type of light is often used to simulate the sun, and it casts parallel light rays at every point in space.

## See Also

### Constants
- [var kFxLightType_Ambient: Int](./kfxlighttype_ambient.md)
  Light that illuminates all objects in the scene evenly.
- [var kFxLightType_Point: Int](./kfxlighttype_point.md)
  Light which exists at a point and illuminates in all directions.
- [var kFxLightType_Spot: Int](./kfxlighttype_spot.md)
  Light which has a limiting cone, and which can be positioned and pointed in a particular direction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/professional_video_applications/kfxlighttype_directional)*