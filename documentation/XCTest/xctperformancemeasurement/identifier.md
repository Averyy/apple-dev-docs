# identifier

**Framework**: XCTest  
**Kind**: property

A unique identifier for a measurement.

## Declaration

```swift
var identifier: String { get }
```

#### Discussion

Make an identifier for a measurement unique to the property being measured; it doesn’t need to be unique for each instance of a measurement. As an example, a measurement of database access performance might have the identifier `com.example.ourdb_transactionthroughput`.

## See Also

- [var displayName: String](xctperformancemeasurement/displayname.md)
  A human-readable name for a measurement.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctperformancemeasurement/identifier)*