# matchingClass

**Framework**: Installer JS  
**Kind**: uid

Returns the IOKit objects of a given class.

## Declaration

```
matchingClass(className, [servicePlane])
```

## Return Value

An array of IOKit object dictionaries.

## Parameters

- `className`: String with an IOKit class name.
- `servicePlane`: *Optional*. String with the service plane to search. When unspecified, `'IOServicePlane'` is used.

## See Also

### Accessing the IOKit Registry
- [fromPath](./api-1812172-frompath.md)
  Returns a dictionary with the properties of a given IOKit object.
- [matchingName](./api-1812200-matchingname.md)
  Returns the IOKit objects of the specified name.
- [childrenOf](./api-1812215-childrenof.md)
  Returns the children of the given IOKit object.
- [parentsOf](./api-1812225-parentsof.md)
  Returns the parents of the given IOKit object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/installer_js/ioregistry/1812186-matchingclass)*