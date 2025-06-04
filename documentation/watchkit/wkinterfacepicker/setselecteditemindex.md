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

## Overview

If the value in `itemIndex` exceeds the number of items in the array, the picker selects the last item. If `itemIndex` is negative, the picker selects the first item in the array.

## Parameters

- `itemIndex`: The index of the item to select. This index represents the index into the array of items you set using the   method.

## See Also

- [func setItems([WKPickerItem]?)](setitems(_:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacepicker/setitems(_:)))
- [class WKPickerItem](wkpickeritem.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkpickeritem))
- [func setCoordinatedAnimations([any WKInterfaceObject & WKImageAnimatable]?)](setcoordinatedanimations(_:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacepicker/setcoordinatedanimations(_:)))


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkinterfacepicker/setselecteditemindex(_:))*