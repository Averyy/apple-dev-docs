# USDPrim.Property.Spec.SymmetryCollection

**Framework**: USDKit  
**Kind**: protocol  
**Role**: Protocol

Symmetry and naming substitutions used in rigging.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
protocol SymmetryCollection
```

## Topics

### Instance Properties
- [var prefix: String?](./symmetrycollection/prefix.md)
  The authored prefix used for symmetry-driven name substitution, or `nil` if not authored.
- [var suffix: String?](./symmetrycollection/suffix.md)
  The authored suffix used for symmetry-driven name substitution, or `nil` if not authored.
- [var symmetricPeer: String?](./symmetrycollection/symmetricpeer.md)
  The symmetric peer path, or `nil` if not authored.
- [var symmetryArguments: Dictionary<String, USDValue>](./symmetrycollection/symmetryarguments.md)
  The symmetry arguments dictionary authored on this property.
- [var symmetryFunction: USDToken?](./symmetrycollection/symmetryfunction.md)
  The symmetry function token, or `nil` if not authored.
### Instance Methods
- [func clearSymmetryArgument(String)](./symmetrycollection/clearsymmetryargument%28_%29.md)
  Removes `name` from the symmetry arguments dictionary.
- [func setSymmetryArgument(String, to: USDValue)](./symmetrycollection/setsymmetryargument%28_,to%29.md)
  Sets `name` in the symmetry arguments dictionary to `value`.

## Relationships

### Conforming Types
- [USDPrim.Attribute.Spec](../../attribute/spec.md)
- [USDPrim.Property.Spec](../spec.md)
- [USDPrim.Relationship.Spec](../../relationship/spec.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdprim/property/spec/symmetrycollection)*