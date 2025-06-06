# cmIndexRangeErr

**Framework**: Core Services  
**Kind**: data

Tag index out of range

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
var cmIndexRangeErr: Int { get }
```

## See Also

- [var cmProfileError: Int](cmprofileerror.md)
  There is something wrong with the content of the profile
- [var cmMethodError: Int](cmmethoderror.md)
  An error occurred during the CMM arbitration process that determines the CMM to use
- [var cmMethodNotFound: Int](cmmethodnotfound.md)
  CMM not present
- [var cmProfileNotFound: Int](cmprofilenotfound.md)
  Responder error
- [var cmProfilesIdentical: Int](cmprofilesidentical.md)
  Profiles are the same
- [var cmCantConcatenateError: Int](cmcantconcatenateerror.md)
  Profiles cannot be concatenated
- [var cmCantXYZ: Int](cmcantxyz.md)
  CMM does not handle XYZ color space
- [var cmCantDeleteProfile: Int](cmcantdeleteprofile.md)
  Responder error
- [var cmUnsupportedDataType: Int](cmunsupporteddatatype.md)
  Responder error
- [var cmNoCurrentProfile: Int](cmnocurrentprofile.md)
  Responder error
- [var cmElementTagNotFound: Int](cmelementtagnotfound.md)
  The tag you specified is not in the specified profile
- [var cmCantDeleteElement: Int](cmcantdeleteelement.md)
  Cannot delete the specified profile element
- [var cmFatalProfileErr: Int](cmfatalprofileerr.md)
  Returned from File Manager while updating a profile file in response to `CMUpdateProfile`; profile content may be corrupted
- [var cmInvalidProfile: Int](cminvalidprofile.md)
  Profile reference is invalid or refers to an inappropriate profile
- [var cmInvalidProfileLocation: Int](cminvalidprofilelocation.md)
  Operation not supported for this profile location
- [var cmInvalidSearch: Int](cminvalidsearch.md)
  Bad search handle
- [var cmSearchError: Int](cmsearcherror.md)
  Internal error occurred during profile search
- [var cmErrIncompatibleProfile: Int](cmerrincompatibleprofile.md)
  Unspecified profile error
- [var cmInvalidColorSpace: Int](cminvalidcolorspace.md)
  Profile color space does not match bitmap type
- [var cmInvalidSrcMap: Int](cminvalidsrcmap.md)
  Source pixel map or bitmap was invalid
- [var cmInvalidDstMap: Int](cminvaliddstmap.md)
  Destination pix/bit map was invalid
- [var cmNoGDevicesError: Int](cmnogdeviceserror.md)
  Begin matching or end matching—no graphics devices available
- [var cmInvalidProfileComment: Int](cminvalidprofilecomment.md)
  Bad profile comment during `drawpicture`
- [var cmRangeOverFlow: Int](cmrangeoverflow.md)
  One or more output color value overflows in color conversion; all input color values will be converted and the overflow will be clipped
- [var cmCantCopyModifiedV1Profile: Int](cmcantcopymodifiedv1profile.md)
  It is illegal to copy version 1.0 profiles that have been modified
- [var cmNamedColorNotFound: Int](cmnamedcolornotfound.md)
  The specified named color was not found in the specified profile
- [var cmCantGamutCheckError: Int](cmcantgamutcheckerror.md)
  Gamut checking not supported by this color world—that is, the color world does not contain a gamut table because it was built with gamut checking turned off
- [var cmDeviceDBNotFoundErr: Int](../applicationservices/cmdevicedbnotfounderr.md)
  Preferences not found or loaded; returned by a CM device integration routine.
- [var cmDeviceAlreadyRegistered: Int](../applicationservices/cmdevicealreadyregistered.md)
  Device already registered; returned by a CM device integration routine.
- [var cmDeviceNotRegistered: Int](../applicationservices/cmdevicenotregistered.md)
  Device not found; returned by a CM device integration routine.
- [var cmDeviceProfilesNotFound: Int](../applicationservices/cmdeviceprofilesnotfound.md)
  Profiles not found; returned by a CM device integration routine.
- [var cmInternalCFErr: Int](../applicationservices/cminternalcferr.md)
  CoreFoundation failure; returned by a CM device integration routine.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/cmindexrangeerr)*