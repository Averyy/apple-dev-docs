# layout()

**Framework**: WebKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Invoked when the receiver should change its layout immediately.

**Availability**:
- macOS 10.3+ - Deprecated in 10.14

## Declaration

```swift
func layout()
```

```objc
- (void) layout;
```

#### Discussion

This message is sent to the view as a hint to perform any calculations and update rendering information. For example, at a minimum, the receiver might set the frame rectangle. This method should not perform any drawing operations.

## See Also

### Controlling the layout
- [func setNeedsLayout(Bool)](./setneedslayout%28_%29.md)
  Sets whether or not the receiver should change its layout.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webdocumentview/layout())*