# kIOAudioControlChannelNameKey

**Framework**: Kernel  
**Kind**: macro  
**Role**: Macro

The key in the IORegistry for the IOAudioControl name attribute.

**Availability**:
- macOS 10.1+

## Declaration

```c
#define kIOAudioControlChannelNameKey
```

#### Discussion

This name should be a human-readable name for the channel(s) represented by the port. *** NOTE *** We really need to make all of the human-readable attributes that have potential to be used in a GUI localizable. There will need to be localized strings in the kext bundle matching the text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/kioaudiocontrolchannelnamekey)*