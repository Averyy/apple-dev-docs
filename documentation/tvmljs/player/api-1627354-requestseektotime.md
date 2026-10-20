# requestSeekToTime

**Framework**: TVMLKit JS  
**Kind**: instp  
**Role**: Instance Property

An event that indicates whether a seek-to-time request was accomplished.

**Availability**:
- tvOS 9.0+

## Declaration

```
attribute  requestSeekToTime;
```

#### Discussion

This event is called after the left or right edge of the Siri Remote is pressed and released. Use [`shouldHandleStateChange`](./api-1627428-shouldhandlestatechange.md) for press and hold events.

Only a single `requestSeekToTime` listener can be active at a time. If multiple listeners are set to listen for `requestSeekToTime`, only the last one will be updated. The listener is passed an event object with the following attributes:

- `currentTime`—The current playback time in seconds.
- `requestedTime`—The requested playback time in seconds.
- `target`—The event object, which is the [`Player`](../player.md) object.
- `timeStamp`—The time that the event occurred.
- `type`—The name of the event.

The listener must return one of the following values:

- `true`. The seek performed as requested.
- `false` or `null`. The seek was not performed.
- An integer value. The seek will be performed to the stated value and not the initial requested value.

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
- [shouldChangeToMediaAtIndex](./api-1682117-shouldchangetomediaatindex.md)
  An event that indicates a request to play a media item in a different index is received.
- [shouldHandleStateChange](./api-1627428-shouldhandlestatechange.md)
  An event that indicates a state change request has occurred.
- [stateDidChange](./api-1627390-statedidchange.md)
  An event that indicates the state of the player has changed.
- [stateWillChange](./api-1627331-statewillchange.md)
  An event that indicates the state of the player is about to change.
- [timeBoundaryDidCross](./api-1627443-timeboundarydidcross.md)
  An event that indicates a specific playback time in the media item has been crossed.
- [timeDidChange](./api-1627344-timedidchange.md)
  An event that happens at a specified interval.
- [timedMetadata](./api-1627384-timedmetadata.md)
  An event that is triggered whenever a specified piece of metadata is encountered.
- [transportBarVisibilityDidChange](./api-1682120-transportbarvisibilitydidchange.md)
  An event that indicates the state of the transport bar has changed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvmljs/player/1627354-requestseektotime)*