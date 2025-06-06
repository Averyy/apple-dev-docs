# update

**Framework**: TVMLKit JS  
**Kind**: instm

Updates an item in the data source array.

**Availability**:
- tvOS 13.0+

## Declaration

```swift
void update(
    in Array items, 
    in Array indexTitle, 
    in int segmentSize
);
```

#### Discussion

The update API allows the existing data source to reuse already loaded items. This reduces any flashes that might traditionally occur in the UI because of these updates.

## See Also

- [insert](datasource/datasource/3192116-insert.md)
  Inserts a new item into the array.
- [delete](datasource/datasource/3192115-delete.md)
  Deletes an item from the data source array.
- [move](datasource/datasource/3192120-move.md)
  Moves an item in the data source array.
- [replace](datasource/datasource/3192121-replace.md)
  Replaces an item in the data source array.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvmljs/datasource/datasource/3192123-update)*