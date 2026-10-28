# getPropertyPath

**Framework**: TVMLKit JS  
**Kind**: instm  
**Role**: Instance Method

Retrieves the value associated with a property path.

**Availability**:
- tvOS 11.0+

## Declaration

```
Object getPropertyPath(
    in String path
);
```

## Return Value

The data item object contained in the path.

## Parameters

- `path`: The dot-separated sequence of properties from the receiver. The path can contain array indexers. For example, `items[0].title` refers to the `title` property stored in index location 0 in the `items` array.

## See Also

### Working with Property Paths
- [setPropertyPath](./api-2897832-setpropertypath.md)
  Sets the value associated with a property path.
- [touchPropertyPath](./api-2897830-touchpropertypath.md)
  Updates the property path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvmljs/dataitem/2897819-getpropertypath)*