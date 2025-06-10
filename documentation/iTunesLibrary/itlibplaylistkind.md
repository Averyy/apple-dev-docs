# ITLibPlaylistKind

**Framework**: iTunes Library  
**Kind**: enum

These constants specify the possible kinds of playlists.

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.13+

## Declaration

```swift
enum ITLibPlaylistKind
```

## Topics

### Playlist Kinds
- [ITLibPlaylistKind.regular](itlibplaylistkind/regular.md)
  A standard playlist that the user or iTunes creates, such as , , , or .
- [ITLibPlaylistKind.smart](itlibplaylistkind/smart.md)
  A playlist with contents that iTunes generates by evaluating a set of rules, such as  or .
- [ITLibPlaylistKind.genius](itlibplaylistkind/genius.md)
  A playlist iTunes creates of songs that go well with a song the user specifies.
- [ITLibPlaylistKind.folder](itlibplaylistkind/folder.md)
  A playlist folder that the user or iTunes creates, such as  or .
- [ITLibPlaylistKind.geniusMix](itlibplaylistkind/geniusmix.md)
  An ongoing playlist in a particular genre—like a commercial-free radio station playing the user’s favorite songs—that iTunes creates from music in the user’s iTunes library.
### Initializers
- [init?(rawValue: UInt)](itlibplaylistkind/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

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
- [var distinguishedKind: ITLibDistinguishedPlaylistKind](itlibplaylist/distinguishedkind.md)
  An indication of whether the playlist has a special distinction.
- [var kind: ITLibPlaylistKind](itlibplaylist/kind.md)
  An indication of the type of playlist.
- [enum ITLibDistinguishedPlaylistKind](itlibdistinguishedplaylistkind.md)
  These constants specify the possible kinds of distinguished playlists.


---

*[View on Apple Developer](https://developer.apple.com/documentation/ituneslibrary/itlibplaylistkind)*