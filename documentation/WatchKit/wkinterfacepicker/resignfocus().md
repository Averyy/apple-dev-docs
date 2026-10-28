# resignFocus()

**Framework**: WatchKit  
**Kind**: method  
**Role**: Instance Method

Removes focus from the picker, causing it to stop receiving input from the Digital Crown.

**Availability**:
- watchOS 2.0+

## Declaration

```swift
func resignFocus()
```

```objc
- (void) resignFocus;
```

## Discussion

When no picker has focus, input from the Digital Crown is once again used to scroll the contents of the screen.

## See Also

### Managing Input from the Digital Crown
- [func focus()](./focus%28%29.md)
  Configures the picker to receive input from the Digital Crown.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkinterfacepicker/resignfocus())*