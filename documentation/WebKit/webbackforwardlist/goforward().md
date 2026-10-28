# goForward()

**Framework**: WebKit  
**Kind**: method  
**Role**: Instance Method

Moves forward one item in the back-forward list.

**Availability**:
- macOS 10.4+ - Deprecated in 10.14

## Declaration

```swift
func goForward()
```

```objc
- (void) goForward;
```

## Discussion

This method works by changing the current item to the item that follows it. This method raises an [`internalInconsistencyException`](../../Foundation/nsexceptionname/internalinconsistencyexception.md) exception if no item follows the current item.

## See Also

### Moving Backward and Forward
- [func goBack()](./goback%28%29.md)
  Moves backward one item in the back-forward list.
- [func go(to: WebHistoryItem!)](./go%28to%29.md)
  Makes the specified item in the back-forward list the current item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webbackforwardlist/goforward())*