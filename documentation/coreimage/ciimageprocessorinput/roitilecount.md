# roiTileCount

**Framework**: Core Image  
**Kind**: property  
**Required**: Yes

This property tells a tiled-input processor how many input tiles will be processed.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
var roiTileCount: Int { get }
```

#### Discussion

This property is only relevant if your processor implements `/CIImageProcessorKernel/roiTileArrayForInput:arguments:outputRect:`

This can be useful if the processor needs to do work [`CIImageProcessorOutput`](ciimageprocessoroutput.md) after the last tile is processed.

## See Also

- [var digest: UInt64](ciimageprocessorinput/digest.md)
  A 64-bit digest that uniquely describes the contents of the input to a processor.
- [var roiTileIndex: Int](ciimageprocessorinput/roitileindex.md)
  This property tells a tiled-input processor which input tile index is being processed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/ciimageprocessorinput/roitilecount)*