# ITLibMediaEntity

**Framework**: Ituneslibrary  
**Kind**: class

This class describes a media entity, which can be a media item, such as an audio track.

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.13+

## Declaration

```swift
class ITLibMediaEntity
```

#### Overview

> **Note**:  Entity properties are specific to each type of entity, and each specific entity class provides individual accessors for its properties.

Each media entity has a persistent unique ID and set of properties that iTunes assigns.

The `ITLibMediaEntity` class serves as the abstract superclass for [`ITLibMediaItem`](itlibmediaitem.md) and [`ITLibPlaylist`](itlibplaylist.md) instances.

## Topics

### Essentials
- [var persistentID: NSNumber](itlibmediaentity/persistentid.md)
  The unique identifier of the media entity.
### Getting Media Item Properties
- [func enumerateValues(forProperties: Set<String>?, using: (String, Any, UnsafeMutablePointer<ObjCBool>) -> Void)](itlibmediaentity/enumeratevalues(forproperties:using:).md)
  Executes a provided block with the fetched values for the item properties.
- [func enumerateValuesExcept(forProperties: Set<String>?, using: (String, Any, UnsafeMutablePointer<ObjCBool>) -> Void)](itlibmediaentity/enumeratevaluesexcept(forproperties:using:).md)
  Executes a provided block with the fetched values for all properties in the entity except for the provided set.
- [func value(forProperty: String) -> Any?](itlibmediaentity/value(forproperty:).md)
  Gets the value for a specified media property key.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Inherited By
- [ITLibMediaItem](itlibmediaitem.md)
- [ITLibPlaylist](itlibplaylist.md)
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
- [class ITLibArtist](itlibartist.md)
  This class represents an artist, such as the performer of a song.
- [class ITLibArtwork](itlibartwork.md)
  This class represents the artwork for a media item.
- [class ITLibMediaItemVideoInfo](itlibmediaitemvideoinfo.md)
  This class encapsulates the video information of a video media item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iTunesLibrary/itlibmediaentity)*