# CMProfileIdentifierFolderSearch

**Framework**: Application Services  
**Kind**: func

Searches the ColorSync Profiles folder and returns a list of profile references, one for each profile that matches the specified profile identifier.

## Declaration

```c
CMError CMProfileIdentifierFolderSearch (
   CMProfileIdentifierPtr ident,
   UInt32 *matchedCount,
   CMProfileSearchRef *searchResult
);
```

#### Return Value

A `CMError` value. See [Result Codes](../colorsync_manager.md#1670295). It is not an error condition if this function finds no matching profiles. It returns an error only if a File Manager or other low-level system error occurs. 

#### Overview

When your application or device driver processes an image, it can keep a list of profile references for each profile it encounters in the image. Each time it encounters an embedded profile identifier, your application can call the function [CMProfileIdentifierListSearch](./api-1805376-cmprofileidentifierlistsearch.md) to see if there is already a matching profile reference in its list. If not, it can call the `CMProfileIdentifierFolderSearch` function to see if the profile is located in the ColorSync Profiles folder.

Although there should typically be at most one profile in the ColorSync Profiles folder that matches the profile identifier, two or more profiles with different filenames may qualify.

## Parameters

- `ident`: A pointer to a profile identifier structure specifying the profile to search for. 
- `matchedCount`: A pointer to a value of type `unsigned long`. On return, the one-based count of profiles that match the specified profile identifier. The count is typically 0 or 1, but can be higher. 
- `searchResult`: A pointer to a search result reference of type `CMProfileSearchRef`. On return, a reference to the profile search result list. Only version 2.x profiles are included in the profile search result. 

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
- [CMProfileIdentifierListSearch](./api-1805376-cmprofileidentifierlistsearch.md)
  Searches a list of profile references and returns a list of all references that match a specified profile identifier. 


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805374-cmprofileidentifierfoldersearch)*