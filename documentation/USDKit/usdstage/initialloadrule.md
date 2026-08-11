# USDStage.InitialLoadRule

**Framework**: USDKit  
**Kind**: enum

Specifies the rule used when opening a stage to determine if referenced payloads are loaded.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
enum InitialLoadRule
```

## Topics

### Enumeration Cases
- [USDStage.InitialLoadRule.all](usdstage/initialloadrule/all.md)
  Load all loadable prims.
- [USDStage.InitialLoadRule.none](usdstage/initialloadrule/none.md)
  Load no loadable prims.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [static func open(rootLayer: USDLayer, sessionLayer: USDLayer?, options: USDStage.OpenOptions) throws -> USDStage](usdstage/open(rootlayer:sessionlayer:options:).md)
  Opens a stage rooted at a given layer.
- [static func open(FilePath, sessionLayer: USDLayer?, options: USDStage.OpenOptions) throws -> USDStage](usdstage/open(_:sessionlayer:options:).md)
  Opens a stage using a file as the root layer.
- [static func open(URL, loadingPayloads: USDStage.InitialLoadRule) throws -> USDStage](usdstage/open(_:loadingpayloads:).md)
  Opens a stage using the file at a URL as its root layer.
- [USDStage.OpenOptions](usdstage/openoptions.md)
  Options that specify behavior related to opening a stage.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdstage/initialloadrule)*