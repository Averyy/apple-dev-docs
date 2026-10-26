# CMNewProfile

**Framework**: Application Services  
**Kind**: func

Creates a new profile and associated backing copy.

## Declaration

```c
CMError CMNewProfile (
   CMProfileRef *prof,
   const CMProfileLocation *theProfile
);
```

#### Return Value

A `CMError` value. See [Result Codes](../colorsync_manager.md#1670295).

#### Overview

The `CMNewProfile` function creates a new profile and backing copy in the location you specify. After you create the profile, you must fill in the profile header fields and populate the profile with tags and their element data, and then call the function [CMUpdateProfile](./api-1804864-cmupdateprofile.md) to save the element data to the profile file. The default ColorSync profile contents include a profile header of type [`CM2Header`](../cm2header.md) and an element table.

To set profile elements outside the header, you use the function [CMSetProfileElement](./api-1804977-cmsetprofileelement.md), the function [CMSetProfileElementSize](./api-1804980-cmsetprofileelementsize.md), and the function [CMSetPartialProfileElement](./api-1804989-cmsetpartialprofileelement.md). You set these elements individually, identifying them by their tag names.

When you create a new profile, all fields of the `CM2Header` profile header are set to 0 except the `size` and `profileVersion` fields. To set the header elements, you call the function [CMGetProfileHeader](./api-1804879-cmgetprofileheader.md) to get a copy of the header, assign values to the header fields, then call the function [CMSetProfileHeader](./api-1804882-cmsetprofileheader.md) to write the new header to the profile.

For each profile class, such as a device profile, there is a specific set of elements and associated tags, defined by the ICC, that a profile must contain to meet the baseline requirements. The ICC also defines optional tags that a particular CMM might use to optimize or improve its processing. You can also define private tags, whose tag signatures you register with the ICC, to provide a CMM with greater capability to refine its processing.

After you fill in the profile with tags and their element data, you must call the `CMUpdateProfile` function to write the new profile elements to the profile file.

This function is most commonly used by profile developers who create profiles for device manufacturers and by calibration applications. In most cases, application developers use existing profiles. 

## Parameters

- `prof`: A pointer to a profile reference of type [`CMProfileRef`](../cmprofileref.md). On return, a reference to the new profile. 
- `theProfile`: A pointer of type [`CMProfileLocation`](../cmprofilelocation.md) to the profile location where the new profile should be created. A profile is commonly disk-file based—the disk file type for a profile is `'prof'`. However, to accommodate special requirements, you can create a handle- or pointer-based profile, you can create a temporary profile that is not saved after you call the `CMCloseProfile` function, or you can create a profile that is accessed through a procedure provided by your application. To create a temporary profile, you either specify `cmNoProfileBase` as the kind of profile in the profile location structure or specify `NULL` for this parameter. 

## See Also

### Creating Profiles
- [CWNewLinkProfile](./api-1804915-cwnewlinkprofile.md)
  Creates a device link profile based on the specified set of profiles.
- [NCWNewLinkProfile](./api-1804918-ncwnewlinkprofile.md)
  Obtains a profile reference for the specified by the profile location.
- [CMMakeProfile](./api-1804920-cmmakeprofile.md)
  Makes a display or abstract profile by modifying an existing one.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1804911-cmnewprofile)*