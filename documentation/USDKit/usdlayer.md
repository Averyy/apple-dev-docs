# USDLayer

**Framework**: USDKit  
**Kind**: struct

A single USD document that stores scene description in a file or in memory.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
struct USDLayer
```

## Topics

### Creating a layer
- [init(displayName: String?) throws](usdlayer/init(displayname:).md)
  Creates an anonymous, in-memory layer.
### Opening and finding layers
- [static func find(identifier: String) -> USDLayer?](usdlayer/find(identifier:).md)
  Returns an already-loaded layer with this identifier, or `nil` if none is loaded. Does no I/O.
- [static func open(String, options: USDLayer.OpenOptions) throws -> USDLayer](usdlayer/open(_:options:).md)
  Returns an already-loaded layer at the identifier, or opens it from the resolved asset path.
- [USDLayer.OpenOptions](usdlayer/openoptions.md)
  Options for opening a layer.
- [USDLayer.Permission](usdlayer/permission.md)
  Access permission for a spec.
### Saving and reloading
- [func save() throws](usdlayer/save.md)
  Saves the layer to its source if it has unsaved changes.
- [func reload() throws](usdlayer/reload.md)
  Reloads the layer from its source, discarding any unsaved changes.
- [func clear()](usdlayer/clear.md)
  Removes all in-memory content from the layer. The file on disk is unaffected until [`save()`](usdlayer/save().md) is called.
### Exporting and importing
- [func export(to: URL) throws](usdlayer/export(to:)-7vouy.md)
  Writes the layer’s contents to a file at the given URL.
- [func export(to: FilePath) throws](usdlayer/export(to:)-5hboj.md)
  Writes the layer’s contents to a file at the given path.
- [func importContents(from: FilePath) throws](usdlayer/importcontents(from:)-2ipug.md)
  Replaces the layer’s contents with the layer file at the given path.
- [func importContents(from: String) throws](usdlayer/importcontents(from:)-99hnf.md)
  Replaces the layer’s contents with the USDA string.
### Inspecting identity and state
- [var identifier: String](usdlayer/identifier.md)
  The layer’s identifier — typically a file path, URL, or anonymous identifier string. Identifies the layer in OpenUSD’s global registry.
- [var resolvedPath: FilePath?](usdlayer/resolvedpath.md)
  The resolved filesystem location of the layer’s source, or `nil` for anonymous layers.
- [var displayName: String](usdlayer/displayname.md)
  A human-readable name for the layer, derived from its identifier. Suitable for display in UI.
- [var isAnonymous: Bool](usdlayer/isanonymous.md)
  Whether the layer is anonymous (in-memory, no file backing).
- [var isValid: Bool](usdlayer/isvalid.md)
  Whether the layer is still valid. Returns `false` if the underlying data has been released.
- [var isDirty: Bool](usdlayer/isdirty.md)
  Whether the layer has unsaved changes.
- [var isMuted: Bool](usdlayer/ismuted.md)
  Whether the layer is muted from composition.
### Composing the scene
- [var defaultPrim: USDToken?](usdlayer/defaultprim.md)
  The name of the layer’s default prim — the prim referenced when this layer is included as a reference or payload without specifying a target. `nil` if not authored.
- [var subLayerPaths: [USDLayer.AssetPath]](usdlayer/sublayerpaths.md)
  The asset paths of the layer’s sublayers, ordered from strongest to weakest opinion.
- [USDLayer.AssetPath](usdlayer/assetpath.md)
  A reference to an external asset such as a texture, audio file, or USD layer.
### Accessing scene description by path
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
- [USDLayer.PathExpression](usdlayer/pathexpression.md)
  A boolean expression over path patterns for selecting sets of prims.
- [USDLayer.Spec](usdlayer/spec.md)
  A handle to a single spec stored in a layer.
- [USDLayer.SpecType](usdlayer/spectype.md)
  The kind of spec stored at a path in a layer.
### Reading and authoring fields
- [func field(at: USDLayer.Path, name: USDToken) -> USDValue?](usdlayer/field(at:name:).md)
  Returns the value of the named field at the given path, or `nil` if no such field is authored.
- [func fields(at: USDLayer.Path) -> [USDToken]](usdlayer/fields(at:).md)
  Returns the names of the fields authored at the given path.
- [func setField(at: USDLayer.Path, name: USDToken, value: USDValue)](usdlayer/setfield(at:name:value:)-83nwe.md)
  Sets the value of the named field at the given path.
- [func setField<T>(at: USDLayer.Path, name: USDToken, value: T)](usdlayer/setfield(at:name:value:)-3242k.md)
  Sets the value of the named field at the given path, wrapping the typed value in a `USDValue`.
### Working with time samples
- [func timeSample(at: USDLayer.Path, time: USDLayer.TimeCode) -> USDValue?](usdlayer/timesample(at:time:).md)
  Returns the time-sampled value for the attribute at the given path at the specified time, or `nil` if none is authored at that time.
- [func timeSamples(at: USDLayer.Path) -> Set<USDLayer.TimeCode>](usdlayer/timesamples(at:).md)
  Returns the time codes for which the attribute at the given path has authored time samples.
- [var allTimeSamples: Set<USDLayer.TimeCode>](usdlayer/alltimesamples.md)
  All time codes for which any attribute in the layer has an authored time sample.
- [func setTimeSample(at: USDLayer.Path, time: USDLayer.TimeCode, value: USDValue)](usdlayer/settimesample(at:time:value:)-6t3qd.md)
  Sets the time-sampled value for the attribute at the given path at the specified time.
- [func setTimeSample<T>(at: USDLayer.Path, time: USDLayer.TimeCode, value: T)](usdlayer/settimesample(at:time:value:)-3ot1j.md)
  Sets the time-sampled value for the attribute at the given path at the specified time, wrapping the typed value in a `USDValue`.
- [func eraseTimeSample(at: USDLayer.Path, time: USDLayer.TimeCode)](usdlayer/erasetimesample(at:time:).md)
  Erases the authored time sample at the given path and time.
### Setting the time range
- [var startTimeCode: USDLayer.TimeCode?](usdlayer/starttimecode.md)
  The first time code in the layer’s animation range. `nil` if not authored.
- [var endTimeCode: USDLayer.TimeCode?](usdlayer/endtimecode.md)
  The last time code in the layer’s animation range. `nil` if not authored.
- [var timeCodesPerSecond: Double?](usdlayer/timecodespersecond.md)
  The rate at which time codes advance per second. `nil` if not authored.
- [USDLayer.TimeCode](usdlayer/timecode.md)
  A time value in USD, typically used for animation keyframe times.
- [USDLayer.TimeOffset](usdlayer/timeoffset.md)
  A time transformation applied when composing layers.
### Editing scene description
- [func copy(from: USDLayer.Path, to: USDLayer.Path, in: USDLayer?) -> Bool](usdlayer/copy(from:to:in:).md)
  Copies the spec at `srcPath` in this layer (and its children) to `dstPath`.
- [USDLayer.ListOperation](usdlayer/listoperation.md)
  A non-destructive list of incremental editing operations for list-valued metadata and properties.
- [USDLayer.ListOperationType](usdlayer/listoperationtype.md)
  Identifies an operation slot in a [`USDLayer.ListOperation`](usdlayer/listoperation.md).
- [typealias Relocate](usdlayer/relocate.md)
  A single path relocation from source to target.
- [typealias RelocatesMap](usdlayer/relocatesmap.md)
  A mapping from source paths to target paths for relocations.
- [USDLayer.ChangeList](usdlayer/changelist.md)
  A list of changes made to a layer.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Escapable](../Swift/Escapable.md)
- [Hashable](../Swift/Hashable.md)

## See Also

- [struct USDStage](usdstage.md)
  A composed, runtime view of a USD scene assembled from one or more layers.
- [struct USDPrim](usdprim.md)
  A single node in a stage’s scene hierarchy that holds attributes, relationships, metadata, and child prims.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdlayer)*