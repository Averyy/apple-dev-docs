# open(_:sessionLayer:options:)

**Framework**: USDKit  
**Kind**: method

Opens a stage using a file as the root layer.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
static func open(_ path: FilePath, sessionLayer: USDLayer? = nil, options: USDStage.OpenOptions = []) throws -> USDStage
```

#### Discussion

Recursively follows the composition rules described by the root layer, opening any files referenced by that layer and assembling a hierarchy of [`USDPrim`](usdprim.md)s from the combined contents of all layers.

This function will not create a file if no file exists at `path`, unless `OpenOptions.createNew` is passed as an option.

This function creates a new, independent stage object even if there is already a stage opened with `path` as its root layer.

Parameters:

- path: A file to use as the root layer of the new stage.
- sessionLayer: A layer to use as a session layer. If `nil`, an anonymous layer will be created.
- options: Options that specify behavior related to opening a stage.

Throws: An error if `path` does not exist or could not be read.

## See Also

- [static func open(rootLayer: USDLayer, sessionLayer: USDLayer?, options: USDStage.OpenOptions) throws -> USDStage](usdstage/open(rootlayer:sessionlayer:options:).md)
  Opens a stage rooted at a given layer.
- [static func open(URL, loadingPayloads: USDStage.InitialLoadRule) throws -> USDStage](usdstage/open(_:loadingpayloads:).md)
- [USDStage.OpenOptions](usdstage/openoptions.md)
  Options that specify behavior related to opening a stage.
- [USDStage.InitialLoadRule](usdstage/initialloadrule.md)
  Specifies the rule used when opening a stage to determine if referenced payloads are loaded.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdstage/open(_:sessionlayer:options:))*