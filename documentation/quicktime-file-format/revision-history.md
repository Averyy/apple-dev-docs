# QuickTime File Format change log

**Framework**: QuickTime File Format

Changes to the QuickTime File Format.

#### Overview

##### 2016 09 13

###### Updated

- Updated the color atom (`'colr'`) to include information on new color standards, including DCI P3, P3 D65, and ITU-R BT.2020.

##### 2015 02 14

###### Added

- A new facility for timed metadata tracks has been incorporated, see [`Timed metadata media`](timed_metadata_media.md). Introduce `'cdsc'` track reference type, see [`Track reference type atom`](track_reference_type_atom.md). Added more well-known metadata data types, see [`Type indicator`](type_indicator.md).

##### 2014 02 11

###### Updated

- Updated the section on closed caption tracks.

##### 2012 08 14

###### Updated

- Corrected the values for `kQTSampleDependency_OtherSamplesDependOnThisSample` and `kQTSampleDependency_-NoOtherSampleDependsOnThisSample`.

##### 2012 08 01

###### Added

- Added [`Track exclude from autoselection atom ('txas')`](track_exclude_from_autoselection_atom.md).
- Added `clcp`, `fall`, `folw`, and `forc` to [`Track reference type atom`](track_reference_type_atom.md).
- Added [`Text media information atom ('text')`](text_media_information_atom.md), [`Closed captioning media`](closed_captioning_media.md), and [`Subtitle media`](subtitle_media.md).
- Added [`Preparing sound and subtitle alternate groups for use with Apple devices`](preparing_sound_and_subtitle_alternate_groups_for_use_with_apple_devices.md).

###### Updated

- In [`User data atoms`](user_data_atoms.md), expanded the description of `'tnam'` and added `'tagc'` with related section Media Characteristic Tags.
- Explained alternate groups in [`Alternate group`](track_header_atom/alternate_group.md).
- Corrected structure of `gmhd` and `gmin` in [`Base media information atom ('minf')`](base_media_information_atom.md).
- General Structure of a Sample Description in [`Sample description atom ('stsd')`](sample_description_atom.md) includes emphasized importance of data size due to occasional terminating zeroes.
- [`Timecode media information atom ('tcmi')`](timecode_media_information_atom.md) now documents the reserved integer after the text size.
- “Audio track” changed to “sound track” for consistency.

###### Deprecated

- Deprecated `‘rsrc’` data reference.

##### 2011 07 13

###### Added

- The sound sample description v2 format along with the definition of two new sound sample description extensions, see [`Sound sample description version 2 ('stsd')`](sound_sample_description_version_2.md).
- New atoms for the display of track aperture in different modes, see [`Track aperture mode dimensions atom ('tapt')`](track_aperture_mode_dimensions_atom.md).
- New sample atoms for handling out-of-order movie samples, see [`Sample atoms`](sample_atoms.md).
- [`Audio priming-handling encoder delay in AAC`](appendix_g_audio_priming_handling_encoder_delay_in_aac.md), which treats how to handle temporal positioning of AAC audio data explicitly.

###### Updated

- The Macintosh language codes table has been updated with current language names, see [`Language code values`](language_code_values.md) and the related [`Extended language tag atom ('elng')`](extended_language_tag_atom.md) defined.

##### 2010 08 03

###### Updated

- Corrected the order of fields described in the [`Metadata handler atom ('hdlr')`](metadata_handler_atom.md) structure.

##### 2010 05 03

###### Added

- Added description of clip-based metadata and specific key/value pairs for location metadata.

##### 2007 09 04

###### Added

- First public release of complete, updated  with information about atoms and atom types.
- Added licensing information and disclaimer for developers.
- A QuickTime file may now contain a file type compatibility atom. See [`File type compatibility atom ('ftyp')`](file_type_compatibility_atom.md).
- A movie atom may now contain a movie profile atom. See [`Movie profile atom ('prfl')`](movie_profile_atom.md).
- A track atom may now contain a track profile atom. See [`Track profile atom ('prfl')`](track_profile_atom.md).
- Video sample descriptions may now contain a pixel aspect ratio atom for non-square pixels. See [`Pixel aspect ratio ('pasp')`](pixel_aspect_ratio.md) (`'pasp'`).
- Video sample descriptions may now also contain a color parameter atom. See [`Color parameter atom ('colr')`](color_parameter_atom.md) (`'colr'`).
- Video sample descriptions may now a clean aperture atom. See [`Clean aperture ('clap')`](clean_aperture.md) (`'clap'`).
- MPEG-4 video and audio sample descriptions may now contain elementary stream descriptor atoms. See [`MPEG-4 elementary stream descriptor atom ('esds')`](mpeg-4_elementary_stream_descriptor_atom.md) (`'esds'`) and [`MPEG-4 elementary stream descriptor atom  ('esds')`](mpeg-4_elementary_sound_stream_descriptor_atom.md) (`'esds'`).

###### Updated

- Modified introductory sections and atom descriptions; updated artwork and edited for technical accuracy.
- The sound description record has been expanded to represent variable bit-rate compression more accurately. See [`Sound sample descriptions`](sound_sample_descriptions.md).
- The section describing MPEG-4 audio has been modified. See MPEG-4 Audio in [`Sound sample data`](sound_sample_data.md).
- It is now recommended that the file creation and modification times be set using UTC, rather than local time zones. See [`Calendar date and time values`](calendar_date_and_time_values.md).
- User data text may now be encoded using either Macintosh text encoding or ISO text encoding (Unicode). See User Data Text Strings and Language Codes in [`User data atoms`](user_data_atoms.md).
- It is now possible to specify languages using either Macintosh language codes or ISO language codes. See [`Language code values`](language_code_values.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicktime-file-format/revision_history)*