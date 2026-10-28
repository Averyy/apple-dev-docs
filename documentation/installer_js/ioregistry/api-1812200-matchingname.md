# matchingName

**Framework**: Installer JS  
**Kind**: instm

Returns the IOKit objects of the specified name.

## Declaration

```
matchingName(objectName, [servicePlane])
```

## Return Value

An array of IOKit object dictionaries.

## Parameters

- `objectName`: String with an IOKit object name.
- `servicePlane`: *Optional*. String with the service plane to search. When unspecified, `'IOServicePlane'` is used.

## See Also

### Accessing the IOKit Registry
- [fromPath](./api-1812172-frompath.md)
  Returns a dictionary with the properties of a given IOKit object.
- [matchingClass](./api-1812186-matchingclass.md)
  Returns the IOKit objects of a given class.
- [childrenOf](./api-1812215-childrenof.md)
  Returns the children of the given IOKit object.
- [parentsOf](./api-1812225-parentsof.md)
  Returns the parents of the given IOKit object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/installer_js/ioregistry/1812200-matchingname)*