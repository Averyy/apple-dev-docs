# goForward()

**Framework**: WebKit  
**Kind**: method

Moves forward one item in the back-forward list.

**Availability**:
- macOS 10.4+

## Declaration

```swift
func goForward()
```

#### Discussion

This method works by changing the current item to the item that follows it. This method raises an [`internalInconsistencyException`](https://developer.apple.com/documentation/Foundation/NSExceptionName/internalInconsistencyException) exception if no item follows the current item.

## See Also

- [func goBack()](webbackforwardlist/goback.md)
  Moves backward one item in the back-forward list.
- [func go(to: WebHistoryItem!)](webbackforwardlist/go(to:).md)
  Makes the specified item in the back-forward list the current item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webbackforwardlist/goforward())*