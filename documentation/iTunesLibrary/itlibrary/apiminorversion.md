# apiMinorVersion

**Framework**: iTunes Library  
**Kind**: property  
**Role**: Instance Property

The minor version number of the API the iTunesLibrary framework exposes.

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.13+

## Declaration

```swift
var apiMinorVersion: Int { get }
```

```objc
@property (nonatomic, assign, readonly) NSUInteger apiMinorVersion;
```

## See Also

### Getting iTunes Library Info
- [var allMediaItems: [ITLibMediaItem]](./allmediaitems.md)
  All the media items (tracks) in the iTunes library.
- [var allPlaylists: [ITLibPlaylist]](./allplaylists.md)
  All the playlists in the iTunes library.
- [var apiMajorVersion: Int](./apimajorversion.md)
  The major version number of the API the iTunesLibrary framework exposes.
- [var applicationVersion: String](./applicationversion.md)
  The version of iTunes that created or modified the iTunes library you’re accessing.
- [var mediaFolderLocation: URL?](./mediafolderlocation.md)
  The location of the iTunes music folder.
- [var shouldShowContentRating: Bool](./shouldshowcontentrating.md)
  A Boolean value indicating whether to show content rating labels.


---

*[View on Apple Developer](https://developer.apple.com/documentation/ituneslibrary/itlibrary/apiminorversion)*