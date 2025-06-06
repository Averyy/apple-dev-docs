# goBack()

**Framework**: Webkit  
**Kind**: method

Moves backward one item in the back-forward list.

**Availability**:
- macOS 10.4+

## Declaration

```swift
func goBack()
```

#### Discussion

This method works by changing the current item to the item that precedes it. This method raises an [`internalInconsistencyException`](https://developer.apple.com/documentation/foundation/nsexceptionname/1416220-internalinconsistencyexception) exception if no item precedes the current item.

## See Also

- [func goForward()](webbackforwardlist/goforward.md)
  Moves forward one item in the back-forward list.
- [func go(to: WebHistoryItem!)](webbackforwardlist/go(to:).md)
  Makes the specified item in the back-forward list the current item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webbackforwardlist/goback())*