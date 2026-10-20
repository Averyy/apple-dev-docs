# segmentSize

**Framework**: TVMLKit JS  
**Kind**: instp  
**Role**: Instance Property

The maximum number of indexes that are loaded each time the [`loadindexes`](./api-3192119-loadindexes.md) event is triggered.

**Availability**:
- tvOS 13.0+

## Declaration

```
readonly attribute int segmentSize;
```

#### Discussion

This property allows you to adjust the number of indexes to be loaded according to the capabilities of your server endpoints.

The `segmentSize` attribute defaults to 20 indexes.

## See Also

### Loading Elements
- [loadindexes](./api-3192119-loadindexes.md)
  An event type that tells the data source to load its indexes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvmljs/datasource/datasource/3192122-segmentsize)*