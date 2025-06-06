# playbackError

**Framework**: TVMLKit JS  
**Kind**: instp

An event that indicates an error has occurred during playback.

**Availability**:
- tvOS 10.0+

## Declaration

```swift
attribute  playbackError;
```

#### Discussion

The listener is passed an event object with the following attributes:

- `reason`—The localized string describing why the error occurred.
- `shouldStopDueToError`—A boolean that provides a hint as to whether the player should be stopped due to this error.

## See Also

- [mediaItemDidChange](player/1627385-mediaitemdidchange.md)
  An event notifying the listener that the player changed a media item.
- [mediaItemWillChange](player/1627345-mediaitemwillchange.md)
  An event notifying the listener that the player is about to changed a media item.
- [playbackDidStall](player/1682114-playbackdidstall.md)
  An event that indicates that playback has stalled.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvmljs/player/1682115-playbackerror)*