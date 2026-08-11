# USDStage

**Framework**: USDKit  
**Kind**: struct

A 3D scene composed from one or more Universal Scene Description (USD) documents.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
struct USDStage
```

#### Overview

Stages support authoring, animating, and composing 3D data from various 3D file formats. A stage can contain meshes, materials, cameras, lights, or arbitrary custom data, as well as references to textures or additional scene data stored in separate files.

A stage is a scene graph formed by opening a single document (the “root layer”) and then recursively following the composition rules described by that document in order to assemble a scene graph. Because of this composition process, a `USDStage` object presents a unified view that may incorporate data from more than one source file.

A `USDStage` object is a mutable view onto the composed scene graph. It consists of a tree-structured hierarchy of [`USDPrim`](usdprim.md) objects representing nodes in the scene graph. Each prim has schemas that give it a kind (is-a) and capabilities (has-a), attributes that contain possibly-animated values, and relationships that connect the prim to other objects in the stage.

The [`USDPrim`](usdprim.md), `USDPrim.Attribute`, and `USDPrim.Relationship` objects in a stage are owned by the `USDStage` object. Values of these types act as views or handles into the composed content of the stage. Modifying any value in a stage authors a modification to an [`USDLayer`](usdlayer.md) that represents a file or file-like storage. Values of these types refer to and act on the current state of a particular stage, and become invalid if the stage is closed.

> **Note**: A stage may also possess a “session layer” that may contain temporary modifications that will not be written to any file.

A composed, runtime view of a USD scene assembled from one or more layers.

## Topics

### Creating a stage
- [init(displayName: String?, loadingPayloads: USDStage.InitialLoadRule)](usdstage/init(displayname:loadingpayloads:).md)
  Creates a new memory-backed stage.
- [init(string: String, loadingPayloads: USDStage.InitialLoadRule) throws](usdstage/init(string:loadingpayloads:).md)
  Creates a stage from a string containing a `.usda` document.
- [init(Data, type: UTType, loadingPayloads: USDStage.InitialLoadRule) throws](usdstage/init(_:type:loadingpayloads:).md)
  Creates a stage from in-memory data in a given format.
### Opening a stage
- [static func open(rootLayer: USDLayer, sessionLayer: USDLayer?, options: USDStage.OpenOptions) throws -> USDStage](usdstage/open(rootlayer:sessionlayer:options:).md)
  Opens a stage rooted at a given layer.
- [static func open(FilePath, sessionLayer: USDLayer?, options: USDStage.OpenOptions) throws -> USDStage](usdstage/open(_:sessionlayer:options:).md)
  Opens a stage using a file as the root layer.
- [static func open(URL, loadingPayloads: USDStage.InitialLoadRule) throws -> USDStage](usdstage/open(_:loadingpayloads:).md)
  Opens a stage using the file at a URL as its root layer.
- [USDStage.OpenOptions](usdstage/openoptions.md)
  Options that specify behavior related to opening a stage.
- [USDStage.InitialLoadRule](usdstage/initialloadrule.md)
  Specifies the rule used when opening a stage to determine if referenced payloads are loaded.
### Saving and reloading
- [func save() throws](usdstage/save.md)
  Saves the stage’s changed layers to their sources.
- [func saveSessionLayers() throws](usdstage/savesessionlayers.md)
  Saves the stage’s changed session layers to their sources.
- [func reload() throws](usdstage/reload.md)
  Reloads the stage’s layers from their sources, discarding any unsaved changes.
### Accessing prims and properties
- [func prim(at: USDLayer.Path) -> USDPrim](usdstage/prim(at:).md)
  Returns the prim at a given path, if it exists.
- [func object(at: USDLayer.Path) -> USDStage.Object](usdstage/object(at:).md)
  Returns the object at a given path, if it exists.
- [func property(at: USDLayer.Path) -> USDPrim.Property](usdstage/property(at:).md)
  Returns the property at a given path, if it exists.
- [func attribute(at: USDLayer.Path) -> USDPrim.Attribute](usdstage/attribute(at:).md)
  Returns the attribute at a given path, if it exists.
- [func relationship(at: USDLayer.Path) -> USDPrim.Relationship](usdstage/relationship(at:).md)
  Returns the relationship at a given path, if it exists.
- [var pseudoRoot: USDPrim](usdstage/pseudoroot.md)
  The prim at the top of the stage’s namespace, whose path is `/`.
- [var defaultPrim: USDPrim?](usdstage/defaultprim.md)
  The prim designated as this stage’s default entry point when the stage is referenced.
- [var hasDefaultPrim: Bool](usdstage/hasdefaultprim.md)
  Return true if this stage’s root layer has an authored opinion for the default prim layer metadata.
- [USDStage.Object](usdstage/object.md)
### Authoring prims
- [func definePrim(at: USDLayer.Path, type: USDToken) -> USDPrim](usdstage/defineprim(at:type:).md)
  Defines a prim at a given path, if none already exists.
- [func overridePrim(at: USDLayer.Path) -> USDPrim](usdstage/overrideprim(at:).md)
  Authors an override prim at a given path, if no prim exists at that path.
- [func removePrim(at: USDLayer.Path) -> Bool](usdstage/removeprim(at:).md)
  Removes all authored data at the given path in the current edit target.
### Traversing the scene
- [var descendants: [USDPrim]](usdstage/descendants.md)
  The active, loaded, defined, non-abstract descendant prims of this stage’s pseudo-root.
- [func descendants(where: USDPrim.Predicate) -> [USDPrim]](usdstage/descendants(where:).md)
  Returns the descendant prims of this stage that satisfy the given predicate.
- [var allDescendants: [USDPrim]](usdstage/alldescendants.md)
  All descendant prims of this stage’s pseudo-root.
### Managing layers
- [var rootLayer: USDLayer](usdstage/rootlayer.md)
  The root layer of this stage.
- [func muteLayer(String)](usdstage/mutelayer(_:).md)
  Mutes the layer with the given identifier, excluding its opinions from composition.
- [func unmuteLayer(String)](usdstage/unmutelayer(_:).md)
  Unmutes the layer with the given identifier, restoring its opinions to composition.
- [func isLayerMuted(String) -> Bool](usdstage/islayermuted(_:).md)
  Returns a Boolean value that indicates whether the layer with the given identifier is muted.
### Setting the edit target
- [var editTarget: USDStage.EditTarget](usdstage/edittarget-swift.property.md)
  The destination for authoring operations on this stage.
- [USDStage.EditTarget](usdstage/edittarget-swift.struct.md)
  A destination for authoring operations on a stage.
### Working with time codes
- [var timeCodeRange: ClosedRange<USDStage.TimeCode>](usdstage/timecoderange.md)
  The range of time codes over which this stage has authored animation.
- [var timeCodesPerSecond: Double](usdstage/timecodespersecond.md)
  The number of time codes per second of playback for this stage.
- [USDStage.TimeCode](usdstage/timecode.md)
  A unitless point in time, used with time-varying values authored in 3D scenes.
### Reading stage metrics
- [var metersPerUnit: Double](usdstage/metersperunit.md)
  The number of meters represented by one unit in this stage’s coordinate system.
- [var hasAuthoredMetersPerUnit: Bool](usdstage/hasauthoredmetersperunit.md)
  A Boolean value that indicates whether this stage has an authored [`metersPerUnit`](usdstage/metersperunit.md) opinion.
- [var upAxis: USDToken](usdstage/upaxis.md)
  The axis that points upward in this stage’s coordinate system.
- [static var fallbackUpAxis: USDToken](usdstage/fallbackupaxis.md)
  The up axis used when a stage has no authored opinion.
### Observing changes
- [func addObserver<Notice>(for: Notice.Type, using: (Notice) -> Void) -> USDStage.ObservationToken](usdstage/addobserver(for:using:).md)
  Registers an observer that runs when a notice of the given type is sent for this stage.
- [USDStage.Notice](usdstage/notice.md)
  A change notification that can be observed on a stage.
- [USDStage.ObjectsDidChange](usdstage/objectsdidchange.md)
  A notice sent when the objects on a stage change.
- [USDStage.ObservationToken](usdstage/observationtoken.md)
  A token that keeps an observer registered for as long as it is retained.
### Exporting the stage
- [func exportPackage(to: URL, options: USDStage.ExportOptions) throws](usdstage/exportpackage(to:options:)-6s2wk.md)
  Packages the stage into a USDZ archive.
- [func exportPackage(to: FilePath, options: USDStage.ExportOptions) throws](usdstage/exportpackage(to:options:)-2x7yr.md)
  Packages the stage into a USDZ archive.
- [func exportFlattened(to: URL) throws](usdstage/exportflattened(to:)-98kpc.md)
  Exports the stage as a flattened USD file.
- [func exportFlattened(to: FilePath) throws](usdstage/exportflattened(to:)-6717d.md)
  Exports the stage as a flattened USD file.
- [USDStage.ExportOptions](usdstage/exportoptions.md)
  Options for packaging a stage into a USDZ file.
### Instance Methods
- [func exportPackage(options: USDStage.ExportOptions) throws -> Data](usdstage/exportpackage(options:).md)
  Packages the stage into a USDZ archive and returns it as in-memory data.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)

## See Also

- [struct USDPrim](usdprim.md)
  A single node in a stage’s scene hierarchy that holds attributes, relationships, metadata, and child prims.
- [struct USDLayer](usdlayer.md)
  A single USD document that stores scene description in a file or in memory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdstage)*