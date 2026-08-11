# init(string:loadingPayloads:)

**Framework**: USDKit  
**Kind**: init

Creates a stage from a string containing a `.usda` document.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
init(string: String, loadingPayloads: USDStage.InitialLoadRule = .all) throws
```

#### Discussion

> **Note**: An error if the string cannot be read as a `.usda` layer.

## Parameters

- `string`: The text of a `.usda` document to open as the root layer.
- `loadingPayloads`: The rule that determines which payloads are loaded when opening the stage.

## See Also

- [init(displayName: String?, loadingPayloads: USDStage.InitialLoadRule)](usdstage/init(displayname:loadingpayloads:).md)
  Creates a new memory-backed stage.
- [init(Data, type: UTType, loadingPayloads: USDStage.InitialLoadRule) throws](usdstage/init(_:type:loadingpayloads:).md)
  Creates a stage from in-memory data in a given format.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdstage/init(string:loadingpayloads:))*