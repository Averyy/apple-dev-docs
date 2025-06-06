# extent

**Framework**: Core Image  
**Kind**: instp

The extent of the image associated with the image accumulator.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var extent: CGRect { get }
```

#### Discussion

Extent is a rectangle that specifies the size of the image associated with the image accumulator. This rectangle is the size of the complete region of the working coordinate space, and is a fixed area. It specifies the x-value of the rectangle origin, the y-value of the rectangle origin, and the width and height.

## See Also

- [var format: CIFormat](ciimageaccumulator/1427716-format.md)
  The pixel format of the image accumulator.
- [func image() -> CIImage](ciimageaccumulator/1427704-image.md)
  Returns the current contents of the image accumulator. 


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/ciimageaccumulator/1427714-extent)*