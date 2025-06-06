# setTitle(_:)

**Framework**: Watchkit  
**Kind**: method

Sets the switch title to the specified string.

**Availability**:
- watchOS 2.0+

## Declaration

```swift
func setTitle(_ title: String?)
```

#### Discussion

This method looks for a localized version of title in your WatchKit extension’s `Localizable.strings` file. If it finds one, it uses the localized string for the switch title. If it does not find a localized version of the string, it uses the value in the title directly. The text replaces the previous text set for the switch.

The switch title is drawn using the font and styling information from your storyboard.

## Parameters

- `title`: The text to be displayed in the switch. Specifying   clears the current text from the switch.

## See Also

- [App Programming Guide for watchOS](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/General/Conceptual/WatchKitProgrammingGuide/index.html#//apple_ref/doc/uid/TP40014969)
- [func setAttributedTitle(NSAttributedString?)](wkinterfaceswitch/setattributedtitle(_:).md)
  Sets the switch title to the specified attributed string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkinterfaceswitch/settitle(_:))*