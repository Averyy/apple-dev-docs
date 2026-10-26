# CMProfileIdentifierListSearch

**Framework**: Application Services  
**Kind**: func

Searches a list of profile references and returns a list of all references that match a specified profile identifier. 

## Declaration

```c
CMError CMProfileIdentifierListSearch (
   CMProfileIdentifierPtr ident,
   CMProfileRef *profileList,
   UInt32 listSize,
   UInt32 *matchedCount,
   CMProfileRef *matchedList
);
```

#### Return Value

A `CMError` value. See [Result Codes](../colorsync_manager.md#1670295). It is not an error condition if the `CMProfileIdentifierListSearch` function finds no matching profiles. The function returns an error only if a Memory Manager or other low-level system error occurs. 

#### Overview

When your application or device driver processes an image, it can keep a list of profile references for each unique profile or profile identifier it encounters in the image. Each time it encounters an embedded profile identifier, your application can call the `CMProfileIdentifierListSearch` function to see if there is already a matching profile reference in the list. Although your list of profile references would normally contain at most one reference that matches the profile identifier, it is possible to have two or more matches. For information on how a profile identifier match is determined, see `CMProfileIdentifier`.

If no matching profile is found in the list, your application can call the function [CMProfileIdentifierFolderSearch](./api-1805374-cmprofileidentifierfoldersearch.md) to see if a matching profile can be found in the ColorSync Profiles folder.

To determine the amount of memory needed for the list of profile references that match a profile identifier, your application may want to call `CMProfileIdentifierListSearch` twice. The first time, on input you set `matchedList` to `NULL` and ignore `matchedCount`. On return, `matchedCount` specifies the number of matching profiles. You then allocate enough memory to hold that many profile references (or a smaller number if you do not want all the references) and call `CMProfileIdentifierListSearch` again. This time you set `matchedList` to a pointer to the allocated memory and set `matchedCount` to the number of references you wish to obtain. To allocate memory, you use code such as the following:

 `myProfileRefListPtr = NewPtr(sizeof(CMProfileRef) * matchedCount);`

If your application is interested in obtaining only the first profile that matches the specified profile, you need call `CMProfileIdentifierListSearch` only once. To do so, you just allocate enough memory to store one profile reference, set `matchedList` to point to that memory (or just set `matchedList` to point to a local variable), and set `matchedCount` to 1. On return, if `matchedCount` still has the value 1, then `CMProfileIdentifierListSearch` found a matching profile. 

## Parameters

- `ident`: A pointer to a profile identifier. The function looks for profile references in `profileList` that match the profile described by this identifier. For information on how a profile identifier match is determined, see `CMProfileIdentifier`. 
- `profileList`: A pointer to a list of profile references to search. 
- `listSize`: The number of profile references in `profileList`. 
- `matchedCount`: A pointer to a count of matching profile references. If you set `matchedList` to `NULL`, On return `matchedCount` specifies the number of references in `profileList` that match `ident`. The count is typically 0 or 1, but can be higher.

  If you do not set `matchedList` to `NULL`, on input you set `matchedCount` to the maximum number of matching references to be returned in `matchedList`. On return, the value of `matchedCount` specifies the actual number of matching references returned, which is always equal to or less than the number passed in.
- `matchedList`: A pointer to a list of profile references. If you set `matchedList` to `NULL` on input, On return nothing is returned in the parameter, and the actual number of matching references is returned in `matchedCount`.

  If you do not set `matchedList` to `NULL` on input, it is treated as a pointer to allocated memory. On return, the allocated memory will contain a list, in no particular order, of profile references that match `ident`. Only version 2.x profiles are included in the profile search result. The number of references in the list is equal to or less than the value you pass in the `matchedCount` parameter. You must allocate enough memory for `matchedList` to store the requested number of profile references.

## See Also

### Not Recommended
- [CMNewProfileSearch](./api-1805344-cmnewprofilesearch.md)
  Searches the ColorSync Profiles folder and returns a list of 2.x profiles that match the search specification.
- [CMUpdateProfileSearch](./api-1805356-cmupdateprofilesearch.md)
  Searches the ColorSync Profiles folder and updates an existing search result obtained originally from the `CMNewProfileSearch` function.
- [CMDisposeProfileSearch](./api-1805358-cmdisposeprofilesearch.md)
  Frees the private memory allocated for a profile search after your application has completed the search. 
- [CMSearchGetIndProfile](./api-1805362-cmsearchgetindprofile.md)
  Opens the profile corresponding to a specific index into a specific search result list and obtains a reference to that profile. 
- [CMSearchGetIndProfileFileSpec](./api-1805365-cmsearchgetindprofilefilespec.md)
  Obtains the file specification for the profile at a specific index into a search result. 
- [CMCreateProfileIdentifier](./api-1805369-cmcreateprofileidentifier.md)
  Creates a profile identifier for a specified profile.
- [CMProfileIdentifierFolderSearch](./api-1805374-cmprofileidentifierfoldersearch.md)
  Searches the ColorSync Profiles folder and returns a list of profile references, one for each profile that matches the specified profile identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805376-cmprofileidentifierlistsearch)*