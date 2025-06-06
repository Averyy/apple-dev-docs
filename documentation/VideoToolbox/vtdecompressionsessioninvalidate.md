# VTDecompressionSessionInvalidate(_:)

**Framework**: Videotoolbox  
**Kind**: func

Tears down a decompression session.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 10.2+
- visionOS 1.0+

## Declaration

```swift
func VTDecompressionSessionInvalidate(_ session: VTDecompressionSession)
```

#### Discussion

When you finish with a decompression session you created, call this function to tear it down, and then [`CFRelease`](https://developer.apple.com/documentation/corefoundation/1521153-cfrelease) to release your object reference.

> **Note**:  A decompression session is automatically invalidated when its retain count reaches zero, but because sessions may be retained by multiple parties, it can be hard to predict when this will happen. Calling `VTDecompressionSessionInvalidate` ensures a deterministic, orderly teardown.

 A decompression session is automatically invalidated when its retain count reaches zero, but because sessions may be retained by multiple parties, it can be hard to predict when this will happen. Calling `VTDecompressionSessionInvalidate` ensures a deterministic, orderly teardown.

## Parameters

- `session`: The decompression session to invalidate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/vtdecompressionsessioninvalidate(_:))*