# setCoordinatedAnimations(_:)

**Framework**: WatchKit  
**Kind**: method

Sets the interface objects that should coordinate their own animations with the picker.

**Availability**:
- watchOS 2.0+

## Declaration

```swift
func setCoordinatedAnimations(_ coordinatedAnimations: [any WKInterfaceObject & WKImageAnimatable]?)
```

#### Discussion

Use this method to link other animatable images to the picker. When the user turns the crown, the picker updates the currently displayed image in each of the linked interface objects.

The animated images associated with the interface objects may have any number of frames. For each object, the picker determines the appropriate image to display based on the percentage offset from the beginning of the picker’s own item list. The first picker item displays the first image in the animated sequence and the last picker item displays the last item. If the picker has ten items and an animated image has 20 images, each new picker item advances the animated image by two frames.

## Parameters

- `coordinatedAnimations`: An array of objects that conform to the   protocol. The objects in this array should be displaying an animated image. Specify   to remove all coordinated objects from the picker.

## See Also

- [func setItems([WKPickerItem]?)](setitems(_:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacepicker/setitems(_:)))
  Sets the list of items displayed by the picker.
- [class WKPickerItem](wkpickeritem.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkpickeritem))
  A single item in a picker interface.
- [func setSelectedItemIndex(Int)](setselecteditemindex(_:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacepicker/setselecteditemindex(_:)))
  Selects the specified item in the list.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkinterfacepicker/setcoordinatedanimations(_:))*