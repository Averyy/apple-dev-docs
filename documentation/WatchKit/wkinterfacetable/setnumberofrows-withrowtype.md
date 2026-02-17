# setNumberOfRows(_:withRowType:)

**Framework**: WatchKit  
**Kind**: method

Creates the specified number of row controllers (of the same type) to use in populating the table with data.

**Availability**:
- watchOS 2.0+

## Declaration

```swift
func setNumberOfRows(_ numberOfRows: Int, withRowType rowType: String)
```

#### Discussion

Use this method when you want to populate a table with rows that are all of the same type. This method removes any existing rows from the table and configures a new set of rows based on the information in the `numberOfRows` and `rowType` parameters. For each row, the method also creates an instance of that row’s class and puts the resulting object in an internal array, which you access using the [`rowController(at:)`](wkinterfacetable/rowcontroller(at:).md) method. It is your responsibility to configure each new row controller with the data you want to display.

## Parameters

- `numberOfRows`: The total number of rows to display in the table.
- `rowType`: The name of a row controller defined in your storyboard file. This string corresponds to the value in the Identifier attribute of a row controller definition in your storyboard file.

## See Also

- [func setRowTypes([String])](wkinterfacetable/setrowtypes(_:).md)
  Creates the row controllers to use when populating the table with data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkinterfacetable/setnumberofrows(_:withrowtype:))*