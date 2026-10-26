# CMSetPartialProfileElement

**Framework**: Application Services  
**Kind**: func

Sets part of the element data for a specific tag in the specified profile.

## Declaration

```c
CMError CMSetPartialProfileElement (
   CMProfileRef prof,
   OSType tag,
   UInt32 offset,
   UInt32 byteCount,
   const void *elementData
);
```

#### Return Value

A `CMError` value. See [Result Codes](../colorsync_manager.md#1670295).

#### Overview

You can use the `CMSetPartialProfileElement` function to set the data for an element when the amount of data is large and you need to copy it to the profile in segments. 

After you set the element size, you can call this function repeatedly, as many times as necessary, each time appending a segment of data to the end of the data already copied until all the element data is copied.

If you know the size of the element data, you should call the function [CMSetProfileElementSize](./api-1804980-cmsetprofileelementsize.md) to reserve it before you call `CMSetPartialProfileElement` to set element data in segments. Setting the size first avoids the extensive overhead required to increase the size for the element data with each call to append another segment of data. 

To copy the entire data for an element as a single operation, when the amount of data is small enough to allow this, call the function [CMSetProfileElement](./api-1804977-cmsetprofileelement.md). 

## Parameters

- `prof`: A profile reference of type [`CMProfileRef`](../cmprofileref.md) to the profile containing the tag for which the element data is set. 
- `tag`: The tag signature for the element whose data is set. The tag identifies the element. For a complete list of the tag signatures a profile may contain, including a description of each tag, refer to the International Color Consortium Profile Format Specification. The signatures for profile tags are defined in the `CMICCProfile.h` header file. 
- `offset`: The offset in the existing element data where data transfer should begin. 
- `byteCount`: The number of bytes of element data to transfer.
- `elementData`: A pointer to the buffer containing the element data to transfer to the profile. 

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
- [CMGetIndProfileElementInfo](./api-1804996-cmgetindprofileelementinfo.md)
  Obtains the element tag and data size of an element by index from the specified profile. 
- [CMGetIndProfileElement](./api-1805002-cmgetindprofileelement.md)
  Obtains the element data corresponding to a particular index from the specified profile. 
- [CMSetProfileElementReference](./api-1805005-cmsetprofileelementreference.md)
  Adds a tag to the specified profile to refer to data corresponding to a previously set element. 
- [CMRemoveProfileElement](./api-1805008-cmremoveprofileelement.md)
  Removes an element corresponding to a specific tag from the specified profile. 


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1804989-cmsetpartialprofileelement)*