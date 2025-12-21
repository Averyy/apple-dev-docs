# roiTileIndex

**Framework**: Core Image  
**Kind**: property  
**Required**: Yes

This property tells a tiled-input processor which input tile index is being processed.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
var roiTileIndex: Int { get }
```

#### Discussion

This property is only relevant if your processor implements `/CIImageProcessorKernel/roiTileArrayForInput:arguments:outputRect:`

This can be useful if the processor needs to clear the [`CIImageProcessorOutput`](ciimageprocessoroutput.md) before the first tile is processed.

## See Also

- [var digest: UInt64](ciimageprocessorinput/digest.md)
  A 64-bit digest that uniquely describes the contents of the input to a processor.
- [var roiTileCount: Int](ciimageprocessorinput/roitilecount.md)
  This property tells a tiled-input processor how many input tiles will be processed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/ciimageprocessorinput/roitileindex)*