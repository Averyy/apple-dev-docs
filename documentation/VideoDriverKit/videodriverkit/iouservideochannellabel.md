# IOUserVideoChannelLabel

**Framework**: VideoDriverKit  
**Kind**: enum

**Availability**:
- DriverKit 27.0+ (Beta)

## Declaration

```swift
enum IOUserVideoChannelLabel : uint32_t;
```

#### Overview

These constants are to set the preferred channel layout on an IOUserVideoDevice

These channel labels attempt to list all labels in common use. Due to the ambiguities in channel labeling by various groups, there may be some overlap or duplication in the labels below. Use the label which most clearly describes what you mean.

## Topics

### Left channels
- [Left](videodriverkit/iouservideochannellabel/left.md)
- [LeftCenter](videodriverkit/iouservideochannellabel/leftcenter.md)
- [LeftTopFront](videodriverkit/iouservideochannellabel/lefttopfront.md)
- [VerticalHeightLeft](videodriverkit/iouservideochannellabel/verticalheightleft.md)
  WAVE: “Top Front Left”
- [LeftTopMiddle](videodriverkit/iouservideochannellabel/lefttopmiddle.md)
- [LeftTopRear](videodriverkit/iouservideochannellabel/lefttoprear.md)
- [LeftTotal](videodriverkit/iouservideochannellabel/lefttotal.md)
  matrix encoded 4 channels
- [LeftWide](videodriverkit/iouservideochannellabel/leftwide.md)
### Right channels
- [Right](videodriverkit/iouservideochannellabel/right.md)
- [RightCenter](videodriverkit/iouservideochannellabel/rightcenter.md)
- [RightTopFront](videodriverkit/iouservideochannellabel/righttopfront.md)
- [VerticalHeightRight](videodriverkit/iouservideochannellabel/verticalheightright.md)
  WAVE: “Top Front Right”
- [RightTopMiddle](videodriverkit/iouservideochannellabel/righttopmiddle.md)
- [RightTopRear](videodriverkit/iouservideochannellabel/righttoprear.md)
- [RightTotal](videodriverkit/iouservideochannellabel/righttotal.md)
  matrix encoded 4 channels
- [RightWide](videodriverkit/iouservideochannellabel/rightwide.md)
### Center channels
- [Center](videodriverkit/iouservideochannellabel/center.md)
- [CenterTopFront](videodriverkit/iouservideochannellabel/centertopfront.md)
- [VerticalHeightCenter](videodriverkit/iouservideochannellabel/verticalheightcenter.md)
  WAVE: “Top Front Center”
- [CenterTopMiddle](videodriverkit/iouservideochannellabel/centertopmiddle.md)
- [CenterTopRear](videodriverkit/iouservideochannellabel/centertoprear.md)
### Back channels
- [TopBackCenter](videodriverkit/iouservideochannellabel/topbackcenter.md)
- [TopCenterSurround](videodriverkit/iouservideochannellabel/topcentersurround.md)
- [TopBackLeft](videodriverkit/iouservideochannellabel/topbackleft.md)
- [TopBackRight](videodriverkit/iouservideochannellabel/topbackright.md)
### Surround channels
- [CenterSurround](videodriverkit/iouservideochannellabel/centersurround.md)
  WAVE: “Back Center” or plain “Rear Surround”
- [CenterSurroundDirect](videodriverkit/iouservideochannellabel/centersurrounddirect.md)
  back center, non diffuse
- [LeftSurround](videodriverkit/iouservideochannellabel/leftsurround.md)
- [LeftSurroundDirect](videodriverkit/iouservideochannellabel/leftsurrounddirect.md)
- [RearSurroundLeft](videodriverkit/iouservideochannellabel/rearsurroundleft.md)
- [RearSurroundRight](videodriverkit/iouservideochannellabel/rearsurroundright.md)
- [RightSurround](videodriverkit/iouservideochannellabel/rightsurround.md)
- [RightSurroundDirect](videodriverkit/iouservideochannellabel/rightsurrounddirect.md)
### Low-Frequency Effects channels
- [LFE2](videodriverkit/iouservideochannellabel/lfe2.md)
- [LFEScreen](videodriverkit/iouservideochannellabel/lfescreen.md)
### Monaural channels
- [Mono](videodriverkit/iouservideochannellabel/mono.md)
### Alternate content channels
- [ClickTrack](videodriverkit/iouservideochannellabel/clicktrack.md)
- [DialogCentricMix](videodriverkit/iouservideochannellabel/dialogcentricmix.md)
- [ForeignLanguage](videodriverkit/iouservideochannellabel/foreignlanguage.md)
- [HearingImpaired](videodriverkit/iouservideochannellabel/hearingimpaired.md)
- [Haptic](videodriverkit/iouservideochannellabel/haptic.md)
- [Narration](videodriverkit/iouservideochannellabel/narration.md)
### Mid/side recording
- [MS_Mid](videodriverkit/iouservideochannellabel/ms_mid.md)
- [MS_Side](videodriverkit/iouservideochannellabel/ms_side.md)
### X/Y recording channels
- [XY_X](videodriverkit/iouservideochannellabel/xy_x.md)
- [XY_Y](videodriverkit/iouservideochannellabel/xy_y.md)
### First-order ambisonic channels
- [Ambisonic_W](videodriverkit/iouservideochannellabel/ambisonic_w.md)
- [Ambisonic_X](videodriverkit/iouservideochannellabel/ambisonic_x.md)
- [Ambisonic_Y](videodriverkit/iouservideochannellabel/ambisonic_y.md)
- [Ambisonic_Z](videodriverkit/iouservideochannellabel/ambisonic_z.md)
### Binaural recording
- [BinauralLeft](videodriverkit/iouservideochannellabel/binauralleft.md)
- [BinauralRight](videodriverkit/iouservideochannellabel/binauralright.md)
### Headphone channels
- [HeadphonesLeft](videodriverkit/iouservideochannellabel/headphonesleft.md)
- [HeadphonesRight](videodriverkit/iouservideochannellabel/headphonesright.md)
### Unnumbered discrete channels
- [Discrete](videodriverkit/iouservideochannellabel/discrete.md)
### Numbered discrete channels
- [Discrete_0](videodriverkit/iouservideochannellabel/discrete_0.md)
- [Discrete_1](videodriverkit/iouservideochannellabel/discrete_1.md)
- [Discrete_2](videodriverkit/iouservideochannellabel/discrete_2.md)
- [Discrete_3](videodriverkit/iouservideochannellabel/discrete_3.md)
- [Discrete_4](videodriverkit/iouservideochannellabel/discrete_4.md)
- [Discrete_5](videodriverkit/iouservideochannellabel/discrete_5.md)
- [Discrete_6](videodriverkit/iouservideochannellabel/discrete_6.md)
- [Discrete_7](videodriverkit/iouservideochannellabel/discrete_7.md)
- [Discrete_8](videodriverkit/iouservideochannellabel/discrete_8.md)
- [Discrete_9](videodriverkit/iouservideochannellabel/discrete_9.md)
- [Discrete_10](videodriverkit/iouservideochannellabel/discrete_10.md)
- [Discrete_11](videodriverkit/iouservideochannellabel/discrete_11.md)
- [Discrete_12](videodriverkit/iouservideochannellabel/discrete_12.md)
- [Discrete_13](videodriverkit/iouservideochannellabel/discrete_13.md)
- [Discrete_14](videodriverkit/iouservideochannellabel/discrete_14.md)
- [Discrete_15](videodriverkit/iouservideochannellabel/discrete_15.md)
- [Discrete_65535](videodriverkit/iouservideochannellabel/discrete_65535.md)
### Generic high order ambisonics ACN channel
- [HOA_ACN](videodriverkit/iouservideochannellabel/hoa_acn.md)
### Numbered high order ambisonics ACN channels
- [HOA_ACN_0](videodriverkit/iouservideochannellabel/hoa_acn_0.md)
- [HOA_ACN_1](videodriverkit/iouservideochannellabel/hoa_acn_1.md)
- [HOA_ACN_2](videodriverkit/iouservideochannellabel/hoa_acn_2.md)
- [HOA_ACN_3](videodriverkit/iouservideochannellabel/hoa_acn_3.md)
- [HOA_ACN_4](videodriverkit/iouservideochannellabel/hoa_acn_4.md)
- [HOA_ACN_5](videodriverkit/iouservideochannellabel/hoa_acn_5.md)
- [HOA_ACN_6](videodriverkit/iouservideochannellabel/hoa_acn_6.md)
- [HOA_ACN_7](videodriverkit/iouservideochannellabel/hoa_acn_7.md)
- [HOA_ACN_8](videodriverkit/iouservideochannellabel/hoa_acn_8.md)
- [HOA_ACN_9](videodriverkit/iouservideochannellabel/hoa_acn_9.md)
- [HOA_ACN_10](videodriverkit/iouservideochannellabel/hoa_acn_10.md)
- [HOA_ACN_11](videodriverkit/iouservideochannellabel/hoa_acn_11.md)
- [HOA_ACN_12](videodriverkit/iouservideochannellabel/hoa_acn_12.md)
- [HOA_ACN_13](videodriverkit/iouservideochannellabel/hoa_acn_13.md)
- [HOA_ACN_14](videodriverkit/iouservideochannellabel/hoa_acn_14.md)
- [HOA_ACN_15](videodriverkit/iouservideochannellabel/hoa_acn_15.md)
- [HOA_ACN_65024](videodriverkit/iouservideochannellabel/hoa_acn_65024.md)
### Special values
- [Unused](videodriverkit/iouservideochannellabel/unused.md)
  channel is present, but has no intended use or destination
- [Unknown](videodriverkit/iouservideochannellabel/unknown.md)
  unknown or unspecified other use
- [UseCoordinates](videodriverkit/iouservideochannellabel/usecoordinates.md)
  channel is described by the mCoordinates fields.
### Reserved values
- [BeginReserved](videodriverkit/iouservideochannellabel/beginreserved.md)
- [EndReserved](videodriverkit/iouservideochannellabel/endreserved.md)

## See Also

- [SetPreferredChannelsForStereo](iouservideodevice/setpreferredchannelsforstereo.md)
- [GetPreferredChannelsForStereo](iouservideodevice/getpreferredchannelsforstereo.md)
- [SetPreferredInputChannelLayout](iouservideodevice/setpreferredinputchannellayout.md)
- [SetPreferredOutputChannelLayout](iouservideodevice/setpreferredoutputchannellayout.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/videodriverkit/videodriverkit/iouservideochannellabel)*