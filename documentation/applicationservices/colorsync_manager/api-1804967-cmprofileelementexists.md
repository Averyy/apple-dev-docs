# CMProfileElementExists

**Framework**: Application Services  
**Kind**: func

Tests whether the specified profile contains a specific element based on the element’s tag signature.

## Declaration

```c
CMError CMProfileElementExists (
   CMProfileRef prof,
   OSType tag,
   Boolean *found
);
```

## Return Value

A `CMError` value. See [Result Codes](../colorsync_manager.md#1670295).

## Overview

You cannot use this function to test whether certain data in the `CM2Header` profile header exists. Instead, you must call the function [CMGetProfileHeader](./api-1804879-cmgetprofileheader.md) to copy the entire profile header and read its contents. 

## Parameters

- `prof`: A profile reference of type [`CMProfileRef`](../cmprofileref.md) that specifies the profile to examine. 
- `tag`: The tag signature (for example, ‘A2B0’, or constant `cmAToB0Tag`) for the element in question. For a complete list of the tag signatures a profile may contain, including a description of each tag, refer to the International Color Consortium Profile Format Specification. The signatures for profile tags are defined in the `CMICCProfile.h` header file. 
- `found`: A pointer to a flag for whether the element was found. On return, the flag has the value `true` if the profile contains the element or `false` if it does not. 

## See Also

### Accessing Profile Elements
- [CMCountProfileElements](./api-1804963-cmcountprofileelements.md)
  Counts the number of elements in the specified profile.
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

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1804967-cmprofileelementexists)*