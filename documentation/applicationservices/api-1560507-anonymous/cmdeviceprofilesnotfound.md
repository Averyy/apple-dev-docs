# cmDeviceProfilesNotFound

**Framework**: Application Services  
**Kind**: econst  
**Role**: Enumeration Case

Profiles not found; returned by a CM device integration routine.

**Availability**:
- macOS 10.0+

## Declaration

```c
cmDeviceProfilesNotFound = -4230
```

## See Also

### Result Codes
- [cmProfileError](../../coreservices/api-1559955-anonymous/cmprofileerror.md)
  There is something wrong with the content of the profile
- [cmMethodError](../../coreservices/api-1559955-anonymous/cmmethoderror.md)
  An error occurred during the CMM arbitration process that determines the CMM to use
- [cmMethodNotFound](../../coreservices/api-1559955-anonymous/cmmethodnotfound.md)
  CMM not present
- [cmProfileNotFound](../../coreservices/api-1559955-anonymous/cmprofilenotfound.md)
  Responder error
- [cmProfilesIdentical](../../coreservices/api-1559955-anonymous/cmprofilesidentical.md)
  Profiles are the same
- [cmCantConcatenateError](../../coreservices/api-1559955-anonymous/cmcantconcatenateerror.md)
  Profiles cannot be concatenated
- [cmCantXYZ](../../coreservices/api-1559955-anonymous/cmcantxyz.md)
  CMM does not handle XYZ color space
- [cmCantDeleteProfile](../../coreservices/api-1559955-anonymous/cmcantdeleteprofile.md)
  Responder error
- [cmUnsupportedDataType](../../coreservices/api-1559955-anonymous/cmunsupporteddatatype.md)
  Responder error
- [cmNoCurrentProfile](../../coreservices/api-1559955-anonymous/cmnocurrentprofile.md)
  Responder error
- [cmElementTagNotFound](../../coreservices/api-1559968-anonymous/cmelementtagnotfound.md)
  The tag you specified is not in the specified profile
- [cmIndexRangeErr](../../coreservices/api-1559968-anonymous/cmindexrangeerr.md)
  Tag index out of range
- [cmCantDeleteElement](../../coreservices/api-1559968-anonymous/cmcantdeleteelement.md)
  Cannot delete the specified profile element
- [cmFatalProfileErr](../../coreservices/api-1559968-anonymous/cmfatalprofileerr.md)
  Returned from File Manager while updating a profile file in response to `CMUpdateProfile`; profile content may be corrupted
- [cmInvalidProfile](../../coreservices/api-1559968-anonymous/cminvalidprofile.md)
  Profile reference is invalid or refers to an inappropriate profile
- [cmInvalidProfileLocation](../../coreservices/api-1559968-anonymous/cminvalidprofilelocation.md)
  Operation not supported for this profile location
- [cmInvalidSearch](../../coreservices/api-1559968-anonymous/cminvalidsearch.md)
  Bad search handle
- [cmSearchError](../../coreservices/api-1559968-anonymous/cmsearcherror.md)
  Internal error occurred during profile search
- [cmErrIncompatibleProfile](../../coreservices/api-1559968-anonymous/cmerrincompatibleprofile.md)
  Unspecified profile error
- [cmInvalidColorSpace](../../coreservices/api-1559968-anonymous/cminvalidcolorspace.md)
  Profile color space does not match bitmap type
- [cmInvalidSrcMap](../../coreservices/api-1559968-anonymous/cminvalidsrcmap.md)
  Source pixel map or bitmap was invalid
- [cmInvalidDstMap](../../coreservices/api-1559968-anonymous/cminvaliddstmap.md)
  Destination pix/bit map was invalid
- [cmNoGDevicesError](../../coreservices/api-1559968-anonymous/cmnogdeviceserror.md)
  Begin matching or end matching—no graphics devices available
- [cmInvalidProfileComment](../../coreservices/api-1559968-anonymous/cminvalidprofilecomment.md)
  Bad profile comment during `drawpicture`
- [cmRangeOverFlow](../../coreservices/api-1559968-anonymous/cmrangeoverflow.md)
  One or more output color value overflows in color conversion; all input color values will be converted and the overflow will be clipped
- [cmCantCopyModifiedV1Profile](../../coreservices/api-1559968-anonymous/cmcantcopymodifiedv1profile.md)
  It is illegal to copy version 1.0 profiles that have been modified
- [cmNamedColorNotFound](../../coreservices/api-1559968-anonymous/cmnamedcolornotfound.md)
  The specified named color was not found in the specified profile
- [cmCantGamutCheckError](../../coreservices/api-1559968-anonymous/cmcantgamutcheckerror.md)
  Gamut checking not supported by this color world—that is, the color world does not contain a gamut table because it was built with gamut checking turned off
- [cmDeviceDBNotFoundErr](./cmdevicedbnotfounderr.md)
  Preferences not found or loaded; returned by a CM device integration routine.
- [cmDeviceAlreadyRegistered](./cmdevicealreadyregistered.md)
  Device already registered; returned by a CM device integration routine.
- [cmDeviceNotRegistered](./cmdevicenotregistered.md)
  Device not found; returned by a CM device integration routine.
- [cmInternalCFErr](./cminternalcferr.md)
  CoreFoundation failure; returned by a CM device integration routine.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/1560507-anonymous/cmdeviceprofilesnotfound)*