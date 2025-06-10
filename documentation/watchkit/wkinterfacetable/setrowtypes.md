# setRowTypes(_:)

**Framework**: WatchKit  
**Kind**: method

Creates the row controllers to use when populating the table with data.

**Availability**:
- watchOS 2.0+

## Declaration

```swift
func setRowTypes(_ rowTypes: [String])
```

#### Discussion

Use this method when you want to display more than one type of row in your table. This method removes any existing rows from the table and configures a new set of rows based on the information in the `rowTypes` parameter. For each row, the method also creates an instance of that row’s class and puts the resulting object in an internal array, which you access using the [`rowController(at:)`](wkinterfacetable/rowcontroller(at:).md) method. It is your responsibility to configure each new row controller with the data you want to display.

The order of the strings in the `rowTypes` parameter determines the order of the row controller objects you retrieve using the [`rowController(at:)`](wkinterfacetable/rowcontroller(at:).md) method, with the first row type used to create the row controller at index 0, the second row type used to create the row controller at index 1, and so on.

## Parameters

- `rowTypes`: An array of strings, each of which corresponds to the name of a row controller defined in your storyboard file. The total number of items in this array is the number of rows to be created in the table.

## See Also

- [App Programming Guide for watchOS](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/General/Conceptual/WatchKitProgrammingGuide/index.html#//apple_ref/doc/uid/TP40014969)
- [func setNumberOfRows(Int, withRowType: String)](wkinterfacetable/setnumberofrows(_:withrowtype:).md)
  Creates the specified number of row controllers (of the same type) to use in populating the table with data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkinterfacetable/setrowtypes(_:))*