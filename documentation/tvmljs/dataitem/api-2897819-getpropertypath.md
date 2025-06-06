# getPropertyPath

**Framework**: TVMLKit JS  
**Kind**: instm

Retrieves the value associated with a property path.

**Availability**:
- tvOS 11.0+

## Declaration

```swift
Object getPropertyPath(
    in String path
);
```

#### Return_value

The data item object contained in the path.

## Parameters

- `path`: The dot-separated sequence of properties from the receiver. The path can contain array indexers. For example,   refers to the   property stored in index location 0 in the   array.

## See Also

- [setPropertyPath](dataitem/2897832-setpropertypath.md)
  Sets the value associated with a property path.
- [touchPropertyPath](dataitem/2897830-touchpropertypath.md)
  Updates the property path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvmljs/dataitem/2897819-getpropertypath)*