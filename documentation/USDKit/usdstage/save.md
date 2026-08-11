# save()

**Framework**: USDKit  
**Kind**: method

Saves the stage’s changed layers to their sources.

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

> **Note**: An error if a layer cannot be saved. Some layers may already have been saved when the failure occurs.

## See Also

- [func saveSessionLayers() throws](usdstage/savesessionlayers.md)
  Saves the stage’s changed session layers to their sources.
- [func reload() throws](usdstage/reload.md)
  Reloads the stage’s layers from their sources, discarding any unsaved changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usdkit/usdstage/save())*