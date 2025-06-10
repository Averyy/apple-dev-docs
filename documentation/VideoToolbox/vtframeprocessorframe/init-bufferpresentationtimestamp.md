# init(buffer:presentationTimeStamp:)

**Framework**: Video Toolbox  
**Kind**: init

Creates a frame object with a pixel buffer and presentation time.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 15.4+
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
init?(buffer: CVPixelBuffer, presentationTimeStamp: CMTime)
```

#### Discussion

Initialization fails if you specify a `NULL` buffer or one that isn’t backed by an `IOSurface`.

## Parameters

- `buffer`: A pixel buffer for the frame. This value must be non-NULL and IOSurface backed.
- `presentationTimeStamp`: The presentation timestamp of the buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/vtframeprocessorframe/init(buffer:presentationtimestamp:))*