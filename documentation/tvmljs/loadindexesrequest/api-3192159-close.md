# close

**Framework**: TVMLKit JS  
**Kind**: instm

Signals whether or not the data fetch is successful.

**Availability**:
- tvOS 13.0+

## Declaration

```swift
void close(
    in Boolean success
);
```

#### Discussion

The Boolean value passed into the `close` method signals whether or not the data fetch succeeded. If true is passed, then those indexes are marked internally as loaded, and a [`loadindexes`](datasource/datasource/3192119-loadindexes.md) event for these indexes won't be invoked again. If false is passed, the [`loadindexes`](datasource/datasource/3192119-loadindexes.md) event will be invoked only when those indexes are needed again.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvmljs/loadindexesrequest/3192159-close)*