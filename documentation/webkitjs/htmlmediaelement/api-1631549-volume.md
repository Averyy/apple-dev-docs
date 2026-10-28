# volume

**Framework**: WebKit JS  
**Kind**: instp  
**Role**: Instance Property

The volume of the audio portion of the media element.

**Availability**:
- Safari Desktop 10.0+
- Safari Mobile 10.0+

## Declaration

```
attribute double volume;
```

## Discussion

The value of this property must be in the range from `0.0` (silent) to `1.0` (loudest); otherwise, a `INDEX_SIZE_ERR` DOM exception is raised. The default value is `1.0`.

## See Also

### Getting and Setting Properties
- [autoplay](./api-1629662-autoplay.md)
  A Boolean value that determines whether the media resource plays automatically when available.
- [controls](./api-1631980-controls.md)
  A Boolean value that determines whether the playback controls appear.
- [currentTime](./api-1631307-currenttime.md)
  The current playback position in seconds.
- [defaultPlaybackRate](./api-1631650-defaultplaybackrate.md)
  The default rate used to play the media resource.
- [loop](./api-1633760-loop.md)
  A Boolean value that determines whether the playback should loop.
- [muted](./api-1630580-muted.md)
  A Boolean value that determines whether the audio content should be muted.
- [playbackRate](./api-1629746-playbackrate.md)
  The speed that the media resource is playing.
- [preload](./api-1633059-preload.md)
  A DOMString value that gives a hint to the browser how much of the media should be fetched when the webpage is loaded.
- [src](./api-1629312-src.md)
  The URI address of the media resource to play.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkitjs/htmlmediaelement/1631549-volume)*