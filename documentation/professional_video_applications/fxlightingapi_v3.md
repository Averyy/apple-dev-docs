# FxLightingAPI_v3

**Framework**: Professional Video Applications  
**Kind**: protocol  
**Role**: Protocol

An API you use to get information about lights in a scene in a Motion project.

**Availability**:
- FxPlug 4.0+

## Declaration

```swift
protocol FxLightingAPI_v3
```

```objc
@protocol FxLightingAPI_v3
```

## Overview

This API provides a plug-in with the number of lights in a scene, as well as information about each light at a given time. A plug-in only has access to lights that are in the same group as the plug-in or a subgroup of such a group.

## Topics

### Getting Lighting Information
- [func lightInfo(UnsafeMutablePointer<FxLight>!, forLight: Int, at: CMTime) throws](./fxlightingapi_v3/lightinfo%28_,forlight,at%29.md)
  Provides information about a light at a particular time.
- [func numberOfLights(at: CMTime) -> Int](./fxlightingapi_v3/numberoflights%28at%29.md)
  Retrieves the number of lights at the passed-in time.
- [struct FxLight](./fxlight.md)
  A structure that contains lighting information.
### Constants
- [var kFxLight_V3: Int32](./kfxlight_v3.md)
  The version number of the lighting information.
- [var FxLight_CurrentVersion: Int32](./fxlight_currentversion.md)
  A property used to define a lighting information structure as being the most current version.
- [struct FxLight](./fxlight.md)
  A structure that contains lighting information.
- [typealias FxLightType](./fxlighttype.md)
  The type of lighting.

## See Also

### 3D and lighting
- [protocol Fx3DAPI_v5](./fx3dapi_v5.md)
  An API that defines the methods the host application provides to get information about the 3D environment, including camera and object transforms.
- [class FxMatrix44](./fxmatrix44.md)
  The `FxMatrix` class encapsulates a 4x4 matrix object and provides matrix inversion and transforming of 2D and 3D points.


---

*[View on Apple Developer](https://developer.apple.com/documentation/professional_video_applications/fxlightingapi_v3)*