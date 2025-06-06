# Playlist

**Framework**: TVMLKit JS  
**Kind**: cl

An array of media items to be played in an Apple TV client-server app.

**Availability**:
- tvOS 9.0+

## Declaration

```swift
interface Playlist
```

#### Overview

In order to play audio or video, at a minimum, there must be a [`Player`](player.md) object that contains a single `Playlist` object, which contains a single [`MediaItem`](mediaitem.md) object.

## Topics

### Modifying the Playlist
- [item](playlist/1627377-item.md)
  Returns the media item located in the indicated array index.
- [length](playlist/1627327-length.md)
  The number of items in the playlist.
- [Playlist](playlist/1627336-playlist.md)
  Creates a new playlist object.
- [pop](playlist/1627310-pop.md)
  Removes a media item from the end of a playlist.
- [push](playlist/1627433-push.md)
  Adds a media item to the end of a playlist.
- [splice](playlist/1627367-splice.md)
  Deletes the indicated array elements and replaces them with the specified elements.

## See Also

- [Playing Media in a Client-Server App](playing_media_in_a_client-server_app.md)
  Play media items in a client-server app using the built-in media player for TVMLKit JS.
- [Player](player.md)
  A media player that displays the UI for playing video and audio in an Apple TV client-server app.
- [MediaItem](mediaitem.md)
  A single audio or video item.
- [Slideshow](slideshow.md)
  An object used to display images on Apple TV in a slideshow format.
- [Browser](browser.md)
  An object used to configure and present a browsable full screen view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvmljs/playlist)*