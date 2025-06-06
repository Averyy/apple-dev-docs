# offset

**Framework**: Metal Performance Shaders  
**Kind**: instp

The position of the destination image's clip rectangle origin, relative to the source image.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
var offset: MPSOffset { get set }
```

#### Discussion

The offset is defined as the position of `clipRect.origin` in source image coordinates. The default value is `{0,0,0}`, indicating that the top left corners of the clip rectangle and the source image align. 

The value of `offset.z` is the index of the starting source image in batch processing mode.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpscnnkernel/1648835-offset)*