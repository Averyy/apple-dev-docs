# setNeedsLayout(_:)

**Framework**: WebKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Sets whether or not the receiver should change its layout.

**Availability**:
- macOS 10.3+ - Deprecated in 10.14

## Declaration

```swift
func setNeedsLayout(_ flag: Bool)
```

```objc
- (void) setNeedsLayout:(BOOL) flag;
```

#### Discussion

A view conforming to this protocol should store the most recent value of this flag in an internal variable. Then, in its drawRect method, if the most recent value of this flag was [`true`](../../Swift/true.md), it should invoke [`layout()`](./layout%28%29.md) and reset the internal variable before updating the contents of the view.

## Parameters

- `flag`: Sets whether the receiver needs to update its layout in the next call to its [`draw(_:)`](../../AppKit/nsview/draw%28_%29.md) method.

## See Also

### Controlling the layout
- [func layout()](./layout%28%29.md)
  Invoked when the receiver should change its layout immediately.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webdocumentview/setneedslayout(_:))*