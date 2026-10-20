# UITraitOverrides

**Framework**: UIKit  
**Kind**: struct  
**Role**: Structure

A mutable container of traits you use to set trait changes for an object and its descendants.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- tvOS 17.0+
- visionOS

## Declaration

```swift
struct UITraitOverrides
```

## Topics

### Inspecting overrides
- [func contains(UITrait) -> Bool](./uitraitoverrides-swift.struct/contains%28_%29.md)
  Returns a Boolean value that indicates whether the trait overrides contain a change for the trait you provide.
### Removing overrides
- [func remove(UITrait)](./uitraitoverrides-swift.struct/remove%28_%29.md)
  Removes the change for the trait you provide.

## Relationships

### Conforms To
- [Copyable](../Swift/copyable.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomReflectable](../Swift/customreflectable.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Escapable](../Swift/escapable.md)
- [UIMutableTraits](./uimutabletraits-13ja5.md)

## See Also

### Overriding trait values
- [var traitOverrides: UITraitOverrides](./uipresentationcontroller/traitoverrides-629ka.md)
- [var overrideTraitCollection: UITraitCollection?](./uipresentationcontroller/overridetraitcollection.md)
  Interface traits for the presented view controller, to use in place of traits from the iOS environment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitraitoverrides-swift.struct)*