# USDLayer.PathExpression

**Framework**: USDKit  
**Kind**: struct  
**Role**: Structure

A boolean expression over path patterns for selecting sets of prims.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
struct PathExpression
```

## Overview

Path expressions combine patterns using set operations (union, intersection, complement, difference) and can reference other named expressions. The struct wraps `pxr::SdfPathExpression` and provides access to common expression patterns through static properties and string-based initialization.

## Topics

### Initializers
- [init()](./pathexpression/init%28%29.md)
  Creates an empty path expression.
- [init(String)](./pathexpression/init%28_%29.md)
  Creates a path expression by parsing the given string.
### Instance Properties
- [var isEmpty: Bool](./pathexpression/isempty.md)
  Whether this expression has no patterns or references.
- [var text: String](./pathexpression/text.md)
  The string form of this expression.
### Type Properties
- [static var everyDescendant: USDLayer.PathExpression](./pathexpression/everydescendant.md)
  An expression that matches all descendant paths from the root.
- [static var everything: USDLayer.PathExpression](./pathexpression/everything.md)
  An expression that matches all paths in the scene hierarchy.
- [static var nothing: USDLayer.PathExpression](./pathexpression/nothing.md)
  An expression that matches no paths, representing an empty selection.
- [static var weakerReference: USDLayer.PathExpression](./pathexpression/weakerreference.md)
  A reference to a weaker expression for composition with stronger layers.

## Relationships

### Conforms To
- [Copyable](../../Swift/copyable.md)
- [CustomStringConvertible](../../Swift/customstringconvertible.md)
- [Escapable](../../Swift/escapable.md)
- [ExpressibleByExtendedGraphemeClusterLiteral](../../Swift/expressiblebyextendedgraphemeclusterliteral.md)
- [ExpressibleByStringLiteral](../../Swift/expressiblebystringliteral.md)
- [ExpressibleByUnicodeScalarLiteral](../../Swift/expressiblebyunicodescalarliteral.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)
- [USDPrim.Attribute.Value](../usdprim/attribute/value.md)
- [USDValueProtocol](../usdvalueprotocol.md)

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
- [func traverse(at: USDLayer.Path, (USDLayer.Path) -> Void)](./traverse%28at,_%29.md)
  Walks the spec tree rooted at the given path, calling `body` for each spec’s path.
- [USDLayer.Path](./path.md)
  A path within a USD scene hierarchy.
- [USDLayer.Spec](./spec.md)
  A handle to a single spec stored in a layer.
- [USDLayer.SpecType](./spectype.md)
  The kind of spec stored at a path in a layer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdlayer/pathexpression)*