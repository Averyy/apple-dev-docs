# VTDecompressionSessionCreate(allocator:formatDescription:decoderSpecification:imageBufferAttributes:outputCallback:decompressionSessionOut:)

**Framework**: Video Toolbox  
**Kind**: func

Creates a session for decompressing video frames.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 10.2+
- visionOS 1.0+

## Declaration

```swift
func VTDecompressionSessionCreate(allocator: CFAllocator?, formatDescription videoFormatDescription: CMVideoFormatDescription, decoderSpecification videoDecoderSpecification: CFDictionary?, imageBufferAttributes destinationImageBufferAttributes: CFDictionary?, outputCallback: UnsafePointer<VTDecompressionOutputCallbackRecord>?, decompressionSessionOut: UnsafeMutablePointer<VTDecompressionSession?>) -> OSStatus
```

#### Discussion

Decompressed frames are emitted through calls to `outputCallback`.

## Parameters

- `allocator`: An allocator for the session. Pass   to use the default allocator.
- `videoFormatDescription`: The description of the source video frames.
- `videoDecoderSpecification`: The particular video decoder that must be used. Pass   to let VideoToolbox choose a decoder.
- `destinationImageBufferAttributes`: Requirements for the emitted pixel buffers. Pass   to set no requirements.
- `outputCallback`: The callback to be called with decompressed frames. Pass   only if you’ll be calling   for decoding frames.
- `decompressionSessionOut`: A pointer to a variable to receive the new decompression session.

## See Also

- [func VTDecompressionSessionCreate(allocator: CFAllocator?, formatDescription: CMVideoFormatDescription, decoderSpecification: CFDictionary?, imageBufferAttributes: CFDictionary?, decompressionSessionOut: UnsafeMutablePointer<VTDecompressionSession?>) -> OSStatus](vtdecompressionsessioncreate(allocator:formatdescription:decoderspecification:imagebufferattributes:decompressionsessionout:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/vtdecompressionsessioncreate(allocator:formatdescription:decoderspecification:imagebufferattributes:outputcallback:decompressionsessionout:))*