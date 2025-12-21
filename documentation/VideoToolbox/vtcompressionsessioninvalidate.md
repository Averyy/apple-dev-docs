# VTCompressionSessionInvalidate(_:)

**Framework**: Video Toolbox  
**Kind**: func

Tears down a compression session.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 10.2+
- visionOS 1.0+

## Declaration

```swift
func VTCompressionSessionInvalidate(_ session: VTCompressionSession)
```

#### Discussion

When you finish using a compression session you created, call `VTCompressionSessionInvalidate` to tear it down, and then call [`CFRelease`](https://developer.apple.com/documentation/CoreFoundation/CFRelease) to release its memory.

> **Note**:  A compression session is automatically invalidated when its retain count reaches zero, but because sessions may be retained by multiple parties, it’s hard to predict when this will happen.  Calling `VTCompressionSessionInvalidate` ensures a deterministic, orderly teardown.

## Parameters

- `session`: The compression session to invalidate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/vtcompressionsessioninvalidate(_:))*