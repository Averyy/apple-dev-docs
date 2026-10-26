# cmNamedColorNotFound

**Framework**: Core Services  
**Kind**: econst  
**Role**: Enumeration Case

The specified named color was not found in the specified profile

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```c
cmNamedColorNotFound = -4216
```

## See Also

### Result Codes
- [cmProfileError](../api-1559955-anonymous/cmprofileerror.md)
  There is something wrong with the content of the profile
- [cmMethodError](../api-1559955-anonymous/cmmethoderror.md)
  An error occurred during the CMM arbitration process that determines the CMM to use
- [cmMethodNotFound](../api-1559955-anonymous/cmmethodnotfound.md)
  CMM not present
- [cmProfileNotFound](../api-1559955-anonymous/cmprofilenotfound.md)
  Responder error
- [cmProfilesIdentical](../api-1559955-anonymous/cmprofilesidentical.md)
  Profiles are the same
- [cmCantConcatenateError](../api-1559955-anonymous/cmcantconcatenateerror.md)
  Profiles cannot be concatenated
- [cmCantXYZ](../api-1559955-anonymous/cmcantxyz.md)
  CMM does not handle XYZ color space
- [cmCantDeleteProfile](../api-1559955-anonymous/cmcantdeleteprofile.md)
  Responder error
- [cmUnsupportedDataType](../api-1559955-anonymous/cmunsupporteddatatype.md)
  Responder error
- [cmNoCurrentProfile](../api-1559955-anonymous/cmnocurrentprofile.md)
  Responder error
- [cmElementTagNotFound](./cmelementtagnotfound.md)
  The tag you specified is not in the specified profile
- [cmIndexRangeErr](./cmindexrangeerr.md)
  Tag index out of range
- [cmCantDeleteElement](./cmcantdeleteelement.md)
  Cannot delete the specified profile element
- [cmFatalProfileErr](./cmfatalprofileerr.md)
  Returned from File Manager while updating a profile file in response to `CMUpdateProfile`; profile content may be corrupted
- [cmInvalidProfile](./cminvalidprofile.md)
  Profile reference is invalid or refers to an inappropriate profile
- [cmInvalidProfileLocation](./cminvalidprofilelocation.md)
  Operation not supported for this profile location
- [cmInvalidSearch](./cminvalidsearch.md)
  Bad search handle
- [cmSearchError](./cmsearcherror.md)
  Internal error occurred during profile search
- [cmErrIncompatibleProfile](./cmerrincompatibleprofile.md)
  Unspecified profile error
- [cmInvalidColorSpace](./cminvalidcolorspace.md)
  Profile color space does not match bitmap type
- [cmInvalidSrcMap](./cminvalidsrcmap.md)
  Source pixel map or bitmap was invalid
- [cmInvalidDstMap](./cminvaliddstmap.md)
  Destination pix/bit map was invalid
- [cmNoGDevicesError](./cmnogdeviceserror.md)
  Begin matching or end matching—no graphics devices available
- [cmInvalidProfileComment](./cminvalidprofilecomment.md)
  Bad profile comment during `drawpicture`
- [cmRangeOverFlow](./cmrangeoverflow.md)
  One or more output color value overflows in color conversion; all input color values will be converted and the overflow will be clipped
- [cmCantCopyModifiedV1Profile](./cmcantcopymodifiedv1profile.md)
  It is illegal to copy version 1.0 profiles that have been modified
- [cmCantGamutCheckError](./cmcantgamutcheckerror.md)
  Gamut checking not supported by this color world—that is, the color world does not contain a gamut table because it was built with gamut checking turned off
- [cmDeviceDBNotFoundErr](../../applicationservices/api-1560507-anonymous/cmdevicedbnotfounderr.md)
  Preferences not found or loaded; returned by a CM device integration routine.
- [cmDeviceAlreadyRegistered](../../applicationservices/api-1560507-anonymous/cmdevicealreadyregistered.md)
  Device already registered; returned by a CM device integration routine.
- [cmDeviceNotRegistered](../../applicationservices/api-1560507-anonymous/cmdevicenotregistered.md)
  Device not found; returned by a CM device integration routine.
- [cmDeviceProfilesNotFound](../../applicationservices/api-1560507-anonymous/cmdeviceprofilesnotfound.md)
  Profiles not found; returned by a CM device integration routine.
- [cmInternalCFErr](../../applicationservices/api-1560507-anonymous/cminternalcferr.md)
  CoreFoundation failure; returned by a CM device integration routine.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1559968-anonymous/cmnamedcolornotfound)*