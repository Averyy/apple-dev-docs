# IOUserVideoChannelLabel

**Framework**: VideoDriverKit  
**Kind**: enum  
**Role**: Enumeration

These constants are to set the preferred channel layout on video device.

**Availability**:
- DriverKit 27.0+

## Declaration

```c
enum IOUserVideoChannelLabel : uint32_t;
```

## Overview

These channel labels attempt to list all labels in common use. Due to the ambiguities in channel labeling by various groups, there may be some overlap or duplication in the labels below. Use the label which most clearly describes what you mean.

## Topics

### Left channels
- [Left](./iouservideochannellabel/left.md)
- [LeftCenter](./iouservideochannellabel/leftcenter.md)
- [LeftTopFront](./iouservideochannellabel/lefttopfront.md)
- [VerticalHeightLeft](./iouservideochannellabel/verticalheightleft.md)
  WAVE: “Top Front Left”
- [LeftTopMiddle](./iouservideochannellabel/lefttopmiddle.md)
- [LeftTopRear](./iouservideochannellabel/lefttoprear.md)
- [LeftTotal](./iouservideochannellabel/lefttotal.md)
  matrix encoded 4 channels
- [LeftWide](./iouservideochannellabel/leftwide.md)
### Right channels
- [Right](./iouservideochannellabel/right.md)
- [RightCenter](./iouservideochannellabel/rightcenter.md)
- [RightTopFront](./iouservideochannellabel/righttopfront.md)
- [VerticalHeightRight](./iouservideochannellabel/verticalheightright.md)
  WAVE: “Top Front Right”
- [RightTopMiddle](./iouservideochannellabel/righttopmiddle.md)
- [RightTopRear](./iouservideochannellabel/righttoprear.md)
- [RightTotal](./iouservideochannellabel/righttotal.md)
  matrix encoded 4 channels
- [RightWide](./iouservideochannellabel/rightwide.md)
### Center channels
- [Center](./iouservideochannellabel/center.md)
- [CenterTopFront](./iouservideochannellabel/centertopfront.md)
- [VerticalHeightCenter](./iouservideochannellabel/verticalheightcenter.md)
  WAVE: “Top Front Center”
- [CenterTopMiddle](./iouservideochannellabel/centertopmiddle.md)
- [CenterTopRear](./iouservideochannellabel/centertoprear.md)
### Back channels
- [TopBackCenter](./iouservideochannellabel/topbackcenter.md)
- [TopCenterSurround](./iouservideochannellabel/topcentersurround.md)
- [TopBackLeft](./iouservideochannellabel/topbackleft.md)
- [TopBackRight](./iouservideochannellabel/topbackright.md)
### Surround channels
- [CenterSurround](./iouservideochannellabel/centersurround.md)
  WAVE: “Back Center” or plain “Rear Surround”
- [CenterSurroundDirect](./iouservideochannellabel/centersurrounddirect.md)
  back center, non diffuse
- [LeftSurround](./iouservideochannellabel/leftsurround.md)
- [LeftSurroundDirect](./iouservideochannellabel/leftsurrounddirect.md)
- [RearSurroundLeft](./iouservideochannellabel/rearsurroundleft.md)
- [RearSurroundRight](./iouservideochannellabel/rearsurroundright.md)
- [RightSurround](./iouservideochannellabel/rightsurround.md)
- [RightSurroundDirect](./iouservideochannellabel/rightsurrounddirect.md)
### Low-Frequency Effects channels
- [LFE2](./iouservideochannellabel/lfe2.md)
- [LFEScreen](./iouservideochannellabel/lfescreen.md)
### Monaural channels
- [Mono](./iouservideochannellabel/mono.md)
### Alternate content channels
- [ClickTrack](./iouservideochannellabel/clicktrack.md)
- [DialogCentricMix](./iouservideochannellabel/dialogcentricmix.md)
- [ForeignLanguage](./iouservideochannellabel/foreignlanguage.md)
- [HearingImpaired](./iouservideochannellabel/hearingimpaired.md)
- [Haptic](./iouservideochannellabel/haptic.md)
- [Narration](./iouservideochannellabel/narration.md)
### Mid/side recording
- [MS_Mid](./iouservideochannellabel/ms_mid.md)
- [MS_Side](./iouservideochannellabel/ms_side.md)
### X/Y recording channels
- [XY_X](./iouservideochannellabel/xy_x.md)
- [XY_Y](./iouservideochannellabel/xy_y.md)
### First-order ambisonic channels
- [Ambisonic_W](./iouservideochannellabel/ambisonic_w.md)
- [Ambisonic_X](./iouservideochannellabel/ambisonic_x.md)
- [Ambisonic_Y](./iouservideochannellabel/ambisonic_y.md)
- [Ambisonic_Z](./iouservideochannellabel/ambisonic_z.md)
### Binaural recording
- [BinauralLeft](./iouservideochannellabel/binauralleft.md)
- [BinauralRight](./iouservideochannellabel/binauralright.md)
### Headphone channels
- [HeadphonesLeft](./iouservideochannellabel/headphonesleft.md)
- [HeadphonesRight](./iouservideochannellabel/headphonesright.md)
### Unnumbered discrete channels
- [Discrete](./iouservideochannellabel/discrete.md)
### Numbered discrete channels
- [Discrete_0](./iouservideochannellabel/discrete_0.md)
- [Discrete_1](./iouservideochannellabel/discrete_1.md)
- [Discrete_2](./iouservideochannellabel/discrete_2.md)
- [Discrete_3](./iouservideochannellabel/discrete_3.md)
- [Discrete_4](./iouservideochannellabel/discrete_4.md)
- [Discrete_5](./iouservideochannellabel/discrete_5.md)
- [Discrete_6](./iouservideochannellabel/discrete_6.md)
- [Discrete_7](./iouservideochannellabel/discrete_7.md)
- [Discrete_8](./iouservideochannellabel/discrete_8.md)
- [Discrete_9](./iouservideochannellabel/discrete_9.md)
- [Discrete_10](./iouservideochannellabel/discrete_10.md)
- [Discrete_11](./iouservideochannellabel/discrete_11.md)
- [Discrete_12](./iouservideochannellabel/discrete_12.md)
- [Discrete_13](./iouservideochannellabel/discrete_13.md)
- [Discrete_14](./iouservideochannellabel/discrete_14.md)
- [Discrete_15](./iouservideochannellabel/discrete_15.md)
- [Discrete_65535](./iouservideochannellabel/discrete_65535.md)
### Generic high order ambisonics ACN channel
- [HOA_ACN](./iouservideochannellabel/hoa_acn.md)
### Numbered high order ambisonics ACN channels
- [HOA_ACN_0](./iouservideochannellabel/hoa_acn_0.md)
- [HOA_ACN_1](./iouservideochannellabel/hoa_acn_1.md)
- [HOA_ACN_2](./iouservideochannellabel/hoa_acn_2.md)
- [HOA_ACN_3](./iouservideochannellabel/hoa_acn_3.md)
- [HOA_ACN_4](./iouservideochannellabel/hoa_acn_4.md)
- [HOA_ACN_5](./iouservideochannellabel/hoa_acn_5.md)
- [HOA_ACN_6](./iouservideochannellabel/hoa_acn_6.md)
- [HOA_ACN_7](./iouservideochannellabel/hoa_acn_7.md)
- [HOA_ACN_8](./iouservideochannellabel/hoa_acn_8.md)
- [HOA_ACN_9](./iouservideochannellabel/hoa_acn_9.md)
- [HOA_ACN_10](./iouservideochannellabel/hoa_acn_10.md)
- [HOA_ACN_11](./iouservideochannellabel/hoa_acn_11.md)
- [HOA_ACN_12](./iouservideochannellabel/hoa_acn_12.md)
- [HOA_ACN_13](./iouservideochannellabel/hoa_acn_13.md)
- [HOA_ACN_14](./iouservideochannellabel/hoa_acn_14.md)
- [HOA_ACN_15](./iouservideochannellabel/hoa_acn_15.md)
- [HOA_ACN_65024](./iouservideochannellabel/hoa_acn_65024.md)
### Special values
- [Unused](./iouservideochannellabel/unused.md)
  channel is present, but has no intended use or destination
- [Unknown](./iouservideochannellabel/unknown.md)
  unknown or unspecified other use
- [UseCoordinates](./iouservideochannellabel/usecoordinates.md)
  channel is described by the mCoordinates fields.
### Reserved values
- [BeginReserved](./iouservideochannellabel/beginreserved.md)
- [EndReserved](./iouservideochannellabel/endreserved.md)

## See Also

### Working with channel layouts
- [SetPreferredChannelsForStereo](../iouservideodevice/setpreferredchannelsforstereo.md)
  Sets the channel indices for the preferred stereo pair
- [GetPreferredChannelsForStereo](../iouservideodevice/getpreferredchannelsforstereo.md)
  Gets the channel indices for the preferred stereo pair.
- [SetPreferredInputChannelLayout](../iouservideodevice/setpreferredinputchannellayout.md)
  Sets the input channel layout with IOUserVideoChannelLabel values
- [SetPreferredOutputChannelLayout](../iouservideodevice/setpreferredoutputchannellayout.md)
  Sets the output channel layout.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/videodriverkit/iouservideochannellabel)*