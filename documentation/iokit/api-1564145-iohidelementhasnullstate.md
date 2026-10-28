# IOHIDElementHasNullState

**Framework**: IOKit  
**Kind**: func  
**Role**: Function

Returns the null state property for the element.

**Availability**:
- Mac Catalyst 13.1+
- macOS 10.5+

## Declaration

```c
Boolean IOHIDElementHasNullState(IOHIDElementRef element);
```

## Return Value

Returns TRUE if null state or FALSE if no null state.

## Discussion

Indicates whether the element has a state in which it is not sending meaningful data.

## Parameters

- `element`: The element to be queried. If this parameter is not a valid IOHIDElementRef, the behavior is undefined.

## See Also

### Miscellaneous
- [IOHIDElementAttach](./api-1564146-iohidelementattach.md)
  Establish a relationship between one or more elements.
- [IOHIDElementCollectionType](./iohidelement_h/api-1812712-iohidelementcollectiontype.md)
  Retrieves the collection type for the element.
- [IOHIDElementCopyAttached](./api-1564123-iohidelementcopyattached.md)
  Obtain attached elements.
- [IOHIDElementCreateWithDictionary](./api-1564115-iohidelementcreatewithdictionary.md)
  Creates an element from a dictionary.
- [IOHIDElementDetach](./api-1564116-iohidelementdetach.md)
  Remove a relationship between one or more elements.
- [IOHIDElementGetChildren](./api-1564119-iohidelementgetchildren.md)
  Returns the children for the element.
- [IOHIDElementGetCollectionType](./api-1564132-iohidelementgetcollectiontype.md)
  Retrieves the collection type for the element.
- [IOHIDElementGetCookie](./api-1564124-iohidelementgetcookie.md)
  Retrieves the cookie for the element.
- [IOHIDElementGetDevice](./api-1564139-iohidelementgetdevice.md)
  Obtain the device associated with the element.
- [IOHIDElementGetLogicalMax](./api-1564143-iohidelementgetlogicalmax.md)
  Returns the maximum value possible for the element.
- [IOHIDElementGetLogicalMin](./api-1564137-iohidelementgetlogicalmin.md)
  Returns the minimum value possible for the element.
- [IOHIDElementGetMax](./iohidelement_h/api-1812802-iohidelementgetmax.md)
  Returns the maximum value possible for the element.
- [IOHIDElementGetName](./api-1564117-iohidelementgetname.md)
  Returns the name for the element.
- [IOHIDElementGetParent](./api-1564144-iohidelementgetparent.md)
  Returns the parent for the element.
- [IOHIDElementGetPhysicalMax](./api-1564134-iohidelementgetphysicalmax.md)
  Returns the scaled maximum value possible for the element.
- [IOHIDElementGetPhysicalMin](./api-1564140-iohidelementgetphysicalmin.md)
  Returns the scaled minimum value possible for the element.
- [IOHIDElementGetProperty](./api-1564118-iohidelementgetproperty.md)
  Returns the an element property.
- [IOHIDElementGetReportCount](./api-1564142-iohidelementgetreportcount.md)
  Returns the report count for the element.
- [IOHIDElementGetReportID](./api-1564122-iohidelementgetreportid.md)
  Returns the report ID for the element.
- [IOHIDElementGetReportSize](./api-1564130-iohidelementgetreportsize.md)
  Returns the report size in bits for the element.
- [IOHIDElementGetType](./api-1564135-iohidelementgettype.md)
  Retrieves the type for the element.
- [IOHIDElementGetTypeID](./api-1564120-iohidelementgettypeid.md)
  Returns the type identifier of all IOHIDElement instances.
- [IOHIDElementGetUnit](./api-1564136-iohidelementgetunit.md)
  Returns the unit property for the element.
- [IOHIDElementGetUnitExponent](./api-1564121-iohidelementgetunitexponent.md)
  Returns the unit exponenet in base 10 for the element.
- [IOHIDElementGetUsage](./api-1564126-iohidelementgetusage.md)
  Retrieves the usage for an element.
- [IOHIDElementGetUsagePage](./api-1564128-iohidelementgetusagepage.md)
  Retrieves the usage page for an element.
- [IOHIDElementHasPreferredState](./api-1564141-iohidelementhaspreferredstate.md)
  Returns the preferred state property for the element.
- [IOHIDElementIsArray](./api-1564133-iohidelementisarray.md)
  Returns the array property for the element.
- [IOHIDElementIsNonLinear](./api-1564131-iohidelementisnonlinear.md)
  Returns the linear property for the element.
- [IOHIDElementIsRelative](./api-1564129-iohidelementisrelative.md)
  Returns the relative property for the element.
- [IOHIDElementIsVirtual](./api-1564125-iohidelementisvirtual.md)
  Returns the virtual property for the element.
- [IOHIDElementIsWrapping](./api-1564127-iohidelementiswrapping.md)
  Returns the wrap property for the element.
- [IOHIDElementSetProperty](./api-1564138-iohidelementsetproperty.md)
  Sets an element property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/1564145-iohidelementhasnullstate)*