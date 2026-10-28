# init(_:type:loadingPayloads:)

**Framework**: USDKit  
**Kind**: init  
**Role**: Initializer

Creates a stage from in-memory data in a given format.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
init(_ buffer: Data, type: UTType, loadingPayloads: USDStage.InitialLoadRule = .all) throws
```

## Discussion

> **Throws**: An error if the data cannot be read as a layer of the given type.

## Parameters

- `buffer`: The serialized USD data to open as the root layer.
- `type`: The content type that identifies the format of `buffer`.
- `loadingPayloads`: The rule that determines which payloads are loaded when opening the stage.

## See Also

### Creating a stage
- [init(displayName: String?, loadingPayloads: USDStage.InitialLoadRule)](./init%28displayname,loadingpayloads%29.md)
  Creates a new memory-backed stage.
- [init(string: String, loadingPayloads: USDStage.InitialLoadRule) throws](./init%28string,loadingpayloads%29.md)
  Creates a stage from a string containing a `.usda` document.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdstage/init(_:type:loadingpayloads:))*