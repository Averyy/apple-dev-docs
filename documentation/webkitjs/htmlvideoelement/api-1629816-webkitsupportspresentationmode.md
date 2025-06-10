# webkitSupportsPresentationMode

**Framework**: WebKit JS  
**Kind**: instm

A Boolean value indicating whether the video can be played in presentation mode.

**Availability**:
- Safari Desktop 10.0+
- Safari Mobile 10.0+

## Declaration

```swift
boolean webkitSupportsPresentationMode(
    VideoPresentationMode mode
);
```

#### Discussion

`true` if the device supports presentation mode; otherwise, `false`. This property is also `false` if the meta data is loaded or the `loadedmetadata` event has not fired, and if the files are audio-only.

## See Also

- [webkitSetPresentationMode](htmlvideoelement/1631224-webkitsetpresentationmode.md)
  Sets the presentation mode for video playback. 
- [webkitPresentationMode](htmlvideoelement/1631913-webkitpresentationmode.md)
  A property indicating the presentation mode. 
- [playsInline](htmlvideoelement/2528111-playsinline.md)
  A Boolean value indicating whether the video plays inline.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkitjs/htmlvideoelement/1629816-webkitsupportspresentationmode)*