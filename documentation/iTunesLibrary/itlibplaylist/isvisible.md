# isVisible

**Framework**: iTunes Library  
**Kind**: property

A Boolean value that indicates whether the playlist is visible to the user in iTunes.

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.13+

## Declaration

```swift
var isVisible: Bool { get }
```

#### Discussion

There are some playlists that iTunes hides, uses, and maintains without displaying them as playlists to the user. Tracks can still be visible when they’re in a playlist that’s not visible.

## See Also

- [var name: String](itlibplaylist/name.md)
  The name or title of the playlist.
- [var items: [ITLibMediaItem]](itlibplaylist/items.md)
  The media items (tracks) in the playlist.
- [var parentID: NSNumber?](itlibplaylist/parentid.md)
  The unique persistent identifier of the playlist’s parent playlist.
- [var isPrimary: Bool](itlibplaylist/isprimary.md)
  A Boolean value that indicates whether the playlist is the primary playlist.
- [var distinguishedKind: ITLibDistinguishedPlaylistKind](itlibplaylist/distinguishedkind.md)
  An indication of whether the playlist has a special distinction.
- [var kind: ITLibPlaylistKind](itlibplaylist/kind.md)
  An indication of the type of playlist.
- [enum ITLibPlaylistKind](itlibplaylistkind.md)
  These constants specify the possible kinds of playlists.
- [enum ITLibDistinguishedPlaylistKind](itlibdistinguishedplaylistkind.md)
  These constants specify the possible kinds of distinguished playlists.


---

*[View on Apple Developer](https://developer.apple.com/documentation/ituneslibrary/itlibplaylist/isvisible)*