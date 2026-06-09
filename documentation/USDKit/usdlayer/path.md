# USDLayer.Path

**Framework**: USDKit  
**Kind**: struct

A path within a USD scene hierarchy.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
struct Path
```

#### Overview

Paths identify scene elements — prims like `/World/Character`, properties like `/World/Character.visibility`, and other addressable targets. Absolute paths begin with `/`; relative paths do not.

## Topics

### Initializers
- [init()](usdlayer/path/init.md)
  Creates an empty path.
- [init(String)](usdlayer/path/init(_:).md)
  Creates a path from its string representation.
- [init?(validating: String)](usdlayer/path/init(validating:).md)
  Creates a path from its string representation, validating that `path` is well-formed.
### Instance Properties
- [var ancestors: [USDLayer.Path]](usdlayer/path/ancestors.md)
  All ancestor paths from leaf to root, excluding self.
- [var depth: Int](usdlayer/path/depth.md)
  The number of components in the path.
- [var isAbsolute: Bool](usdlayer/path/isabsolute.md)
  Whether the path begins with `/`.
- [var isNamespacedProperty: Bool](usdlayer/path/isnamespacedproperty.md)
  Whether the leaf property name contains a namespace.
- [var isPrimProperty: Bool](usdlayer/path/isprimproperty.md)
  Whether the path is a property on a prim, as opposed to one on a relationship target.
- [var isRelationalAttribute: Bool](usdlayer/path/isrelationalattribute.md)
  Whether the path is an attribute on a relationship target.
- [var isRootPrim: Bool](usdlayer/path/isrootprim.md)
  Whether the path is a top-level prim like a child of the absolute root.
- [var kind: USDLayer.Path.Kind](usdlayer/path/kind-swift.property.md)
  What kind of element the path’s leaf represents.
- [var name: USDToken](usdlayer/path/name.md)
  The identifier of the path’s leaf element.
- [var parent: USDLayer.Path?](usdlayer/path/parent.md)
  The parent of this path, or `nil` if this path is the absolute root or the empty path.
- [var primPath: USDLayer.Path](usdlayer/path/primpath.md)
  The containing prim path, stripped of any property, target, or variant selection elements.
- [var target: USDLayer.Path?](usdlayer/path/target.md)
  The target component if the path contains one, otherwise `nil`.
- [var variantSelection: (set: String, variant: String)?](usdlayer/path/variantselection.md)
  The variant set and value if the path’s leaf is a variant selection, otherwise `nil`.
### Instance Methods
- [func absolute(at: USDLayer.Path) -> USDLayer.Path](usdlayer/path/absolute(at:).md)
  Returns this path made absolute, anchored at the given path.
- [func appending(child: USDToken) -> USDLayer.Path](usdlayer/path/appending(child:).md)
  Returns a new path with the named child prim appended.
- [func appending(path: USDLayer.Path) -> USDLayer.Path](usdlayer/path/appending(path:).md)
  Returns a new path with `newSuffix` appended.
- [func appending(property: USDToken) -> USDLayer.Path](usdlayer/path/appending(property:).md)
  Returns a new path with the named property appended.
- [func appending(relationalAttribute: USDToken) -> USDLayer.Path](usdlayer/path/appending(relationalattribute:).md)
  Returns a new path with a relational attribute appended.
- [func appending(target: USDLayer.Path) -> USDLayer.Path](usdlayer/path/appending(target:).md)
  Returns a new path with a relationship target appended.
- [func appending(variantSet: USDToken, variant: USDToken) -> USDLayer.Path](usdlayer/path/appending(variantset:variant:).md)
  Returns a new path with a variant selection appended.
- [func commonPrefix(with: USDLayer.Path) -> USDLayer.Path](usdlayer/path/commonprefix(with:).md)
  Returns the longest common ancestor path of this path and `other`.
- [func hasPrefix(USDLayer.Path) -> Bool](usdlayer/path/hasprefix(_:).md)
  Returns a Boolean value that indicates whether this path begins with `prefix`.
- [func relative(to: USDLayer.Path) -> USDLayer.Path](usdlayer/path/relative(to:).md)
  Returns this path made relative to the given anchor.
- [func replacing(name: USDToken) -> USDLayer.Path](usdlayer/path/replacing(name:).md)
  Returns a new path with the leaf name replaced.
- [func replacing(target: USDLayer.Path) -> USDLayer.Path](usdlayer/path/replacing(target:).md)
  Returns a new path with the target component replaced.
- [func strippingAllVariantSelections() -> USDLayer.Path](usdlayer/path/strippingallvariantselections.md)
  Returns a new path with all variant selections removed.
### Type Properties
- [static let absoluteRoot: USDLayer.Path](usdlayer/path/absoluteroot.md)
  The absolute root, `/`.
- [static let empty: USDLayer.Path](usdlayer/path/empty.md)
  The empty path.
### Enumerations
- [USDLayer.Path.Kind](usdlayer/path/kind-swift.enum.md)
  The classification of the path’s leaf element.

## Relationships

### Conforms To
- [Comparable](../Swift/Comparable.md)
- [Copyable](../Swift/Copyable.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Escapable](../Swift/Escapable.md)
- [ExpressibleByExtendedGraphemeClusterLiteral](../Swift/ExpressibleByExtendedGraphemeClusterLiteral.md)
- [ExpressibleByStringInterpolation](../Swift/ExpressibleByStringInterpolation.md)
- [ExpressibleByStringLiteral](../Swift/ExpressibleByStringLiteral.md)
- [ExpressibleByUnicodeScalarLiteral](../Swift/ExpressibleByUnicodeScalarLiteral.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
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
- [USDLayer.PathExpression](usdlayer/pathexpression.md)
  A boolean expression over path patterns for selecting sets of prims.
- [USDLayer.Spec](usdlayer/spec.md)
  A handle to a single spec stored in a layer.
- [USDLayer.SpecType](usdlayer/spectype.md)
  The kind of spec stored at a path in a layer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdlayer/path)*