# webkitSupportsFullscreen

**Framework**: Webkitjs  
**Kind**: instp

A Boolean value indicating whether the video can be played in fullscreen mode.

**Availability**:
- Safari Desktop 5.0+
- Safari Mobile 4.0+

## Declaration

```swift
readonly attribute boolean webkitSupportsFullscreen;
```

#### Discussion

`true` if the device supports fullscreen mode; otherwise, `false`. This property is also `false` if the meta data is loaded or the `loadedmetadata` event has not fired, and if the files are audio-only.

## See Also

- [webkitDisplayingFullscreen](htmlvideoelement/1630493-webkitdisplayingfullscreen.md)
  A Boolean value indicating whether the video is displaying in fullscreen mode.
- [webkitEnterFullscreen](htmlvideoelement/1633500-webkitenterfullscreen.md)
  Enters fullscreen mode.
- [webkitExitFullscreen](htmlvideoelement/1629468-webkitexitfullscreen.md)
  Exits fullscreen mode.
- [webkitWirelessVideoPlaybackDisabled](htmlvideoelement/1630084-webkitwirelessvideoplaybackdisab.md)
  A Boolean value indicating whether wireless video playback is disabled.
- [webkitEnterFullScreen](htmlvideoelement/1630649-webkitenterfullscreen.md)
  Use [`webkitEnterFullscreen`](htmlvideoelement/1633500-webkitenterfullscreen.md).
- [webkitExitFullScreen](htmlvideoelement/1628991-webkitexitfullscreen.md)
  Use [`webkitExitFullscreen`](htmlvideoelement/1629468-webkitexitfullscreen.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkitjs/htmlvideoelement/1628805-webkitsupportsfullscreen)*