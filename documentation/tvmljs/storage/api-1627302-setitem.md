# setItem

**Framework**: TVMLKit JS  
**Kind**: instm

Associates the given data with the given key.

**Availability**:
- tvOS 9.0+
- Safari Desktop 4.0+
- Safari Mobile 3.0+

## Declaration

```swift
void setItem(
    DOMString key, 
    DOMString data
);
```

#### Discussion

The `setItem` function first checks whether the given key already exists in the storage. If it does not, then the key and associated value are stored. If the key already exists and the data in storage is different than the data being passed, the new data is saved to storage.

## Parameters

- `key`: A   object containing the key associated with the data to be saved.
- `data`: A   object containing the data to be stored.

## See Also

- [clear](storage/1627404-clear.md)
  Removes all instances of key-value pairs from the storage list.
- [getItem](storage/1627333-getitem.md)
  Retrieves the data associated with the specified key.
- [key](storage/1627380-key.md)
  Returns the key located in the specified location.
- [length](storage/1627448-length.md)
  The number of key-value pairs currently in the storage list.
- [removeItem](storage/1627332-removeitem.md)
  Deletes a key and all associated data from storage.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvmljs/storage/1627302-setitem)*