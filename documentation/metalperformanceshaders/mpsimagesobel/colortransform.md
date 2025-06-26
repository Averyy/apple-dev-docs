# colorTransform

**Framework**: Metal Performance Shaders  
**Kind**: property

The color transform used to initialize the Sobel filter.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var colorTransform: UnsafePointer<Float> { get }
```

#### Discussion

This property returns a pointer to the array of 3 floats used to convert RGBA, RGB or RG source images to the destination texture format when said destination is monochrome.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsimagesobel/colortransform)*