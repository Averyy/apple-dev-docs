# UITraitOverrides

**Framework**: UIKit  
**Kind**: struct

A mutable container of traits you use to set trait changes for an object and its descendants.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- tvOS 17.0+
- visionOS ?+

## Declaration

```swift
struct UITraitOverrides
```

## Topics

### Inspecting overrides
- [func contains(UITrait) -> Bool](uitraitoverrides-swift.struct/contains(_:).md)
  Returns a Boolean value that indicates whether the trait overrides contain a change for the trait you provide.
### Removing overrides
- [func remove(UITrait)](uitraitoverrides-swift.struct/remove(_:).md)
  Removes the change for the trait you provide.

## Relationships

### Conforms To
- [Copyable](../swift/copyable.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomReflectable](../swift/customreflectable.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Escapable](../swift/escapable.md)
- [UIMutableTraits](uimutabletraits-13ja5.md)

## See Also

- [var traitOverrides: UITraitOverrides](uipresentationcontroller/traitoverrides-629ka.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitraitoverrides-swift.struct)*