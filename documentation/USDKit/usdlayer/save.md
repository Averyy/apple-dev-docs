# save()

**Framework**: USDKit  
**Kind**: method

Saves the layer to its source if it has unsaved changes.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
func save() throws
```

#### Discussion

> **Note**: An error if the layer cannot be saved.

## See Also

- [func reload() throws](usdlayer/reload.md)
  Reloads the layer from its source, discarding any unsaved changes.
- [func clear()](usdlayer/clear.md)
  Removes all in-memory content from the layer. The file on disk is unaffected until [`save()`](usdlayer/save().md) is called.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdlayer/save())*