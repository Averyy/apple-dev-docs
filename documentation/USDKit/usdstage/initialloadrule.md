# USDStage.InitialLoadRule

**Framework**: USDKit  
**Kind**: enum  
**Role**: Enumeration

Specifies the rule used when opening a stage to determine if referenced payloads are loaded.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
enum InitialLoadRule
```

## Topics

### Enumeration Cases
- [USDStage.InitialLoadRule.all](./initialloadrule/all.md)
  Load all loadable prims.
- [USDStage.InitialLoadRule.none](./initialloadrule/none.md)
  Load no loadable prims.

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
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
- [USDStage.OpenOptions](./openoptions.md)
  Options that specify behavior related to opening a stage.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdstage/initialloadrule)*