# VTPixelTransferSessionCreate(allocator:pixelTransferSessionOut:)

**Framework**: Videotoolbox  
**Kind**: func

Creates a session for transferring images between Core Video image buffers that hold pixels in main memory.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 10.8+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
func VTPixelTransferSessionCreate(allocator: CFAllocator?, pixelTransferSessionOut: UnsafeMutablePointer<VTPixelTransferSession?>) -> OSStatus
```

#### Discussion

The function creates a session for transferring images between [`CVPixelBuffer`](https://developer.apple.com/documentation/CoreVideo/cvpixelbuffer-q2e) objects.

## Parameters

- `allocator`: An allocator for the session.  Pass   to use the default allocator.
- `pixelTransferSessionOut`: Points to a variable to receive the new pixel transfer session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/vtpixeltransfersessioncreate(allocator:pixeltransfersessionout:))*