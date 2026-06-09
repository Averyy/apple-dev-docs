# USDStage.OpenOptions

**Framework**: USDKit  
**Kind**: struct

Options that specify behavior related to opening a stage.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
struct OpenOptions
```

## Topics

### Initializers
- [init()](usdstage-4sfi1/openoptions/init.md)
### Type Properties
- [static var createNew: USDStage.OpenOptions](usdstage-4sfi1/openoptions/createnew.md)
  Creates a new layer instead of opening an existing file. Any existing file at the specified path will be overwritten.
### Type Methods
- [static func loadRule(USDStage.InitialLoadRule) -> USDStage.OpenOptions](usdstage-4sfi1/openoptions/loadrule(_:).md)
  Specifies the rule used to determine if referenced payloads are loaded.

## Relationships

### Conforms To
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [static func open(rootLayer: USDLayer, sessionLayer: USDLayer?, options: USDStage.OpenOptions) throws -> USDStage](usdstage-4sfi1/open(rootlayer:sessionlayer:options:).md)
  Opens a stage rooted at a given layer.
- [static func open(FilePath, sessionLayer: USDLayer?, options: USDStage.OpenOptions) throws -> USDStage](usdstage-4sfi1/open(_:sessionlayer:options:).md)
  Opens a stage using a file as the root layer.
- [static func open(URL, loadingPayloads: USDStage.InitialLoadRule) throws -> USDStage](usdstage-4sfi1/open(_:loadingpayloads:).md)
- [USDStage.InitialLoadRule](usdstage-4sfi1/initialloadrule.md)
  Specifies the rule used when opening a stage to determine if referenced payloads are loaded.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdstage-4sfi1/openoptions)*