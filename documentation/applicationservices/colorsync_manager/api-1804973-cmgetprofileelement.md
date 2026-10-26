# CMGetProfileElement

**Framework**: Application Services  
**Kind**: func

Obtains element data from the specified profile based on the specified element tag signature.

## Declaration

```c
CMError CMGetProfileElement (
   CMProfileRef prof,
   OSType tag,
   UInt32 *elementSize,
   void *elementData
);
```

#### Return Value

A `CMError` value. See [Result Codes](../colorsync_manager.md#1670295).

#### Overview

Before you call the `CMGetProfileElement` function to obtain the element data for a specific element, you must know the size in bytes of the element data so you can allocate a buffer to hold the returned data.

The `CMGetProfileElement` function serves two purposes: to get an element’s size and to obtain an element’s data. In both instances, you provide a reference to the profile containing the element in the `prof` parameter and the tag signature of the element in the `tag` parameter.

To obtain the element data size, call the `CMGetProfileElement` function specifying a pointer to an unsigned long data type in the `elementSize` field and a `NULL` value in the `elementData` field.

After you obtain the element size, you should allocate a buffer large enough to hold the returned element data, then call the `CMGetProfileElement` function again, specifying `NULL` in the `elementSize` parameter to copy the entire element data and a pointer to the data buffer in the `elementData` parameter.

To copy only a portion of the element data beginning from the first byte, allocate a buffer the size of the number of bytes of element data you want to obtain and specify the number of bytes to copy in the `elementSize` parameter. In this case, On return the `elementSize` parameter contains the size in bytes of the element data actually returned.

You cannot use the `CMGetProfileElement` function to copy a portion of element data beginning from an offset into the data. To copy a portion of the element data beginning from any offset, use the function [CMGetPartialProfileElement](./api-1804984-cmgetpartialprofileelement.md).

You cannot use this function to obtain a portion of the `CM2Header` profile header. Instead, you must call the function [CMGetProfileHeader](./api-1804879-cmgetprofileheader.md) to copy the entire profile header and read its contents. 

## Parameters

- `prof`: A profile reference of type [`CMProfileRef`](../cmprofileref.md) to the profile containing the target element. 
- `tag`: The tag signature (for example, ‘A2B0’, or constant `cmAToB0Tag`) for the element in question. The tag identifies the element. For a complete list of the public tag signatures a profile may contain, including a description of each tag, refer to the International Color Consortium Profile Format Specification. The signatures for profile tags are defined in the `CMICCProfile.h` header file. 
- `elementSize`: A pointer to a size value. On input, you specify the size of the element data to copy. Specify `NULL` to copy the entire element data. To obtain a portion of the element data, specify the number of bytes to copy. 

  On return, the size of the data returned.
- `elementData`: A pointer to memory for element data. On input, you allocate memory. On return, this buffer holds the element data.

  To obtain the element size in the `elementSize` parameter without copying the element data to this buffer, specify `NULL` for this parameter.

## See Also

### Accessing Profile Elements
- [CMCountProfileElements](./api-1804963-cmcountprofileelements.md)
  Counts the number of elements in the specified profile.
- [CMProfileElementExists](./api-1804967-cmprofileelementexists.md)
  Tests whether the specified profile contains a specific element based on the element’s tag signature.
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

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1804973-cmgetprofileelement)*