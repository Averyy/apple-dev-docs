# kVTHDRPerFrameMetadataGenerationOptionsKey_HDRFormats

**Framework**: Video Toolbox  
**Kind**: var  
**Role**: Global Variable

Specifies an array of HDR formats to generate.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
let kVTHDRPerFrameMetadataGenerationOptionsKey_HDRFormats: CFString
```

```c
extern CFStringRef const kVTHDRPerFrameMetadataGenerationOptionsKey_HDRFormats;
```

#### Discussion

This key represents a CFArrayRef. Only a value of [`kVTHDRPerFrameMetadataGenerationHDRFormatType_DolbyVision`](./kvthdrperframemetadatagenerationhdrformattype_dolbyvision.md) is supported.

## See Also

### Data types
- [class VTHDRPerFrameMetadataGenerationSession](./vthdrperframemetadatagenerationsession.md)
  An object that generates per-frame HDR metadata.
- [struct VTHDRPerFrameMetadataGenerationHDRFormatType](./vthdrperframemetadatagenerationhdrformattype.md)
  The HDR format type.
- [VTHDRPerFrameMetadataGenerationSessionRef](./vthdrperframemetadatagenerationsessionref.md)
  A mechanism for generating HDR Per Frame Metadata and attaching that metadata to a pixel buffer and the backing IOSurface.
- [kVTHDRPerFrameMetadataGenerationHDRFormatType_DolbyVision](./kvthdrperframemetadatagenerationhdrformattype_dolbyvision.md)
  Specifies that DolbyVision data should be generated and attached for each pixel buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/kvthdrperframemetadatagenerationoptionskey_hdrformats)*