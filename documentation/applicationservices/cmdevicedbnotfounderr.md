# cmDeviceDBNotFoundErr

**Framework**: Application Services  
**Kind**: data

Preferences not found or loaded; returned by a CM device integration routine.

**Availability**:
- macOS 10.0+

## Declaration

```swift
var cmDeviceDBNotFoundErr: Int { get }
```

## See Also

- [var cmProfileError: Int](../coreservices/cmprofileerror.md)
  There is something wrong with the content of the profile
- [var cmMethodError: Int](../coreservices/cmmethoderror.md)
  An error occurred during the CMM arbitration process that determines the CMM to use
- [var cmMethodNotFound: Int](../coreservices/cmmethodnotfound.md)
  CMM not present
- [var cmProfileNotFound: Int](../coreservices/cmprofilenotfound.md)
  Responder error
- [var cmProfilesIdentical: Int](../coreservices/cmprofilesidentical.md)
  Profiles are the same
- [var cmCantConcatenateError: Int](../coreservices/cmcantconcatenateerror.md)
  Profiles cannot be concatenated
- [var cmCantXYZ: Int](../coreservices/cmcantxyz.md)
  CMM does not handle XYZ color space
- [var cmCantDeleteProfile: Int](../coreservices/cmcantdeleteprofile.md)
  Responder error
- [var cmUnsupportedDataType: Int](../coreservices/cmunsupporteddatatype.md)
  Responder error
- [var cmNoCurrentProfile: Int](../coreservices/cmnocurrentprofile.md)
  Responder error
- [var cmElementTagNotFound: Int](../coreservices/cmelementtagnotfound.md)
  The tag you specified is not in the specified profile
- [var cmIndexRangeErr: Int](../coreservices/cmindexrangeerr.md)
  Tag index out of range
- [var cmCantDeleteElement: Int](../coreservices/cmcantdeleteelement.md)
  Cannot delete the specified profile element
- [var cmFatalProfileErr: Int](../coreservices/cmfatalprofileerr.md)
  Returned from File Manager while updating a profile file in response to `CMUpdateProfile`; profile content may be corrupted
- [var cmInvalidProfile: Int](../coreservices/cminvalidprofile.md)
  Profile reference is invalid or refers to an inappropriate profile
- [var cmInvalidProfileLocation: Int](../coreservices/cminvalidprofilelocation.md)
  Operation not supported for this profile location
- [var cmInvalidSearch: Int](../coreservices/cminvalidsearch.md)
  Bad search handle
- [var cmSearchError: Int](../coreservices/cmsearcherror.md)
  Internal error occurred during profile search
- [var cmErrIncompatibleProfile: Int](../coreservices/cmerrincompatibleprofile.md)
  Unspecified profile error
- [var cmInvalidColorSpace: Int](../coreservices/cminvalidcolorspace.md)
  Profile color space does not match bitmap type
- [var cmInvalidSrcMap: Int](../coreservices/cminvalidsrcmap.md)
  Source pixel map or bitmap was invalid
- [var cmInvalidDstMap: Int](../coreservices/cminvaliddstmap.md)
  Destination pix/bit map was invalid
- [var cmNoGDevicesError: Int](../coreservices/cmnogdeviceserror.md)
  Begin matching or end matching—no graphics devices available
- [var cmInvalidProfileComment: Int](../coreservices/cminvalidprofilecomment.md)
  Bad profile comment during `drawpicture`
- [var cmRangeOverFlow: Int](../coreservices/cmrangeoverflow.md)
  One or more output color value overflows in color conversion; all input color values will be converted and the overflow will be clipped
- [var cmCantCopyModifiedV1Profile: Int](../coreservices/cmcantcopymodifiedv1profile.md)
  It is illegal to copy version 1.0 profiles that have been modified
- [var cmNamedColorNotFound: Int](../coreservices/cmnamedcolornotfound.md)
  The specified named color was not found in the specified profile
- [var cmCantGamutCheckError: Int](../coreservices/cmcantgamutcheckerror.md)
  Gamut checking not supported by this color world—that is, the color world does not contain a gamut table because it was built with gamut checking turned off
- [var cmDeviceAlreadyRegistered: Int](cmdevicealreadyregistered.md)
  Device already registered; returned by a CM device integration routine.
- [var cmDeviceNotRegistered: Int](cmdevicenotregistered.md)
  Device not found; returned by a CM device integration routine.
- [var cmDeviceProfilesNotFound: Int](cmdeviceprofilesnotfound.md)
  Profiles not found; returned by a CM device integration routine.
- [var cmInternalCFErr: Int](cminternalcferr.md)
  CoreFoundation failure; returned by a CM device integration routine.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/cmdevicedbnotfounderr)*