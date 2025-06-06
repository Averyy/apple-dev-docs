# VTPixelTransferSessionInvalidate(_:)

**Framework**: Videotoolbox  
**Kind**: func

Tears down a pixel transfer session.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 10.8+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
func VTPixelTransferSessionInvalidate(_ session: VTPixelTransferSession)
```

#### Discussion

When you finish with a pixel transfer session you created, call this function to tear it down, and then call [`CFRelease`](https://developer.apple.com/documentation/corefoundation/1521153-cfrelease) to release your object reference.

> **Note**:  A pixel transfer session is automatically invalidated when its retain count reaches zero, but because sessions may be retained by multiple parties, it’s hard to predict when the invalidation will happen.  Calling this function ensures a deterministic, orderly teardown.

## Parameters

- `session`: The pixel transfer session to invalidate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/vtpixeltransfersessioninvalidate(_:))*