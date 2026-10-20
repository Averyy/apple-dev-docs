# traverse(at:_:)

**Framework**: USDKit  
**Kind**: method  
**Role**: Instance Method

Walks the spec tree rooted at the given path, calling `body` for each spec’s path.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
func traverse(at path: USDLayer.Path, _ body: (USDLayer.Path) -> Void)
```

## Parameters

- `path`: The root path to traverse from.
- `body`: A closure invoked once per visited path.

## See Also

### Accessing scene description by path
- [func prim(at: USDLayer.Path) -> USDPrim.Spec?](./prim%28at%29.md)
  Returns the prim spec authored at the given path, or `nil` if no prim spec exists there.
- [func property(at: USDLayer.Path) -> USDPrim.Property.Spec?](./property%28at%29.md)
  Returns the property spec at the given path.
- [func attribute(at: USDLayer.Path) -> USDPrim.Attribute.Spec?](./attribute%28at%29.md)
  Returns the attribute spec at the given path.
- [func relationship(at: USDLayer.Path) -> USDPrim.Relationship.Spec?](./relationship%28at%29.md)
  Returns the relationship spec at the given path.
- [func spec(at: USDLayer.Path) -> USDLayer.Spec?](./spec%28at%29.md)
  Returns the spec at the given path, or `nil` if no spec is authored there.
- [func specType(at: USDLayer.Path) -> USDLayer.SpecType?](./spectype%28at%29.md)
  Returns the kind of spec authored at the given path, or `nil` if nothing is authored there.
- [USDLayer.Path](./path.md)
  A path within a USD scene hierarchy.
- [USDLayer.PathExpression](./pathexpression.md)
  A boolean expression over path patterns for selecting sets of prims.
- [USDLayer.Spec](./spec.md)
  A handle to a single spec stored in a layer.
- [USDLayer.SpecType](./spectype.md)
  The kind of spec stored at a path in a layer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdlayer/traverse(at:_:))*