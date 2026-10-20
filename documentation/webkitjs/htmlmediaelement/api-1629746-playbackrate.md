# playbackRate

**Framework**: WebKit JS  
**Kind**: instp  
**Role**: Instance Property

The speed that the media resource is playing.

**Availability**:
- Safari Desktop 10.0+
- Safari Mobile 10.0+

## Declaration

```
attribute unrestricted double playbackRate;
```

#### Discussion

The value of this property is a multiple of the media resource’s intrinsic speed. If set to `0.0`, a `NOT_SUPPORTED_ERR` DOM exception is raised. The default value is `1.0`. Use this property to create custom controls for playback rate. Values greater than `1.0` fast-forward media and values less than `0.0` rewind. This property can not be set for HTML5 audio/video elements on iOS.

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
- [preload](./api-1633059-preload.md)
  A DOMString value that gives a hint to the browser how much of the media should be fetched when the webpage is loaded.
- [src](./api-1629312-src.md)
  The URI address of the media resource to play.
- [volume](./api-1631549-volume.md)
  The volume of the audio portion of the media element.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkitjs/htmlmediaelement/1629746-playbackrate)*