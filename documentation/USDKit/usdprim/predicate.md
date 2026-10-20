# USDPrim.Predicate

**Framework**: USDKit  
**Kind**: struct  
**Role**: Structure

A filter which returns true or false for prims based on their flags.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
struct Predicate
```

#### Overview

A predicate checks flags on a [`USDPrim`](../usdprim.md) and can require that each flag is set or not set.

```swift
let loadedModels = prim.children(where: [.isModel, .isLoaded])
let inactiveGroups = prim.children(where: [.isGroup, !.isActive])
```

## Topics

### Operators
- [static func ! (USDPrim.Predicate) -> USDPrim.Predicate](./predicate/not%28_%29.md)
  Returns the opposite of a predicate.
### Initializers
- [init(arrayLiteral: USDPrim.Predicate...)](./predicate/init%28arrayliteral%29.md)
  A predicate which accepts only prims with all of the specified flags.
### Type Properties
- [static var all: USDPrim.Predicate](./predicate/all.md)
  A predicate which is always true, and accepts all prims.
- [static var hasDefSpecifier: USDPrim.Predicate](./predicate/hasdefspecifier.md)
  True if the prim has a def specifier.
- [static var isAbstract: USDPrim.Predicate](./predicate/isabstract.md)
  True if the prim or any of its ancestors are a class.
- [static var isActive: USDPrim.Predicate](./predicate/isactive.md)
  True if the prim and all of its ancestors are active.
- [static var isComponent: USDPrim.Predicate](./predicate/iscomponent.md)
  Returns true if this prim’s kind metadata identifies it as a model component.
- [static var isDefined: USDPrim.Predicate](./predicate/isdefined.md)
  True if the prim and all its ancestors have a `def` specifier.
- [static var isGroup: USDPrim.Predicate](./predicate/isgroup.md)
  Returns true if this prim’s kind metadata identifies it as a model group.
- [static var isInstance: USDPrim.Predicate](./predicate/isinstance.md)
  True if the prim is an instance of a prototype.
- [static var isLoaded: USDPrim.Predicate](./predicate/isloaded.md)
  True if the prim is active and none of its loadable ancestors are unloaded.
- [static var isModel: USDPrim.Predicate](./predicate/ismodel.md)
  Returns true if this prim’s kind metadata identifies it as a model.
- [static var none: USDPrim.Predicate](./predicate/none.md)
  A predicate which is always false, and accepts no prims.
### Default Implementations
- [CustomStringConvertible Implementations](./predicate/customstringconvertible-implementations.md)

## Relationships

### Conforms To
- [Copyable](../../Swift/copyable.md)
- [CustomStringConvertible](../../Swift/customstringconvertible.md)
- [Escapable](../../Swift/escapable.md)
- [ExpressibleByArrayLiteral](../../Swift/expressiblebyarrayliteral.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Traversing the hierarchy
- [var children: [USDPrim]](./children.md)
  The active, loaded, defined, non-abstract child prims of this prim.
- [var allChildren: [USDPrim]](./allchildren.md)
  The child prims of this prim.
- [var descendants: [USDPrim]](./descendants.md)
  The active, loaded, defined, non-abstract descendant prims of this prim, in depth-first order.
- [var allDescendants: [USDPrim]](./alldescendants.md)
  The descendant prims of this prim.
- [var nextSibling: USDPrim?](./nextsibling.md)
  The active, loaded, defined, non-abstract successor of this prim in its parent’s list of children.
- [func children(where: USDPrim.Predicate) -> [USDPrim]](./children%28where%29.md)
  Returns the child prims of this prim that satisfy the given predicate.
- [func descendants(where: USDPrim.Predicate) -> [USDPrim]](./descendants%28where%29.md)
  Returns the descendant prims of this prim that satisfy the given predicate.
- [func nextSibling(where: USDPrim.Predicate) -> USDPrim](./nextsibling%28where%29.md)
  The successor of this prim in its parent’s list of children that satisfies the given predicate.
- [func prim(at: USDLayer.Path) -> USDPrim](./prim%28at%29.md)
  Returns the prim at a given path, relative to this prim.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdprim/predicate)*