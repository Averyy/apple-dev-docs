# layout()

**Framework**: WebKit  
**Kind**: method  
**Required**: Yes

Invoked when the receiver should change its layout immediately.

**Availability**:
- macOS 10.3+

## Declaration

```swift
func layout()
```

#### Discussion

This message is sent to the view as a hint to perform any calculations and update rendering information. For example, at a minimum, the receiver might set the frame rectangle. This method should not perform any drawing operations.

## See Also

- [func setNeedsLayout(Bool)](webdocumentview/setneedslayout(_:).md)
  Sets whether or not the receiver should change its layout.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webdocumentview/layout())*