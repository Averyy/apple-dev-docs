# ColorSync Manager

**Framework**: Application Services  
**Role**: API Collection

## Overview

The ColorSync Manager is the API for ColorSync, a platform-independent color management system from Apple. ColorSync provides essential services for fast, consistent, and accurate color calibration, proofing, and reproduction using input, output, and display devices. ColorSync also provides an interface to system-wide color management settings that allows users to save color settings for specific jobs and switch between settings.

You need this reference if your software product performs color drawing, printing, or calculation, or if your peripheral device supports color. You also need this reference if you are creating a color management module (CMM)—a component that implements color-matching, color-conversion, and gamut-checking services.

The Color Picker Manager, documented separately, provides a standard user interface for soliciting color choices.

Carbon supports the majority of the ColorSync Manager programming interface. However, ColorSync 1.0 compatibility calls such as `CWNewColorWorld`, `GetProfile`, and `SetProfile` are not supported.

Nor does Carbon support ColorSync functions used for color management modules (CMMs). These functions aren't supported because macOS uses Bundle Services to implement CMMs. 

Some applications use the Component Manager to determine what CMMs are available. You cannot use the Component Manager for this purpose in macOS. Apple has, however, provided the function `CMIterateCMMInfo` to query for available CMMs. 

## Topics

### Working With Universal Procedure Pointers
- [NewCMBitmapCallBackUPP](./colorsync_manager/api-1805297-newcmbitmapcallbackupp.md)
  Creates a new universal procedure pointer (UPP) to a bitmap callback.
- [DisposeCMBitmapCallBackUPP](./colorsync_manager/api-1805300-disposecmbitmapcallbackupp.md)
  Disposes of a universal procedure pointer (UPP) to a bitmap callback.
- [InvokeCMBitmapCallBackUPP](./colorsync_manager/api-1805303-invokecmbitmapcallbackupp.md)
  Invokes a universal procedure pointer (UPP) to a bitmap callback.
- [NewCMConcatCallBackUPP](./colorsync_manager/api-1805306-newcmconcatcallbackupp.md)
  Creates a new universal procedure pointer (UPP) to a progress-monitoring callback.
- [DisposeCMConcatCallBackUPP](./colorsync_manager/api-1805310-disposecmconcatcallbackupp.md)
  Disposes of a universal procedure pointer (UPP) to a progress-monitoring callback.
- [InvokeCMConcatCallBackUPP](./colorsync_manager/api-1805312-invokecmconcatcallbackupp.md)
  Invokes a universal procedure pointer (UPP) to a progress-monitoring callback.
- [NewCMFlattenUPP](./colorsync_manager/api-1805315-newcmflattenupp.md)
  Creates a new universal procedure pointer (UPP) to a data-flattening callback.
- [DisposeCMFlattenUPP](./colorsync_manager/api-1805318-disposecmflattenupp.md)
  Disposes of a universal procedure pointer (UPP) to a data-flattening callback.
- [InvokeCMFlattenUPP](./colorsync_manager/api-1805320-invokecmflattenupp.md)
  Invokes a universal procedure pointer (UPP) to a data-flattening callback.
- [NewCMMIterateUPP](./colorsync_manager/api-1805322-newcmmiterateupp.md)
  Creates a new universal procedure pointer (UPP) to a progress-monitoring callback for the `CMIterateCMMInfo` function.
- [DisposeCMMIterateUPP](./colorsync_manager/api-1805323-disposecmmiterateupp.md)
  Disposes of a universal procedure pointer (UPP) to a progress-monitoring callback for the `CMIterateCMMInfo` function.
- [InvokeCMMIterateUPP](./colorsync_manager/api-1805325-invokecmmiterateupp.md)
  Invokes a universal procedure pointer (UPP) to a progress-monitoring callback for the [CMIterateCMMInfo](./colorsync_manager/api-1805185-cmiteratecmminfo.md) function.
- [NewCMProfileIterateUPP](./colorsync_manager/api-1805339-newcmprofileiterateupp.md)
  Creates a new universal procedure pointer (UPP) to a profile-iteration callback.
- [DisposeCMProfileIterateUPP](./colorsync_manager/api-1805341-disposecmprofileiterateupp.md)
  Disposes of a universal procedure pointer (UPP) to a profile-iteration callback.
- [InvokeCMProfileIterateUPP](./colorsync_manager/api-1805343-invokecmprofileiterateupp.md)
  Invokes a universal procedure pointer (UPP) to a profile-iteration callback.
- [NewCMProfileAccessUPP](./colorsync_manager/api-1805327-newcmprofileaccessupp.md)
  Creates a new universal procedure pointer (UPP) to a profile-access callback.
- [DisposeCMProfileAccessUPP](./colorsync_manager/api-1805329-disposecmprofileaccessupp.md)
  Disposes of a universal procedure pointer (UPP) to a profile-access callback.
- [InvokeCMProfileAccessUPP](./colorsync_manager/api-1805333-invokecmprofileaccessupp.md)
  Invokes a universal procedure pointer (UPP) to a profile-access callback.
- [NewCMProfileFilterUPP](./colorsync_manager/api-1805336-newcmprofilefilterupp.md)
  Creates a new universal procedure pointer (UPP) to a profile-filter callback.
- [DisposeCMProfileFilterUPP](./colorsync_manager/api-1805337-disposecmprofilefilterupp.md)
  Disposes of a universal procedure pointer (UPP) to a profile-filter callback.
- [InvokeCMProfileFilterUPP](./colorsync_manager/api-1805338-invokecmprofilefilterupp.md)
  Invokes a universal procedure pointer (UPP) to a profile-filter callback.
### Callbacks
- [typealias CMFlattenProcPtr](./cmflattenprocptr.md)
  Defines a pointer to a data transfer callback function that transfers profile data from the format for embedded profiles to disk file format or vice versa.
- [CMBitmapCallBackProcPtr](./cmbitmapcallbackprocptr.md)
  Defines a pointer to a bitmap callback function that function reports on the progress of a color-matching or color-checking session being performed for a bitmap or a pixel map.
- [CMConcatCallBackProcPtr](./cmconcatcallbackprocptr.md)
  Defines a pointer to a progress-monitoring function that the ColorSync Manager calls during lengthy color world processing.
- [CMCountImageProfilesProcPtr](./colorsync_manager/cmcountimageprofilesprocptr.md)
  Defines a pointer to a function that obtains a count of the number of embedded profiles for a given image.
- [CMEmbedImageProcPtr](./colorsync_manager/cmembedimageprocptr.md)
  Defines a pointer to a function that embeds an image with an ICC profile.
- [CMGetImageSpaceProcPtr](./colorsync_manager/cmgetimagespaceprocptr.md)
  Defines a pointer to a function that obtains the signature of the data color space in which the color values of colors in an image are expressed.
- [CMGetIndImageProfileProcPtr](./colorsync_manager/cmgetindimageprofileprocptr.md)
  Defines a pointer to a function that obtains a specific embedded profile for a given image.
- [CMIterateDeviceInfoProcPtr](./cmiteratedeviceinfoprocptr.md)
  Defines a pointer to a function that iterates through device information available on the system.
- [CMIterateDeviceProfileProcPtr](./cmiteratedeviceprofileprocptr.md)
  Defines a pointer to a function that iterates through the device profiles available on the system.
- [CMLinkImageProcPtr](./colorsync_manager/cmlinkimageprocptr.md)
  Defines a pointer to a function that matches an image file with a device link profile.
- [CMMatchImageProcPtr](./colorsync_manager/cmmatchimageprocptr.md)
  Defines a pointer to a function that color matches an image file.
- [CMMIterateProcPtr](./cmmiterateprocptr.md)
  Defines a pointer to a function that iterates through color management modules installed on the system.
- [CMProofImageProcPtr](./colorsync_manager/cmproofimageprocptr.md)
  Defines a pointer to a function that proofs an image.
- [CMProfileIterateProcPtr](./cmprofileiterateprocptr.md)
  Defines a pointer to a profile iteration callback function that the ColorSync Manager calls for each found profile file as it iterates over the available profiles.
- [CMSetIndImageProfileProcPtr](./colorsync_manager/cmsetindimageprofileprocptr.md)
  Defines a pointer to a function that sets a specific embedded profile for a given image.
- [CMUnembedImageProcPtr](./colorsync_manager/cmunembedimageprocptr.md)
  Defines a pointer to a function that umembeds an ICC profile from an image.
- [CMValidImageProcPtr](./colorsync_manager/cmvalidimageprocptr.md)
  Defines a pointer to a function that validates a specified image file.
- [CountImageProfilesProcPtr](./colorsync_manager/countimageprofilesprocptr.md)
  Defines a pointer to a function that counts the number of embedded profiles for a given image. 
- [EmbedImageProcPtr](./colorsync_manager/embedimageprocptr.md)
  Defines a pointer to an embed-image function.
- [GetImageSpaceProcPtr](./colorsync_manager/getimagespaceprocptr.md)
  Defines a pointer to a get-image-space function.
- [GetIndImageProfileProcPtr](./colorsync_manager/getindimageprofileprocptr.md)
  Defines a pointer to a function that obtains a color profile for an individual image.
- [MatchImageProcPtr](./colorsync_manager/matchimageprocptr.md)
  Defines a pointer to a match-image function.
- [SetIndImageProfileProcPtr](./colorsync_manager/setindimageprofileprocptr.md)
  Defines a pointer to a function that sets a color profile for an individual image.
- [UnembedImageProcPtr](./colorsync_manager/unembedimageprocptr.md)
  Defines a pointer to an umembed-image function.
- [ValidateImageProcPtr](./colorsync_manager/validateimageprocptr.md)
  Defines a pointer to a validate-image function.
- [ValidateSpaceProcPtr](./colorsync_manager/validatespaceprocptr.md)
  Defines a pointer to a validate-space function.
### Data Types
- [struct CM2Profile](./cm2profile.md)
- [struct CMDeviceInfo](./cmdeviceinfo.md)
- [struct CMDeviceProfileArray](./cmdeviceprofilearray.md)
- [struct CMDeviceScope](./cmdevicescope.md)
- [struct CMError](../CoreMotion/cmerror.md)
  Defines motion errors.
- [typealias CMFlattenUPP](./cmflattenupp.md)
  Defines a universal procedure pointer to a data-flattening callback.
- [typealias CMMultiFunctLutA2BType](./cmmultifunctluta2btype.md)
- [struct CMMultiFunctLutType](./cmmultifunctluttype.md)
- [struct CMXYZColor](./cmxyzcolor.md)
  Contains values for a color specified in XYZ color space.
- [typealias CMXYZComponent](./cmxyzcomponent.md)
- [CM2Header](./cm2header.md)
  Contains information that supports the header format specified by the ICC format specification for version 2.x profiles.
- [CM4Header](./cm4header.md)
- [CMAccelerationCalcData](./colorsync_manager/cmaccelerationcalcdata.md)
- [CMAccelerationCalcDataPtr](./colorsync_manager/cmaccelerationcalcdataptr.md)
- [CMAccelerationCalcDataHdl](./colorsync_manager/cmaccelerationcalcdatahdl.md)
- [CMAccelerationTableData](./colorsync_manager/cmaccelerationtabledata.md)
- [CMAccelerationTableDataPtr](./colorsync_manager/cmaccelerationtabledataptr.md)
- [CMAccelerationTableDataHdl](./colorsync_manager/cmaccelerationtabledatahdl.md)
- [CMAdaptationMatrixType](./cmadaptationmatrixtype.md)
- [CMAppleProfileHeader](./api-1560290-cmappleprofileheader.md)
  Defines a data structure to provide access to both version 2.x and version 1.0 profiles, as specified by the International Color Consortium.
- [CMBitmap](./cmbitmap.md)
  Contains information that describes color bitmap images.
- [CMBitmapCallBackProc](./colorsync_manager/cmbitmapcallbackproc.md)
- [CMBitmapCallBackUPP](./cmbitmapcallbackupp.md)
  Defines a universal procedure pointer to a bitmap callback.
- [CMBufferLocation](./cmbufferlocation.md)
- [CMCMYColor](./cmcmycolor.md)
  Contains color values expressed in the CMY color space.
- [CMCMYKColor](./cmcmykcolor.md)
  Contains color values expressed in the CMYK color space.
- [CMColor](./api-1560453-cmcolor.md)
  Defines a union that can be used to specify a color value defined by one of the 15 data types supported by the union. 
- [CMConcatCallBackUPP](./cmconcatcallbackupp.md)
  Defines a universal procedure pointer to a progress-monitoring function that the ColorSync Manager calls during lengthy color world processing.
- [CMConcatProfileSet](./cmconcatprofileset.md)
  Contains profile and other information needed to set up a color world.
- [CMCurveType](./cmcurvetype.md)
- [CMDataType](./cmdatatype.md)
- [CMDateTime](./cmdatetime.md)
  Contains data that specifies a date and time in year, month, day of the month, hours, minutes, and seconds
- [CMDateTimeType](./cmdatetimetype.md)
- [CMDeviceData](./colorsync_manager/cmdevicedata.md)
- [CMDeviceDataPtr](./colorsync_manager/cmdevicedataptr.md)
- [CMDeviceID](./cmdeviceid.md)
  Defines a data type for a CM device ID.
- [CMDeviceName](./colorsync_manager/cmdevicename.md)
- [CMDeviceNamePtr](./colorsync_manager/cmdevicenameptr.md)
- [CMDeviceProfileID](./cmdeviceprofileid.md)
- [CMDeviceProfileInfo](./cmdeviceprofileinfo.md)
- [CMDeviceProfileScope](./cmdeviceprofilescope.md)
- [CMDeviceSpec](./colorsync_manager/cmdevicespec.md)
- [CMDeviceSpecPtr](./colorsync_manager/cmdevicespecptr.md)
- [CMDeviceState](./cmdevicestate.md)
- [CMDisplayIDType](./cmdisplayidtype.md)
  Defines a data type for a display ID type.
- [CMFixedXYColor](./cmfixedxycolor.md)
- [CMFixedXYZColor](./cmfixedxyzcolor.md)
  Contains data that specifies the profile illuminant in the profile header’s `white` field and other profile element values. 
- [CMGrayColor](./cmgraycolor.md)
  Contains a color value expressed in the gray color space.
- [CMHandleLocation](./cmhandlelocation.md)
  Contains a handle specification for a profile stored in relocatable memory. 
- [CMHLSColor](./cmhlscolor.md)
  Contains a color value expressed in the HLS color space.
- [CMHSVColor](./cmhsvcolor.md)
  Contains a color value expressed in the HSV color space.
- [CMIntentCRDVMSize](./cmintentcrdvmsize.md)
  Defines the rendering intent and its maximum VM size. 
- [CMLabColor](./cmlabcolor.md)
  Contains a color value expressed in the L*a*b* color space.
- [CMLut16Type](./cmlut16type.md)
- [CMLut8Type](./cmlut8type.md)
- [CMLuvColor](./cmluvcolor.md)
  Contains a color value expressed in the L*u*v* color space.
- [CMMakeAndModel](./cmmakeandmodel.md)
  Contains make and model information fro a device.
- [CMMakeAndModelType](./cmmakeandmodeltype.md)
  Contains make and model information along with a type descriptor.
- [CMMeasurementType](./cmmeasurementtype.md)
  Contains measurement type information.
- [CMMInfo](./cmminfo.md)
  Contains information pertaining to a color management module.
- [CMMIterateUPP](./cmmiterateupp.md)
  Defines a universal procedure pointer to a CMM iteration callback.
- [CMMultichannel5Color](./cmmultichannel5color.md)
  Contains a color value expressed in the multichannel color space with 5 channels.
- [CMMultichannel6Color](./cmmultichannel6color.md)
  Contains a color expressed in the multichannel color space with 6 channels.
- [CMMultichannel7Color](./cmmultichannel7color.md)
  Contains a color value expressed in the multichannel color space with 7 channels. 
- [CMMultichannel8Color](./cmmultichannel8color.md)
  Contains a color value expressed in the multichannel color space with 8 channels
- [CMMultiFunctCLUTType](./cmmultifunctcluttype.md)
- [CMMultiFunctLutB2AType](./cmmultifunctlutb2atype.md)
- [CMMultiLocalizedUniCodeEntryRec](./cmmultilocalizedunicodeentryrec.md)
- [CMMultiLocalizedUniCodeType](./cmmultilocalizedunicodetype.md)
- [CMNamedColor](./cmnamedcolor.md)
  Contains a color value expressed in a named color space.
- [CMNamedColor2EntryType](./cmnamedcolor2entrytype.md)
- [CMNamedColor2Type](./cmnamedcolor2type.md)
- [CMNamedColorType](./cmnamedcolortype.md)
- [CMNativeDisplayInfo](./cmnativedisplayinfo.md)
  Contains color information for a native display.
- [CMNativeDisplayInfoType](./cmnativedisplayinfotype.md)
  Contains color information and a type descriptor for a native display.
- [CMParametricCurveType](./cmparametriccurvetype.md)
- [CMPathLocation](./cmpathlocation.md)
  Contains path information.
- [CMProfileFilterProc](./colorsync_manager/cmprofilefilterproc.md)
- [CMProfileIterateData](./cmprofileiteratedata.md)
  Contains a callback routine with a description of a profile that is during an iteration through the available profiles.
- [CMProfileIterateUPP](./cmprofileiterateupp.md)
  Defines a universal procedure pointer to a profile iteration callback.
- [CMProfileLocation](./cmprofilelocation.md)
  Contains profile location information.
- [CMProfileMD5](./cmprofilemd5.md)
  Defines a data type for an MD5 digest.
- [CMProfileName](./colorsync_manager/cmprofilename.md)
  Contains profile name and length.
- [CMProfileNamePtr](./colorsync_manager/cmprofilenameptr.md)
  Defines a pointer to a profile name data structure.
- [CMProfileRef](./cmprofileref.md)
  Defines a reference to an opaque data type that specifies profile information.
- [CMProfileSequenceDescType](./cmprofilesequencedesctype.md)
- [CMProfLoc](./api-1560460-cmprofloc.md)
  Defines a union that identifies the location of a profile. 
- [CMPS2CRDVMSizeType](./cmps2crdvmsizetype.md)
  Defines the Apple-defined `'psvm'` optional tag.
- [CMRGBColor](./cmrgbcolor.md)
   Contains a color value expressed in the RGB color space.
- [CMS15Fixed16ArrayType](./cms15fixed16arraytype.md)
- [CMScreeningChannelRec](./cmscreeningchannelrec.md)
- [CMScreeningType](./cmscreeningtype.md)
- [CMSignatureType](./cmsignaturetype.md)
- [CMTagElemTable](./cmtagelemtable.md)
- [CMTagRecord](./cmtagrecord.md)
- [CMTextDescriptionType](./cmtextdescriptiontype.md)
- [CMTextType](./cmtexttype.md)
- [CMU16Fixed16ArrayType](./cmu16fixed16arraytype.md)
- [CMUcrBgType](./cmucrbgtype.md)
- [CMUInt16ArrayType](./cmuint16arraytype.md)
- [CMUInt32ArrayType](./cmuint32arraytype.md)
- [CMUInt64ArrayType](./cmuint64arraytype.md)
- [CMUInt8ArrayType](./cmuint8arraytype.md)
- [CMUnicodeTextType](./cmunicodetexttype.md)
- [CMVideoCardGamma](./cmvideocardgamma.md)
  Contains video gamma data to store with a video gamma profile tag. 
- [CMVideoCardGammaFormula](./cmvideocardgammaformula.md)
- [CMVideoCardGammaTable](./cmvideocardgammatable.md)
- [CMVideoCardGammaType](./cmvideocardgammatype.md)
  Specifies a video card gamma profile tag.
- [CMViewingConditionsType](./cmviewingconditionstype.md)
- [CMWorldRef](./cmworldref.md)
  Defines an opaque data type used for color-matching and color-checking sessions.
- [CMXYZType](./cmxyztype.md)
- [CMYKColor](./colorsync_manager/cmykcolor.md)
- [CMYxyColor](./cmyxycolor.md)
  Contains values for a color expressed in the Yxy color space.
- [NCMConcatProfileSet](./ncmconcatprofileset.md)
- [NCMConcatProfileSpec](./ncmconcatprofilespec.md)
- [NCMDeviceProfileInfo](./ncmdeviceprofileinfo.md)
### Constants
- [Abstract Color Space Constants](./colorsync_manager/api-1560701-abstract_color_space_constants.md)
  Specify values that represent general color spaces.
- [Channel Encoding Format](./colorsync_manager/api-1560324-channel_encoding_format.md)
  Specify an encoding format for sRGB64.
- [Color Packing for Color Spaces](./colorsync_manager/api-1560270-color_packing_for_color_spaces.md)
  Specify how color values are stored.
- [Color Space Signatures](./colorsync_manager/api-1560276-color_space_signatures.md)
  Define four-character-sequences associated with color spaces.
- [Color Space Masks](./colorsync_manager/api-1560521-color_space_masks.md)
  Specify masks used for color spaces.
- [Current Device Versions](./colorsync_manager/api-1560472-current_device_versions.md)
  Specify the current versions of the data structure containing information on registered devices.
- [Current Info Versions](./colorsync_manager/api-1560146-current_info_versions.md)
  Specify current device and profile versions.
- [Current Major Version Mask](./colorsync_manager/api-1560659-current_major_version_mask.md)
  Specifies the current major version number.
- [Data Transfer Commands](./colorsync_manager/api-1560166-data_transfer_commands.md)
  Specify commands for caller-supplied ColorSync data transfer functions.
- [Data Type Element Values](./colorsync_manager/api-1560593-data_type_element_values.md)
  Specify a data type.
- [Default CMM Signature](./colorsync_manager/api-1560689-default_cmm_signature.md)
  Specifies a signature for the default color management module supplied by Color Sync.
- [Default IDs](./colorsync_manager/api-1560386-default_ids.md)
  Specify default values for device and profile IDs.
- [Device Attribute Values for Version 2.x Profiles](./colorsync_manager/api-1560447-device_attribute_values_for_vers.md)
  Define masks your application can use to set or test bits in the `deviceAttributes `field of the `CM2Header` structure.
- [typealias CMDeviceClass](./cmdeviceclass.md)
  Define constants to represent a variety of input and output devices.
- [Device and Media Attributes](./colorsync_manager/api-1560327-device_and_media_attributes.md)
  Used to set or obtain device or media attributes.
- [Device States](./colorsync_manager/api-1560516-device_states.md)
  Specify device states.
- [Element Tags and Signatures for Version 1.0 Profiles](./colorsync_manager/api-1560273-element_tags_and_signatures_for_.md)
  Define tags and signatures used for version 1.0 profiles.
- [Embedded Profile Flags](./colorsync_manager/api-1560148-embedded_profile_flags.md)
  Specify copyright-protection flag options,
- [Flag Mask Definitions for Version 2.x Profiles](./colorsync_manager/api-1560699-flag_mask_definitions_for_versio.md)
  Define masks your application can use to set or test various bits in the `flags` field of the `CM2Header` structure.
- [ICC Profile Versions](./colorsync_manager/api-1560658-icc_profile_versions.md)
  Specify IDD profile version numbers.
- [Illuminant Measurement Endocings](./colorsync_manager/api-1560108-illuminant_measurement_endocings.md)
  Specify standard illuminate measurement encodings.
- [Magic Cookie Number](./colorsync_manager/api-1560690-magic_cookie_number.md)
  Specifies a magic cookie number for anonymous file ID.
- [Maximum Path Size](./colorsync_manager/api-1560101-maximum_path_size.md)
  Specifies the maximum length for a path name.
- [Measurement Flares](./colorsync_manager/api-1560283-measurement_flares.md)
  Specify measurement flare encodings.
- [Measurement Geometries](./colorsync_manager/api-1560539-measurement_geometries.md)
  Specify measurement geometry encodings.
- [Parametric Types](./colorsync_manager/api-1560541-parametric_types.md)
  Specify a parametric curve type enumeration,
- [Platform Enumeration Values](./colorsync_manager/api-1560191-platform_enumeration_values.md)
  Specify computer platforms.
- [Profile Iteration Values](./colorsync_manager/api-1560091-profile_iteration_values.md)
  Specify profiles to iterate.
- [Profile Location Sizes](./colorsync_manager/api-1560369-profile_location_sizes.md)
  Specify a location size.
- [PostScript Data Formats](./colorsync_manager/api-1560551-postscript_data_formats.md)
  Specify constants that indicate the format of PostScript data.
- [Profile Access Procedures](./colorsync_manager/api-1560733-profile_access_procedures.md)
  Specify operations used to access profiles.
- [Profile Classes](./colorsync_manager/api-1560630-profile_classes.md)
  Specify profile class enumerations.
- [Profile Concatenation Values](./colorsync_manager/api-1560373-profile_concatenation_values.md)
  Specify values to use when concatenating profiles.
- [Profile Iteration Constants](./colorsync_manager/api-1560189-profile_iteration_constants.md)
  Define an iteration version.
- [Profile Location Type](./colorsync_manager/api-1560599-profile_location_type.md)
  Defines profile location kinds.
- [Public Tags](./colorsync_manager/api-1560717-public_tags.md)
  Specify tag values available for public use.
- [Public Type Signatures](./colorsync_manager/api-1560346-public_type_signatures.md)
  Specify signatures for public types.
- [Quality Flag Values for Version 2.x Profiles](./colorsync_manager/api-1560115-quality_flag_values_for_version_.md)
  Define the possible values for the quality bits in the `flags` field of the `CM2Header` structure. 
- [Rendering Intent Values for Version 2.x Profiles](./colorsync_manager/api-1560278-rendering_intent_values_for_vers.md)
  Define the four possible values for the rendering intent bits of the `renderingIntent` field of the `CM2Header` structure. 
- [Screen Encoding Tags](./colorsync_manager/api-1560247-screen_encoding_tags.md)
  Specify tags to use for screen encodings.
- [Spot Function Values](./colorsync_manager/api-1560411-spot_function_values.md)
  Specify values for spot functions.
- [Standard Observer](./colorsync_manager/api-1560388-standard_observer.md)
  Standard observer measurement type encodings.
- [Tag Type Information](./colorsync_manager/api-1560086-tag_type_information.md)
  Defines a constant for 2.0 tag type information.
- [Technology Tag Descriptions](./colorsync_manager/api-1560433-technology_tag_descriptions.md)
  Define descriptor tags for technologies.
- [Use Types](./colorsync_manager/api-1560730-use_types.md)
  Specify use types.
- [Video Card Gamma Storage Types](./colorsync_manager/api-1560344-video_card_gamma_storage_types.md)
  Specify data storage type constants.
- [Video Card Gamma Tags](./colorsync_manager/api-1560164-video_card_gamma_tags.md)
  Specify video card gamma information.
- [Video Card Gamma Signatures](./colorsync_manager/api-1560275-video_card_gamma_signatures.md)
  Specify signatures used for video card gamma information.
- [Abstract Color Space Constants](./api-1560701-abstract_color_space_constants.md)
  Specify values that represent general color spaces.
- [Channel Encoding Format](./api-1560324-channel_encoding_format.md)
  Specify an encoding format for sRGB64.
- [CMChromaticAdaptation](./cmchromaticadaptation.md)
  Specify a transformation to use for chromaric adaptation.
- [CMM Function Selectors](./colorsync_manager/cmm_function_selectors.md)
  Define selectors used for component-based CMM functions.
- [Color Management Module Component Interface](./colorsync_manager/color_management_module_component_interface.md)
  Specify a CMM interface version.
- [Color Packing for Color Spaces](./api-1560270-color_packing_for_color_spaces.md)
  Specify how color values are stored.
- [CMBitmapColorSpace](./cmbitmapcolorspace.md)
  Specifies bitmap spaces with a wide range of data formats appropriate for multiple platforms.
- [Color Space Signatures](./api-1560276-color_space_signatures.md)
  Define four-character-sequences associated with color spaces.
- [Color Space Masks](./api-1560521-color_space_masks.md)
  Specify masks used for color spaces.
- [Current Device Versions](./api-1560472-current_device_versions.md)
  Specify the current versions of the data structure containing information on registered devices.
- [Current Info Versions](./api-1560146-current_info_versions.md)
  Specify current device and profile versions.
- [Current Major Version Mask](./api-1560659-current_major_version_mask.md)
  Specifies the current major version number.
- [Data Transfer Commands](./api-1560166-data_transfer_commands.md)
  Specify commands for caller-supplied ColorSync data transfer functions.
- [Data Type Element Values](./api-1560593-data_type_element_values.md)
  Specify a data type.
- [Default CMM Signature](./api-1560689-default_cmm_signature.md)
  Specifies a signature for the default color management module supplied by Color Sync.
- [Default IDs](./api-1560386-default_ids.md)
  Specify default values for device and profile IDs.
- [Device Attribute Values for Version 2.x Profiles](./api-1560447-x_profiles.md)
  Define masks your application can use to set or test bits in the `deviceAttributes `field of the `CM2Header` structure.
- [Device and Media Attributes](./api-1560327-device_and_media_attributes.md)
  Used to set or obtain device or media attributes.
- [Device States](./api-1560516-device_states.md)
  Specify device states.
- [Element Tags and Signatures for Version 1.0 Profiles](./api-1560273-0_profiles.md)
  Define tags and signatures used for version 1.0 profiles.
- [Embedded Profile Flags](./api-1560148-embedded_profile_flags.md)
  Specify copyright-protection flag options,
- [Flag Mask Definitions for Version 2.x Profiles](./api-1560699-x_profiles.md)
  Define masks your application can use to set or test various bits in the `flags` field of the `CM2Header` structure.
- [ICC Profile Versions](./api-1560658-icc_profile_versions.md)
  Specify IDD profile version numbers.
- [Illuminant Measurement Endocings](./api-1560108-illuminant_measurement_endocings.md)
  Specify standard illuminate measurement encodings.
- [Macintosh 68K Trap Word](./colorsync_manager/macintosh_68k_trap_word.md)
  Specifies a 68K trap word for the Macintosh.
- [Magic Cookie Number](./api-1560690-magic_cookie_number.md)
  Specifies a magic cookie number for anonymous file ID.
- [Maximum Path Size](./api-1560101-maximum_path_size.md)
  Specifies the maximum length for a path name.
- [Measurement Flares](./api-1560283-measurement_flares.md)
  Specify measurement flare encodings.
- [Measurement Geometries](./api-1560539-measurement_geometries.md)
  Specify measurement geometry encodings.
- [Parametric Types](./api-1560541-parametric_types.md)
  Specify a parametric curve type enumeration,
- [Platform Enumeration Values](./api-1560191-platform_enumeration_values.md)
  Specify computer platforms.
- [Profile Iteration Values](./api-1560091-profile_iteration_values.md)
  Specify profiles to iterate.
- [Profile Location Sizes](./api-1560369-profile_location_sizes.md)
  Specify a location size.
- [PostScript Data Formats](./api-1560551-postscript_data_formats.md)
  Specify constants that indicate the format of PostScript data.
- [Profile Access Procedures](./api-1560733-profile_access_procedures.md)
  Specify operations used to access profiles.
- [Profile Classes](./api-1560630-profile_classes.md)
  Specify profile class enumerations.
- [Profile Concatenation Values](./api-1560373-profile_concatenation_values.md)
  Specify values to use when concatenating profiles.
- [Profile Iteration Constants](./api-1560189-profile_iteration_constants.md)
  Define an iteration version.
- [Profile Location Type](./api-1560599-profile_location_type.md)
  Defines profile location kinds.
- [Public Tags](./api-1560717-public_tags.md)
  Specify tag values available for public use.
- [Public Type Signatures](./api-1560346-public_type_signatures.md)
  Specify signatures for public types.
- [Quality Flag Values for Version 2.x Profiles](./api-1560115-x_profiles.md)
  Define the possible values for the quality bits in the `flags` field of the `CM2Header` structure. 
- [Rendering Intent Values for Version 2.x Profiles](./api-1560278-x_profiles.md)
  Define the four possible values for the rendering intent bits of the `renderingIntent` field of the `CM2Header` structure. 
- [Screen Encoding Tags](./api-1560247-screen_encoding_tags.md)
  Specify tags to use for screen encodings.
- [Spot Function Values](./api-1560411-spot_function_values.md)
  Specify values for spot functions.
- [Standard Observer](./api-1560388-standard_observer.md)
  Standard observer measurement type encodings.
- [Tag Type Information](./api-1560086-tag_type_information.md)
  Defines a constant for 2.0 tag type information.
- [Technology Tag Descriptions](./api-1560433-technology_tag_descriptions.md)
  Define descriptor tags for technologies.
- [Use Types](./api-1560730-use_types.md)
  Specify use types.
- [Video Card Gamma Storage Types](./api-1560344-video_card_gamma_storage_types.md)
  Specify data storage type constants.
- [Video Card Gamma Tags](./api-1560164-video_card_gamma_tags.md)
  Specify video card gamma information.
- [Video Card Gamma Signatures](./api-1560275-video_card_gamma_signatures.md)
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
- [var cmDeviceDBNotFoundErr: Int](./cmdevicedbnotfounderr.md)
  Preferences not found or loaded; returned by a CM device integration routine.
- [var cmDeviceAlreadyRegistered: Int](./cmdevicealreadyregistered.md)
  Device already registered; returned by a CM device integration routine.
- [var cmDeviceNotRegistered: Int](./cmdevicenotregistered.md)
  Device not found; returned by a CM device integration routine.
- [var cmDeviceProfilesNotFound: Int](./cmdeviceprofilesnotfound.md)
  Profiles not found; returned by a CM device integration routine.
- [var cmInternalCFErr: Int](./cminternalcferr.md)
  CoreFoundation failure; returned by a CM device integration routine.
- [cmProfileError](../coreservices/api-1559955-anonymous/cmprofileerror.md)
  There is something wrong with the content of the profile
- [cmMethodError](../coreservices/api-1559955-anonymous/cmmethoderror.md)
  An error occurred during the CMM arbitration process that determines the CMM to use
- [cmMethodNotFound](../coreservices/api-1559955-anonymous/cmmethodnotfound.md)
  CMM not present
- [cmProfileNotFound](../coreservices/api-1559955-anonymous/cmprofilenotfound.md)
  Responder error
- [cmProfilesIdentical](../coreservices/api-1559955-anonymous/cmprofilesidentical.md)
  Profiles are the same
- [cmCantConcatenateError](../coreservices/api-1559955-anonymous/cmcantconcatenateerror.md)
  Profiles cannot be concatenated
- [cmCantXYZ](../coreservices/api-1559955-anonymous/cmcantxyz.md)
  CMM does not handle XYZ color space
- [cmCantDeleteProfile](../coreservices/api-1559955-anonymous/cmcantdeleteprofile.md)
  Responder error
- [cmUnsupportedDataType](../coreservices/api-1559955-anonymous/cmunsupporteddatatype.md)
  Responder error
- [cmNoCurrentProfile](../coreservices/api-1559955-anonymous/cmnocurrentprofile.md)
  Responder error
- [cmElementTagNotFound](../coreservices/api-1559968-anonymous/cmelementtagnotfound.md)
  The tag you specified is not in the specified profile
- [cmIndexRangeErr](../coreservices/api-1559968-anonymous/cmindexrangeerr.md)
  Tag index out of range
- [cmCantDeleteElement](../coreservices/api-1559968-anonymous/cmcantdeleteelement.md)
  Cannot delete the specified profile element
- [cmFatalProfileErr](../coreservices/api-1559968-anonymous/cmfatalprofileerr.md)
  Returned from File Manager while updating a profile file in response to `CMUpdateProfile`; profile content may be corrupted
- [cmInvalidProfile](../coreservices/api-1559968-anonymous/cminvalidprofile.md)
  Profile reference is invalid or refers to an inappropriate profile
- [cmInvalidProfileLocation](../coreservices/api-1559968-anonymous/cminvalidprofilelocation.md)
  Operation not supported for this profile location
- [cmInvalidSearch](../coreservices/api-1559968-anonymous/cminvalidsearch.md)
  Bad search handle
- [cmSearchError](../coreservices/api-1559968-anonymous/cmsearcherror.md)
  Internal error occurred during profile search
- [cmErrIncompatibleProfile](../coreservices/api-1559968-anonymous/cmerrincompatibleprofile.md)
  Unspecified profile error
- [cmInvalidColorSpace](../coreservices/api-1559968-anonymous/cminvalidcolorspace.md)
  Profile color space does not match bitmap type
- [cmInvalidSrcMap](../coreservices/api-1559968-anonymous/cminvalidsrcmap.md)
  Source pixel map or bitmap was invalid
- [cmInvalidDstMap](../coreservices/api-1559968-anonymous/cminvaliddstmap.md)
  Destination pix/bit map was invalid
- [cmNoGDevicesError](../coreservices/api-1559968-anonymous/cmnogdeviceserror.md)
  Begin matching or end matching—no graphics devices available
- [cmInvalidProfileComment](../coreservices/api-1559968-anonymous/cminvalidprofilecomment.md)
  Bad profile comment during `drawpicture`
- [cmRangeOverFlow](../coreservices/api-1559968-anonymous/cmrangeoverflow.md)
  One or more output color value overflows in color conversion; all input color values will be converted and the overflow will be clipped
- [cmCantCopyModifiedV1Profile](../coreservices/api-1559968-anonymous/cmcantcopymodifiedv1profile.md)
  It is illegal to copy version 1.0 profiles that have been modified
- [cmNamedColorNotFound](../coreservices/api-1559968-anonymous/cmnamedcolornotfound.md)
  The specified named color was not found in the specified profile
- [cmCantGamutCheckError](../coreservices/api-1559968-anonymous/cmcantgamutcheckerror.md)
  Gamut checking not supported by this color world—that is, the color world does not contain a gamut table because it was built with gamut checking turned off
- [cmDeviceDBNotFoundErr](./api-1560507-anonymous/cmdevicedbnotfounderr.md)
  Preferences not found or loaded; returned by a CM device integration routine.
- [cmDeviceAlreadyRegistered](./api-1560507-anonymous/cmdevicealreadyregistered.md)
  Device already registered; returned by a CM device integration routine.
- [cmDeviceNotRegistered](./api-1560507-anonymous/cmdevicenotregistered.md)
  Device not found; returned by a CM device integration routine.
- [cmDeviceProfilesNotFound](./api-1560507-anonymous/cmdeviceprofilesnotfound.md)
  Profiles not found; returned by a CM device integration routine.
- [cmInternalCFErr](./api-1560507-anonymous/cminternalcferr.md)
  CoreFoundation failure; returned by a CM device integration routine.
### Accessing Profiles
- [CMOpenProfile](./colorsync_manager/api-1804853-cmopenprofile.md)
  Opens the specified profile and returns a reference to the profile.
- [CMValidateProfile](./colorsync_manager/api-1804856-cmvalidateprofile.md)
  Indicates whether the specified profile contains the minimum set of elements required by the current color management module (CMM) for color matching or color checking.
- [CMCloseProfile](./colorsync_manager/api-1804861-cmcloseprofile.md)
  Decrements the reference count for the specified profile reference and, if the reference count reaches 0, frees all private memory and other resources associated with the profile.
- [CMUpdateProfile](./colorsync_manager/api-1804864-cmupdateprofile.md)
  Saves modifications to the specified profile.
- [CMCopyProfile](./colorsync_manager/api-1804870-cmcopyprofile.md)
  Duplicates the specified existing profile.
- [CMProfileModified](./colorsync_manager/api-1804872-cmprofilemodified.md)
  Indicates whether the specified profile has been modified since it was created or last updated.
- [CMGetProfileMD5](./colorsync_manager/api-1804876-cmgetprofilemd5.md)
  Gets the MD5 checksum from the profile header (message digest)
- [CMGetProfileHeader](./colorsync_manager/api-1804879-cmgetprofileheader.md)
  Obtains the profile header for the specified profile. 
- [CMSetProfileHeader](./colorsync_manager/api-1804882-cmsetprofileheader.md)
  Sets the header for the specified profile. 
- [CMGetProfileLocation](./colorsync_manager/api-1804885-cmgetprofilelocation.md)
  Obtains the location of a profile based on the specified profile reference.
- [NCMGetProfileLocation](./colorsync_manager/api-1804889-ncmgetprofilelocation.md)
  Obtains either a profile location structure for a specified profile or the size of the location structure for the profile.
- [CMCloneProfileRef](./colorsync_manager/api-1804891-cmcloneprofileref.md)
  Increments the reference count for the specified profile reference.
- [CMGetProfileRefCount](./colorsync_manager/api-1804894-cmgetprofilerefcount.md)
  Obtains the current reference count for the specified profile.
- [CMFlattenProfile](./colorsync_manager/api-1804897-cmflattenprofile.md)
  Transfers a profile stored in an independent disk file to an external profile format that can be embedded in a graphics document.
- [NCMUnflattenProfile](./colorsync_manager/api-1804901-ncmunflattenprofile.md)
  Unflattens a previously flattened profile.
### Iterating Installed Profiles
- [CMIterateColorSyncFolder](./colorsync_manager/api-1804904-cmiteratecolorsyncfolder.md)
  Iterates over the available profiles.
- [CMGetColorSyncFolderSpec](./colorsync_manager/api-1804907-cmgetcolorsyncfolderspec.md)
  Obtains the volume reference number and the directory ID for a ColorSync Profiles folder.
### Creating Profiles
- [CMNewProfile](./colorsync_manager/api-1804911-cmnewprofile.md)
  Creates a new profile and associated backing copy.
- [CWNewLinkProfile](./colorsync_manager/api-1804915-cwnewlinkprofile.md)
  Creates a device link profile based on the specified set of profiles.
- [NCWNewLinkProfile](./colorsync_manager/api-1804918-ncwnewlinkprofile.md)
  Obtains a profile reference for the specified by the profile location.
- [CMMakeProfile](./colorsync_manager/api-1804920-cmmakeprofile.md)
  Makes a display or abstract profile by modifying an existing one.
### Accessing Special Profiles
- [CMGetSystemProfile](./colorsync_manager/api-1804926-cmgetsystemprofile.md)
  Obtains a reference to the current system profile.
- [CMSetSystemProfile](./colorsync_manager/api-1804932-cmsetsystemprofile.md)
  Sets the current system profile.
- [NCMSetSystemProfile](./colorsync_manager/api-1804936-ncmsetsystemprofile.md)
  Sets the location of a color profile.
- [CMGetDefaultProfileBySpace](./colorsync_manager/api-1804940-cmgetdefaultprofilebyspace.md)
  Gets the default profile for the specified color space.
- [CMSetDefaultProfileBySpace](./colorsync_manager/api-1804944-cmsetdefaultprofilebyspace.md)
  Sets the default profile for the specified color space.
- [CMGetDefaultProfileByUse](./colorsync_manager/api-1804948-cmgetdefaultprofilebyuse.md)
  Obtains the users’ preferred device profile setting.
- [CMSetDefaultProfileByUse](./colorsync_manager/api-1804951-cmsetdefaultprofilebyuse.md)
  Sets values for device profile settings.
- [CMGetProfileByAVID](./colorsync_manager/api-1804955-cmgetprofilebyavid.md)
  Gets the current profile for a monitor.
- [CMSetProfileByAVID](./colorsync_manager/api-1804959-cmsetprofilebyavid.md)
  Sets the profile for the specified monitor, optionally setting video card gamma.
### Accessing Profile Elements
- [CMCountProfileElements](./colorsync_manager/api-1804963-cmcountprofileelements.md)
  Counts the number of elements in the specified profile.
- [CMProfileElementExists](./colorsync_manager/api-1804967-cmprofileelementexists.md)
  Tests whether the specified profile contains a specific element based on the element’s tag signature.
- [CMGetProfileElement](./colorsync_manager/api-1804973-cmgetprofileelement.md)
  Obtains element data from the specified profile based on the specified element tag signature.
- [CMSetProfileElement](./colorsync_manager/api-1804977-cmsetprofileelement.md)
  Sets or replaces the element data for a specific tag in the specified profile. 
- [CMSetProfileElementSize](./colorsync_manager/api-1804980-cmsetprofileelementsize.md)
  Reserves the element data size for a specific tag in the specified profile before setting the element data. 
- [CMGetPartialProfileElement](./colorsync_manager/api-1804984-cmgetpartialprofileelement.md)
  Obtains a portion of the element data from the specified profile based on the specified element tag signature.
- [CMSetPartialProfileElement](./colorsync_manager/api-1804989-cmsetpartialprofileelement.md)
  Sets part of the element data for a specific tag in the specified profile.
- [CMGetIndProfileElementInfo](./colorsync_manager/api-1804996-cmgetindprofileelementinfo.md)
  Obtains the element tag and data size of an element by index from the specified profile. 
- [CMGetIndProfileElement](./colorsync_manager/api-1805002-cmgetindprofileelement.md)
  Obtains the element data corresponding to a particular index from the specified profile. 
- [CMSetProfileElementReference](./colorsync_manager/api-1805005-cmsetprofileelementreference.md)
  Adds a tag to the specified profile to refer to data corresponding to a previously set element. 
- [CMRemoveProfileElement](./colorsync_manager/api-1805008-cmremoveprofileelement.md)
  Removes an element corresponding to a specific tag from the specified profile. 
### Accessing Profile Descriptions
- [CMCopyProfileDescriptionString](./colorsync_manager/api-1805012-cmcopyprofiledescriptionstring.md)
  Returns the name of a profile as a CFString.
- [CMCopyProfileLocalizedString](./colorsync_manager/api-1805016-cmcopyprofilelocalizedstring.md)
  Gets one specific string out of a profile 
- [CMCopyProfileLocalizedStringDictionary](./colorsync_manager/api-1805020-cmcopyprofilelocalizedstringdict.md)
  Obtains a CFDictionary which contains the language locale and string for multiple localizations from a given tag.
- [CMSetProfileLocalizedStringDictionary](./colorsync_manager/api-1805025-cmsetprofilelocalizedstringdicti.md)
  Writes a dictionary of localized strings to a given tag in a profile. 
- [CMGetScriptProfileDescription](./colorsync_manager/api-1805029-cmgetscriptprofiledescription.md)
  Obtains the internal name (or description) of a profile and the script code identifying the language in which the profile name is specified from the specified profile.
- [CMGetProfileDescriptions](./colorsync_manager/api-1805034-cmgetprofiledescriptions.md)
  Obtains the description tag data for a specified profile.
- [CMSetProfileDescriptions](./colorsync_manager/api-1805039-cmsetprofiledescriptions.md)
  Sets the description tag data for a specified profile.
### Accessing Name-Class Profiles
- [CMGetNamedColorInfo](./colorsync_manager/api-1805047-cmgetnamedcolorinfo.md)
  Obtains information about a named color space from its profile reference.
- [CMGetNamedColorValue](./colorsync_manager/api-1805053-cmgetnamedcolorvalue.md)
  Obtains device and PCS color values for a specific color name from a named color space profile.
- [CMGetIndNamedColorValue](./colorsync_manager/api-1805059-cmgetindnamedcolorvalue.md)
  Obtains device and PCS color values for a specific named color index from a named color space profile.
- [CMGetNamedColorIndex](./colorsync_manager/api-1805065-cmgetnamedcolorindex.md)
  Obtains a named color index for a specific color name from a named color space profile.
- [CMGetNamedColorName](./colorsync_manager/api-1805072-cmgetnamedcolorname.md)
  Obtains a named color name for a specific named color index from a named color space profile.
### Working With ColorWorlds
- [NCWNewColorWorld](./colorsync_manager/api-1805079-ncwnewcolorworld.md)
  Creates a color world for color matching based on the specified source and destination profiles. 
- [CWConcatColorWorld](./colorsync_manager/api-1805087-cwconcatcolorworld.md)
  Sets up a color world that includes a set of profiles for various color transformations among devices in a sequence.
- [NCWConcatColorWorld](./colorsync_manager/api-1805091-ncwconcatcolorworld.md)
  Defines a color world for color transformations among a series of concatenated profiles. 
- [CMGetCWInfo](./colorsync_manager/api-1805097-cmgetcwinfo.md)
  Obtains information about the color management modules (CMMs) used for a specific color world.
- [CWDisposeColorWorld](./colorsync_manager/api-1805102-cwdisposecolorworld.md)
  Releases the private storage associated with a color world when your application has finished using the color world. 
- [CWMatchColors](./colorsync_manager/api-1805108-cwmatchcolors.md)
  Matches colors in a color list, using the specified color world.
- [CWCheckColors](./colorsync_manager/api-1805111-cwcheckcolors.md)
  Tests a list of colors using a specified color world to see if they fall within the gamut of a destination device.
- [CWMatchBitmap](./colorsync_manager/api-1805116-cwmatchbitmap.md)
  Matches the colors of a bitmap to the gamut of a destination device using the profiles specified by a color world.
- [CWCheckBitmap](./colorsync_manager/api-1805121-cwcheckbitmap.md)
  Tests the colors of the pixel data of a bitmap to determine whether the colors map to the gamut of the destination device.
- [CWFillLookupTexture](./colorsync_manager/api-1805126-cwfilllookuptexture.md)
  Fills a 3-D lookup texture from a color world.
### Converting Colors
- [CMConvertXYZToLab](./colorsync_manager/api-1805133-cmconvertxyztolab.md)
  Converts colors specified in the XYZ color space to the L*a*b* color space. 
- [CMConvertLabToXYZ](./colorsync_manager/api-1805134-cmconvertlabtoxyz.md)
  Converts colors specified in the L*a*b* color space to the XYZ color space. 
- [CMConvertXYZToLuv](./colorsync_manager/api-1805137-cmconvertxyztoluv.md)
  Converts colors specified in the XYZ color space to the L*u*v* color space. 
- [CMConvertLuvToXYZ](./colorsync_manager/api-1805140-cmconvertluvtoxyz.md)
  Converts colors specified in the L*u*v* color space to the XYZ color space. 
- [CMConvertXYZToYxy](./colorsync_manager/api-1805142-cmconvertxyztoyxy.md)
  Converts colors specified in the XYZ color space to the Yxy color space. 
- [CMConvertYxyToXYZ](./colorsync_manager/api-1805146-cmconvertyxytoxyz.md)
  Converts colors specified in the Yxy color space to the XYZ color space. 
- [CMConvertRGBToHLS](./colorsync_manager/api-1805149-cmconvertrgbtohls.md)
  Converts colors specified in the RGB color space to equivalent colors defined in the HLS color space. 
- [CMConvertHLSToRGB](./colorsync_manager/api-1805152-cmconverthlstorgb.md)
  Converts colors specified in the HLS color space to equivalent colors defined in the RGB color space. 
- [CMConvertRGBToHSV](./colorsync_manager/api-1805155-cmconvertrgbtohsv.md)
  Converts colors specified in the RGB color space to equivalent colors defined in the HSV color space when the device types are the same. 
- [CMConvertHSVToRGB](./colorsync_manager/api-1805160-cmconverthsvtorgb.md)
  Converts colors specified in the HSV color space to equivalent colors defined in the RGB color space. 
- [CMConvertRGBToGray](./colorsync_manager/api-1805164-cmconvertrgbtogray.md)
  Converts colors specified in the RGB color space to equivalent colors defined in the Gray color space. 
- [CMConvertXYZToFixedXYZ](./colorsync_manager/api-1805169-cmconvertxyztofixedxyz.md)
  Converts colors specified in the XYZ color space whose components are expressed as XYZ 16-bit unsigned values of type `CMXYZColor` to equivalent colors expressed as 32-bit signed values of type `CMFixedXYZColor`.
- [CMConvertFixedXYZToXYZ](./colorsync_manager/api-1805174-cmconvertfixedxyztoxyz.md)
  Converts colors specified in XYZ color space whose components are expressed as Fixed XYZ 32-bit signed values of type `CMFixedXYZColor` to equivalent colors expressed as XYZ 16-bit unsigned values of type `CMXYZColor`.
- [CMConvertXYZToXYZ](./colorsync_manager/api-1805177-cmconvertxyztoxyz.md)
  Converts a source color to a destination color using the specified chromatic adaptation method.
### Working With CMMs
- [CMGetPreferredCMM](./colorsync_manager/api-1805182-cmgetpreferredcmm.md)
  Identifies the preferred CMM specified by the ColorSync control panel.
- [CMIterateCMMInfo](./colorsync_manager/api-1805185-cmiteratecmminfo.md)
  Iterates through the color management modules installed on the system.
### Working With PostScript
- [CMGetPS2ColorSpace](./colorsync_manager/api-1805191-cmgetps2colorspace.md)
  Obtains color space element data in text format usable as the parameter to the PostScript `setColorSpace` operator, which characterizes the color space of subsequent graphics data. 
- [CMGetPS2ColorRenderingIntent](./colorsync_manager/api-1805196-cmgetps2colorrenderingintent.md)
  Obtains the rendering intent element data in text format usable as the parameter to the PostScript `findRenderingIntent` operator, which specifies the color-matching option for subsequent graphics data.
- [CMGetPS2ColorRendering](./colorsync_manager/api-1805202-cmgetps2colorrendering.md)
  Obtains the color rendering dictionary (CRD) element data usable as the parameter to the PostScript `setColorRendering` operator, which specifies the PostScript color rendering dictionary to use for the following graphics data.
- [CMGetPS2ColorRenderingVMSize](./colorsync_manager/api-1805206-cmgetps2colorrenderingvmsize.md)
  Determines the virtual memory size of the color rendering dictionary (CRD) for a printer profile before your application or driver obtains the CRD and sends it to the printer.
### Working With QuickDraw
- [CWMatchPixMap](./colorsync_manager/api-1805211-cwmatchpixmap.md)
  Matches a pixel map in place based on a specified color world. 
- [CWCheckPixMap](./colorsync_manager/api-1805214-cwcheckpixmap.md)
  Checks the colors of a pixel map using the profiles of a specified color world to determine whether the colors are in the gamut of the destination device. 
- [NCMBeginMatching](./colorsync_manager/api-1805216-ncmbeginmatching.md)
  Sets up a QuickDraw-specific ColorSync matching session, using the specified source and destination profiles. 
- [CMEndMatching](./colorsync_manager/api-1805220-cmendmatching.md)
  Concludes a QuickDraw-specific ColorSync matching session initiated by a previous call to the `NCMBeginMatching` function. 
- [NCMDrawMatchedPicture](./colorsync_manager/api-1805223-ncmdrawmatchedpicture.md)
  Matches a picture’s colors to a destination device’s color gamut, as the picture is drawn, using the specified destination profile.
- [CMEnableMatchingComment](./colorsync_manager/api-1805227-cmenablematchingcomment.md)
  Inserts a comment into the currently open picture to turn matching on or off. 
- [NCMUseProfileComment](./colorsync_manager/api-1805229-ncmuseprofilecomment.md)
  Automatically embeds a profile or a profile identifier into an open picture.
### Registering Devices
- [CMRegisterColorDevice](./colorsync_manager/api-1805231-cmregistercolordevice.md)
  Registers a device with ColorSync.
- [CMUnregisterColorDevice](./colorsync_manager/api-1805234-cmunregistercolordevice.md)
  Unregisters a device.
### Accessing Default Devices
- [CMGetDefaultDevice](./colorsync_manager/api-1805235-cmgetdefaultdevice.md)
  Gets the default device.
- [CMSetDefaultDevice](./colorsync_manager/api-1805238-cmsetdefaultdevice.md)
  Sets the default device.
### Accessing Devices Profiles
- [CMGetDeviceFactoryProfiles](./colorsync_manager/api-1805240-cmgetdevicefactoryprofiles.md)
  Retrieves the original profiles for a given device. 
- [CMSetDeviceFactoryProfiles](./colorsync_manager/api-1805241-cmsetdevicefactoryprofiles.md)
  Establishes the profiles used by a given device. 
- [CMGetDeviceProfiles](./colorsync_manager/api-1805245-cmgetdeviceprofiles.md)
  Gets the profiles used by a given device.
- [CMSetDeviceProfiles](./colorsync_manager/api-1805247-cmsetdeviceprofiles.md)
  Changes the profiles used by a given device.
- [CMGetDeviceDefaultProfileID](./colorsync_manager/api-1805249-cmgetdevicedefaultprofileid.md)
  Gets the default profile ID for a given device. 
- [CMSetDeviceDefaultProfileID](./colorsync_manager/api-1805251-cmsetdevicedefaultprofileid.md)
  Sets the default profile ID for a given device. 
- [CMSetDeviceProfile](./colorsync_manager/api-1805253-cmsetdeviceprofile.md)
  Change the profile used by a given device. 
- [CMGetDeviceProfile](./colorsync_manager/api-1805256-cmgetdeviceprofile.md)
  Gets a profile used by a given device. 
### Accessing Device State and Information
- [CMGetDeviceState](./colorsync_manager/api-1805257-cmgetdevicestate.md)
  Gets the state of a device.
- [CMSetDeviceState](./colorsync_manager/api-1805258-cmsetdevicestate.md)
  Sets the state of a device.
- [CMGetDeviceInfo](./colorsync_manager/api-1805260-cmgetdeviceinfo.md)
  Gets information about a specified device.
### Iterating Over Devices and Device Profiles
- [CMIterateColorDevices](./colorsync_manager/api-1805262-cmiteratecolordevices.md)
  Iterates through the color devices available on the system, returning device information to a callback you supply.
- [CMIterateDeviceProfiles](./colorsync_manager/api-1805263-cmiteratedeviceprofiles.md)
  Iterates through the device profiles available on the system and returns information about profiles of the devices to a callback you supply.
### Working With Image Files
- [CMValidImage](./colorsync_manager/api-1805264-cmvalidimage.md)
  Validates the specified image file.
- [CMGetImageSpace](./colorsync_manager/api-1805267-cmgetimagespace.md)
  Returns the signature of the data color space in which the color values of colors in an image are expressed. 
- [CMEmbedImage](./colorsync_manager/api-1805269-cmembedimage.md)
  Embeds an image with an ICC profile. 
- [CMUnembedImage](./colorsync_manager/api-1805271-cmunembedimage.md)
  Removes any ICC profiles embedded in an image.
- [CMMatchImage](./colorsync_manager/api-1805273-cmmatchimage.md)
  Color matches an image file.
- [CMProofImage](./colorsync_manager/api-1805276-cmproofimage.md)
  Proofs an image.
- [CMLinkImage](./colorsync_manager/api-1805278-cmlinkimage.md)
  Matches an image file with a device link profile. 
- [CMCountImageProfiles](./colorsync_manager/api-1805281-cmcountimageprofiles.md)
  Obtains a count of the number of embedded profiles for a given image. 
- [CMGetIndImageProfile](./colorsync_manager/api-1805284-cmgetindimageprofile.md)
  Obtains a specific embedded profile for a given image. 
- [CMSetIndImageProfile](./colorsync_manager/api-1805286-cmsetindimageprofile.md)
  Sets a specific embedded profile for a given image. 
### Working With Video Card Lookup Tables
- [CMGetGammaByAVID](./colorsync_manager/api-1805289-cmgetgammabyavid.md)
  Obtains the gamma value for the specified display device.
- [CMSetGammaByAVID](./colorsync_manager/api-1805291-cmsetgammabyavid.md)
  Sets the gamma for the specified display device.
### Miscellaneous
- [CMGetColorSyncVersion](./colorsync_manager/api-1805293-cmgetcolorsyncversion.md)
  Gets ColorSync version information.
- [CMLaunchControlPanel](./colorsync_manager/api-1805294-cmlaunchcontrolpanel.md)
  Launches the ColorSync preferences pane.
### Not Recommended
- [CMNewProfileSearch](./colorsync_manager/api-1805344-cmnewprofilesearch.md)
  Searches the ColorSync Profiles folder and returns a list of 2.x profiles that match the search specification.
- [CMUpdateProfileSearch](./colorsync_manager/api-1805356-cmupdateprofilesearch.md)
  Searches the ColorSync Profiles folder and updates an existing search result obtained originally from the `CMNewProfileSearch` function.
- [CMDisposeProfileSearch](./colorsync_manager/api-1805358-cmdisposeprofilesearch.md)
  Frees the private memory allocated for a profile search after your application has completed the search. 
- [CMSearchGetIndProfile](./colorsync_manager/api-1805362-cmsearchgetindprofile.md)
  Opens the profile corresponding to a specific index into a specific search result list and obtains a reference to that profile. 
- [CMSearchGetIndProfileFileSpec](./colorsync_manager/api-1805365-cmsearchgetindprofilefilespec.md)
  Obtains the file specification for the profile at a specific index into a search result. 
- [CMCreateProfileIdentifier](./colorsync_manager/api-1805369-cmcreateprofileidentifier.md)
  Creates a profile identifier for a specified profile.
- [CMProfileIdentifierFolderSearch](./colorsync_manager/api-1805374-cmprofileidentifierfoldersearch.md)
  Searches the ColorSync Profiles folder and returns a list of profile references, one for each profile that matches the specified profile identifier.
- [CMProfileIdentifierListSearch](./colorsync_manager/api-1805376-cmprofileidentifierlistsearch.md)
  Searches a list of profile references and returns a list of all references that match a specified profile identifier. 

## See Also

### Managers
- [Apple Event Manager](./apple_event_manager.md)
- [Speech Synthesis Manager](./speech_synthesis_manager.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/colorsync_manager)*