# VTHDRPerFrameMetadataGenerationSession

**Framework**: Video Toolbox  
**Role**: API Collection

An object that generates per-frame HDR metadata.

## Topics

### Data types
- [class VTHDRPerFrameMetadataGenerationSession](./vthdrperframemetadatagenerationsession.md)
  An object that generates per-frame HDR metadata.
- [struct VTHDRPerFrameMetadataGenerationHDRFormatType](./vthdrperframemetadatagenerationhdrformattype.md)
  The HDR format type.
- [let kVTHDRPerFrameMetadataGenerationOptionsKey_HDRFormats: CFString](./kvthdrperframemetadatagenerationoptionskey_hdrformats.md)
  Specifies an array of HDR formats to generate.
- [VTHDRPerFrameMetadataGenerationSessionRef](./vthdrperframemetadatagenerationsessionref.md)
  A mechanism for generating HDR Per Frame Metadata and attaching that metadata to a pixel buffer and the backing IOSurface.
- [kVTHDRPerFrameMetadataGenerationHDRFormatType_DolbyVision](./kvthdrperframemetadatagenerationhdrformattype_dolbyvision.md)
  Specifies that DolbyVision data should be generated and attached for each pixel buffer.
### Creating a session
- [VTHDRPerFrameMetadataGenerationSessionCreate](./vthdrperframemetadatagenerationsessioncreate.md)
  Creates a metadata generation session object.
### Attaching metadata
- [VTHDRPerFrameMetadataGenerationSessionAttachMetadata](./vthdrperframemetadatagenerationsessionattachmetadata.md)
  Attaches per-frame metadata to the pixel buffer and the backing IOSurface.
### Accessing the type identifier
- [VTHDRPerFrameMetadataGenerationSessionGetTypeID](./vthdrperframemetadatagenerationsessiongettypeid.md)
  Retrieves the Core Foundation type identifier for the session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/vthdrperframemetadatagenerationsession-api-collection)*