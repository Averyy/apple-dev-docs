# CompositeExtremumIndex

**Framework**: hvf  
**Kind**: struct

The index of an extremum rotation or translation in a Composite part

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
struct CompositeExtremumIndex
```

## Topics

### Operators
- [static func == (CompositeExtremumIndex, CompositeExtremumIndex) -> Bool](compositeextremumindex/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Initializers
- [init(row: UInt16, column: UInt16)](compositeextremumindex/init(row:column:).md)
### Instance Properties
- [var column: UInt16](compositeextremumindex/column.md)
  The column (offset of the extremum of the composite)
- [var hashValue: Int](compositeextremumindex/hashvalue.md)
  The hash value.
- [var row: UInt16](compositeextremumindex/row.md)
  The row (offset into the part’s render transform subtree)
### Instance Methods
- [func hash(into: inout Hasher)](compositeextremumindex/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Default Implementations
- [Equatable Implementations](compositeextremumindex/equatable-implementations.md)

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/hvf/compositeextremumindex)*