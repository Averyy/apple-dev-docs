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
  Manages reference composition arcs on a prim.
- [USDPrim.Payload](usdprim/payload.md)
  A payload to an external asset.
- [USDPrim.ListPosition](usdprim/listposition.md)
  Where a new composition arc should be inserted relative to existing arcs.
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
### Structures
- [USDPrim.InheritCollection](usdprim/inheritcollection.md)
  Manages inherit composition arcs on a prim.
- [USDPrim.PayloadCollection](usdprim/payloadcollection.md)
  Manages payload composition arcs on a prim.
- [USDPrim.SpecializeCollection](usdprim/specializecollection.md)
  Manages specializes composition arcs on a prim.
- [USDPrim.VariantSet](usdprim/variantset.md)
  Represents a single variant set on a prim.
- [USDPrim.VariantSetCollection](usdprim/variantsetcollection.md)
  Manages variant sets on a prim.
### Instance Properties
- [var hasAuthoredInherits: Bool](usdprim/hasauthoredinherits.md)
  A Boolean value indicating whether the prim has authored inherit arcs.
- [var hasAuthoredPayloads: Bool](usdprim/hasauthoredpayloads.md)
  A Boolean value indicating whether the prim has authored payload arcs.
- [var hasAuthoredReferences: Bool](usdprim/hasauthoredreferences.md)
  A Boolean value indicating whether the prim has authored reference arcs.
- [var hasAuthoredSpecializes: Bool](usdprim/hasauthoredspecializes.md)
  A Boolean value indicating whether the prim has authored specializes arcs.
- [var inherits: USDPrim.InheritCollection](usdprim/inherits.md)
  The inherit composition arcs on this prim.
- [var payloads: USDPrim.PayloadCollection](usdprim/payloads.md)
  The payload composition arcs on this prim.
- [var specializes: USDPrim.SpecializeCollection](usdprim/specializes.md)
  The specializes composition arcs on this prim.
- [var transformOperations: [USDTransformOperation]](usdprim/transformoperations.md)
  The transform operations on this prim, in evaluation order.
- [var variantSets: USDPrim.VariantSetCollection](usdprim/variantsets.md)
  The variant sets on this prim.
### Instance Methods
- [func clearTransformOperations()](usdprim/cleartransformoperations.md)
  Removes all transform operations from the prim’s transform stack.
- [func hasAPISchema(USDToken) -> Bool](usdprim/hasapischema(_:).md)
  Returns true if this prim has a particular API schema applied.
- [func isSchema(USDToken) -> Bool](usdprim/isschema(_:).md)
  Returns true if this prim has the given type or a more derived type.
- [func makeRelationship(named: USDToken, custom: Bool) -> USDPrim.Relationship](usdprim/makerelationship(named:custom:).md)
- [func transform(at: USDStage.TimeCode) -> USDValue.Matrix4d?](usdprim/transform(at:).md)
  Computes the prim’s composed local transform at the specified time.
### Subscripts
- [subscript(USDToken, as _: Int.Type) -> Int?](usdprim/subscript(_:as:)-127jz.md)
- [subscript<T>(USDToken, as _: T.Type) -> T?](usdprim/subscript(_:as:)-1frls.md)
  Access or modify the value of a named attribute on this prim.
- [subscript(USDToken, as _: USDArray<UInt>.Type) -> USDArray<UInt>?](usdprim/subscript(_:as:)-2pr71.md)
- [subscript(USDToken, as _: USDArray<Int>.Type) -> USDArray<Int>?](usdprim/subscript(_:as:)-7uc7b.md)
- [subscript(USDToken, as _: UInt.Type) -> UInt?](usdprim/subscript(_:as:)-okns.md)
### Default Implementations
- [CustomStringConvertible Implementations](usdprim/customstringconvertible-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Escapable](../Swift/Escapable.md)
- [Hashable](../Swift/Hashable.md)
- [USDStage.Object.MetadataCollection](usdstage/object/metadatacollection.md)

## See Also

- [struct USDStage](usdstage.md)
  A composed, runtime view of a USD scene assembled from one or more layers.
- [struct USDLayer](usdlayer.md)
  A single USD document that stores scene description in a file or in memory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdprim)*