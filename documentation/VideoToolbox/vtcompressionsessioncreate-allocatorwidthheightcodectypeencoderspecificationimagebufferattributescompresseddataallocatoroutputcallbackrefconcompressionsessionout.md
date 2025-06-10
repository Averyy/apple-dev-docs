# VTCompressionSessionCreate(allocator:width:height:codecType:encoderSpecification:imageBufferAttributes:compressedDataAllocator:outputCallback:refcon:compressionSessionOut:)

**Framework**: Video Toolbox  
**Kind**: func

Creates an object that compresses video frames.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 10.2+
- visionOS 1.0+

## Declaration

```swift
func VTCompressionSessionCreate(allocator: CFAllocator?, width: Int32, height: Int32, codecType: CMVideoCodecType, encoderSpecification: CFDictionary?, imageBufferAttributes sourceImageBufferAttributes: CFDictionary?, compressedDataAllocator: CFAllocator?, outputCallback: VTCompressionOutputCallback?, refcon outputCallbackRefCon: UnsafeMutableRawPointer?, compressionSessionOut: UnsafeMutablePointer<VTCompressionSession?>) -> OSStatus
```

#### Discussion

The session outputs compressed frames through the output callback.

## Parameters

- `allocator`: An allocator for the session. Pass   to use the default allocator.
- `width`: The pixel width of video frames.
- `height`: The pixel height of video frames.
- `codecType`: The codec type.
- `encoderSpecification`: A video encoder to use. Pass   to let VideoToolbox choose an encoder.
- `sourceImageBufferAttributes`: Using pixel buffers not allocated by VideoToolbox increases the chance that you’ll have to copy image data.
- `compressedDataAllocator`: In MacOS 10.12 and later, using a   may trigger an extra buffer copy.
- `outputCallback`: Pass   only if you’ll be calling   for encoding frames.
- `outputCallbackRefCon`: Client-defined reference value for the output callback.
- `compressionSessionOut`: A pointer to a variable to receive the new compression session.

## Topics

### Callbacks
- [typealias VTCompressionOutputCallback](vtcompressionoutputcallback.md)
  A callback for the system to invoke when it’s finished compressing a frame.
- [typealias VTCompressionOutputHandler](vtcompressionoutputhandler.md)
  A callback for the system to invoke when it’s finished compressing a frame.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/vtcompressionsessioncreate(allocator:width:height:codectype:encoderspecification:imagebufferattributes:compresseddataallocator:outputcallback:refcon:compressionsessionout:))*