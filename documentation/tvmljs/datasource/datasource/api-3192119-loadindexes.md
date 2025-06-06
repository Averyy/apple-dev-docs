# loadindexes

**Framework**: TVMLKit JS  
**Kind**: instp

An event type that tells the data source to load its indexes.

**Availability**:
- tvOS 13.0+

## Declaration

```swift
attribute  loadindexes;
```

#### Discussion

This event gets triggered when TVMLKit recognizes that the `DataSource` needs to load more indexes. TVMLKit invokes the event when there are visible cells onscreen consisting of incomplete data segments. For example, when the `DataSource` is set up to support lazy loading of data and it begins to request uninitialized objects, this event is triggered.

The `loadIndexes` event contains its `DataSource `object` `as the target, as well as a `request` property, which is a [`LoadIndexesRequest`](loadindexesrequest.md) object.

## See Also

- [segmentSize](datasource/datasource/3192122-segmentsize.md)
  The maximum number of indexes that are loaded each time the [`loadindexes`](datasource/datasource/3192119-loadindexes.md) event is triggered.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvmljs/datasource/datasource/3192119-loadindexes)*