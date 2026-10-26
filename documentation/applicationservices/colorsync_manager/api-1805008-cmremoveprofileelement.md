# CMRemoveProfileElement

**Framework**: Application Services  
**Kind**: func

Removes an element corresponding to a specific tag from the specified profile. 

## Declaration

```c
CMError CMRemoveProfileElement (
   CMProfileRef prof,
   OSType tag
);
```

#### Return Value

A `CMError` value. See [Result Codes](../colorsync_manager.md#1670295).

#### Overview

The `CMRemoveProfileElement` function deletes the tag as well as the element data from the profile. 

## Parameters

- `prof`: A profile reference of type [`CMProfileRef`](../cmprofileref.md) to the profile containing the tag remove. 
- `tag`: The tag signature for the element to remove. 

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
- [CMGetIndProfileElement](./api-1805002-cmgetindprofileelement.md)
  Obtains the element data corresponding to a particular index from the specified profile. 
- [CMSetProfileElementReference](./api-1805005-cmsetprofileelementreference.md)
  Adds a tag to the specified profile to refer to data corresponding to a previously set element. 


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805008-cmremoveprofileelement)*