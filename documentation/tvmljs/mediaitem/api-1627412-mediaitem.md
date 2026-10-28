# MediaItem

**Framework**: TVMLKit JS  
**Kind**: instm  
**Role**: Instance Method

Creates a new `MediaItem` object from the information stored in the URL location.

**Availability**:
- tvOS 9.0+

## Declaration

```
new MediaItem(
    in String type, 
    in optional String url
);
```

## Return Value

Returns the `MediaItem` object found in the location specified by the URL.

## Parameters

- `type`: The type of media item to be created. Valid values are `audio` and `video`. The default is `video`.
- `url`: The URL pointing to the media item information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvmljs/mediaitem/1627412-mediaitem)*