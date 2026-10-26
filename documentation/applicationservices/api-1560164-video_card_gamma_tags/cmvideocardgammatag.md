# cmVideoCardGammaTag

**Framework**: Application Services  
**Kind**: econst  
**Role**: Enumeration Case

**Availability**:
- macOS 10.0+

## Declaration

```c
cmVideoCardGammaTag = 'vcgt'
```

#### Discussion

Constant for profile tag that specifies video card gamma information. When you create a tag to store video card gamma data in a profile, you use the `cmVideoCardGammaTag` constant to specify the tag.

Starting with version 2.5, ColorSync supports an optional profile tag for video card gamma. The tag specifies gamma information, stored either as a formula or in table format, to be loaded into the video card when the profile containing the tag is put into use. As of version 2.5, the only ColorSync function that attempts to take advantage of video card gamma data is [CMSetProfileByAVID](../colorsync_manager/api-1804959-cmsetprofilebyavid.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/1560164-video_card_gamma_tags/cmvideocardgammatag)*