# playlist

**Framework**: TVMLKit JS  
**Kind**: instp  
**Role**: Instance Property

The playlist for a player.

**Availability**:
- tvOS 9.0+

## Declaration

```
attribute Playlist playlist;
```

## Discussion

Setting this attribute changes the [`Playlist`](../playlist.md) object associated with the player. Inspect this attribute to get the [`Playlist`](../playlist.md) object currently associated with the player.

## See Also

### Setting Up the Player
- [interactiveOverlayDismissable](./api-2123044-interactiveoverlaydismissable.md)
  Determines if an interactive overlay can be dismissed using the Menu button.
- [interactiveOverlayDocument](./api-2123043-interactiveoverlaydocument.md)
  A DOM document that is presented over the entire video player, including the transport bar.
- [overlayDocument](./api-1627320-overlaydocument.md)
  The annotations for a video created by placing a DOM document over the video.
- [Player](./api-1627447-player.md)
  Creates a new player object.
- [present](./api-1627418-present.md)
  Shows the player UI if it is not currently visible.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvmljs/player/1627389-playlist)*