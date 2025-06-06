# MDItemCopyAttributes(_:_:)

**Framework**: Core Services  
**Kind**: func

Returns the values of the specified attributes in the metadata item.

**Availability**:
- macOS 10.4+

## Declaration

```swift
func MDItemCopyAttributes(_ item: MDItem!, _ names: CFArray!) -> CFDictionary!
```

#### Return_value

A CFDictionary containing keys for the requested attribute names, and the corresponding values. If an attribute does not exist, or the attribute is unreadable, there will be no key-value pair for it in the dictionary. Returns `NULL` on failure.

## Parameters

- `item`: The item to be queried.
- `names`: A CFArray containing the names of the requested attributes.

## See Also

- [func MDItemCopyAttribute(MDItem!, CFString!) -> CFTypeRef!](1427080-mditemcopyattribute.md)
  Returns the value of the specified attribute in the metadata item.
- [func MDItemCopyAttributeNames(MDItem!) -> CFArray!](1427066-mditemcopyattributenames.md)
  Returns an array containing the attribute names existing in the metadata item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1426980-mditemcopyattributes)*