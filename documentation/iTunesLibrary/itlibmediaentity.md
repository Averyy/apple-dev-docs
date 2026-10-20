# ITLibMediaEntity

**Framework**: iTunes Library  
**Kind**: class  
**Role**: Class

This class describes a media entity, which can be a media item, such as an audio track.

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.13+

## Declaration

```swift
class ITLibMediaEntity
```

```objc
@interface ITLibMediaEntity : NSObject
```

#### Overview

> **Note**:  Entity properties are specific to each type of entity, and each specific entity class provides individual accessors for its properties.

Each media entity has a persistent unique ID and set of properties that iTunes assigns.

The `ITLibMediaEntity` class serves as the abstract superclass for [`ITLibMediaItem`](./itlibmediaitem.md) and [`ITLibPlaylist`](./itlibplaylist.md) instances.

## Topics

### Essentials
- [var persistentID: NSNumber](./itlibmediaentity/persistentid.md)
  The unique identifier of the media entity.
### Getting Media Item Properties
- [func enumerateValues(forProperties: Set<String>?, using: (String, Any, UnsafeMutablePointer<ObjCBool>) -> Void)](./itlibmediaentity/enumeratevalues%28forproperties,using%29.md)
  Executes a provided block with the fetched values for the item properties.
- [func enumerateValuesExcept(forProperties: Set<String>?, using: (String, Any, UnsafeMutablePointer<ObjCBool>) -> Void)](./itlibmediaentity/enumeratevaluesexcept%28forproperties,using%29.md)
  Executes a provided block with the fetched values for all properties in the entity except for the provided set.
- [func value(forProperty: String) -> Any?](./itlibmediaentity/value%28forproperty%29.md)
  Gets the value for a specified media property key.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Inherited By
- [ITLibMediaItem](./itlibmediaitem.md)
- [ITLibPlaylist](./itlibplaylist.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Media Items
- [class ITLibMediaItem](./itlibmediaitem.md)
  This class describes a media item (a track) in the iTunes library, such as a song, a video, or a podcast.
- [class ITLibArtist](./itlibartist.md)
  This class represents an artist, such as the performer of a song.
- [class ITLibArtwork](./itlibartwork.md)
  This class represents the artwork for a media item.
- [class ITLibMediaItemVideoInfo](./itlibmediaitemvideoinfo.md)
  This class encapsulates the video information of a video media item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/ituneslibrary/itlibmediaentity)*