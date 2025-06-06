# artwork(forMediaFile:)

**Framework**: iTunes Library  
**Kind**: method

Retrieves the artwork from a media file that may or may not be in the iTunes library.

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.13+

## Declaration

```swift
func artwork(forMediaFile mediaFileURL: URL) -> ITLibArtwork?
```

#### Return Value

An [`ITLibArtwork`](itlibartwork.md) instance representing the media file artwork, or `nil` if the media file doesn’t contain any artwork or the system can’t extract the artwork.

## Parameters

- `mediaFileURL`: The URL of the media file whose artwork you want to retrieve. The media file may or may not be in the iTunes library.


---

*[View on Apple Developer](https://developer.apple.com/documentation/ituneslibrary/itlibrary/artwork(formediafile:))*