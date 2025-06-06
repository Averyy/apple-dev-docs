# webkitEnterFullscreen

**Framework**: Webkitjs  
**Kind**: instm

Enters fullscreen mode.

**Availability**:
- Safari Desktop 5.0+
- Safari Mobile 4.2+

## Declaration

```swift
void webkitEnterFullscreen();
```

#### Discussion

This method throws an exception if the element is not allowed to enter fullscreen—that is, if [`webkitSupportsFullscreen`](htmlvideoelement/1628805-webkitsupportsfullscreen.md) is `false`.

## See Also

- [webkitDisplayingFullscreen](htmlvideoelement/1630493-webkitdisplayingfullscreen.md)
  A Boolean value indicating whether the video is displaying in fullscreen mode.
- [webkitExitFullscreen](htmlvideoelement/1629468-webkitexitfullscreen.md)
  Exits fullscreen mode.
- [webkitSupportsFullscreen](htmlvideoelement/1628805-webkitsupportsfullscreen.md)
  A Boolean value indicating whether the video can be played in fullscreen mode.
- [webkitWirelessVideoPlaybackDisabled](htmlvideoelement/1630084-webkitwirelessvideoplaybackdisab.md)
  A Boolean value indicating whether wireless video playback is disabled.
- [webkitEnterFullScreen](htmlvideoelement/1630649-webkitenterfullscreen.md)
  Use [`webkitEnterFullscreen`](htmlvideoelement/1633500-webkitenterfullscreen.md).
- [webkitExitFullScreen](htmlvideoelement/1628991-webkitexitfullscreen.md)
  Use [`webkitExitFullscreen`](htmlvideoelement/1629468-webkitexitfullscreen.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkitjs/htmlvideoelement/1633500-webkitenterfullscreen)*