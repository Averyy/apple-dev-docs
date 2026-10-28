# init(displayName:loadingPayloads:)

**Framework**: USDKit  
**Kind**: init  
**Role**: Initializer

Creates a new memory-backed stage.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
init(displayName: String? = nil, loadingPayloads: USDStage.InitialLoadRule = .all)
```

## Discussion

This is analogous to creating an anonymous [`USDLayer`](../usdlayer.md).

## See Also

### Creating a stage
- [init(string: String, loadingPayloads: USDStage.InitialLoadRule) throws](./init%28string,loadingpayloads%29.md)
  Creates a stage from a string containing a `.usda` document.
- [init(Data, type: UTType, loadingPayloads: USDStage.InitialLoadRule) throws](./init%28_,type,loadingpayloads%29.md)
  Creates a stage from in-memory data in a given format.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdstage/init(displayname:loadingpayloads:))*