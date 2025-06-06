# Player

**Framework**: TVMLKit JS  
**Kind**: cl

A media player that displays the UI for playing video and audio in an Apple TV client-server app.

**Availability**:
- tvOS 9.0+

## Declaration

```swift
interface Player
```

#### Overview

After you create a new player, associate the player with a playlist that contains media items. In order to play audio or video, at a minimum, there must be a `Player` object that contains a single [`Playlist`](playlist.md) object, which contains a single [`MediaItem`](mediaitem.md) object.

## Topics

### Setting Up the Player
- [interactiveOverlayDismissable](player/2123044-interactiveoverlaydismissable.md)
  Determines if an interactive overlay can be dismissed using the Menu button.
- [interactiveOverlayDocument](player/2123043-interactiveoverlaydocument.md)
  A DOM document that is presented over the entire video player, including the transport bar.
- [overlayDocument](player/1627320-overlaydocument.md)
  The annotations for a video created by placing a DOM document over the video.
- [Player](player/1627447-player.md)
  Creates a new player object.
- [playlist](player/1627389-playlist.md)
  The playlist for a player.
- [present](player/1627418-present.md)
  Shows the player UI if it is not currently visible.
### Controlling Playback
- [changeToMediaAtIndex](player/1682100-changetomediaatindex.md)
  Immediately begins playing the media item at the specified index in the playlist.
- [pause](player/1627417-pause.md)
  Pauses the currently playing media item.
- [next](player/1682103-next.md)
  Immediately begins playing the next media item in the playlist.
- [play](player/1627432-play.md)
  Plays the currently selected media item.
- [playbackState](player/1627387-playbackstate.md)
  The current state of the player.
- [playbackRate](player/1682104-playbackrate.md)
  The playback speed.
- [previous](player/1682106-previous.md)
  Immediately begins playing the previous media item in the playlist.
- [seekToTime](player/1627368-seektotime.md)
  Sets the playback point to a specified time.
- [stop](player/1627406-stop.md)
  Stops the currently playing item and dismisses the player UI.
### Inspecting Media Items
- [currentMediaItem](player/1627325-currentmediaitem.md)
  The currently selected media item in the playlist.
- [currentMediaItemDate](player/1837542-currentmediaitemdate.md)
  Contains the current time of the media item as a `Date` object.
- [currentMediaItemDuration](player/1682110-currentmediaitemduration.md)
  The length, in seconds, of the current media item.
- [nextMediaItem](player/1627338-nextmediaitem.md)
  The next media item in the playlist after the currently selected item.
- [previousMediaItem](player/1627373-previousmediaitem.md)
  The item in the playlist previous to the currently selected item.
### Responding to Events
- [mediaItemDidChange](player/1627385-mediaitemdidchange.md)
  An event notifying the listener that the player changed a media item.
- [mediaItemWillChange](player/1627345-mediaitemwillchange.md)
  An event notifying the listener that the player is about to changed a media item.
- [playbackDidStall](player/1682114-playbackdidstall.md)
  An event that indicates that playback has stalled.
- [playbackError](player/1682115-playbackerror.md)
  An event that indicates an error has occurred during playback.
- [requestSeekToTime](player/1627354-requestseektotime.md)
  An event that indicates whether a seek-to-time request was accomplished.
- [shouldChangeToMediaAtIndex](player/1682117-shouldchangetomediaatindex.md)
  An event that indicates a request to play a media item in a different index is received.
- [shouldHandleStateChange](player/1627428-shouldhandlestatechange.md)
  An event that indicates a state change request has occurred.
- [stateDidChange](player/1627390-statedidchange.md)
  An event that indicates the state of the player has changed.
- [stateWillChange](player/1627331-statewillchange.md)
  An event that indicates the state of the player is about to change.
- [timeBoundaryDidCross](player/1627443-timeboundarydidcross.md)
  An event that indicates a specific playback time in the media item has been crossed.
- [timeDidChange](player/1627344-timedidchange.md)
  An event that happens at a specified interval.
- [timedMetadata](player/1627384-timedmetadata.md)
  An event that is triggered whenever a specified piece of metadata is encountered.
- [transportBarVisibilityDidChange](player/1682120-transportbarvisibilitydidchange.md)
  An event that indicates the state of the transport bar has changed.

## Relationships

### Inherits From
- [EventListenerObject](eventlistenerobject.md)

## See Also

- [Playing Media in a Client-Server App](playing_media_in_a_client-server_app.md)
  Play media items in a client-server app using the built-in media player for TVMLKit JS.
- [Playlist](playlist.md)
  An array of media items to be played in an Apple TV client-server app.
- [MediaItem](mediaitem.md)
  A single audio or video item.
- [Slideshow](slideshow.md)
  An object used to display images on Apple TV in a slideshow format.
- [Browser](browser.md)
  An object used to configure and present a browsable full screen view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvmljs/player)*