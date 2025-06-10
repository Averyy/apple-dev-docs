# setNeedsLayout(_:)

**Framework**: WebKit  
**Kind**: method  
**Required**: Yes

Sets whether or not the receiver should change its layout.

**Availability**:
- macOS 10.3+

## Declaration

```swift
func setNeedsLayout(_ flag: Bool)
```

#### Discussion

A view conforming to this protocol should store the most recent value of this flag in an internal variable. Then, in its drawRect method, if the most recent value of this flag was [`true`](https://developer.apple.com/documentation/swift/true), it should invoke [`layout()`](webdocumentview/layout().md) and reset the internal variable before updating the contents of the view.

## Parameters

- `flag`: Sets whether the receiver needs to update its layout in the next call to its   method.

## See Also

- [func layout()](webdocumentview/layout.md)
  Invoked when the receiver should change its layout immediately.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webdocumentview/setneedslayout(_:))*