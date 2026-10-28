# CMIterateColorSyncFolder

**Framework**: Application Services  
**Kind**: func

Iterates over the available profiles.

## Declaration

```c
CMError CMIterateColorSyncFolder (
   CMProfileIterateUPP proc,
   UInt32 *seed,
   UInt32 *count,
   void *refCon
);
```

## Return Value

A `CMError` value. See [Result Codes](../colorsync_manager.md#1670295).

## Overview

Starting with ColorSync version 2.5, when your application needs information about the profiles currently available in the ColorSync Profiles folder, it can call the `CMIterateColorSyncFolder` routine, which in turn calls your callback routine once for each profile.

Even though there may be many profiles available, `CMIterateColorSyncFolder` can take advantage of ColorSync’s profile cache to return profile information quickly, and (if the cache is valid) without having to open any profiles. For each profile, `CMIterateColorSyncFolder` supplies your routine with the profile header, script code, name, and location, in a structure of type [`CMProfileIterateData`](../cmprofileiteratedata.md). As a result, your routine may be able to perform its function, such as building a list of profiles to display in a pop-up menu, without further effort (such as opening each file-based profile).

Only 2.x profiles are included in the profile search result. 

Before calling `CMIterateColorSyncFolder` for the first time, you typically set `seed` to 0. ColorSync compares 0 to its current seed for the profile cache. It is not likely they will match—the odds are roughly one in two billion against it. If the values do not match, the routine iterates through all the profiles in the cache, calling your callback routine once for each profile. `CMIterateColorSyncFolder` then returns the actual seed value in `seed `  (unless you passed `NULL` for that parameter).

If you pass the returned seed value in a subsequent call, and if there has been no change in the available profiles, the passed seed will match the stored cache seed and no iteration will take place.

Note that you can pass a `NULL` pointer for the `seed` parameter without harm. The result is the same as if you passed a pointer to 0, in that the function iterates through the available profiles, calling your callback routine once for each profile. However, the function does not return a seed value, since you have not passed a valid pointer.

You can force ColorSync to call your callback routine (if any profiles are available) by passing a `NULL` pointer or by passing 0 for the seed value. But suppose you have an operation, such as building a pop-up menu, that you only want to perform if the available profiles have changed. In that case, you pass the seed value from a previous call to `CMIterateColorSyncFolder`. If the profile folder has not changed, ColorSync will not call your callback routine.

Note that if there are no profiles available, ColorSync does not call your callback routine.

You can safely pass `NULL` for any or all of the parameters to the `CMIterateColorSyncFolder` function. If you pass `NULL` for all of the parameters, calling the function merely forces rebuilding of the profile cache, if necessary. 

### Version-Notes

Starting with version 2.5, the name and location of the profile folder changed. In addition, the folder can now contain profiles within nested folders, as well as aliases to profiles or aliases to folders containing profiles. There are limits on the nesting of folders and aliases.

## Parameters

- `proc`: A universal procedure pointer of type `CMProfileIterateUPP`, which is described in [`CMProfileIterateData`](../cmprofileiteratedata.md). If you do not wish to receive callbacks, pass `NULL` for this parameter. Otherwise, pass a pointer to your callback routine. 
- `seed`: A pointer to a value of type `long`. The first time you call `CMIterateColorSyncFolder`, you typically set the value to 0. In subsequent calls, you set the value to the seed value obtained from the previous call. ColorSync uses the value in determining whether to call your callback routine, as described in the discussion for this function.

  On return, the value is the current seed for the profile cache (unless you pass `NULL`, as described in the discussion).
- `count`: A pointer to a value of type `long`. On return, the value is the number of available profiles. `CMIterateColorSyncFolder` provides the number of profiles even when no iteration occurs (unless you pass `NULL`, as described in the discussion below). To determine the count alone, without iteration, call `CMIterateColorSyncFolder` and pass a value of `NULL` for all parameters except `count`.
- `refCon`: An untyped pointer to arbitrary data supplied by your application. `CMIterateColorSyncFolder` passes this data to your callback routine. If you pass `NULL` for the `refCon` parameter, `CMIterateColorSyncFolder` passes `NULL` to your callback routine. 

## See Also

### Iterating Installed Profiles
- [CMGetColorSyncFolderSpec](./api-1804907-cmgetcolorsyncfolderspec.md)
  Obtains the volume reference number and the directory ID for a ColorSync Profiles folder.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1804904-cmiteratecolorsyncfolder)*