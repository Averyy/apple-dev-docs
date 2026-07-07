# USDStage

**Framework**: USDKit  
**Kind**: struct

A composed, runtime view of a USD scene assembled from one or more layers.

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

## Topics

### Creating a stage
- [init(displayName: String?, loadingPayloads: USDStage.InitialLoadRule)](usdstage/init(displayname:loadingpayloads:).md)
  Creates a new memory-backed stage.
- [init(string: String, loadingPayloads: USDStage.InitialLoadRule) throws](usdstage/init(string:loadingpayloads:).md)
- [init(Data, type: UTType, loadingPayloads: USDStage.InitialLoadRule) throws](usdstage/init(_:type:loadingpayloads:).md)
### Opening a stage
- [static func open(rootLayer: USDLayer, sessionLayer: USDLayer?, options: USDStage.OpenOptions) throws -> USDStage](usdstage/open(rootlayer:sessionlayer:options:).md)
  Opens a stage rooted at a given layer.
- [static func open(FilePath, sessionLayer: USDLayer?, options: USDStage.OpenOptions) throws -> USDStage](usdstage/open(_:sessionlayer:options:).md)
  Opens a stage using a file as the root layer.
- [static func open(URL, loadingPayloads: USDStage.InitialLoadRule) throws -> USDStage](usdstage/open(_:loadingpayloads:).md)
- [USDStage.OpenOptions](usdstage/openoptions.md)
  Options that specify behavior related to opening a stage.
- [USDStage.InitialLoadRule](usdstage/initialloadrule.md)
  Specifies the rule used when opening a stage to determine if referenced payloads are loaded.
### Saving and reloading
- [func save() throws](usdstage/save.md)
  Saves the stage’s dirty layers to their sources.
- [func saveSessionLayers() throws](usdstage/savesessionlayers.md)
  Saves the stage’s dirty session layers to their sources.
- [func reload() throws](usdstage/reload.md)
  Reloads the stage’s layers from their sources, discarding any unsaved changes.
### Accessing prims and properties
- [func prim(at: USDLayer.Path) -> USDPrim](usdstage/prim(at:).md)
- [func object(at: USDLayer.Path) -> USDStage.Object](usdstage/object(at:).md)
- [func property(at: USDLayer.Path) -> USDPrim.Property](usdstage/property(at:).md)
- [func attribute(at: USDLayer.Path) -> USDPrim.Attribute](usdstage/attribute(at:).md)
- [func relationship(at: USDLayer.Path) -> USDPrim.Relationship](usdstage/relationship(at:).md)
- [var pseudoRoot: USDPrim](usdstage/pseudoroot.md)
- [var defaultPrim: USDPrim?](usdstage/defaultprim.md)
- [var hasDefaultPrim: Bool](usdstage/hasdefaultprim.md)
  Return true if this stage’s root layer has an authored opinion for the default prim layer metadata.
- [USDStage.Object](usdstage/object.md)
### Authoring prims
- [func definePrim(at: USDLayer.Path, type: USDToken) -> USDPrim](usdstage/defineprim(at:type:).md)
- [func overridePrim(at: USDLayer.Path) -> USDPrim](usdstage/overrideprim(at:).md)
- [func removePrim(at: USDLayer.Path) -> Bool](usdstage/removeprim(at:).md)
### Traversing the scene
- [var descendants: [USDPrim]](usdstage/descendants.md)
  The active, loaded, defined, non-abstract descendant prims of this stage’s pseudo-root.
- [func descendants(where: USDPrim.Predicate) -> [USDPrim]](usdstage/descendants(where:).md)
  Returns the descendant prims of this stage that satisfy the given predicate.
- [var allDescendants: [USDPrim]](usdstage/alldescendants.md)
  All descendant prims of this stage’s pseudo-root.
### Managing layers
- [var rootLayer: USDLayer](usdstage/rootlayer.md)
- [func muteLayer(String)](usdstage/mutelayer(_:).md)
- [func unmuteLayer(String)](usdstage/unmutelayer(_:).md)
- [func isLayerMuted(String) -> Bool](usdstage/islayermuted(_:).md)
### Setting the edit target
- [var editTarget: USDStage.EditTarget](usdstage/edittarget-swift.property.md)
- [USDStage.EditTarget](usdstage/edittarget-swift.struct.md)
### Working with time codes
- [var timeCodeRange: ClosedRange<USDStage.TimeCode>](usdstage/timecoderange.md)
  The animation range authored on this stage, in time codes.
- [var timeCodesPerSecond: Double](usdstage/timecodespersecond.md)
  The rate at which time codes advance per second on this stage.
- [USDStage.TimeCode](usdstage/timecode.md)
  A unitless point in time, used with time-varying values authored in 3D scenes.
### Reading stage metrics
- [var metersPerUnit: Double](usdstage/metersperunit.md)
- [var hasAuthoredMetersPerUnit: Bool](usdstage/hasauthoredmetersperunit.md)
- [var upAxis: USDToken](usdstage/upaxis.md)
- [static var fallbackUpAxis: USDToken](usdstage/fallbackupaxis.md)
### Observing changes
- [func addObserver<Notice>(for: Notice.Type, using: (Notice) -> Void) -> USDStage.ObservationToken](usdstage/addobserver(for:using:).md)
- [USDStage.Notice](usdstage/notice.md)
- [USDStage.ObjectsDidChange](usdstage/objectsdidchange.md)
- [USDStage.ObservationToken](usdstage/observationtoken.md)
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