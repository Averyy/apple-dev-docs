# ColorSync Manager

**Framework**: Application Services

#### Overview

The ColorSync Manager is the API for ColorSync, a platform-independent color management system from Apple. ColorSync provides essential services for fast, consistent, and accurate color calibration, proofing, and reproduction using input, output, and display devices. ColorSync also provides an interface to system-wide color management settings that allows users to save color settings for specific jobs and switch between settings.

You need this reference if your software product performs color drawing, printing, or calculation, or if your peripheral device supports color. You also need this reference if you are creating a color management module (CMM)—a component that implements color-matching, color-conversion, and gamut-checking services.

The Color Picker Manager, documented separately, provides a standard user interface for soliciting color choices.

Carbon supports the majority of the ColorSync Manager programming interface. However, ColorSync 1.0 compatibility calls such as `CWNewColorWorld`, `GetProfile`, and `SetProfile` are not supported.

Nor does Carbon support ColorSync functions used for color management modules (CMMs). These functions aren't supported because macOS uses Bundle Services to implement CMMs. 

Some applications use the Component Manager to determine what CMMs are available. You cannot use the Component Manager for this purpose in macOS. Apple has, however, provided the function `CMIterateCMMInfo` to query for available CMMs. 

## Topics

### Working With Universal Procedure Pointers
- [NewCMBitmapCallBackUPP](colorsync_manager/1805297-newcmbitmapcallbackupp.md)
  Creates a new universal procedure pointer (UPP) to a bitmap callback.
- [DisposeCMBitmapCallBackUPP](colorsync_manager/1805300-disposecmbitmapcallbackupp.md)
  Disposes of a universal procedure pointer (UPP) to a bitmap callback.
- [InvokeCMBitmapCallBackUPP](colorsync_manager/1805303-invokecmbitmapcallbackupp.md)
  Invokes a universal procedure pointer (UPP) to a bitmap callback.
- [NewCMConcatCallBackUPP](colorsync_manager/1805306-newcmconcatcallbackupp.md)
  Creates a new universal procedure pointer (UPP) to a progress-monitoring callback.
- [DisposeCMConcatCallBackUPP](colorsync_manager/1805310-disposecmconcatcallbackupp.md)
  Disposes of a universal procedure pointer (UPP) to a progress-monitoring callback.
- [InvokeCMConcatCallBackUPP](colorsync_manager/1805312-invokecmconcatcallbackupp.md)
  Invokes a universal procedure pointer (UPP) to a progress-monitoring callback.
- [NewCMFlattenUPP](colorsync_manager/1805315-newcmflattenupp.md)
  Creates a new universal procedure pointer (UPP) to a data-flattening callback.
- [DisposeCMFlattenUPP](colorsync_manager/1805318-disposecmflattenupp.md)
  Disposes of a universal procedure pointer (UPP) to a data-flattening callback.
- [InvokeCMFlattenUPP](colorsync_manager/1805320-invokecmflattenupp.md)
  Invokes a universal procedure pointer (UPP) to a data-flattening callback.
- [NewCMMIterateUPP](colorsync_manager/1805322-newcmmiterateupp.md)
  Creates a new universal procedure pointer (UPP) to a progress-monitoring callback for the `CMIterateCMMInfo` function.
- [DisposeCMMIterateUPP](colorsync_manager/1805323-disposecmmiterateupp.md)
  Disposes of a universal procedure pointer (UPP) to a progress-monitoring callback for the `CMIterateCMMInfo` function.
- [InvokeCMMIterateUPP](colorsync_manager/1805325-invokecmmiterateupp.md)
  Invokes a universal procedure pointer (UPP) to a progress-monitoring callback for the [`CMIterateCMMInfo`](colorsync_manager/1805185-cmiteratecmminfo.md) function.
- [NewCMProfileIterateUPP](colorsync_manager/1805339-newcmprofileiterateupp.md)
  Creates a new universal procedure pointer (UPP) to a profile-iteration callback.
- [DisposeCMProfileIterateUPP](colorsync_manager/1805341-disposecmprofileiterateupp.md)
  Disposes of a universal procedure pointer (UPP) to a profile-iteration callback.
- [InvokeCMProfileIterateUPP](colorsync_manager/1805343-invokecmprofileiterateupp.md)
  Invokes a universal procedure pointer (UPP) to a profile-iteration callback.
### Callbacks
- [typealias CMFlattenProcPtr](cmflattenprocptr.md)
  Defines a pointer to a data transfer callback function that transfers profile data from the format for embedded profiles to disk file format or vice versa.
### Data Types
- [struct CM2Profile](cm2profile.md)
- [struct CMDeviceInfo](cmdeviceinfo.md)
- [struct CMDeviceProfileArray](cmdeviceprofilearray.md)
- [struct CMDeviceScope](cmdevicescope.md)
- [struct CMError](../coremotion/cmerror.md)
  Defines motion errors.
- [typealias CMFlattenUPP](cmflattenupp.md)
  Defines a universal procedure pointer to a data-flattening callback.
- [typealias CMMultiFunctLutA2BType](cmmultifunctluta2btype.md)
- [struct CMMultiFunctLutType](cmmultifunctluttype.md)
- [struct CMXYZColor](cmxyzcolor.md)
  Contains values for a color specified in XYZ color space.
- [typealias CMXYZComponent](cmxyzcomponent.md)
### Constants
- [Abstract Color Space Constants](colorsync_manager/1560701-abstract_color_space_constants.md)
  Specify values that represent general color spaces.
- [Channel Encoding Format](colorsync_manager/1560324-channel_encoding_format.md)
  Specify an encoding format for sRGB64.
- [Color Packing for Color Spaces](colorsync_manager/1560270-color_packing_for_color_spaces.md)
  Specify how color values are stored.
- [Color Space Signatures](colorsync_manager/1560276-color_space_signatures.md)
  Define four-character-sequences associated with color spaces.
- [Color Space Masks](colorsync_manager/1560521-color_space_masks.md)
  Specify masks used for color spaces.
- [Current Device Versions](colorsync_manager/1560472-current_device_versions.md)
  Specify the current versions of the data structure containing information on registered devices.
- [Current Info Versions](colorsync_manager/1560146-current_info_versions.md)
  Specify current device and profile versions.
- [Current Major Version Mask](colorsync_manager/1560659-current_major_version_mask.md)
  Specifies the current major version number.
- [Data Transfer Commands](colorsync_manager/1560166-data_transfer_commands.md)
  Specify commands for caller-supplied ColorSync data transfer functions.
- [Data Type Element Values](colorsync_manager/1560593-data_type_element_values.md)
  Specify a data type.
- [Default CMM Signature](colorsync_manager/1560689-default_cmm_signature.md)
  Specifies a signature for the default color management module supplied by Color Sync.
- [Default IDs](colorsync_manager/1560386-default_ids.md)
  Specify default values for device and profile IDs.
- [Device Attribute Values for Version 2.x Profiles](colorsync_manager/1560447-device_attribute_values_for_vers.md)
  Define masks your application can use to set or test bits in the `deviceAttributes `field of the `CM2Header` structure.
- [typealias CMDeviceClass](cmdeviceclass.md)
  Define constants to represent a variety of input and output devices.
- [Device and Media Attributes](colorsync_manager/1560327-device_and_media_attributes.md)
  Used to set or obtain device or media attributes.
- [Device States](colorsync_manager/1560516-device_states.md)
  Specify device states.
- [Element Tags and Signatures for Version 1.0 Profiles](colorsync_manager/1560273-element_tags_and_signatures_for_.md)
  Define tags and signatures used for version 1.0 profiles.
- [Embedded Profile Flags](colorsync_manager/1560148-embedded_profile_flags.md)
  Specify copyright-protection flag options,
- [Flag Mask Definitions for Version 2.x Profiles](colorsync_manager/1560699-flag_mask_definitions_for_versio.md)
  Define masks your application can use to set or test various bits in the `flags` field of the `CM2Header` structure.
- [ICC Profile Versions](colorsync_manager/1560658-icc_profile_versions.md)
  Specify IDD profile version numbers.
- [Illuminant Measurement Endocings](colorsync_manager/1560108-illuminant_measurement_endocings.md)
  Specify standard illuminate measurement encodings.
- [Magic Cookie Number](colorsync_manager/1560690-magic_cookie_number.md)
  Specifies a magic cookie number for anonymous file ID.
- [Maximum Path Size](colorsync_manager/1560101-maximum_path_size.md)
  Specifies the maximum length for a path name.
- [Measurement Flares](colorsync_manager/1560283-measurement_flares.md)
  Specify measurement flare encodings.
- [Measurement Geometries](colorsync_manager/1560539-measurement_geometries.md)
  Specify measurement geometry encodings.
- [Parametric Types](colorsync_manager/1560541-parametric_types.md)
  Specify a parametric curve type enumeration,
- [Platform Enumeration Values](colorsync_manager/1560191-platform_enumeration_values.md)
  Specify computer platforms.
- [Profile Iteration Values](colorsync_manager/1560091-profile_iteration_values.md)
  Specify profiles to iterate.
- [Profile Location Sizes](colorsync_manager/1560369-profile_location_sizes.md)
  Specify a location size.
- [PostScript Data Formats](colorsync_manager/1560551-postscript_data_formats.md)
  Specify constants that indicate the format of PostScript data.
- [Profile Access Procedures](colorsync_manager/1560733-profile_access_procedures.md)
  Specify operations used to access profiles.
- [Profile Classes](colorsync_manager/1560630-profile_classes.md)
  Specify profile class enumerations.
- [Profile Concatenation Values](colorsync_manager/1560373-profile_concatenation_values.md)
  Specify values to use when concatenating profiles.
- [Profile Iteration Constants](colorsync_manager/1560189-profile_iteration_constants.md)
  Define an iteration version.
- [Profile Location Type](colorsync_manager/1560599-profile_location_type.md)
  Defines profile location kinds.
- [Public Tags](colorsync_manager/1560717-public_tags.md)
  Specify tag values available for public use.
- [Public Type Signatures](colorsync_manager/1560346-public_type_signatures.md)
  Specify signatures for public types.
- [Quality Flag Values for Version 2.x Profiles](colorsync_manager/1560115-quality_flag_values_for_version_.md)
  Define the possible values for the quality bits in the `flags` field of the `CM2Header` structure. 
- [Rendering Intent Values for Version 2.x Profiles](colorsync_manager/1560278-rendering_intent_values_for_vers.md)
  Define the four possible values for the rendering intent bits of the `renderingIntent` field of the `CM2Header` structure. 
- [Screen Encoding Tags](colorsync_manager/1560247-screen_encoding_tags.md)
  Specify tags to use for screen encodings.
- [Spot Function Values](colorsync_manager/1560411-spot_function_values.md)
  Specify values for spot functions.
- [Standard Observer](colorsync_manager/1560388-standard_observer.md)
  Standard observer measurement type encodings.
- [Tag Type Information](colorsync_manager/1560086-tag_type_information.md)
  Defines a constant for 2.0 tag type information.
- [Technology Tag Descriptions](colorsync_manager/1560433-technology_tag_descriptions.md)
  Define descriptor tags for technologies.
- [Use Types](colorsync_manager/1560730-use_types.md)
  Specify use types.
- [Video Card Gamma Storage Types](colorsync_manager/1560344-video_card_gamma_storage_types.md)
  Specify data storage type constants.
- [Video Card Gamma Tags](colorsync_manager/1560164-video_card_gamma_tags.md)
  Specify video card gamma information.
- [Video Card Gamma Signatures](colorsync_manager/1560275-video_card_gamma_signatures.md)
  Specify signatures used for video card gamma information.
### Result Codes
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
- [var cmDeviceDBNotFoundErr: Int](cmdevicedbnotfounderr.md)
  Preferences not found or loaded; returned by a CM device integration routine.
- [var cmDeviceAlreadyRegistered: Int](cmdevicealreadyregistered.md)
  Device already registered; returned by a CM device integration routine.
- [var cmDeviceNotRegistered: Int](cmdevicenotregistered.md)
  Device not found; returned by a CM device integration routine.
- [var cmDeviceProfilesNotFound: Int](cmdeviceprofilesnotfound.md)
  Profiles not found; returned by a CM device integration routine.
- [var cmInternalCFErr: Int](cminternalcferr.md)
  CoreFoundation failure; returned by a CM device integration routine.

## See Also

- [Apple Event Manager](apple_event_manager.md)
- [Speech Synthesis Manager](speech_synthesis_manager.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/colorsync_manager)*