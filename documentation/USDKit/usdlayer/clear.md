# clear()

**Framework**: USDKit  
**Kind**: method

Removes all in-memory content from the layer. The file on disk is unaffected until [`save()`](usdlayer/save().md) is called.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
func clear()
```

## See Also

- [func save() throws](usdlayer/save.md)
  Saves the layer to its source if it has unsaved changes.
- [func reload() throws](usdlayer/reload.md)
  Reloads the layer from its source, discarding any unsaved changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdlayer/clear())*