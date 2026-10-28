# webkitEnterFullscreen

**Framework**: WebKit JS  
**Kind**: instm  
**Role**: Instance Method

Enters fullscreen mode.

**Availability**:
- Safari Desktop 5.0+
- Safari Mobile 4.2+

## Declaration

```
void webkitEnterFullscreen();
```

## Discussion

This method throws an exception if the element is not allowed to enter fullscreen—that is, if [`webkitSupportsFullscreen`](./api-1628805-webkitsupportsfullscreen.md) is `false`.

## See Also

### Displaying Video Fullscreen
- [webkitDisplayingFullscreen](./api-1630493-webkitdisplayingfullscreen.md)
  A Boolean value indicating whether the video is displaying in fullscreen mode.
- [webkitExitFullscreen](./api-1629468-webkitexitfullscreen.md)
  Exits fullscreen mode.
- [webkitSupportsFullscreen](./api-1628805-webkitsupportsfullscreen.md)
  A Boolean value indicating whether the video can be played in fullscreen mode.
- [webkitWirelessVideoPlaybackDisabled](./api-1630084-webkitwirelessvideoplaybackdisab.md)
  A Boolean value indicating whether wireless video playback is disabled.
- [webkitEnterFullScreen](./api-1630649-webkitenterfullscreen.md)
  Use [`webkitEnterFullscreen`](./api-1633500-webkitenterfullscreen.md).
- [webkitExitFullScreen](./api-1628991-webkitexitfullscreen.md)
  Use [`webkitExitFullscreen`](./api-1629468-webkitexitfullscreen.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkitjs/htmlvideoelement/1633500-webkitenterfullscreen)*