# resignFocus()

**Framework**: WatchKit  
**Kind**: method  
**Role**: Instance Method

Removes focus from the volume control, causing it to stop receiving input from the Digital Crown.

**Availability**:
- watchOS 6.0+

## Declaration

```swift
func resignFocus()
```

```objc
- (void) resignFocus;
```

## Discussion

If the volume control is inside a scrollable view, resigning the focus enables scrolling with the Digital Crown.

## See Also

### Managing Input from the Digital Crown
- [func focus()](./focus%28%29.md)
  Sets the volume control as the focus for input from the Digital Crown.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkinterfacevolumecontrol/resignfocus())*