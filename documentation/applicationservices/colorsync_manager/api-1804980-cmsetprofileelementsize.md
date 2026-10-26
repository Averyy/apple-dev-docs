# CMSetProfileElementSize

**Framework**: Application Services  
**Kind**: func

Reserves the element data size for a specific tag in the specified profile before setting the element data. 

## Declaration

```c
CMError CMSetProfileElementSize (
   CMProfileRef prof,
   OSType tag,
   UInt32 elementSize
);
```

#### Return Value

A `CMError` value. See [Result Codes](../colorsync_manager.md#1670295).

#### Overview

Your application can use the `CMSetProfileElementSize` function to reserve the size of element data for a specific tag before you call the function [CMGetPartialProfileElement](./api-1804984-cmgetpartialprofileelement.md) to set the element data. The most efficient way to set a large amount of element data when you know the size of the data is to first set the size, then call the `CMSetPartialProfileElement` function to set each of the data segments. Calling the `CMSetProfileElementSize` function first eliminates the need for the ColorSync Manager to repeatedly increase the size for the data each time you call the `CMSetPartialProfileElement` function. 

In addition to reserving the element data size, the `CMSetProfileElementSize` function sets the element tag, if it does not already exist. 

## Parameters

- `prof`: A profile reference of type [`CMProfileRef`](../cmprofileref.md) to the profile in which the element data size is reserved. 
- `tag`: The tag signature for the element whose size is reserved. The tag identifies the element. For a complete list of the tag signatures a profile may contain, including a description of each tag, refer to the International Color Consortium Profile Format Specification. The signatures for profile tags are defined in the `CMICCProfile.h` header file. 
- `elementSize`: The total size in bytes to reserve for the element data. 

## See Also

### Accessing Profile Elements
- [CMCountProfileElements](./api-1804963-cmcountprofileelements.md)
  Counts the number of elements in the specified profile.
- [CMProfileElementExists](./api-1804967-cmprofileelementexists.md)
  Tests whether the specified profile contains a specific element based on the element’s tag signature.
- [CMGetProfileElement](./api-1804973-cmgetprofileelement.md)
  Obtains element data from the specified profile based on the specified element tag signature.
- [CMSetProfileElement](./api-1804977-cmsetprofileelement.md)
  Sets or replaces the element data for a specific tag in the specified profile. 
- [CMGetPartialProfileElement](./api-1804984-cmgetpartialprofileelement.md)
  Obtains a portion of the element data from the specified profile based on the specified element tag signature.
- [CMSetPartialProfileElement](./api-1804989-cmsetpartialprofileelement.md)
  Sets part of the element data for a specific tag in the specified profile.
- [CMGetIndProfileElementInfo](./api-1804996-cmgetindprofileelementinfo.md)
  Obtains the element tag and data size of an element by index from the specified profile. 
- [CMGetIndProfileElement](./api-1805002-cmgetindprofileelement.md)
  Obtains the element data corresponding to a particular index from the specified profile. 
- [CMSetProfileElementReference](./api-1805005-cmsetprofileelementreference.md)
  Adds a tag to the specified profile to refer to data corresponding to a previously set element. 
- [CMRemoveProfileElement](./api-1805008-cmremoveprofileelement.md)
  Removes an element corresponding to a specific tag from the specified profile. 


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1804980-cmsetprofileelementsize)*