# HTMLVideoElement

**Framework**: WebKit JS  
**Kind**: cl

A class representing the HTML `video` element that plays a video in a webpage. Use the [`HTMLAudioElement`](htmlaudioelement.md) class for the HTML `audio` element.

**Availability**:
- Safari Desktop 10.0+
- Safari Mobile 3.0+

## Declaration

```swift
interface HTMLVideoElement
```

## Topics

### Getting and Setting Properties
- [width](htmlvideoelement/1631245-width.md)
  The width of the video element in CSS pixels.
- [height](htmlvideoelement/1633722-height.md)
  The height of the video element in CSS pixels.
- [poster](htmlvideoelement/1631880-poster.md)
  The URI address of an image file that is shown when no video data is available.
### Getting State
- [videoWidth](htmlvideoelement/1631691-videowidth.md)
  The native width of the video in CSS pixels. (read-only)
- [videoHeight](htmlvideoelement/1629096-videoheight.md)
  The native height of the video in CSS pixels. (read-only)
### Displaying Video Fullscreen
- [webkitDisplayingFullscreen](htmlvideoelement/1630493-webkitdisplayingfullscreen.md)
  A Boolean value indicating whether the video is displaying in fullscreen mode.
- [webkitEnterFullscreen](htmlvideoelement/1633500-webkitenterfullscreen.md)
  Enters fullscreen mode.
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
### Displaying Presentation Mode
- [webkitSetPresentationMode](htmlvideoelement/1631224-webkitsetpresentationmode.md)
  Sets the presentation mode for video playback. 
- [webkitSupportsPresentationMode](htmlvideoelement/1629816-webkitsupportspresentationmode.md)
  A Boolean value indicating whether the video can be played in presentation mode.
- [webkitPresentationMode](htmlvideoelement/1631913-webkitpresentationmode.md)
  A property indicating the presentation mode. 
- [playsInline](htmlvideoelement/2528111-playsinline.md)
  A Boolean value indicating whether the video plays inline.

## Relationships

### Inherits From
- [HTMLMediaElement](htmlmediaelement.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkitjs/htmlvideoelement)*