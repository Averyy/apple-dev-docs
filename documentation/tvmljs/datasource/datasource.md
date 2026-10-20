# DataSource.DataSource

**Framework**: TVMLKit JS  
**Kind**: cl  
**Role**: Class

Methods and attributes that you use to create, modify, and access data in the data source.

**Availability**:
- tvOS 13.0+

## Declaration

```
interface DataSource
```

## Topics

### Creating the Data Source
- [DataSource](./datasource/api-3192114-datasource.md)
  Creates a new data source object.
### Modifying the Data Source
- [insert](./datasource/api-3192116-insert.md)
  Inserts a new item into the array.
- [delete](./datasource/api-3192115-delete.md)
  Deletes an item from the data source array.
- [move](./datasource/api-3192120-move.md)
  Moves an item in the data source array.
- [replace](./datasource/api-3192121-replace.md)
  Replaces an item in the data source array.
- [update](./datasource/api-3192123-update.md)
  Updates an item in the data source array.
### Accessing Elements
- [item](./datasource/api-3192117-item.md)
  Returns the array item at the specified index.
- [length](./datasource/api-3192118-length.md)
  The number of items in the data source.
### Loading Elements
- [loadindexes](./datasource/api-3192119-loadindexes.md)
  An event type that tells the data source to load its indexes.
- [segmentSize](./datasource/api-3192122-segmentsize.md)
  The maximum number of indexes that are loaded each time the [`loadindexes`](./datasource/api-3192119-loadindexes.md) event is triggered.

## Relationships

### Inherits From
- [EventListenerObject](../eventlistenerobject.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvmljs/datasource/datasource)*