# USDStage.OpenOptions

**Framework**: USDKit  
**Kind**: struct  
**Role**: Structure

Options that specify behavior related to opening a stage.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
struct OpenOptions
```

## Topics

### Type Properties
- [static var createNew: USDStage.OpenOptions](./openoptions/createnew.md)
  Creates a new layer instead of opening an existing file. Any existing file at the specified path will be overwritten.
### Type Methods
- [static func loadRule(USDStage.InitialLoadRule) -> USDStage.OpenOptions](./openoptions/loadrule%28_%29.md)
  Specifies the rule used to determine if referenced payloads are loaded.

## Relationships

### Conforms To
- [ExpressibleByArrayLiteral](../../Swift/expressiblebyarrayliteral.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Opening a stage
- [static func open(rootLayer: USDLayer, sessionLayer: USDLayer?, options: USDStage.OpenOptions) throws -> USDStage](./open%28rootlayer,sessionlayer,options%29.md)
  Opens a stage rooted at a given layer.
- [static func open(FilePath, sessionLayer: USDLayer?, options: USDStage.OpenOptions) throws -> USDStage](./open%28_,sessionlayer,options%29.md)
  Opens a stage using a file as the root layer.
- [static func open(URL, loadingPayloads: USDStage.InitialLoadRule) throws -> USDStage](./open%28_,loadingpayloads%29.md)
  Opens a stage using the file at a URL as its root layer.
- [USDStage.InitialLoadRule](./initialloadrule.md)
  Specifies the rule used when opening a stage to determine if referenced payloads are loaded.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdstage/openoptions)*