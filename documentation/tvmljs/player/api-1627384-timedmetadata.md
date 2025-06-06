# timedMetadata

**Framework**: TVMLKit JS  
**Kind**: instp

An event that is triggered whenever a specified piece of metadata is encountered.

**Availability**:
- tvOS 9.0+

## Declaration

```swift
attribute  timedMetadata;
```

#### Discussion

Specify the metadata this event fires on in the `extraInfo` parameter for the listener. The parameter is an array of keys. Valid key values are: `identifier`, `key`, `stringValue`, and `time`. Passing an empty array or `nil` to observe all timed metadata for HLS streams.

## See Also

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
- [transportBarVisibilityDidChange](player/1682120-transportbarvisibilitydidchange.md)
  An event that indicates the state of the transport bar has changed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvmljs/player/1627384-timedmetadata)*