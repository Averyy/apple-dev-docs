# setPropertyPath

**Framework**: TVMLKit JS  
**Kind**: instm

Sets the value associated with a property path.

**Availability**:
- tvOS 11.0+

## Declaration

```swift
void setPropertyPath(
    in String path, 
    in Object value
);
```

#### Discussion

Set the property path to associate the data item objects contained in the `value` parameter with a section element. [`Listing 1`](dataitem/2897832-setpropertypath#2902804.md) shows an example of data item objects contained in the `newItems` object added to the section that binds the `images` path; for example `<section binding="items:{images};" />`.

```javascript
let section = shelf.getElementsByTagName("section").item(0)section.dataItem = new DataItem()

let newItems = results.map((result) => {
    let objectItem = new DataItem(result.type, result.ID);
    objectItem.url = result.url;
    return objectItem;
});

section.dataItem.setPropertyPath("images", newItems)
```

## Parameters

- `path`: The dot-separated sequence of properties from the receiver. The path can contain array indexers. For example,   refers to the   property stored in index location 0 in the   array.
- `value`: An object associated with the property path.

## See Also

- [getPropertyPath](dataitem/2897819-getpropertypath.md)
  Retrieves the value associated with a property path.
- [touchPropertyPath](dataitem/2897830-touchpropertypath.md)
  Updates the property path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvmljs/dataitem/2897832-setpropertypath)*