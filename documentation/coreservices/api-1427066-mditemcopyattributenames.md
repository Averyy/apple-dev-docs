# MDItemCopyAttributeNames(_:)

**Framework**: Core Services  
**Kind**: func

Returns an array containing the attribute names existing in the metadata item.

**Availability**:
- macOS 10.4+

## Declaration

```swift
func MDItemCopyAttributeNames(_ item: MDItem!) -> CFArray!
```

#### Return_value

A CFArray of CFString attribute names, or `NULL` on failure.

## Parameters

- `item`: The item to be queried.

## See Also

- [func MDItemCopyAttribute(MDItem!, CFString!) -> CFTypeRef!](1427080-mditemcopyattribute.md)
  Returns the value of the specified attribute in the metadata item.
- [func MDItemCopyAttributes(MDItem!, CFArray!) -> CFDictionary!](1426980-mditemcopyattributes.md)
  Returns the values of the specified attributes in the metadata item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1427066-mditemcopyattributenames)*