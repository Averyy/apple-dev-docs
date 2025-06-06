# Browser

**Framework**: TVMLKit JS  
**Kind**: cl

An object used to configure and present a browsable full screen view.

**Availability**:
- tvOS 13.0+

## Declaration

```swift
interface Browser
```

#### Overview

There is no constructor for this object. Configure the `Browser` by modifying its properties. When appropriately configured, use the `present `method to display a new `Browser`.

## Topics

### Creating a Browser
- [present](browser/3192100-present.md)
  Shows the Browser UI if it is not currently visible.
### Modifying a Browser
- [maskInset](browser/3192099-maskinset.md)
  The insets from the edges of the full screen layout.
- [interitemSpacing](browser/3192098-interitemspacing.md)
  The spacing between full screen browser items.
- [cornerRadius](browser/3192097-cornerradius.md)
  The corner radius of each full screen browser item.

## See Also

- [Playing Media in a Client-Server App](playing_media_in_a_client-server_app.md)
  Play media items in a client-server app using the built-in media player for TVMLKit JS.
- [Player](player.md)
  A media player that displays the UI for playing video and audio in an Apple TV client-server app.
- [Playlist](playlist.md)
  An array of media items to be played in an Apple TV client-server app.
- [MediaItem](mediaitem.md)
  A single audio or video item.
- [Slideshow](slideshow.md)
  An object used to display images on Apple TV in a slideshow format.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvmljs/browser)*