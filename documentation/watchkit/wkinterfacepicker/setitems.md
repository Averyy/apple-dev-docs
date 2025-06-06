# setItems(_:)

**Framework**: Watchkit  
**Kind**: method

Sets the list of items displayed by the picker.

**Availability**:
- watchOS 2.0+

## Declaration

```swift
func setItems(_ items: [WKPickerItem]?)
```

#### Discussion

The items you specify must be configured appropriate for the picker style. For example, items displayed using the list style must contain a title. The picker displays items in the order they appear in the `items` array. When a selection occurs, the picker reports the index of the selected item to its associated action method.

This method displays the new items in the picker right away. If the previously specified selection index exceeds the number of items in the new array, the picker selects the last item in the array.

## Parameters

- `items`: An array of   objects. Each item in the array represents a single selectable item.

## See Also

- [class WKPickerItem](wkpickeritem.md)
  A single item in a picker interface.
- [func setSelectedItemIndex(Int)](wkinterfacepicker/setselecteditemindex(_:).md)
  Selects the specified item in the list.
- [func setCoordinatedAnimations([any WKInterfaceObject & WKImageAnimatable]?)](wkinterfacepicker/setcoordinatedanimations(_:).md)
  Sets the interface objects that should coordinate their own animations with the picker.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkinterfacepicker/setitems(_:))*