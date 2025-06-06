# CompositeSubpart

**Framework**: hvf  
**Kind**: struct

A subpart in a Composite part

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
struct CompositeSubpart
```

## Topics

### Operators
- [static func == (CompositeSubpart, CompositeSubpart) -> Bool](compositesubpart/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Initializers
- [init(partIndex: UInt32, treePartOffset: UInt16, treeAxisOffset: UInt16)](compositesubpart/init(partindex:treepartoffset:treeaxisoffset:).md)
### Instance Properties
- [var hashValue: Int](compositesubpart/hashvalue.md)
  The hash value.
- [var partIndex: UInt32](compositesubpart/partindex.md)
  The index of the part this subpart renders
- [var treeAxisOffset: UInt16](compositesubpart/treeaxisoffset.md)
  The offset of the part’s axis value settings in the render context axis value tree (depth first)
- [var treePartOffset: UInt16](compositesubpart/treepartoffset.md)
  The offset of the part’s data in the render context transform tree (depth first)
### Instance Methods
- [func hash(into: inout Hasher)](compositesubpart/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Default Implementations
- [Equatable Implementations](compositesubpart/equatable-implementations.md)

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/hvf/compositesubpart)*