# reload()

**Framework**: USDKit  
**Kind**: method  
**Role**: Instance Method

Reloads the layer from its source, discarding any unsaved changes.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
func reload() throws
```

#### Discussion

> **Throws**: An error if the layer cannot be reloaded.

## See Also

### Saving and reloading
- [func save() throws](./save%28%29.md)
  Saves the layer to its source if it has unsaved changes.
- [func clear()](./clear%28%29.md)
  Removes all in-memory content from the layer. The file on disk is unaffected until [`save()`](./save%28%29.md) is called.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdlayer/reload())*