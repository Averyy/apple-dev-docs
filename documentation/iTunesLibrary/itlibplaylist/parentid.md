# parentID

**Framework**: iTunes Library  
**Kind**: property  
**Role**: Instance Property

The unique persistent identifier of the playlist’s parent playlist.

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.13+

## Declaration

```swift
var parentID: NSNumber? { get }
```

```objc
@property (nonatomic, retain, readonly, nullable) NSNumber * parentID;
```

## Discussion

If the playlist doesn’t have a parent, this property is `nil`.

## See Also

### Getting Playlist Info
- [var name: String](./name.md)
  The name or title of the playlist.
- [var items: [ITLibMediaItem]](./items.md)
  The media items (tracks) in the playlist.
- [var isPrimary: Bool](./isprimary.md)
  A Boolean value that indicates whether the playlist is the primary playlist.
- [var isVisible: Bool](./isvisible.md)
  A Boolean value that indicates whether the playlist is visible to the user in iTunes.
- [var distinguishedKind: ITLibDistinguishedPlaylistKind](./distinguishedkind.md)
  An indication of whether the playlist has a special distinction.
- [var kind: ITLibPlaylistKind](./kind.md)
  An indication of the type of playlist.
- [enum ITLibPlaylistKind](../itlibplaylistkind.md)
  These constants specify the possible kinds of playlists.
- [enum ITLibDistinguishedPlaylistKind](../itlibdistinguishedplaylistkind.md)
  These constants specify the possible kinds of distinguished playlists.


---

*[View on Apple Developer](https://developer.apple.com/documentation/ituneslibrary/itlibplaylist/parentid)*