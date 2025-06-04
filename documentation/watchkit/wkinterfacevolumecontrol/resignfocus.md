# resignFocus()

**Framework**: WatchKit  
**Kind**: method

Removes focus from the volume control, causing it to stop receiving input from the Digital Crown.

**Availability**:
- watchOS 6.0+

## Declaration

```swift
func resignFocus()
```

#### Discussion

If the volume control is inside a scrollable view, resigning the focus enables scrolling with the Digital Crown.

## See Also

- [func focus()](focus().md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacevolumecontrol/focus()))
  Sets the volume control as the focus for input from the Digital Crown.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkinterfacevolumecontrol/resignfocus())*