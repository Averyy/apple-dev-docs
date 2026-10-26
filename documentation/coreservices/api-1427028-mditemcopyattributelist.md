# MDItemCopyAttributeList

**Framework**: Core Services  
**Kind**: func  
**Role**: Function

Returns the values of the specified attributes in the metadata item.

**Availability**:
- macOS 10.4+

## Declaration

```c
CFDictionaryRef MDItemCopyAttributeList(MDItemRef item, ...);
```

#### Return Value

A CFDictionary containing keys for the requested attribute names, and the corresponding values. If an attribute does not exist, or the attribute is unreadable, there will be no key-value pair for it in the dictionary. Returns `NULL` on failure.

## Parameters

- `item`: The item to be queried.
- `...`: A comma-separated varargs list of the string attribute names..

## See Also

### Retrieving Metadata Attributes 
- [MDItemCopyAttribute](./api-1427080-mditemcopyattribute.md)
  Returns the value of the specified attribute in the metadata item.
- [MDItemCopyAttributes](./api-1426980-mditemcopyattributes.md)
  Returns the values of the specified attributes in the metadata item.
- [MDItemCopyAttributeNames](./api-1427066-mditemcopyattributenames.md)
  Returns an array containing the attribute names existing in the metadata item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1427028-mditemcopyattributelist)*