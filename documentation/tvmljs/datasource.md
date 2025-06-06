# DataSource

**Framework**: TVMLKit JS  
**Kind**: cl

An interface that allows the system to detect and respond to changes in your data.

**Availability**:
- tvOS 13.0+

## Declaration

```swift
interface DataSource
```

#### Overview

Use the `DataSource` interface to manage data represented as an array. You can modify your array and consequently generate a notification that makes the app aware of any data changes. Thus user interfaces can respond to changes in the array, without needing to repopulate the entire interface for every change.

For example, the `DataSource` interface makes it easy to lazily load objects. When you want to load an element into the UI, append it to the `DataSource`. TVMLKit will trigger the `loadindexes` event when it recognizes the need to fill in certain indexes.

`DataSource` is also useful when you implement an infinite scrolling feature using the `needsmore` event to request more data. When the `needsmore` event is triggered, you can make modifications to the `DataSource` to suit your needs.

## Topics

### Accessing and Modifying Data
- [DataSource.DataSource](datasource/datasource.md)
  Methods and attributes that you use to create, modify, and access data in the data source.

## Relationships

### Inherits From
- [EventListenerObject](eventlistenerobject.md)

## See Also

- [Binding JSON data to TVML documents](binding_json_data_to_tvml_documents.md)
  Create full-fledged TVML documents by using data binding and queries on simplified TVML files.
- [XMLHttpRequest](xmlhttprequest.md)
  An object used to retrieve data from a URL.
- [DataItem](dataitem.md)
  An object used to create observable objects from JSON objects for data binding.
- [Storage](storage.md)
  An object used to store key-value-pair information.
- [LoadIndexesRequest](loadindexesrequest.md)
  A request created when the [`loadindexes`](datasource/datasource/3192119-loadindexes.md) event is triggered.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvmljs/datasource)*