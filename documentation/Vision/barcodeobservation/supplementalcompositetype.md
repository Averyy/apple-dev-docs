# supplementalCompositeType

**Framework**: Vision  
**Kind**: property

The supplemental composite type.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
let supplementalCompositeType: BarcodeObservation.CompositeType?
```

#### Discussion

Currently, this can only refer to the composite flag of the 2D symbology as part of a GS1 composite symbology.

This attribute only exists when the primary descriptor is the 1D symbology of a GS1 composite symbology, and of which a valid 2D counterpart has been coalesced into.

## See Also

- [BarcodeObservation.CompositeType](barcodeobservation/compositetype.md)
  Composite types for barcode requests.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/barcodeobservation/supplementalcompositetype)*