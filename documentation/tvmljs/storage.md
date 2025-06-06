# Storage

**Framework**: TVMLKit JS  
**Kind**: cl

An object used to store key-value-pair information.

**Availability**:
- tvOS 9.0+
- Safari Desktop 10.0+
- Safari Mobile 3.0+

## Declaration

```swift
interface Storage
```

#### Overview

You cannot create a new instance of the `Storage` class. The available instances in TVMLKit JS are `localStorage` and `sessionStorage`. Local storage writes the data to the disk, while session storage writes the data to the memory only. Any data written to the session storage is purged when your app exits.

## Topics

### Accessing Key-Value Pair Information
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
- [setItem](storage/1627302-setitem.md)
  Associates the given data with the given key.

## See Also

- [Binding JSON data to TVML documents](binding_json_data_to_tvml_documents.md)
  Create full-fledged TVML documents by using data binding and queries on simplified TVML files.
- [XMLHttpRequest](xmlhttprequest.md)
  An object used to retrieve data from a URL.
- [DataItem](dataitem.md)
  An object used to create observable objects from JSON objects for data binding.
- [DataSource](datasource.md)
  An interface that allows the system to detect and respond to changes in your data.
- [LoadIndexesRequest](loadindexesrequest.md)
  A request created when the [`loadindexes`](datasource/datasource/3192119-loadindexes.md) event is triggered.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvmljs/storage)*