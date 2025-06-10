# go(to:)

**Framework**: WebKit  
**Kind**: method

Makes the specified item in the back-forward list the current item.

**Availability**:
- macOS 10.4+

## Declaration

```swift
func go(to item: WebHistoryItem!)
```

## Parameters

- `item`: A web history item that represents a visited webpage. If   is not in the back-forward list, an   exception is raised.

## See Also

- [func goBack()](webbackforwardlist/goback.md)
  Moves backward one item in the back-forward list.
- [func goForward()](webbackforwardlist/goforward.md)
  Moves forward one item in the back-forward list.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webbackforwardlist/go(to:))*