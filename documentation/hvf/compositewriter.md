# CompositeWriter

**Framework**: hvf  
**Kind**: protocol

Protocol for creating a Composite part for rendering or to build an HVGL table

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst ?+
- macOS 15.4+
- tvOS 18.4+
- visionOS 2.4+
- watchOS 11.4+

## Declaration

```swift
protocol CompositeWriter
```

## Topics

### Instance Properties
- [var axisCount: Int](compositewriter/axiscount.md)
  The number of axes the part has
- [var extremumCSCAxisValues: [Float]](compositewriter/extremumcscaxisvalues.md)
  The axis values for extrema, in CSC sparse matrix format
- [var extremumCSCColumnStarts: [UInt16]](compositewriter/extremumcsccolumnstarts.md)
  The CSC column starts for extremum axis values The columns correspond to the axis extrema, with minimum first, then maximum
- [var extremumCSCRowIndices: [UInt16]](compositewriter/extremumcscrowindices.md)
  The CSC row indices for the extremum axis values
- [var extremumRotationIndices: [CompositeExtremumIndex]](compositewriter/extremumrotationindices.md)
  The row/column indices for extremum rotations, ascending by row/column
- [var extremumRotations: [Float]](compositewriter/extremumrotations.md)
  The corresponding extremum rotations
- [var extremumTranslationIndices: [CompositeExtremumIndex]](compositewriter/extremumtranslationindices.md)
  The row/column indices for extremum translations, ascending by row/column
- [var extremumTranslations: [CompositeSubpartTranslation]](compositewriter/extremumtranslations.md)
  The corresponding extremum translations
- [var masterCSCAxisValues: [Float]](compositewriter/mastercscaxisvalues.md)
  The axis values for the master, corresponding to the row indices
- [var masterCSCRowIndices: [UInt16]](compositewriter/mastercscrowindices.md)
  The row indices for the master axis values, ascending order
- [var masterRotationIndices: [UInt16]](compositewriter/masterrotationindices.md)
  The row indices for master rotations, ascending
- [var masterRotations: [Float]](compositewriter/masterrotations.md)
  The corresponding master rotations, in radians, counterclockwise
- [var masterTranslationIndices: [UInt16]](compositewriter/mastertranslationindices.md)
  The row indices for master translations, ascending
- [var masterTranslations: [CompositeSubpartTranslation]](compositewriter/mastertranslations.md)
  The corresponding master translations
- [var maximumExtremumCount: Int](compositewriter/maximumextremumcount.md)
  The largest number of axis extrema of any part in the structure tree
- [var subpartCount: Int](compositewriter/subpartcount.md)
  The number of subparts the part has
- [var subparts: [CompositeSubpart]](compositewriter/subparts.md)
  The composite’s subparts
- [var totalAxisCount: Int](compositewriter/totalaxiscount.md)
  The total number of axes in the composite’s structure tree (including its own)
- [var totalPartCount: Int](compositewriter/totalpartcount.md)
  The total number of parts in the composite’s structure tree (including its own)
### Instance Methods
- [func column(axis: Int, extremum: AxisExtremum) -> Int](compositewriter/column(axis:extremum:).md)
  Convenience for computing matrix column
- [func finalize() -> Bool](compositewriter/finalize.md)
  Call when done writing the Composite


---

*[View on Apple Developer](https://developer.apple.com/documentation/hvf/compositewriter)*