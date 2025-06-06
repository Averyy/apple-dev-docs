# allPlaylists

**Framework**: iTunes Library  
**Kind**: property

All the playlists in the iTunes library.

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.13+

## Declaration

```swift
var allPlaylists: [ITLibPlaylist] { get }
```

#### Return Value

An array of [`ITLibPlaylist`](itlibplaylist.md) items.

## See Also

- [var allMediaItems: [ITLibMediaItem]](itlibrary/allmediaitems.md)
  All the media items (tracks) in the iTunes library.
- [var apiMajorVersion: Int](itlibrary/apimajorversion.md)
  The major version number of the API the iTunesLibrary framework exposes.
- [var apiMinorVersion: Int](itlibrary/apiminorversion.md)
  The minor version number of the API the iTunesLibrary framework exposes.
- [var applicationVersion: String](itlibrary/applicationversion.md)
  The version of iTunes that created or modified the iTunes library you’re accessing.
- [var mediaFolderLocation: URL?](itlibrary/mediafolderlocation.md)
  The location of the iTunes music folder.
- [var shouldShowContentRating: Bool](itlibrary/shouldshowcontentrating.md)
  A Boolean value indicating whether to show content rating labels.


---

*[View on Apple Developer](https://developer.apple.com/documentation/ituneslibrary/itlibrary/allplaylists)*