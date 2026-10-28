# CMNewProfileSearch

**Framework**: Application Services  
**Kind**: func

Searches the ColorSync Profiles folder and returns a list of 2.x profiles that match the search specification.

## Declaration

```c
CMError CMNewProfileSearch (
   CMSearchRecord *searchSpec,
   void *refCon,
   UInt32 *count,
   CMProfileSearchRef *searchResult
);
```

## Return Value

A `CMError` value. See [Result Codes](../colorsync_manager.md#1670295).

## Overview

The `CMNewProfileSearch` function sets up and defines a new search identifying through the search record the elements that a profile must contain to qualify for inclusion in the search result list. The function searches the ColorSync profiles folder for version 2.x profiles that meet the criteria and returns a list of these profiles in an internal private data structure whose reference is returned to you in the `searchResult` parameter. 

You must provide a search record of type `CMSearchRecord` identifying the search criteria. You specify which fields of the search record to use for any given search through a search bit mask whose value you set in the search record’s `searchMask` field. 

Among the information you can provide in the search record is a pointer to a filter function to use to eliminate profiles from the search based on additional criteria not defined by the search record. The search result reference is passed to the filter function after the search is performed. For a description of the filter function and its prototype, see the function `CMProfileFilterProcPtr`. 

Your application cannot directly access the search result list. Instead, you pass the returned search result list reference to other search-related functions that allow you to use the result list.

When your application has completed its search, it should call the function [CMDisposeProfileSearch](./api-1805358-cmdisposeprofilesearch.md) to free the private memory allocated for the search.

To obtain a reference to a profile corresponding to a specific index in the list, use the function [CMSearchGetIndProfile](./api-1805362-cmsearchgetindprofile.md). To obtain the file specification for a profile corresponding to a specific index in the list, use the function  [CMSearchGetIndProfileFileSpec](./api-1805365-cmsearchgetindprofilefilespec.md). To update the search result list, use the function  [CMUpdateProfileSearch](./api-1805356-cmupdateprofilesearch.md). To free the private memory allocated for a profile search after your application has completed the search, use the function  [CMDisposeProfileSearch](./api-1805358-cmdisposeprofilesearch.md). 

### Version-Notes

The `CMNewProfileSearch` function does not take full advantage of the optimized profile searching available starting with ColorSync version 2.5. Use [CMIterateColorSyncFolder](./api-1804904-cmiteratecolorsyncfolder.md) instead.

This function is not recommended for use in ColorSync 2.5.

## Parameters

- `searchSpec`: A pointer to a search specification. For a description of the information you can provide in a search record of type `CMSearchRecord` to define the search, see `CMSearchRecord`. See the QuickDraw Reference for a description of the PixMap data type.
- `refCon`: An untyped pointer to arbitrary data supplied by your application. `CMNewProfileSearch` passes this data to your filter routine. For a description of the filter routine, see the function `CMProfileFilterProcPtr`. 
- `count`: A pointer to a profile count. On return, a one-based count of profiles matching the search specification. 
- `searchResult`: A pointer to a search result reference. On return, a reference to the profile search result list. For a description of the `CMProfileSearchRef` private data type, see `CMProfileSearchRef`. See the QuickDraw Reference for a description of the PixMap data type.

## See Also

### Not Recommended
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
- [CMProfileIdentifierListSearch](./api-1805376-cmprofileidentifierlistsearch.md)
  Searches a list of profile references and returns a list of all references that match a specified profile identifier. 


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805344-cmnewprofilesearch)*