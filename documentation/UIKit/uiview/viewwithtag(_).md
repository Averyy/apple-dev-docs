# viewWithTag(_:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Returns the view whose tag matches the specified value.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- tvOS
- visionOS

## Declaration

```swift
func viewWithTag(_ tag: Int) -> UIView?
```

```objc
- (UIView *) viewWithTag:(NSInteger) tag;
```

## Return Value

The view in the receiver’s hierarchy whose tag property matches the value in the `tag` parameter.

## Discussion

This method searches the current view and all of its subviews for the specified view.

## Parameters

- `tag`: The tag value to search for.

## See Also

### Identifying the view at runtime
- [var tag: Int](./tag.md)
  An integer that you can use to identify view objects in your application.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiview/viewwithtag(_:))*