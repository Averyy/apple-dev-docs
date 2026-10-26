# eCEColorSpace

**Framework**: Professional Video Applications  
**Kind**: struct  
**Role**: Structure

The list of color spaces an encoder extension can support.

**Availability**:
- ProVideo Encoder Extensions 1.0+

## Declaration

```swift
struct eCEColorSpace
```

```c
typedef enum eCEColorSpace;
```

## Topics

### Constants
- [var eCEColorSpace601NTSC: eCEColorSpace](./ececolorspace601ntsc.md)
- [var eCEColorSpace601PAL: eCEColorSpace](./ececolorspace601pal.md)
- [var eCEColorSpace709: eCEColorSpace](./ececolorspace709.md)
- [var eCEColorSpaceDeviceRGB: eCEColorSpace](./ececolorspacedevicergb.md)
- [var eCEColorSpaceUnknown: eCEColorSpace](./ececolorspaceunknown.md)
- [var eCEColorSpecDCIP3: eCEColorSpace](./ececolorspecdcip3.md)
- [var eCEColorSpecITUR2020: eCEColorSpace](./ececolorspecitur2020.md)
- [var eCEColorSpecP3D65: eCEColorSpace](./ececolorspecp3d65.md)
- [var eCEColorSpecP3D65HLG: eCEColorSpace](./ececolorspecp3d65hlg.md)
- [var eCEColorSpecP3D65PQ: eCEColorSpace](./ececolorspecp3d65pq.md)
- [var eCEColorSpecP3DCIPQ: eCEColorSpace](./ececolorspecp3dcipq.md)
- [var eCEColorSpecRGBHDRLinear: eCEColorSpace](./ececolorspecrgbhdrlinear.md)
- [var eCEColorSpecRGBSDRLinear: eCEColorSpace](./ececolorspecrgbsdrlinear.md)
- [var eCEColorSpecSRGB: eCEColorSpace](./ececolorspecsrgb.md)
- [var eCEColorSpectITUR2020HLG: eCEColorSpace](./ececolorspectitur2020hlg.md)
- [var eCEColorSpectITUR2020PQ: eCEColorSpace](./ececolorspectitur2020pq.md)
### Initializers
- [init(Int32)](./ececolorspace/init%28_%29.md)
- [init(rawValue: Int32)](./ececolorspace/init%28rawvalue%29.md)
### Instance Properties
- [var rawValue: Int32](./ececolorspace/rawvalue.md)
### Default Implementations
- [Equatable Implementations](./ececolorspace/equatable-implementations.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)

## See Also

### Supporting Color Spaces
- [func supportedColorSpaces() -> [NSNumber]!](./compressorextensioncolorspaces/supportedcolorspaces%28%29.md)
  Returns the supported color spaces in an extension.


---

*[View on Apple Developer](https://developer.apple.com/documentation/professional_video_applications/ececolorspace)*