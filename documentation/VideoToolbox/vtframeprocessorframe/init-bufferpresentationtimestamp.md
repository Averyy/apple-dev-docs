# init(buffer:presentationTimeStamp:)

**Framework**: Videotoolbox  
**Kind**: init

Creates a frame object with a pixel buffer and presentation time.

**Availability**:
- macOS 15.4+

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