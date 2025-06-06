# getItem

**Framework**: TVMLKit JS  
**Kind**: instm

Retrieves the data associated with the specified key.

**Availability**:
- tvOS 9.0+
- Safari Desktop 4.0+
- Safari Mobile 3.0+

## Declaration

```swift
getter DOMString? getItem(
    DOMString key
);
```

#### Return_value

A `String` object containing the data associated with the passed key.

#### Discussion

The `getItem` function retrieves the data associated with the given key. If the key does not exist, the function returns `null`.

## Parameters

- `key`: A   object containing the key being searched for.

## See Also

- [clear](storage/1627404-clear.md)
  Removes all instances of key-value pairs from the storage list.
- [key](storage/1627380-key.md)
  Returns the key located in the specified location.
- [length](storage/1627448-length.md)
  The number of key-value pairs currently in the storage list.
- [removeItem](storage/1627332-removeitem.md)
  Deletes a key and all associated data from storage.
- [setItem](storage/1627302-setitem.md)
  Associates the given data with the given key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvmljs/storage/1627333-getitem)*