# MDItemCopyAttribute(_:_:)

**Framework**: Core Services  
**Kind**: func  
**Role**: Function

Returns the value of the specified attribute in the metadata item.

**Availability**:
- macOS 10.4+

## Declaration

```swift
func MDItemCopyAttribute(_ item: MDItem!, _ name: CFString!) -> CFTypeRef!
```

```c
CFTypeRef MDItemCopyAttribute(MDItemRef item, CFStringRef name);
```

## Return Value

A CFTypeRef, or `NULL` if there was a failure reading the attribute or the attribute does not exist.

## Parameters

- `item`: The item to be queried.
- `name`: The name of the requested attribute.

## See Also

### Retrieving Metadata Attributes 
- [func MDItemCopyAttributes(MDItem!, CFArray!) -> CFDictionary!](./api-1426980-mditemcopyattributes.md)
  Returns the values of the specified attributes in the metadata item.
- [func MDItemCopyAttributeNames(MDItem!) -> CFArray!](./api-1427066-mditemcopyattributenames.md)
  Returns an array containing the attribute names existing in the metadata item.
- [MDItemCopyAttributeList](./api-1427028-mditemcopyattributelist.md)
  Returns the values of the specified attributes in the metadata item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1427080-mditemcopyattribute)*