# playbackState

**Framework**: TVMLKit JS  
**Kind**: instp

The current state of the player.

**Availability**:
- tvOS 9.0+

## Declaration

```swift
readonly attribute String playbackState;
```

#### Discussion

This property can contain the following valid values: `begin`, `end`, `loading`, `playing`, `paused`, and `scanning`.

## See Also

- [changeToMediaAtIndex](player/1682100-changetomediaatindex.md)
  Immediately begins playing the media item at the specified index in the playlist.
- [pause](player/1627417-pause.md)
  Pauses the currently playing media item.
- [next](player/1682103-next.md)
  Immediately begins playing the next media item in the playlist.
- [play](player/1627432-play.md)
  Plays the currently selected media item.
- [playbackRate](player/1682104-playbackrate.md)
  The playback speed.
- [previous](player/1682106-previous.md)
  Immediately begins playing the previous media item in the playlist.
- [seekToTime](player/1627368-seektotime.md)
  Sets the playback point to a specified time.
- [stop](player/1627406-stop.md)
  Stops the currently playing item and dismisses the player UI.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvmljs/player/1627387-playbackstate)*