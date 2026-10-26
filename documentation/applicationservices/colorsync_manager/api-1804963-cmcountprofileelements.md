# CMCountProfileElements

**Framework**: Application Services  
**Kind**: func

Counts the number of elements in the specified profile.

## Declaration

```c
CMError CMCountProfileElements (
   CMProfileRef prof,
   UInt32 *elementCount
);
```

#### Return Value

A `CMError` value. See [Result Codes](../colorsync_manager.md#1670295).

#### Overview

Every element in the profile outside the header is counted. A profile may contain tags that are references to other elements. These tags are included in the count. 

## Parameters

- `prof`: A profile reference of type [`CMProfileRef`](../cmprofileref.md) to the profile to examine. 
- `elementCount`: A pointer to an element count. On return, a one-based count of the number of elements. 

## See Also

### Accessing Profile Elements
- [CMProfileElementExists](./api-1804967-cmprofileelementexists.md)
  Tests whether the specified profile contains a specific element based on the element’s tag signature.
- [CMGetProfileElement](./api-1804973-cmgetprofileelement.md)
  Obtains element data from the specified profile based on the specified element tag signature.
- [CMSetProfileElement](./api-1804977-cmsetprofileelement.md)
  Sets or replaces the element data for a specific tag in the specified profile. 
- [CMSetProfileElementSize](./api-1804980-cmsetprofileelementsize.md)
  Reserves the element data size for a specific tag in the specified profile before setting the element data. 
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

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1804963-cmcountprofileelements)*