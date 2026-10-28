# CMGetIndProfileElement

**Framework**: Application Services  
**Kind**: func

Obtains the element data corresponding to a particular index from the specified profile. 

## Declaration

```c
CMError CMGetIndProfileElement (
   CMProfileRef prof,
   UInt32 index,
   UInt32 *elementSize,
   void *elementData
);
```

## Return Value

A `CMError` value. See [Result Codes](../colorsync_manager.md#1670295).

## Overview

Before you call the `CMGetIndProfileElement` function to obtain the element data for an element at a specific index, you first determine the size in bytes of the element data. To determine the data size, you can

-  call the function [CMGetIndProfileElementInfo](./api-1804996-cmgetindprofileelementinfo.md), passing the element’s index 
-  call the `CMGetIndProfileElement` function itself, specifying a pointer to an unsigned long data type in the `elementSize` field and a `NULL` value in the `elementData` field 

Once you have determined the size of the element data, you allocate a buffer to hold as much of the data as you need. If you want all of the element data, you specify `NULL` in the `elementSize` parameter. If you want only a portion of the element data, you specify the number of bytes you want in the `elementSize` parameter. You supply a pointer to the data buffer in the `elementData` parameter. After calling `CMGetIndProfileElement`, the `elementSize` parameter contains the size in bytes of the element data actually copied. 

Before calling this function, you should call the function [CMCountProfileElements](./api-1804963-cmcountprofileelements.md). It returns the profile’s total element count in the `elementCount` parameter. 

## Parameters

- `prof`: A profile reference of type [`CMProfileRef`](../cmprofileref.md) to the profile containing the element. 
- `index`: The index of the element whose data you want to obtain. This is a one-based element index within the range returned as the `elementCount` parameter of the `CMCountProfileElements` function. 
- `elementSize`: A pointer to an element data size. On input, specify the size of the element data to copy (except when `elementData` is set to `NULL`). Specify `NULL` to copy the entire element data. To obtain a portion of the element data, specify the number of bytes to be copy. 

  On return, the size of the element data actually copied.
- `elementData`: A pointer to memory for element data. On input, you allocate memory. On return, this buffer holds the element data. 

  To obtain the element size in the `elementSize` parameter without copying the element data to this buffer, specify `NULL` for this parameter.

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
- [CMGetIndProfileElementInfo](./api-1804996-cmgetindprofileelementinfo.md)
  Obtains the element tag and data size of an element by index from the specified profile. 
- [CMSetProfileElementReference](./api-1805005-cmsetprofileelementreference.md)
  Adds a tag to the specified profile to refer to data corresponding to a previously set element. 
- [CMRemoveProfileElement](./api-1805008-cmremoveprofileelement.md)
  Removes an element corresponding to a specific tag from the specified profile. 


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805002-cmgetindprofileelement)*