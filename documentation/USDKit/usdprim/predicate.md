# USDPrim.Predicate

**Framework**: USDKit  
**Kind**: struct

A filter which returns true or false for prims based on their flags.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
struct Predicate
```

#### Overview

A predicate checks flags on a [`USDPrim`](usdprim.md) and can require that each flag is set or not set.

```swift
let loadedModels = prim.children(where: [.isModel, .isLoaded])
let inactiveGroups = prim.children(where: [.isGroup, !.isActive])
```

## Topics

### Operators
- [static func ! (USDPrim.Predicate) -> USDPrim.Predicate](usdprim/predicate/!(_:).md)
  Returns the opposite of a predicate.
### Initializers
- [init(arrayLiteral: USDPrim.Predicate...)](usdprim/predicate/init(arrayliteral:).md)
  A predicate which accepts only prims with all of the specified flags.
### Type Properties
- [static var all: USDPrim.Predicate](usdprim/predicate/all.md)
  A predicate which is always true, and accepts all prims.
- [static var hasDefSpecifier: USDPrim.Predicate](usdprim/predicate/hasdefspecifier.md)
  True if the prim has a def specifier.
- [static var isAbstract: USDPrim.Predicate](usdprim/predicate/isabstract.md)
  True if the prim or any of its ancestors are a class.
- [static var isActive: USDPrim.Predicate](usdprim/predicate/isactive.md)
  True if the prim and all of its ancestors are active.
- [static var isComponent: USDPrim.Predicate](usdprim/predicate/iscomponent.md)
  Returns true if this prim’s kind metadata identifies it as a model component.
- [static var isDefined: USDPrim.Predicate](usdprim/predicate/isdefined.md)
  True if the prim (and all its ancestors) are not a class and not an override.
- [static var isGroup: USDPrim.Predicate](usdprim/predicate/isgroup.md)
  Returns true if this prim’s kind metadata identifies it as a model group.
- [static var isInstance: USDPrim.Predicate](usdprim/predicate/isinstance.md)
  True if the prim is an instance of a prototype.
- [static var isLoaded: USDPrim.Predicate](usdprim/predicate/isloaded.md)
  True if the prim is active and none of its loadable ancestors are unloaded.
- [static var isModel: USDPrim.Predicate](usdprim/predicate/ismodel.md)
  Returns true if this prim’s kind metadata identifies it as a model.
- [static var none: USDPrim.Predicate](usdprim/predicate/none.md)
  A predicate which is always false, and accepts no prims.
### Default Implementations
- [CustomStringConvertible Implementations](usdprim/predicate/customstringconvertible-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Escapable](../Swift/Escapable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var children: [USDPrim]](usdprim/children.md)
  The active, loaded, defined, non-abstract child prims of this prim.
- [var allChildren: [USDPrim]](usdprim/allchildren.md)
  The child prims of this prim.
- [var descendants: [USDPrim]](usdprim/descendants.md)
  The active, loaded, defined, non-abstract descendant prims of this prim, in depth-first order.
- [var allDescendants: [USDPrim]](usdprim/alldescendants.md)
  The descendant prims of this prim.
- [var nextSibling: USDPrim?](usdprim/nextsibling.md)
  The active, loaded, defined, non-abstract successor of this prim in its parent’s list of children.
- [func children(where: USDPrim.Predicate) -> [USDPrim]](usdprim/children(where:).md)
  Returns the child prims of this prim that satisfy the given predicate.
- [func descendants(where: USDPrim.Predicate) -> [USDPrim]](usdprim/descendants(where:).md)
  Returns the descendant prims of this prim that satisfy the given predicate.
- [func nextSibling(where: USDPrim.Predicate) -> USDPrim](usdprim/nextsibling(where:).md)
  The successor of this prim in its parent’s list of children that satisfies the given predicate.
- [func prim(at: USDLayer.Path) -> USDPrim](usdprim/prim(at:).md)
  Returns the prim at a given path, relative to this prim.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdprim/predicate)*