# go(to:)

**Framework**: WebKit  
**Kind**: method  
**Role**: Instance Method

Makes the specified item in the back-forward list the current item.

**Availability**:
- macOS 10.4+ - Deprecated in 10.14

## Declaration

```swift
func go(to item: WebHistoryItem!)
```

```objc
- (void) goToItem:(WebHistoryItem *) item;
```

## Parameters

- `item`: A web history item that represents a visited webpage. If `item` is not in the back-forward list, an [`invalidArgumentException`](../../Foundation/nsexceptionname/invalidargumentexception.md) exception is raised.

## See Also

### Moving Backward and Forward
- [func goBack()](./goback%28%29.md)
  Moves backward one item in the back-forward list.
- [func goForward()](./goforward%28%29.md)
  Moves forward one item in the back-forward list.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webbackforwardlist/go(to:))*