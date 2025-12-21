# init(buffer:presentationTimeStamp:)

**Framework**: Video Toolbox  
**Kind**: init

Creates a frame object with a pixel buffer and presentation time.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 15.4+
- tvOS 26.0+
- visionOS 26.0+

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