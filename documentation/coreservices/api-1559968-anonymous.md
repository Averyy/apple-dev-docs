# Anonymous

**Framework**: Core Services  
**Kind**: enum  
**Role**: Enumeration

**Availability**:
- Mac Catalyst 17.0+
- macOS 10.0+

## Declaration

```c
enum : int {
    ...
};
```

## Topics

### Constants
- [cmCantCopyModifiedV1Profile](./api-1559968-anonymous/cmcantcopymodifiedv1profile.md)
  It is illegal to copy version 1.0 profiles that have been modified
- [cmCantDeleteElement](./api-1559968-anonymous/cmcantdeleteelement.md)
  Cannot delete the specified profile element
- [cmCantGamutCheckError](./api-1559968-anonymous/cmcantgamutcheckerror.md)
  Gamut checking not supported by this color world—that is, the color world does not contain a gamut table because it was built with gamut checking turned off
- [cmElementTagNotFound](./api-1559968-anonymous/cmelementtagnotfound.md)
  The tag you specified is not in the specified profile
- [cmErrIncompatibleProfile](./api-1559968-anonymous/cmerrincompatibleprofile.md)
  Unspecified profile error
- [cmFatalProfileErr](./api-1559968-anonymous/cmfatalprofileerr.md)
  Returned from File Manager while updating a profile file in response to `CMUpdateProfile`; profile content may be corrupted
- [cmIndexRangeErr](./api-1559968-anonymous/cmindexrangeerr.md)
  Tag index out of range
- [cmInvalidColorSpace](./api-1559968-anonymous/cminvalidcolorspace.md)
  Profile color space does not match bitmap type
- [cmInvalidDstMap](./api-1559968-anonymous/cminvaliddstmap.md)
  Destination pix/bit map was invalid
- [cmInvalidProfile](./api-1559968-anonymous/cminvalidprofile.md)
  Profile reference is invalid or refers to an inappropriate profile
- [cmInvalidProfileComment](./api-1559968-anonymous/cminvalidprofilecomment.md)
  Bad profile comment during `drawpicture`
- [cmInvalidProfileLocation](./api-1559968-anonymous/cminvalidprofilelocation.md)
  Operation not supported for this profile location
- [cmInvalidSearch](./api-1559968-anonymous/cminvalidsearch.md)
  Bad search handle
- [cmInvalidSrcMap](./api-1559968-anonymous/cminvalidsrcmap.md)
  Source pixel map or bitmap was invalid
- [cmNamedColorNotFound](./api-1559968-anonymous/cmnamedcolornotfound.md)
  The specified named color was not found in the specified profile
- [cmNoGDevicesError](./api-1559968-anonymous/cmnogdeviceserror.md)
  Begin matching or end matching—no graphics devices available
- [cmRangeOverFlow](./api-1559968-anonymous/cmrangeoverflow.md)
  One or more output color value overflows in color conversion; all input color values will be converted and the overflow will be clipped
- [cmSearchError](./api-1559968-anonymous/cmsearcherror.md)
  Internal error occurred during profile search


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1559968-anonymous)*