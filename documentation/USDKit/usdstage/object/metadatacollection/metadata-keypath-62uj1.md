# metadata(_:keyPath:)

**Framework**: USDKit  
**Kind**: method

Returns the value at `keyPath` within the dictionary-valued metadata for the given key.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
func metadata<T>(_ key: USDToken, keyPath: USDToken) -> T? where T : USDStage.Object.MetadataValue
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdstage/object/metadatacollection/metadata(_:keypath:)-62uj1)*