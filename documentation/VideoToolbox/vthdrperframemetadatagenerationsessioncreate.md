# VTHDRPerFrameMetadataGenerationSessionCreate

**Framework**: Video Toolbox  
**Kind**: func  
**Role**: Function

Creates a metadata generation session object.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```c
extern OSStatus VTHDRPerFrameMetadataGenerationSessionCreate(CFAllocatorRef allocator, float framesPerSecond, CFDictionaryRef options, VTHDRPerFrameMetadataGenerationSessionRef*hdrPerFrameMetadataGenerationSessionOut);
```

#### Discussion

The returned session object may be used to perform HDR Per Frame Metadata Generation.

Call CFRelease to release your object reference.

## Parameters

- `allocator`: The allocator.
- `framesPerSecond`: Value must be greater than 0.0
- `options`: `CFDictionary` may contain the key [`kVTHDRPerFrameMetadataGenerationOptionsKey_HDRFormats`](./kvthdrperframemetadatagenerationoptionskey_hdrformats.md).
- `hdrPerFrameMetadataGenerationSessionOut`: A pointer to a variable to receive the new session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/vthdrperframemetadatagenerationsessioncreate)*