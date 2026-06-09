# USDPrim

**Framework**: USDKit  
**Kind**: struct

A single node in a stage’s scene hierarchy that holds attributes, relationships, metadata, and child prims.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
struct USDPrim
```

## Topics

### Creating a prim
- [init()](usdprim/init.md)
  An invalid prim handle.
- [init?(USDStage.Object)](usdprim/init(_:).md)
  Casts an object handle to a prim handle.
### Identifying the prim
- [var path: USDLayer.Path](usdprim/path.md)
  The complete scene path to this prim, relative to its stage.
- [var primPath: USDLayer.Path](usdprim/primpath.md)
  The complete scene path to this prim, relative to its stage.
- [var isValid: Bool](usdprim/isvalid.md)
  A Boolean value indicating whether this prim is valid.
- [var specifier: USDPrim.Specifier](usdprim/specifier-swift.property.md)
- [var stage: USDStage](usdprim/stage.md)
  The stage that owns this prim.
- [var parent: USDPrim?](usdprim/parent.md)
  The immediate parent prim of this prim.
- [var description: String](usdprim/description.md)
  A summary description of this prim.
- [USDPrim.Specifier](usdprim/specifier-swift.enum.md)
  How a prim definition behaves in composition.
### Traversing the hierarchy
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
- [USDPrim.Predicate](usdprim/predicate.md)
  A filter which returns true or false for prims based on their flags.
### Accessing properties
- [var properties: [USDPrim.Property]](usdprim/properties.md)
- [var authoredProperties: [USDPrim.Property]](usdprim/authoredproperties.md)
- [var propertyNames: [USDToken]](usdprim/propertynames.md)
- [var authoredPropertyNames: [USDToken]](usdprim/authoredpropertynames.md)
- [func property(named: USDToken) -> USDPrim.Property](usdprim/property(named:).md)
- [func hasProperty(named: USDToken) -> Bool](usdprim/hasproperty(named:).md)
- [func object(at: USDLayer.Path) -> USDStage.Object](usdprim/object(at:).md)
  Returns the object at a given path, relative to this prim.
- [USDPrim.Property](usdprim/property.md)
### Accessing attributes
- [var attributes: [USDPrim.Attribute]](usdprim/attributes.md)
- [var authoredAttributes: [USDPrim.Attribute]](usdprim/authoredattributes.md)
- [func attribute(named: USDToken) -> USDPrim.Attribute](usdprim/attribute(named:).md)
- [func attribute(at: USDLayer.Path) -> USDPrim.Attribute](usdprim/attribute(at:).md)
- [func hasAttribute(named: USDToken) -> Bool](usdprim/hasattribute(named:).md)
- [func makeAttribute(named: USDToken, as: USDPrim.Attribute.ValueType, custom: Bool, variability: USDPrim.Property.Variability) -> USDPrim.Attribute](usdprim/makeattribute(named:as:custom:variability:).md)
- [subscript<T>(USDToken, as _: T.Type) -> T?](usdprim/subscript(_:as:).md)
  Access or modify the value of a named attribute on this prim.
- [USDPrim.Attribute](usdprim/attribute.md)
### Accessing relationships
- [func relationship(named: USDToken) -> USDPrim.Relationship?](usdprim/relationship(named:).md)
  Returns the relationship with a given name on this prim.
- [func relationship(at: USDLayer.Path) -> USDPrim.Relationship](usdprim/relationship(at:).md)
  Returns the relationship at a given path, relative to this prim.
- [func hasRelationship(named: USDToken) -> Bool](usdprim/hasrelationship(named:).md)
  Returns true if a relationship with a given name exists on this prim.
- [USDPrim.Relationship](usdprim/relationship.md)
### Composing references and payloads
- [var references: USDPrim.ReferenceCollection](usdprim/references.md)
  The reference composition arcs on this prim.
- [USDPrim.Reference](usdprim/reference.md)
  A reference to an external layer or asset.
- [USDPrim.ReferenceCollection](usdprim/referencecollection.md)
- [USDPrim.Payload](usdprim/payload.md)
  A payload to an external asset.
- [USDPrim.ListPosition](usdprim/listposition.md)
### Authoring variants
- [USDPrim.VariantSpec](usdprim/variantspec.md)
  A handle to a single variant option within a variant set.
- [USDPrim.VariantSetSpec](usdprim/variantsetspec.md)
  A handle to a variant set — a named group of variant options.
- [typealias VariantsMap](usdprim/variantsmap.md)
  Maps variant set names to lists of available variant names.
- [typealias VariantSelectionMap](usdprim/variantselectionmap.md)
  Maps variant set names to selected variant names.
### Applying schemas and transforms
- [func applyAPISchema(USDToken) throws](usdprim/applyapischema(_:).md)
  Applies a single-apply API schema to this prim.
- [func applyAPISchema(USDToken, instanceName: USDToken) throws](usdprim/applyapischema(_:instancename:).md)
  Applies a multi-apply API schema to this prim with the given instance name.
- [func addTransformOperation(type: USDTransformOperation.Kind)](usdprim/addtransformoperation(type:).md)
  Adds a transform operation of the given kind to this prim’s transform stack.
### Working with scene-description specs
- [USDPrim.Spec](usdprim/spec.md)
  A handle to a prim definition stored in a layer.
- [USDPrim.PseudoRootSpec](usdprim/pseudorootspec.md)
  A handle to a layer’s pseudo-root — the implicit parent of all top-level prims in a layer.
### Default Implementations
- [CustomStringConvertible Implementations](usdprim/customstringconvertible-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Escapable](../Swift/Escapable.md)
- [Hashable](../Swift/Hashable.md)
- [USDStage.Object.MetadataCollection](usdstage-4sfi1/object/metadatacollection.md)

## See Also

- [struct USDStage](usdstage-4sfi1.md)
  A composed, runtime view of a USD scene assembled from one or more layers.
- [struct USDLayer](usdlayer.md)
  A single USD document that stores scene description in a file or in memory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdprim)*