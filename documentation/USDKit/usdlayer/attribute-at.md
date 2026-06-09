# attribute(at:)

**Framework**: USDKit  
**Kind**: method

Returns the attribute spec at the given path.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
func attribute(at path: USDLayer.Path) -> USDPrim.Attribute.Spec?
```

#### Return Value

The attribute spec, or `nil` if none is authored at `path`.

## Parameters

- `path`: The path to look up.

## See Also

- [func prim(at: USDLayer.Path) -> USDPrim.Spec?](usdlayer/prim(at:).md)
  Returns the prim spec authored at the given path, or `nil` if no prim spec exists there.
- [func property(at: USDLayer.Path) -> USDPrim.Property.Spec?](usdlayer/property(at:).md)
  Returns the property spec at the given path.
- [func relationship(at: USDLayer.Path) -> USDPrim.Relationship.Spec?](usdlayer/relationship(at:).md)
  Returns the relationship spec at the given path.
- [func spec(at: USDLayer.Path) -> USDLayer.Spec?](usdlayer/spec(at:).md)
  Returns the spec at the given path, or `nil` if no spec is authored there.
- [func specType(at: USDLayer.Path) -> USDLayer.SpecType?](usdlayer/spectype(at:).md)
  Returns the kind of spec authored at the given path, or `nil` if nothing is authored there.
- [func traverse(at: USDLayer.Path, (USDLayer.Path) -> Void)](usdlayer/traverse(at:_:).md)
  Walks the spec tree rooted at the given path, calling `body` for each spec’s path.
- [USDLayer.Path](usdlayer/path.md)
  A path within a USD scene hierarchy.
- [USDLayer.PathExpression](usdlayer/pathexpression.md)
  A boolean expression over path patterns for selecting sets of prims.
- [USDLayer.Spec](usdlayer/spec.md)
  A handle to a single spec stored in a layer.
- [USDLayer.SpecType](usdlayer/spectype.md)
  The kind of spec stored at a path in a layer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdlayer/attribute(at:))*