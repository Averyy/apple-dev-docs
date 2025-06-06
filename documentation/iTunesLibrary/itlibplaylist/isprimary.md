# isPrimary

**Framework**: iTunes Library  
**Kind**: property

A Boolean value that indicates whether the playlist is the primary playlist.

**Availability**:
- Mac Catalyst 14.0+
- macOS 12.0+

## Declaration

```swift
var isPrimary: Bool { get }
```

## See Also

- [var name: String](itlibplaylist/name.md)
  The name or title of the playlist.
- [var items: [ITLibMediaItem]](itlibplaylist/items.md)
  The media items (tracks) in the playlist.
- [var parentID: NSNumber?](itlibplaylist/parentid.md)
  The unique persistent identifier of the playlist’s parent playlist.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/ituneslibrary/itlibplaylist/isprimary)*