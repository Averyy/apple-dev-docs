# iTunes Library

**Framework**: iTunes Library  
**Kind**: module

Retrieve the properties of the media in the user’s iTunes library.

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.13+

#### Overview

With this framework, you can retrieve media information, such as track and playlist metadata, directly from the user’s iTunes library, eliminating the need to query the iTunes XML file.

To use this framework, create an [`ITLibrary`](itlibrary.md) object by calling the [`libraryWithAPIVersion:error:`](itlibrary/librarywithapiversion:error:.md) class method. You can interrogate the instance that returns to obtain its properties and the properties of its media items. For example:

> ❗ **Important**:  You must code sign your app to retrieve information with this framework, and iTunes library access is read-only. This framework is available to users with iTunes 11 or later.

 You must code sign your app to retrieve information with this framework, and iTunes library access is read-only. This framework is available to users with iTunes 11 or later.

## Topics

### Essentials
- [class ITLibrary](itlibrary.md)
  This class serves as the entry point to the iTunesLibrary framework.
### Albums and Playlists
- [class ITLibAlbum](itlibalbum.md)
  This class provides information about an album in the iTunes library.
- [class ITLibPlaylist](itlibplaylist.md)
  This class describes a playlist in the iTunes library.
### Media Items
- [class ITLibMediaItem](itlibmediaitem.md)
  This class describes a media item (a track) in the iTunes library, such as a song, a video, or a podcast.
- [class ITLibMediaEntity](itlibmediaentity.md)
  This class describes a media entity, which can be a media item, such as an audio track.
- [class ITLibArtist](itlibartist.md)
  This class represents an artist, such as the performer of a song.
- [class ITLibArtwork](itlibartwork.md)
  This class represents the artwork for a media item.
- [class ITLibMediaItemVideoInfo](itlibmediaitemvideoinfo.md)
  This class encapsulates the video information of a video media item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iTunesLibrary)*