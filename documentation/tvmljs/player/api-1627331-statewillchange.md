# stateWillChange

**Framework**: TVMLKit JS  
**Kind**: instp  
**Role**: Instance Property

An event that indicates the state of the player is about to change.

**Availability**:
- tvOS 9.0+

## Declaration

```
attribute  stateWillChange;
```

## Discussion

The listener is passed an event object with the following attributes:

- `oldState`—The previous state of the player. Valid values are `playing`, `paused`, and `scanning`.
- `state`—The state that the player is has switched to. Valid values are `playing`, `paused`, and `scanning`.
- `target`—The event object, which is the [`Player`](../player.md) object.
- `timeStamp`—The time that the event occurred.
- `type`—The name of the event.

## See Also

### Responding to Events
- [mediaItemDidChange](./api-1627385-mediaitemdidchange.md)
  An event notifying the listener that the player changed a media item.
- [mediaItemWillChange](./api-1627345-mediaitemwillchange.md)
  An event notifying the listener that the player is about to changed a media item.
- [playbackDidStall](./api-1682114-playbackdidstall.md)
  An event that indicates that playback has stalled.
- [playbackError](./api-1682115-playbackerror.md)
  An event that indicates an error has occurred during playback.
- [requestSeekToTime](./api-1627354-requestseektotime.md)
  An event that indicates whether a seek-to-time request was accomplished.
- [shouldChangeToMediaAtIndex](./api-1682117-shouldchangetomediaatindex.md)
  An event that indicates a request to play a media item in a different index is received.
- [shouldHandleStateChange](./api-1627428-shouldhandlestatechange.md)
  An event that indicates a state change request has occurred.
- [stateDidChange](./api-1627390-statedidchange.md)
  An event that indicates the state of the player has changed.
- [timeBoundaryDidCross](./api-1627443-timeboundarydidcross.md)
  An event that indicates a specific playback time in the media item has been crossed.
- [timeDidChange](./api-1627344-timedidchange.md)
  An event that happens at a specified interval.
- [timedMetadata](./api-1627384-timedmetadata.md)
  An event that is triggered whenever a specified piece of metadata is encountered.
- [transportBarVisibilityDidChange](./api-1682120-transportbarvisibilitydidchange.md)
  An event that indicates the state of the transport bar has changed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvmljs/player/1627331-statewillchange)*