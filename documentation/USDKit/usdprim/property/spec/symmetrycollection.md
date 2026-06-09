# USDPrim.Property.Spec.SymmetryCollection

**Framework**: USDKit  
**Kind**: protocol

Symmetry and naming substitutions used in rigging.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
protocol SymmetryCollection
```

## Topics

### Instance Properties
- [var prefix: String?](usdprim/property/spec/symmetrycollection/prefix.md)
  The authored prefix used for symmetry-driven name substitution, or `nil` if not authored.
- [var suffix: String?](usdprim/property/spec/symmetrycollection/suffix.md)
  The authored suffix used for symmetry-driven name substitution, or `nil` if not authored.
- [var symmetricPeer: String?](usdprim/property/spec/symmetrycollection/symmetricpeer.md)
  The symmetric peer path, or `nil` if not authored.
- [var symmetryArguments: Dictionary<String, USDValue>](usdprim/property/spec/symmetrycollection/symmetryarguments.md)
  The symmetry arguments dictionary authored on this property.
- [var symmetryFunction: USDToken?](usdprim/property/spec/symmetrycollection/symmetryfunction.md)
  The symmetry function token, or `nil` if not authored.
### Instance Methods
- [func clearSymmetryArgument(String)](usdprim/property/spec/symmetrycollection/clearsymmetryargument(_:).md)
  Removes `name` from the symmetry arguments dictionary.
- [func setSymmetryArgument(String, to: USDValue)](usdprim/property/spec/symmetrycollection/setsymmetryargument(_:to:).md)
  Sets `name` in the symmetry arguments dictionary to `value`.

## Relationships

### Conforming Types
- [USDPrim.Attribute.Spec](usdprim/attribute/spec.md)
- [USDPrim.Property.Spec](usdprim/property/spec.md)
- [USDPrim.Relationship.Spec](usdprim/relationship/spec.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdprim/property/spec/symmetrycollection)*