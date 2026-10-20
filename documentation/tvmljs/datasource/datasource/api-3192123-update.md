# update

**Framework**: TVMLKit JS  
**Kind**: instm  
**Role**: Instance Method

Updates an item in the data source array.

**Availability**:
- tvOS 13.0+

## Declaration

```
void update(
    in Array items, 
    in Array indexTitle, 
    in int segmentSize
);
```

#### Discussion

The update API allows the existing data source to reuse already loaded items. This reduces any flashes that might traditionally occur in the UI because of these updates.

## See Also

### Modifying the Data Source
- [insert](./api-3192116-insert.md)
  Inserts a new item into the array.
- [delete](./api-3192115-delete.md)
  Deletes an item from the data source array.
- [move](./api-3192120-move.md)
  Moves an item in the data source array.
- [replace](./api-3192121-replace.md)
  Replaces an item in the data source array.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvmljs/datasource/datasource/3192123-update)*