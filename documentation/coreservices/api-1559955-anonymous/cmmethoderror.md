# cmMethodError

**Framework**: Core Services  
**Kind**: econst  
**Role**: Enumeration Case

An error occurred during the CMM arbitration process that determines the CMM to use

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```c
cmMethodError = -171
```

## See Also

### Result Codes
- [cmProfileError](./cmprofileerror.md)
  There is something wrong with the content of the profile
- [cmMethodNotFound](./cmmethodnotfound.md)
  CMM not present
- [cmProfileNotFound](./cmprofilenotfound.md)
  Responder error
- [cmProfilesIdentical](./cmprofilesidentical.md)
  Profiles are the same
- [cmCantConcatenateError](./cmcantconcatenateerror.md)
  Profiles cannot be concatenated
- [cmCantXYZ](./cmcantxyz.md)
  CMM does not handle XYZ color space
- [cmCantDeleteProfile](./cmcantdeleteprofile.md)
  Responder error
- [cmUnsupportedDataType](./cmunsupporteddatatype.md)
  Responder error
- [cmNoCurrentProfile](./cmnocurrentprofile.md)
  Responder error
- [cmElementTagNotFound](../api-1559968-anonymous/cmelementtagnotfound.md)
  The tag you specified is not in the specified profile
- [cmIndexRangeErr](../api-1559968-anonymous/cmindexrangeerr.md)
  Tag index out of range
- [cmCantDeleteElement](../api-1559968-anonymous/cmcantdeleteelement.md)
  Cannot delete the specified profile element
- [cmFatalProfileErr](../api-1559968-anonymous/cmfatalprofileerr.md)
  Returned from File Manager while updating a profile file in response to `CMUpdateProfile`; profile content may be corrupted
- [cmInvalidProfile](../api-1559968-anonymous/cminvalidprofile.md)
  Profile reference is invalid or refers to an inappropriate profile
- [cmInvalidProfileLocation](../api-1559968-anonymous/cminvalidprofilelocation.md)
  Operation not supported for this profile location
- [cmInvalidSearch](../api-1559968-anonymous/cminvalidsearch.md)
  Bad search handle
- [cmSearchError](../api-1559968-anonymous/cmsearcherror.md)
  Internal error occurred during profile search
- [cmErrIncompatibleProfile](../api-1559968-anonymous/cmerrincompatibleprofile.md)
  Unspecified profile error
- [cmInvalidColorSpace](../api-1559968-anonymous/cminvalidcolorspace.md)
  Profile color space does not match bitmap type
- [cmInvalidSrcMap](../api-1559968-anonymous/cminvalidsrcmap.md)
  Source pixel map or bitmap was invalid
- [cmInvalidDstMap](../api-1559968-anonymous/cminvaliddstmap.md)
  Destination pix/bit map was invalid
- [cmNoGDevicesError](../api-1559968-anonymous/cmnogdeviceserror.md)
  Begin matching or end matching—no graphics devices available
- [cmInvalidProfileComment](../api-1559968-anonymous/cminvalidprofilecomment.md)
  Bad profile comment during `drawpicture`
- [cmRangeOverFlow](../api-1559968-anonymous/cmrangeoverflow.md)
  One or more output color value overflows in color conversion; all input color values will be converted and the overflow will be clipped
- [cmCantCopyModifiedV1Profile](../api-1559968-anonymous/cmcantcopymodifiedv1profile.md)
  It is illegal to copy version 1.0 profiles that have been modified
- [cmNamedColorNotFound](../api-1559968-anonymous/cmnamedcolornotfound.md)
  The specified named color was not found in the specified profile
- [cmCantGamutCheckError](../api-1559968-anonymous/cmcantgamutcheckerror.md)
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

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1559955-anonymous/cmmethoderror)*