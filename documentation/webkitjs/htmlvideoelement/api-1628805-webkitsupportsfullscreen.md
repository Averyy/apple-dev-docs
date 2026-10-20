# webkitSupportsFullscreen

**Framework**: WebKit JS  
**Kind**: instp  
**Role**: Instance Property

A Boolean value indicating whether the video can be played in fullscreen mode.

**Availability**:
- Safari Desktop 5.0+
- Safari Mobile 4.0+

## Declaration

```
readonly attribute boolean webkitSupportsFullscreen;
```

#### Discussion

`true` if the device supports fullscreen mode; otherwise, `false`. This property is also `false` if the meta data is loaded or the `loadedmetadata` event has not fired, and if the files are audio-only.

## See Also

### Displaying Video Fullscreen
- [webkitDisplayingFullscreen](./api-1630493-webkitdisplayingfullscreen.md)
  A Boolean value indicating whether the video is displaying in fullscreen mode.
- [webkitEnterFullscreen](./api-1633500-webkitenterfullscreen.md)
  Enters fullscreen mode.
- [webkitExitFullscreen](./api-1629468-webkitexitfullscreen.md)
  Exits fullscreen mode.
- [webkitWirelessVideoPlaybackDisabled](./api-1630084-webkitwirelessvideoplaybackdisab.md)
  A Boolean value indicating whether wireless video playback is disabled.
- [webkitEnterFullScreen](./api-1630649-webkitenterfullscreen.md)
  Use [`webkitEnterFullscreen`](./api-1633500-webkitenterfullscreen.md).
- [webkitExitFullScreen](./api-1628991-webkitexitfullscreen.md)
  Use [`webkitExitFullscreen`](./api-1629468-webkitexitfullscreen.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkitjs/htmlvideoelement/1628805-webkitsupportsfullscreen)*