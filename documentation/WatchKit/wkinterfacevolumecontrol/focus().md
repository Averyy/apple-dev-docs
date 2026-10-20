# focus()

**Framework**: WatchKit  
**Kind**: method  
**Role**: Instance Method

Sets the volume control as the focus for input from the Digital Crown.

**Availability**:
- watchOS 6.0+

## Declaration

```swift
func focus()
```

```objc
- (void) focus;
```

#### Discussion

When the volume control has the focus, the system highlights it. The user can then use the Digital Crown to increase or decrease the volume.

## See Also

### Managing Input from the Digital Crown
- [func resignFocus()](./resignfocus%28%29.md)
  Removes focus from the volume control, causing it to stop receiving input from the Digital Crown.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkinterfacevolumecontrol/focus())*