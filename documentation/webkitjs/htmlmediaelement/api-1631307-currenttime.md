# currentTime

**Framework**: WebKit JS  
**Kind**: instp

The current playback position in seconds.

**Availability**:
- Safari Desktop 3.1+
- Safari Mobile 3.0+

## Declaration

```swift
attribute unrestricted double currentTime;
```

#### Discussion

When you set this property, the media play head moves to the new location. An `INVALID_STATE_ERR` DOM exception is raised if there is no selected media resource when you set this property. An `INDEX_SIZE_ERR` DOM exception is raised if the specified time is not within the start and end times.

## See Also

- [autoplay](htmlmediaelement/1629662-autoplay.md)
  A Boolean value that determines whether the media resource plays automatically when available.
- [controls](htmlmediaelement/1631980-controls.md)
  A Boolean value that determines whether the playback controls appear.
- [defaultPlaybackRate](htmlmediaelement/1631650-defaultplaybackrate.md)
  The default rate used to play the media resource.
- [loop](htmlmediaelement/1633760-loop.md)
  A Boolean value that determines whether the playback should loop.
- [muted](htmlmediaelement/1630580-muted.md)
  A Boolean value that determines whether the audio content should be muted.
- [playbackRate](htmlmediaelement/1629746-playbackrate.md)
  The speed that the media resource is playing.
- [preload](htmlmediaelement/1633059-preload.md)
  A DOMString value that gives a hint to the browser how much of the media should be fetched when the webpage is loaded.
- [src](htmlmediaelement/1629312-src.md)
  The URI address of the media resource to play.
- [volume](htmlmediaelement/1631549-volume.md)
  The volume of the audio portion of the media element.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkitjs/htmlmediaelement/1631307-currenttime)*