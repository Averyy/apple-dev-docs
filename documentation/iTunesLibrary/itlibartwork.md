# ITLibArtwork

**Framework**: iTunes Library  
**Kind**: class

This class represents the artwork for a media item.

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.13+

## Declaration

```swift
class ITLibArtwork
```

## Topics

### Getting Artwork Info
- [var image: NSImage?](itlibartwork/image.md)
  The artwork image.
- [var imageData: Data?](itlibartwork/imagedata.md)
  The raw image data of the artwork in the format that [`imageDataFormat`](itlibartwork/imagedataformat.md) specifies.
- [var imageDataFormat: ITLibArtworkFormat](itlibartwork/imagedataformat.md)
  The format of the artwork image data that [`imageData`](itlibartwork/imagedata.md) returns.
### Artwork Formats
- [enum ITLibArtworkFormat](itlibartworkformat.md)
  These constants specify the possible formats of the data that [`imageDataFormat`](itlibartwork/imagedataformat.md) returns.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class ITLibMediaItem](itlibmediaitem.md)
  This class describes a media item (a track) in the iTunes library, such as a song, a video, or a podcast.
- [class ITLibMediaEntity](itlibmediaentity.md)
  This class describes a media entity, which can be a media item, such as an audio track.
- [class ITLibArtist](itlibartist.md)
  This class represents an artist, such as the performer of a song.
- [class ITLibMediaItemVideoInfo](itlibmediaitemvideoinfo.md)
  This class encapsulates the video information of a video media item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/ituneslibrary/itlibartwork)*