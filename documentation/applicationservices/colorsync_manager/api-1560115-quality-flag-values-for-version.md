# Quality Flag Values for Version 2.x Profiles

**Framework**: Application Services

Define the possible values for the quality bits in the `flags` field of the `CM2Header` structure. 

#### Overview

To determine the value of the quality flag, you mask the `flags` field of the profile header with the `cmQualityMask` mask, right shift 16 bits, then compare the result to the enumerated constants shown here. For more information on the quality flag, see [`Flag Mask Definitions for Version 2.x Profiles`](colorsync_manager/1560699-flag_mask_definitions_for_versio.md).

When you start a color-matching session, ColorSync sends all involved profiles to the color management module (CMM). The CMM extracts the information it needs from the profiles and stores an internal representation in private memory. ColorSync’s default CMM samples the input space and stores the results in a lookup table, a common technique that speeds up conversion for runtime applications. The size of the table is based on the quality flag setting in the source profile header. The setting of the quality flag can affect the memory requirements, accuracy, and speed of the color-matching session. In general, the higher the quality setting, the larger the lookup table, the more accurate the matching, and the slower the matching process. Note however, that the default CMM currently produces the same results for both normal and draft mode. 

## Topics

### Constants
- [var cmNormalMode: Int](cmnormalmode.md)
  This is the default setting. Normal mode indicates that the CMM should use its default method to compromise between performance and resource requirements.
- [var cmDraftMode: Int](cmdraftmode.md)
  Draft mode indicates that the CMM should sacrifice quality, if necessary, to minimize resource requirements. Note that the default CMM currently produces the same results for both normal and draft mode.
- [var cmBestMode: Int](cmbestmode.md)
  Best mode indicates that the CMM should maximize resource usage to ensure the highest possible quality.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1560115-quality_flag_values_for_version_)*