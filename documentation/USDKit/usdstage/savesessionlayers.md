# saveSessionLayers()

**Framework**: USDKit  
**Kind**: method

Saves the stage’s changed session layers to their sources.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
func saveSessionLayers() throws
```

#### Discussion

> **Note**: An error if a layer cannot be saved. Some session layers may already have been saved when the failure occurs.

## See Also

- [func save() throws](usdstage/save.md)
  Saves the stage’s changed layers to their sources.
- [func reload() throws](usdstage/reload.md)
  Reloads the stage’s layers from their sources, discarding any unsaved changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdstage/savesessionlayers())*