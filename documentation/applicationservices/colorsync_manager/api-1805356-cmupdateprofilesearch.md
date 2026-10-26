# CMUpdateProfileSearch

**Framework**: Application Services  
**Kind**: func

Searches the ColorSync Profiles folder and updates an existing search result obtained originally from the `CMNewProfileSearch` function.

## Declaration

```c
CMError CMUpdateProfileSearch (
   CMProfileSearchRef search,
   void *refCon,
   UInt32 *count
);
```

#### Return Value

A `CMError` value. See [Result Codes](../colorsync_manager.md#1670295).

#### Overview

After a profile search has been set up and performed through a call to the `CMNewProfileSearch` function, the `CMUpdateProfileSearch` function updates the existing search result. You must use this function if the contents of the ColorSync Profiles folder have changed since the original search result was created.

The search update uses the original search specification, including the filter function indicated by the search record. Data given in the `CMUpdateProfileSearch` function’s `refCon` parameter is passed to the filter function each time it is called. 

Sharing a disk over a network makes it possible for modification of the contents of the ColorSync Profiles folder to occur at any time. 

For a description of the function you call to begin a new search, see the function [CMNewProfileSearch](./api-1805344-cmnewprofilesearch.md). That function specifies the filter function referred to in the description of the `refCon` parameter.  

##### Version-Notes

Starting with version 2.5, you should use the function [CMIterateColorSyncFolder](./api-1804904-cmiteratecolorsyncfolder.md) for profile searching.

This function is not recommended for use in ColorSync 2.5.

## Parameters

- `search`: A reference to a search result list returned to your application when you called the `CMNewProfileSearch` function. For a description of the `CMProfileSearchRef` private data type, see `CMProfileSearchRef`. See the QuickDraw Reference for a description of the PixMap data type.
- `refCon`: A pointer to a reference constant for application data passed as a parameter to calls to the filter function specified by the original search specification. For a description of the filter function, see the function `CMProfileFilterProcPtr`. 
- `count`: A pointer to a profile count. On return, if the function result is `noErr`, a one-based count of the number of profiles matching the original search specification passed to the `CMNewProfileSearch` function. Otherwise undefined. 

## See Also

### Not Recommended
- [CMNewProfileSearch](./api-1805344-cmnewprofilesearch.md)
  Searches the ColorSync Profiles folder and returns a list of 2.x profiles that match the search specification.
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

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805356-cmupdateprofilesearch)*