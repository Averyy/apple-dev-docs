# playbackRate

**Framework**: TVMLKit JS  
**Kind**: instp

The playback speed.

**Availability**:
- tvOS 10.0+

## Declaration

```swift
attribute int playbackRate;
```

#### Discussion

The default playback speed is `1.0`. Speeds with values smaller than `1.0` play in slow motion. Values higher than `1.0` are time-lapsed. Setting the playback rate to `0` or `1` is not supported, use [`stop`](player/1627406-stop.md) and [`play`](player/1627432-play.md) respectively.

## See Also

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
- [previous](player/1682106-previous.md)
  Immediately begins playing the previous media item in the playlist.
- [seekToTime](player/1627368-seektotime.md)
  Sets the playback point to a specified time.
- [stop](player/1627406-stop.md)
  Stops the currently playing item and dismisses the player UI.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvmljs/player/1682104-playbackrate)*