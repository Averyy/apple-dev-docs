# setHidden(_:)

**Framework**: WatchKit  
**Kind**: method

Hides or shows the interface object in your user interface.

**Availability**:
- watchOS 2.0+

## Declaration

```swift
func setHidden(_ hidden: Bool)
```

## Mentions

- [Connecting Your User Interface to Your Code](connecting-your-user-interface-to-your-code.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/connecting-your-user-interface-to-your-code))

#### Discussion

When you hide or show an object in your interface, WatchKit makes a note to update the layout during the next refresh cycle. During that cycle, WatchKit adjusts the layout to display only the currently visible objects.

## Parameters

- `hidden`: A Boolean value indicating the visibility of the object. Specify   to hide the object. Specify   to show it.

## See Also

- [App Programming Guide for watchOS](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/General/Conceptual/WatchKitProgrammingGuide/index.html#//apple_ref/doc/uid/TP40014969)
- [func setAlpha(CGFloat)](setalpha(_:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfaceobject/setalpha(_:)))
  Sets the opacity of the interface object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkinterfaceobject/sethidden(_:))*