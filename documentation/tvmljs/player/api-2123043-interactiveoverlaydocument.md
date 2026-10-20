# interactiveOverlayDocument

**Framework**: TVMLKit JS  
**Kind**: instp  
**Role**: Instance Property

A DOM document that is presented over the entire video player, including the transport bar.

**Availability**:
- tvOS 10.0+

## Declaration

```
attribute Document interactiveOverlayDocument;
```

#### Discussion

The interactive overlay document can contain focusable elements and can be any template document. Set this attribute to `null` to remove the current overlay document.

## See Also

### Setting Up the Player
- [interactiveOverlayDismissable](./api-2123044-interactiveoverlaydismissable.md)
  Determines if an interactive overlay can be dismissed using the Menu button.
- [overlayDocument](./api-1627320-overlaydocument.md)
  The annotations for a video created by placing a DOM document over the video.
- [Player](./api-1627447-player.md)
  Creates a new player object.
- [playlist](./api-1627389-playlist.md)
  The playlist for a player.
- [present](./api-1627418-present.md)
  Shows the player UI if it is not currently visible.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvmljs/player/2123043-interactiveoverlaydocument)*