# open(_:loadingPayloads:)

**Framework**: USDKit  
**Kind**: method  
**Role**: Type Method

Opens a stage using the file at a URL as its root layer.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
static func open(_ url: URL, loadingPayloads: USDStage.InitialLoadRule = .all) throws -> USDStage
```

## Return Value

A new stage rooted at the layer loaded from `url`.

## Discussion

> **Throws**: An error if the URL does not refer to a readable file.

## Parameters

- `url`: A file URL to use as the root layer of the new stage.
- `loadingPayloads`: The rule that determines which payloads are loaded when opening the stage.

## See Also

### Opening a stage
- [static func open(rootLayer: USDLayer, sessionLayer: USDLayer?, options: USDStage.OpenOptions) throws -> USDStage](./open%28rootlayer,sessionlayer,options%29.md)
  Opens a stage rooted at a given layer.
- [static func open(FilePath, sessionLayer: USDLayer?, options: USDStage.OpenOptions) throws -> USDStage](./open%28_,sessionlayer,options%29.md)
  Opens a stage using a file as the root layer.
- [USDStage.OpenOptions](./openoptions.md)
  Options that specify behavior related to opening a stage.
- [USDStage.InitialLoadRule](./initialloadrule.md)
  Specifies the rule used when opening a stage to determine if referenced payloads are loaded.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdstage/open(_:loadingpayloads:))*