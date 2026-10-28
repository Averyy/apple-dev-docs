# setTitle(_:)

**Framework**: WatchKit  
**Kind**: method  
**Role**: Instance Method

Sets the switch title to the specified string.

**Availability**:
- watchOS 2.0+

## Declaration

```swift
func setTitle(_ title: String?)
```

```objc
- (void) setTitle:(NSString *) title;
```

## Discussion

This method looks for a localized version of title in your WatchKit extension’s `Localizable.strings` file. If it finds one, it uses the localized string for the switch title. If it does not find a localized version of the string, it uses the value in the title directly. The text replaces the previous text set for the switch.

The switch title is drawn using the font and styling information from your storyboard.

## Parameters

- `title`: The text to be displayed in the switch. Specifying `nil` clears the current text from the switch.

## See Also

### Related Documentation
- [App Programming Guide for watchOS](https://developer.apple.com/library/archive/documentation/General/Conceptual/WatchKitProgrammingGuide/index.html#//apple_ref/doc/uid/TP40014969)
### Setting the Switch’s Title
- [func setAttributedTitle(NSAttributedString?)](./setattributedtitle%28_%29.md)
  Sets the switch title to the specified attributed string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkinterfaceswitch/settitle(_:))*