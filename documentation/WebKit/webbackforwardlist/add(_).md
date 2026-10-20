# add(_:)

**Framework**: WebKit  
**Kind**: method  
**Role**: Instance Method

Inserts an item into the back-forward list, immediately after the current item.

**Availability**:
- macOS 10.4+ - Deprecated in 10.14

## Declaration

```swift
func add(_ item: WebHistoryItem!)
```

```objc
- (void) addItem:(WebHistoryItem *) item;
```

#### Discussion

Any items following `item` in the back-forward list are removed. This method also removes items if the capacity of the receiver is exceeded.

## Parameters

- `item`: A web history item that represents a visited webpage. If `item` is `nil`, an [`invalidArgumentException`](../../Foundation/nsexceptionname/invalidargumentexception.md) exception is raised.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webbackforwardlist/add(_:))*