# USDLayer.Path

**Framework**: USDKit  
**Kind**: struct  
**Role**: Structure

A path within a USD scene hierarchy.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
struct Path
```

## Overview

Paths identify scene elements — prims like `/World/Character`, properties like `/World/Character.visibility`, and other addressable targets. Absolute paths begin with `/`; relative paths do not.

## Topics

### Initializers
- [init()](./path/init%28%29.md)
  Creates an empty path.
- [init(String)](./path/init%28_%29.md)
  Creates a path from its string representation.
- [init?(validating: String)](./path/init%28validating%29.md)
  Creates a path from its string representation, validating that `path` is well-formed.
### Instance Properties
- [var ancestors: [USDLayer.Path]](./path/ancestors.md)
  All ancestor paths from leaf to root, excluding self.
- [var depth: Int](./path/depth.md)
  The number of components in the path.
- [var isAbsolute: Bool](./path/isabsolute.md)
  Whether the path begins with `/`.
- [var isNamespacedProperty: Bool](./path/isnamespacedproperty.md)
  Whether the leaf property name contains a namespace.
- [var isPrimProperty: Bool](./path/isprimproperty.md)
  Whether the path is a property on a prim, as opposed to one on a relationship target.
- [var isRelationalAttribute: Bool](./path/isrelationalattribute.md)
  Whether the path is an attribute on a relationship target.
- [var isRootPrim: Bool](./path/isrootprim.md)
  Whether the path is a top-level prim like a child of the absolute root.
- [var kind: USDLayer.Path.Kind](./path/kind-swift.property.md)
  What kind of element the path’s leaf represents.
- [var name: USDToken](./path/name.md)
  The identifier of the path’s leaf element.
- [var parent: USDLayer.Path?](./path/parent.md)
  The parent of this path, or `nil` if this path is the absolute root or the empty path.
- [var primPath: USDLayer.Path](./path/primpath.md)
  The containing prim path, stripped of any property, target, or variant selection elements.
- [var target: USDLayer.Path?](./path/target.md)
  The target component if the path contains one, otherwise `nil`.
- [var variantSelection: (set: String, variant: String)?](./path/variantselection.md)
  The variant set and value if the path’s leaf is a variant selection, otherwise `nil`.
### Instance Methods
- [func absolute(at: USDLayer.Path) -> USDLayer.Path](./path/absolute%28at%29.md)
  Returns this path made absolute, anchored at the given path.
- [func appending(child: USDToken) -> USDLayer.Path](./path/appending%28child%29.md)
  Returns a new path with the named child prim appended.
- [func appending(path: USDLayer.Path) -> USDLayer.Path](./path/appending%28path%29.md)
  Returns a new path with `newSuffix` appended.
- [func appending(property: USDToken) -> USDLayer.Path](./path/appending%28property%29.md)
  Returns a new path with the named property appended.
- [func appending(relationalAttribute: USDToken) -> USDLayer.Path](./path/appending%28relationalattribute%29.md)
  Returns a new path with a relational attribute appended.
- [func appending(target: USDLayer.Path) -> USDLayer.Path](./path/appending%28target%29.md)
  Returns a new path with a relationship target appended.
- [func appending(variantSet: USDToken, variant: USDToken) -> USDLayer.Path](./path/appending%28variantset,variant%29.md)
  Returns a new path with a variant selection appended.
- [func commonPrefix(with: USDLayer.Path) -> USDLayer.Path](./path/commonprefix%28with%29.md)
  Returns the longest common ancestor path of this path and `other`.
- [func hasPrefix(USDLayer.Path) -> Bool](./path/hasprefix%28_%29.md)
  Returns a Boolean value that indicates whether this path begins with `prefix`.
- [func relative(to: USDLayer.Path) -> USDLayer.Path](./path/relative%28to%29.md)
  Returns this path made relative to the given anchor.
- [func replacing(name: USDToken) -> USDLayer.Path](./path/replacing%28name%29.md)
  Returns a new path with the leaf name replaced.
- [func replacing(target: USDLayer.Path) -> USDLayer.Path](./path/replacing%28target%29.md)
  Returns a new path with the target component replaced.
- [func strippingAllVariantSelections() -> USDLayer.Path](./path/strippingallvariantselections%28%29.md)
  Returns a new path with all variant selections removed.
### Type Properties
- [static let absoluteRoot: USDLayer.Path](./path/absoluteroot.md)
  The absolute root, `/`.
- [static let empty: USDLayer.Path](./path/empty.md)
  The empty path.
### Enumerations
- [USDLayer.Path.Kind](./path/kind-swift.enum.md)
  The classification of the path’s leaf element.

## Relationships

### Conforms To
- [Comparable](../../Swift/comparable.md)
- [Copyable](../../Swift/copyable.md)
- [CustomStringConvertible](../../Swift/customstringconvertible.md)
- [Equatable](../../Swift/equatable.md)
- [Escapable](../../Swift/escapable.md)
- [ExpressibleByExtendedGraphemeClusterLiteral](../../Swift/expressiblebyextendedgraphemeclusterliteral.md)
- [ExpressibleByStringInterpolation](../../Swift/expressiblebystringinterpolation.md)
- [ExpressibleByStringLiteral](../../Swift/expressiblebystringliteral.md)
- [ExpressibleByUnicodeScalarLiteral](../../Swift/expressiblebyunicodescalarliteral.md)
- [Hashable](../../Swift/hashable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)
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
- [USDLayer.PathExpression](./pathexpression.md)
  A boolean expression over path patterns for selecting sets of prims.
- [USDLayer.Spec](./spec.md)
  A handle to a single spec stored in a layer.
- [USDLayer.SpecType](./spectype.md)
  The kind of spec stored at a path in a layer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdlayer/path)*