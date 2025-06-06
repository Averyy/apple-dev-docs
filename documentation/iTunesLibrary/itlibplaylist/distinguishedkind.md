# distinguishedKind

**Framework**: iTunes Library  
**Kind**: property

An indication of whether the playlist has a special distinction.

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.13+

## Declaration

```swift
var distinguishedKind: ITLibDistinguishedPlaylistKind { get }
```

#### Discussion

 are special playlists that iTunes generates to organize media items inside the library. If the playlist isn’t a distinguished playlist, this property returns [`ITLibDistinguishedPlaylistKind.kindNone`](itlibdistinguishedplaylistkind/kindnone.md).

## See Also

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
- [var kind: ITLibPlaylistKind](itlibplaylist/kind.md)
  An indication of the type of playlist.
- [enum ITLibPlaylistKind](itlibplaylistkind.md)
  These constants specify the possible kinds of playlists.
- [enum ITLibDistinguishedPlaylistKind](itlibdistinguishedplaylistkind.md)
  These constants specify the possible kinds of distinguished playlists.


---

*[View on Apple Developer](https://developer.apple.com/documentation/ituneslibrary/itlibplaylist/distinguishedkind)*