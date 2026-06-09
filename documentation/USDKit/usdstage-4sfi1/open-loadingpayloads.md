# open(_:loadingPayloads:)

**Framework**: USDKit  
**Kind**: method

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
static func open(_ url: URL, loadingPayloads: USDStage.InitialLoadRule = .all) throws -> USDStage
```

## See Also

- [static func open(rootLayer: USDLayer, sessionLayer: USDLayer?, options: USDStage.OpenOptions) throws -> USDStage](usdstage-4sfi1/open(rootlayer:sessionlayer:options:).md)
  Opens a stage rooted at a given layer.
- [static func open(FilePath, sessionLayer: USDLayer?, options: USDStage.OpenOptions) throws -> USDStage](usdstage-4sfi1/open(_:sessionlayer:options:).md)
  Opens a stage using a file as the root layer.
- [USDStage.OpenOptions](usdstage-4sfi1/openoptions.md)
  Options that specify behavior related to opening a stage.
- [USDStage.InitialLoadRule](usdstage-4sfi1/initialloadrule.md)
  Specifies the rule used when opening a stage to determine if referenced payloads are loaded.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdstage-4sfi1/open(_:loadingpayloads:))*