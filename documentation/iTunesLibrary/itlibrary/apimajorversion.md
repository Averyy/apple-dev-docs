# apiMajorVersion

**Framework**: iTunes Library  
**Kind**: property  
**Role**: Instance Property

The major version number of the API the iTunesLibrary framework exposes.

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.13+

## Declaration

```swift
var apiMajorVersion: Int { get }
```

```objc
@property (nonatomic, assign, readonly) NSUInteger apiMajorVersion;
```

## See Also

### Getting iTunes Library Info
- [var allMediaItems: [ITLibMediaItem]](./allmediaitems.md)
  All the media items (tracks) in the iTunes library.
- [var allPlaylists: [ITLibPlaylist]](./allplaylists.md)
  All the playlists in the iTunes library.
- [var apiMinorVersion: Int](./apiminorversion.md)
  The minor version number of the API the iTunesLibrary framework exposes.
- [var applicationVersion: String](./applicationversion.md)
  The version of iTunes that created or modified the iTunes library you’re accessing.
- [var mediaFolderLocation: URL?](./mediafolderlocation.md)
  The location of the iTunes music folder.
- [var shouldShowContentRating: Bool](./shouldshowcontentrating.md)
  A Boolean value indicating whether to show content rating labels.


---

*[View on Apple Developer](https://developer.apple.com/documentation/ituneslibrary/itlibrary/apimajorversion)*