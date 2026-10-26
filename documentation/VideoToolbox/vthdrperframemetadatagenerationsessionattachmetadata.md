# VTHDRPerFrameMetadataGenerationSessionAttachMetadata

**Framework**: Video Toolbox  
**Kind**: func  
**Role**: Function

Attaches per-frame metadata to the pixel buffer and the backing IOSurface.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```c
extern OSStatus VTHDRPerFrameMetadataGenerationSessionAttachMetadata(VTHDRPerFrameMetadataGenerationSessionRef hdrPerFrameMetadataGenerationSession, CVPixelBufferRef pixelBuffer, Boolean sceneChange);
```

#### Discussion

Call this to analyze and attach HDR Metadata. This call will change CVPixelBuffer attachments and backing IOSurface attachments.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/vthdrperframemetadatagenerationsessionattachmetadata)*