# VTHDRPerFrameMetadataGenerationSessionRef

**Framework**: Video Toolbox  
**Kind**: typealias  
**Role**: Type Alias

A mechanism for generating HDR Per Frame Metadata and attaching that metadata to a pixel buffer and the backing IOSurface.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```c
typedef struct OpaqueVTHDRPerFrameMetadataGenerationSession * VTHDRPerFrameMetadataGenerationSessionRef;
```

## Discussion

This object is a CF type, so call `CFRelease` to release your object reference.

## See Also

### Data types
- [struct VTHDRPerFrameMetadataGenerationHDRFormatType](./vthdrperframemetadatagenerationhdrformattype.md)
  The HDR format type.
- [kVTHDRPerFrameMetadataGenerationHDRFormatType_DolbyVision](./kvthdrperframemetadatagenerationhdrformattype_dolbyvision.md)
  Specifies that DolbyVision data should be generated and attached for each pixel buffer.
- [let kVTHDRPerFrameMetadataGenerationOptionsKey_HDRFormats: CFString](./kvthdrperframemetadatagenerationoptionskey_hdrformats.md)
  Specifies an array of HDR formats to generate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/vthdrperframemetadatagenerationsessionref)*