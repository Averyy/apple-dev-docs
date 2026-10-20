# MDItemCopyAttributeNames(_:)

**Framework**: Core Services  
**Kind**: func  
**Role**: Function

Returns an array containing the attribute names existing in the metadata item.

**Availability**:
- macOS 10.4+

## Declaration

```swift
func MDItemCopyAttributeNames(_ item: MDItem!) -> CFArray!
```

```c
CFArrayRef MDItemCopyAttributeNames(MDItemRef item);
```

#### Return Value

A CFArray of CFString attribute names, or `NULL` on failure.

## Parameters

- `item`: The item to be queried.

## See Also

### Retrieving Metadata Attributes 
- [func MDItemCopyAttribute(MDItem!, CFString!) -> CFTypeRef!](./api-1427080-mditemcopyattribute.md)
  Returns the value of the specified attribute in the metadata item.
- [func MDItemCopyAttributes(MDItem!, CFArray!) -> CFDictionary!](./api-1426980-mditemcopyattributes.md)
  Returns the values of the specified attributes in the metadata item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1427066-mditemcopyattributenames)*