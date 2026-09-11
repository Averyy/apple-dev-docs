# metadata(_:keyPath:)

**Framework**: USDKit  
**Kind**: method

Returns the value at `keyPath` within the dictionary-valued metadata for the given key.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
func metadata<T>(_ key: USDToken, keyPath: USDToken) -> T? where T : USDStage.Object.MetadataValue
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdstage/object/metadatacollection/metadata(_:keypath:)-62uj1)*