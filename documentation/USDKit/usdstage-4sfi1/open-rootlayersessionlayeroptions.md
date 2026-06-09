# open(rootLayer:sessionLayer:options:)

**Framework**: USDKit  
**Kind**: method

Opens a stage rooted at a given layer.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
static func open(rootLayer: USDLayer, sessionLayer: USDLayer? = nil, options: USDStage.OpenOptions = []) throws -> USDStage
```

#### Discussion

Recursively follows the composition rules described by `rootLayer`, opening any files referenced by the layer and assembling a hierarchy of [`USDPrim`](usdprim.md)s from the combined contents of all layers.

This function creates a new, independent stage object even if there is already a stage opened with `rootLayer` as its root layer.

Parameters:

- rootLayer: The root layer of the new stage.
- sessionLayer: A layer to use as a session layer. If `nil`, an anonymous layer will be created.
- options: Options that specify behavior related to opening a stage.

## See Also

- [static func open(FilePath, sessionLayer: USDLayer?, options: USDStage.OpenOptions) throws -> USDStage](usdstage-4sfi1/open(_:sessionlayer:options:).md)
  Opens a stage using a file as the root layer.
- [static func open(URL, loadingPayloads: USDStage.InitialLoadRule) throws -> USDStage](usdstage-4sfi1/open(_:loadingpayloads:).md)
- [USDStage.OpenOptions](usdstage-4sfi1/openoptions.md)
  Options that specify behavior related to opening a stage.
- [USDStage.InitialLoadRule](usdstage-4sfi1/initialloadrule.md)
  Specifies the rule used when opening a stage to determine if referenced payloads are loaded.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdstage-4sfi1/open(rootlayer:sessionlayer:options:))*