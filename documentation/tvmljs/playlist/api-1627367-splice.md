# splice

**Framework**: TVMLKit JS  
**Kind**: instm  
**Role**: Instance Method

Deletes the indicated array elements and replaces them with the specified elements.

**Availability**:
- tvOS 9.0+

## Declaration

```
Array splice(
    in int start, 
    in int deleteCount, 
    in Object elements
);
```

## Return Value

An array of the deleted elements.

## Discussion

Use this method to modify the contents of the playlist.

## Parameters

- `index`: The array index indicating the beginning of the splice to be deleted.
- `howMany`: The length of the splice, in number of elements.
- `elements`: An array of new elements that are replacing the deleted elements.

## See Also

### Modifying the Playlist
- [item](./api-1627377-item.md)
  Returns the media item located in the indicated array index.
- [length](./api-1627327-length.md)
  The number of items in the playlist.
- [Playlist](./api-1627336-playlist.md)
  Creates a new playlist object.
- [pop](./api-1627310-pop.md)
  Removes a media item from the end of a playlist.
- [push](./api-1627433-push.md)
  Adds a media item to the end of a playlist.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvmljs/playlist/1627367-splice)*