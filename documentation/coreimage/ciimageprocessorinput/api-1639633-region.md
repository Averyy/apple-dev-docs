# region

**Framework**: Core Image  
**Kind**: intfp  
**Required**: Yes

The area within the input image to be processed.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
var region: CGRect { get }
```

#### Discussion

This region will always contain, but may be larger than, the region produced by the `roiCallback` block parameter of the `withExtent(_:processorDescription:argumentDigest:inputFormat:outputFormat:options:roiCallback:processor:)` method. 

## See Also

- [var bytesPerRow: Int](ciimageprocessorinput/1639655-bytesperrow.md)
  The number of bytes per row of pixels in the input image data.
- [var format: CIFormat](ciimageprocessorinput/1639639-format.md)
  The per-pixel data format of the image to be processed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/ciimageprocessorinput/1639633-region)*