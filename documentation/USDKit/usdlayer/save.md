# save()

**Framework**: USDKit  
**Kind**: method

Saves the layer to its source if it has unsaved changes.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

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