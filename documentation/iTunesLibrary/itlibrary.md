# ITLibrary

**Framework**: iTunes Library  
**Kind**: class

This class serves as the entry point to the iTunesLibrary framework.

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.13+

## Declaration

```swift
class ITLibrary
```

#### Overview

Use the [`ITLibrary`](itlibrary.md) properties and methods to retrieve media items (tracks) and playlists from the user’s iTunes library. [`ITLibrary`](itlibrary.md) also provides methods for extracting artwork from a media file that may or may not be in the iTunes library. Sandboxed and nonsandboxed apps can also use iTunes’ ability to extract artwork.

> ❗ **Important**: A person needs to grant your app permission before it can access their iTunes library. Add the [`NSAppleMusicUsageDescription`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/NSAppleMusicUsageDescription) key to your app’s `Info.plist` file, and include a description of how you intend to use their library. If this key isn’t present, the system terminates your app when it tries to access the library.

A person needs to grant your app permission before it can access their iTunes library. Add the [`NSAppleMusicUsageDescription`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/NSAppleMusicUsageDescription) key to your app’s `Info.plist` file, and include a description of how you intend to use their library. If this key isn’t present, the system terminates your app when it tries to access the library.

## Topics

### Essentials
- [convenience init(apiVersion: String) throws](itlibrary/init(apiversion:).md)
  Initializes an instance of [`ITLibrary`](itlibrary.md) that can retrieve media entities.
- [init(apiVersion: String, options: ITLibInitOptions) throws](itlibrary/init(apiversion:options:).md)
  Initializes an instance of `ITLibrary` that can retrieve media entities.
- [enum ITLibInitOptions](itlibinitoptions.md)
  These constants describe initialization options for an iTunes library.
### Getting iTunes Library Info
- [var allMediaItems: [ITLibMediaItem]](itlibrary/allmediaitems.md)
  All the media items (tracks) in the iTunes library.
- [var allPlaylists: [ITLibPlaylist]](itlibrary/allplaylists.md)
  All the playlists in the iTunes library.
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
### Loading and Unloading Data
- [func reloadData() -> Bool](itlibrary/reloaddata.md)
  Refreshes the data that the framework uses.
- [func unloadData()](itlibrary/unloaddata.md)
  Unloads the data that the framework uses.
### Accessing Artwork
- [func artwork(forMediaFile: URL) -> ITLibArtwork?](itlibrary/artwork(formediafile:).md)
  Retrieves the artwork from a media file that may or may not be in the iTunes library.
### Deprecated
- [var features: ITLibExportFeature](itlibrary/features.md)
  A bitwise OR combination of the features of this library.
- [enum ITLibExportFeature](itlibexportfeature.md)
  These constants describe the features that an iTunes library supports.
- [var musicFolderLocation: URL?](itlibrary/musicfolderlocation.md)
  The location of the iTunes music folder.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/ituneslibrary/itlibrary)*