# overlayDocument

**Framework**: TVMLKit JS  
**Kind**: instp  
**Role**: Instance Property

The annotations for a video created by placing a DOM document over the video.

**Availability**:
- tvOS 9.0+

## Declaration

```
attribute Document overlayDocument;
```

## Discussion

Create a DOM document using the [divTemplate](https://developer.apple.com/library/archive/documentation/LanguagesUtilities/Conceptual/ATV_Template_Guide/DivTemplate.html#//apple_ref/doc/uid/TP40015064-CH28) and assign it to the `overlayDocument` property. Set this attribute to `null` to remove the current overlay document.

## See Also

### Setting Up the Player
- [interactiveOverlayDismissable](./api-2123044-interactiveoverlaydismissable.md)
  Determines if an interactive overlay can be dismissed using the Menu button.
- [interactiveOverlayDocument](./api-2123043-interactiveoverlaydocument.md)
  A DOM document that is presented over the entire video player, including the transport bar.
- [Player](./api-1627447-player.md)
  Creates a new player object.
- [playlist](./api-1627389-playlist.md)
  The playlist for a player.
- [present](./api-1627418-present.md)
  Shows the player UI if it is not currently visible.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvmljs/player/1627320-overlaydocument)*