# previousMediaItem

**Framework**: TVMLKit JS  
**Kind**: instp

The item in the playlist previous to the currently selected item.

**Availability**:
- tvOS 9.0+

## Declaration

```swift
readonly attribute MediaItem previousMediaItem;
```

#### Discussion

This property returns `null` if there are no items in the playlist previous to the currently playing item.

## See Also

- [currentMediaItem](player/1627325-currentmediaitem.md)
  The currently selected media item in the playlist.
- [currentMediaItemDate](player/1837542-currentmediaitemdate.md)
  Contains the current time of the media item as a `Date` object.
- [currentMediaItemDuration](player/1682110-currentmediaitemduration.md)
  The length, in seconds, of the current media item.
- [nextMediaItem](player/1627338-nextmediaitem.md)
  The next media item in the playlist after the currently selected item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvmljs/player/1627373-previousmediaitem)*