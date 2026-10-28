# CMGetIndProfileElementInfo

**Framework**: Application Services  
**Kind**: func

Obtains the element tag and data size of an element by index from the specified profile. 

## Declaration

```c
CMError CMGetIndProfileElementInfo (
   CMProfileRef prof,
   UInt32 index,
   OSType *tag,
   UInt32 *elementSize,
   Boolean *refs
);
```

## Return Value

A `CMError` value. See [Result Codes](../colorsync_manager.md#1670295).

## Overview

The index order of elements is determined internally by the ColorSync Manager and is not publicly defined.

Before calling the `CMGetIndProfileElementInfo` function, you should call the function [CMCountProfileElements](./api-1804963-cmcountprofileelements.md), which returns the total number of elements in the profile in the `elementCount` parameter. The number you specify for the `index` parameter when calling `CMGetIndProfileElementInfo` should be in the range of 1 to `elementCount`; otherwise the function will return a result code of `cmIndexRangeErr`. 

You might want to call this function, for example, to print out the contents of a profile. 

## Parameters

- `prof`: A profile reference of type [`CMProfileRef`](../cmprofileref.md) to the profile containing the element. 
- `index`: A one-based element index within the range returned by the `elementCount` parameter of the `CMCountProfileElements` function. 
- `tag`: A pointer to an element signature. On return, the tag signature of the element corresponding to the index. 
- `elementSize`: A pointer to an element size. On return, the size in bytes of the element data corresponding to the tag.
- `refs`: A pointer to a reference count flag. On return, set to `true` if more than one tag in the profile refers to element data associated with the tag corresponding to the index. 

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
- [CMSetProfileElementSize](./api-1804980-cmsetprofileelementsize.md)
  Reserves the element data size for a specific tag in the specified profile before setting the element data. 
- [CMGetPartialProfileElement](./api-1804984-cmgetpartialprofileelement.md)
  Obtains a portion of the element data from the specified profile based on the specified element tag signature.
- [CMSetPartialProfileElement](./api-1804989-cmsetpartialprofileelement.md)
  Sets part of the element data for a specific tag in the specified profile.
- [CMGetIndProfileElement](./api-1805002-cmgetindprofileelement.md)
  Obtains the element data corresponding to a particular index from the specified profile. 
- [CMSetProfileElementReference](./api-1805005-cmsetprofileelementreference.md)
  Adds a tag to the specified profile to refer to data corresponding to a previously set element. 
- [CMRemoveProfileElement](./api-1805008-cmremoveprofileelement.md)
  Removes an element corresponding to a specific tag from the specified profile. 


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1804996-cmgetindprofileelementinfo)*