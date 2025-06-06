# preload

**Framework**: Webkitjs  
**Kind**: instp

A DOMString value that gives a hint to the browser how much of the media should be fetched when the webpage is loaded.

**Availability**:
- Safari Desktop 10.0+
- Safari Mobile 10.0+

## Declaration

```swift
attribute DOMString preload;
```

#### Discussion

Possible values are `auto`, `metadata`, and `none`. The attribute defaults to `auto`, suggesting to the browser the server is able to provide the media for immediate and agressive downloading. The `metadata` value suggests minimal server interaction to retrieve only metadata and the first frames of the media resource, while `none` suggests no server interaction is needed. These `preload` values can be changed dynamically. There is no guarantee that you get the behavior that you request.

## See Also

- [autoplay](htmlmediaelement/1629662-autoplay.md)
  A Boolean value that determines whether the media resource plays automatically when available.
- [controls](htmlmediaelement/1631980-controls.md)
  A Boolean value that determines whether the playback controls appear.
- [currentTime](htmlmediaelement/1631307-currenttime.md)
  The current playback position in seconds.
- [defaultPlaybackRate](htmlmediaelement/1631650-defaultplaybackrate.md)
  The default rate used to play the media resource.
- [loop](htmlmediaelement/1633760-loop.md)
  A Boolean value that determines whether the playback should loop.
- [muted](htmlmediaelement/1630580-muted.md)
  A Boolean value that determines whether the audio content should be muted.
- [playbackRate](htmlmediaelement/1629746-playbackrate.md)
  The speed that the media resource is playing.
- [src](htmlmediaelement/1629312-src.md)
  The URI address of the media resource to play.
- [volume](htmlmediaelement/1631549-volume.md)
  The volume of the audio portion of the media element.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkitjs/htmlmediaelement/1633059-preload)*