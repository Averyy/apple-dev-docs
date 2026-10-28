# playbackState

**Framework**: TVMLKit JS  
**Kind**: instp  
**Role**: Instance Property

The current state of the player.

**Availability**:
- tvOS 9.0+

## Declaration

```
readonly attribute String playbackState;
```

## Discussion

This property can contain the following valid values: `begin`, `end`, `loading`, `playing`, `paused`, and `scanning`.

## See Also

### Controlling Playback
- [changeToMediaAtIndex](./api-1682100-changetomediaatindex.md)
  Immediately begins playing the media item at the specified index in the playlist.
- [pause](./api-1627417-pause.md)
  Pauses the currently playing media item.
- [next](./api-1682103-next.md)
  Immediately begins playing the next media item in the playlist.
- [play](./api-1627432-play.md)
  Plays the currently selected media item.
- [playbackRate](./api-1682104-playbackrate.md)
  The playback speed.
- [previous](./api-1682106-previous.md)
  Immediately begins playing the previous media item in the playlist.
- [seekToTime](./api-1627368-seektotime.md)
  Sets the playback point to a specified time.
- [stop](./api-1627406-stop.md)
  Stops the currently playing item and dismisses the player UI.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvmljs/player/1627387-playbackstate)*