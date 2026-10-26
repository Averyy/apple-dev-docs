# VTHDRPerFrameMetadataGenerationHDRFormatType

**Framework**: Video Toolbox  
**Kind**: struct  
**Role**: Structure

The HDR format type.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
struct VTHDRPerFrameMetadataGenerationHDRFormatType
```

```c
typedef CFStringRef VTHDRPerFrameMetadataGenerationHDRFormatType;
```

## Topics

### Initializers
- [init(CFString)](./vthdrperframemetadatagenerationhdrformattype/init%28_%29.md)
- [init(rawValue: CFString)](./vthdrperframemetadatagenerationhdrformattype/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Data types
- [class VTHDRPerFrameMetadataGenerationSession](./vthdrperframemetadatagenerationsession.md)
  An object that generates per-frame HDR metadata.
- [let kVTHDRPerFrameMetadataGenerationOptionsKey_HDRFormats: CFString](./kvthdrperframemetadatagenerationoptionskey_hdrformats.md)
  Specifies an array of HDR formats to generate.
- [VTHDRPerFrameMetadataGenerationSessionRef](./vthdrperframemetadatagenerationsessionref.md)
  A mechanism for generating HDR Per Frame Metadata and attaching that metadata to a pixel buffer and the backing IOSurface.
- [kVTHDRPerFrameMetadataGenerationHDRFormatType_DolbyVision](./kvthdrperframemetadatagenerationhdrformattype_dolbyvision.md)
  Specifies that DolbyVision data should be generated and attached for each pixel buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/vthdrperframemetadatagenerationhdrformattype)*