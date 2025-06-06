# matchingClass

**Framework**: Installer JS  
**Kind**: uid

Returns the IOKit objects of a given class.

## Declaration

```swift
matchingClass(className, [servicePlane])
```

#### Return_value

An array of IOKit object dictionaries.

## Parameters

- `className`: String with an IOKit class name.
- `servicePlane`: . String with the service plane to search. When unspecified,   is used.

## See Also

- [fromPath](ioregistry/1812172-frompath.md)
  Returns a dictionary with the properties of a given IOKit object.
- [matchingName](ioregistry/1812200-matchingname.md)
  Returns the IOKit objects of the specified name.
- [childrenOf](ioregistry/1812215-childrenof.md)
  Returns the children of the given IOKit object.
- [parentsOf](ioregistry/1812225-parentsof.md)
  Returns the parents of the given IOKit object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/installer_js/ioregistry/1812186-matchingclass)*