# setSelectedItemIndex(_:)

**Framework**: Watchkit  
**Kind**: method

Selects the specified item in the list.

**Availability**:
- watchOS 2.0+

## Declaration

```swift
func setSelectedItemIndex(_ itemIndex: Int)
```

#### Discussion

If the value in `itemIndex` exceeds the number of items in the array, the picker selects the last item. If `itemIndex` is negative, the picker selects the first item in the array.

## Parameters

- `itemIndex`: The index of the item to select. This index represents the index into the array of items you set using the   method.

## See Also

- [func setItems([WKPickerItem]?)](wkinterfacepicker/setitems(_:).md)
  Sets the list of items displayed by the picker.
- [class WKPickerItem](wkpickeritem.md)
  A single item in a picker interface.
- [func setCoordinatedAnimations([any WKInterfaceObject & WKImageAnimatable]?)](wkinterfacepicker/setcoordinatedanimations(_:).md)
  Sets the interface objects that should coordinate their own animations with the picker.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkinterfacepicker/setselecteditemindex(_:))*