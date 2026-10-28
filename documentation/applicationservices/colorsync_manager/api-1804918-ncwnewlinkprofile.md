# NCWNewLinkProfile

**Framework**: Application Services  
**Kind**: func

Obtains a profile reference for the specified by the profile location.

## Declaration

```c
CMError NCWNewLinkProfile (
   CMProfileRef *prof,
   const CMProfileLocation *targetLocation,
   NCMConcatProfileSet *profileSet,
   CMConcatCallBackUPP proc,
   void *refCon
);
```

## Return Value

A `CMError` value. See [Result Codes](../colorsync_manager.md#1670295).

## Overview

The same new flexibility in creating color worlds is extended to link profiles, which are not assumed to go from input device color space to output device color space. The returned profile is open, and should be closed when you are finished with it. 

## Parameters

- `prof`: The returned profile reference. 
- `targetLocation`: The location of the profile. Commonly a profile is disk-file based. However, the profile may be a file-based profile, a handle-based profile, or a pointer-based profile. 
- `profileSet`: A pointer to the profile set structure. 
- `proc`: A calling-program-supplied callback function that allows your application to monitor progress or abort the operation. 
- `refCon`: A reference constant containing data specified by the calling application program. 

## See Also

### Creating Profiles
- [CMNewProfile](./api-1804911-cmnewprofile.md)
  Creates a new profile and associated backing copy.
- [CWNewLinkProfile](./api-1804915-cwnewlinkprofile.md)
  Creates a device link profile based on the specified set of profiles.
- [CMMakeProfile](./api-1804920-cmmakeprofile.md)
  Makes a display or abstract profile by modifying an existing one.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1804918-ncwnewlinkprofile)*