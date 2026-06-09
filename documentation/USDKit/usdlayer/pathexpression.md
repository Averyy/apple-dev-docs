# USDLayer.PathExpression

**Framework**: USDKit  
**Kind**: struct

A boolean expression over path patterns for selecting sets of prims.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
struct PathExpression
```

#### Overview

Path expressions combine patterns using set operations (union, intersection, complement, difference) and can reference other named expressions. The struct wraps `pxr::SdfPathExpression` and provides access to common expression patterns through static properties and string-based initialization.

## Topics

### Initializers
- [init()](usdlayer/pathexpression/init.md)
  Creates an empty path expression.
- [init(String)](usdlayer/pathexpression/init(_:).md)
  Creates a path expression by parsing the given string.
### Instance Properties
- [var isEmpty: Bool](usdlayer/pathexpression/isempty.md)
  Whether this expression has no patterns or references.
- [var text: String](usdlayer/pathexpression/text.md)
  The string form of this expression.
### Type Properties
- [static var everyDescendant: USDLayer.PathExpression](usdlayer/pathexpression/everydescendant.md)
  An expression that matches all descendant paths from the root.
- [static var everything: USDLayer.PathExpression](usdlayer/pathexpression/everything.md)
  An expression that matches all paths in the scene hierarchy.
- [static var nothing: USDLayer.PathExpression](usdlayer/pathexpression/nothing.md)
  An expression that matches no paths, representing an empty selection.
- [static var weakerReference: USDLayer.PathExpression](usdlayer/pathexpression/weakerreference.md)
  A reference to a weaker expression for composition with stronger layers.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Escapable](../Swift/Escapable.md)
- [ExpressibleByExtendedGraphemeClusterLiteral](../Swift/ExpressibleByExtendedGraphemeClusterLiteral.md)
- [ExpressibleByStringLiteral](../Swift/ExpressibleByStringLiteral.md)
- [ExpressibleByUnicodeScalarLiteral](../Swift/ExpressibleByUnicodeScalarLiteral.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [USDPrim.Attribute.Value](usdprim/attribute/value.md)
- [USDValueProtocol](usdvalueprotocol.md)

## See Also

- [func prim(at: USDLayer.Path) -> USDPrim.Spec?](usdlayer/prim(at:).md)
  Returns the prim spec authored at the given path, or `nil` if no prim spec exists there.
- [func property(at: USDLayer.Path) -> USDPrim.Property.Spec?](usdlayer/property(at:).md)
  Returns the property spec at the given path.
- [func attribute(at: USDLayer.Path) -> USDPrim.Attribute.Spec?](usdlayer/attribute(at:).md)
  Returns the attribute spec at the given path.
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
- [USDLayer.Spec](usdlayer/spec.md)
  A handle to a single spec stored in a layer.
- [USDLayer.SpecType](usdlayer/spectype.md)
  The kind of spec stored at a path in a layer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdlayer/pathexpression)*