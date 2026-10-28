# seekToTime

**Framework**: TVMLKit JS  
**Kind**: instm  
**Role**: Instance Method

Sets the playback point to a specified time.

**Availability**:
- tvOS 9.0+

## Declaration

```
void seekToTime(
    in int time
);
```

## Discussion

Use this function to change where playback for a media item begins. The time where playback begins is passed, in seconds, by the `time` parameter. For example, to start a media item 5 minutes into playback, set the `time` parameter to 300.

## Parameters

- `time`: The time, in seconds from the beginning of media item, that play begins.

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
- [playbackState](./api-1627387-playbackstate.md)
  The current state of the player.
- [playbackRate](./api-1682104-playbackrate.md)
  The playback speed.
- [previous](./api-1682106-previous.md)
  Immediately begins playing the previous media item in the playlist.
- [stop](./api-1627406-stop.md)
  Stops the currently playing item and dismisses the player UI.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvmljs/player/1627368-seektotime)*