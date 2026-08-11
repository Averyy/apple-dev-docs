# init(_:type:loadingPayloads:)

**Framework**: USDKit  
**Kind**: init

Creates a stage from in-memory data in a given format.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
init(_ buffer: Data, type: UTType, loadingPayloads: USDStage.InitialLoadRule = .all) throws
```

#### Discussion

> **Note**: An error if the data cannot be read as a layer of the given type.

## Parameters

- `buffer`: The serialized USD data to open as the root layer.
- `type`: The content type that identifies the format of `buffer`.
- `loadingPayloads`: The rule that determines which payloads are loaded when opening the stage.

## See Also

- [init(displayName: String?, loadingPayloads: USDStage.InitialLoadRule)](usdstage/init(displayname:loadingpayloads:).md)
  Creates a new memory-backed stage.
- [init(string: String, loadingPayloads: USDStage.InitialLoadRule) throws](usdstage/init(string:loadingpayloads:).md)
  Creates a stage from a string containing a `.usda` document.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdstage/init(_:type:loadingpayloads:))*