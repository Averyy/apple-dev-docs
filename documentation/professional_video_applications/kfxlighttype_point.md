# kFxLightType_Point

**Framework**: Professional Video Applications  
**Kind**: var  
**Role**: Global Variable

Light which exists at a point and illuminates in all directions.

**Availability**:
- FxPlug 3.1+

## Declaration

```swift
var kFxLightType_Point: Int { get }
```

```c
kFxLightType_Point
```

## Discussion

Unlike ambient light, light eminating from a point light can be occluded.

## See Also

### Constants
- [var kFxLightType_Ambient: Int](./kfxlighttype_ambient.md)
  Light that illuminates all objects in the scene evenly.
- [var kFxLightType_Directional: Int](./kfxlighttype_directional.md)
  Light that comes from a particular direction, but which is infinitely far away.
- [var kFxLightType_Spot: Int](./kfxlighttype_spot.md)
  Light which has a limiting cone, and which can be positioned and pointed in a particular direction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/professional_video_applications/kfxlighttype_point)*