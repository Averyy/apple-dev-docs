# ITLibPlaylist

**Framework**: iTunes Library  
**Kind**: class

This class describes a playlist in the iTunes library.

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.13+

## Declaration

```swift
class ITLibPlaylist
```

#### Overview

A  is a collection of media items (tracks). The user creates and organizes playlists manually, or iTunes automatically generates them. Playlists are media entities. Each contains a unique identifier and a set of properties. Playlists can form a hierarchical structure. In those cases, the [`parentID`](itlibplaylist/parentid.md) property of [`ITLibPlaylist`](itlibplaylist.md) returns the persistent ID of the parent playlist.

## Topics

### Getting Playlist Info
- [var name: String](itlibplaylist/name.md)
  The name or title of the playlist.
- [var items: [ITLibMediaItem]](itlibplaylist/items.md)
  The media items (tracks) in the playlist.
- [var parentID: NSNumber?](itlibplaylist/parentid.md)
  The unique persistent identifier of the playlist’s parent playlist.
- [var isPrimary: Bool](itlibplaylist/isprimary.md)
  A Boolean value that indicates whether the playlist is the primary playlist.
- [var isVisible: Bool](itlibplaylist/isvisible.md)
  A Boolean value that indicates whether the playlist is visible to the user in iTunes.
- [var distinguishedKind: ITLibDistinguishedPlaylistKind](itlibplaylist/distinguishedkind.md)
  An indication of whether the playlist has a special distinction.
- [var kind: ITLibPlaylistKind](itlibplaylist/kind.md)
  An indication of the type of playlist.
- [enum ITLibPlaylistKind](itlibplaylistkind.md)
  These constants specify the possible kinds of playlists.
- [enum ITLibDistinguishedPlaylistKind](itlibdistinguishedplaylistkind.md)
  These constants specify the possible kinds of distinguished playlists.
### Playlist Properties
- [let ITLibPlaylistPropertyAllItemsPlaylist: String](itlibplaylistpropertyallitemsplaylist.md)
  A Boolean value that indicates whether the API exposes every item in the playlist.
- [let ITLibPlaylistPropertyDistinguisedKind: String](itlibplaylistpropertydistinguisedkind.md)
  An indication of whether the playlist has a special distinction.
- [let ITLibPlaylistPropertyItems: String](itlibplaylistpropertyitems.md)
  The media items (tracks) in the playlist.
- [let ITLibPlaylistPropertyKind: String](itlibplaylistpropertykind.md)
  An indication of the type of playlist.
- [let ITLibPlaylistPropertyPrimary: String](itlibplaylistpropertyprimary.md)
  A Boolean value that indicates whether the playlist is the primary playlist.
- [let ITLibPlaylistPropertyName: String](itlibplaylistpropertyname.md)
  The name or title of the playlist.
- [let ITLibPlaylistPropertyParentPersistentID: String](itlibplaylistpropertyparentpersistentid.md)
  The unique persistent identifier of the playlist’s parent playlist.
- [let ITLibPlaylistPropertyVisible: String](itlibplaylistpropertyvisible.md)
  A Boolean value that indicates whether the playlist is visible to the user in iTunes.
### Deprecated
- [var isAllItemsPlaylist: Bool](itlibplaylist/isallitemsplaylist.md)
  Indicates whether the API exposes every item in the playlist.
- [var isMaster: Bool](itlibplaylist/ismaster.md)
  A Boolean value that indicates whether the playlist represents the entire iTunes library.
- [let ITLibPlaylistPropertyMaster: String](itlibplaylistpropertymaster.md)
  A Boolean value that indicates whether the playlist represents the entire iTunes library.

## Relationships

### Inherits From
- [ITLibMediaEntity](itlibmediaentity.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class ITLibAlbum](itlibalbum.md)
  This class provides information about an album in the iTunes library.


---

*[View on Apple Developer](https://developer.apple.com/documentation/ituneslibrary/itlibplaylist)*