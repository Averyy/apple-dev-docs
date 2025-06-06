# touchPropertyPath

**Framework**: TVMLKit JS  
**Kind**: instm

Updates the property path.

**Availability**:
- tvOS 11.0+

## Declaration

```swift
void touchPropertyPath(
    in String path
);
```

#### Discussion

The property path is explicitly updated, and all bound objects are notified.

## Parameters

- `path`: The dot-separated sequence of properties from the receiver. The path can contain array indexers. For example,   refers to the   property stored in index location 0 in the   array.

## See Also

- [setPropertyPath](dataitem/2897832-setpropertypath.md)
  Sets the value associated with a property path.
- [getPropertyPath](dataitem/2897819-getpropertypath.md)
  Retrieves the value associated with a property path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvmljs/dataitem/2897830-touchpropertypath)*