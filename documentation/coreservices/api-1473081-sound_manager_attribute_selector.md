# Sound Manager Attribute Selectors

**Framework**: Core Services  
**Kind**: enum  
**Role**: Enumeration

Specify feature availability information for the Sound Manager.

**Availability**:
- Mac Catalyst 17.0+
- macOS 10.0+

## Declaration

```c
enum : unsigned int {
    ...
};
```

## Topics

### Constants
- [gestaltSoundAttr](./api-1473081-sound_manager_attribute_selector/gestaltsoundattr.md)
  The Gestalt selector which you pass to the `Gestalt` function.
- [gestaltStereoCapability](./api-1473081-sound_manager_attribute_selector/gestaltstereocapability.md)
  Set if the built-in sound hardware is able to produce stereo sounds.
- [gestaltStereoMixing](./api-1473081-sound_manager_attribute_selector/gestaltstereomixing.md)
  Set if the built-in sound hardware mixes both left and right channels of stereo sound into a single audio signal for the internal speaker.
- [gestaltSoundIOMgrPresent](./api-1473081-sound_manager_attribute_selector/gestaltsoundiomgrpresent.md)
  Set if the Sound Input Manager is available.
- [gestaltBuiltInSoundInput](./api-1473081-sound_manager_attribute_selector/gestaltbuiltinsoundinput.md)
  Set if a built-in sound input device is available.
- [gestaltHasSoundInputDevice](./api-1473081-sound_manager_attribute_selector/gestalthassoundinputdevice.md)
  Set if a sound input device is available. This device can be either built-in or external.
- [gestaltPlayAndRecord](./api-1473081-sound_manager_attribute_selector/gestaltplayandrecord.md)
- [gestalt16BitSoundIO](./api-1473081-sound_manager_attribute_selector/gestalt16bitsoundio.md)
- [gestaltStereoInput](./api-1473081-sound_manager_attribute_selector/gestaltstereoinput.md)
- [gestaltLineLevelInput](./api-1473081-sound_manager_attribute_selector/gestaltlinelevelinput.md)
- [gestaltSndPlayDoubleBuffer](./api-1473081-sound_manager_attribute_selector/gestaltsndplaydoublebuffer.md)
- [gestaltMultiChannels](./api-1473081-sound_manager_attribute_selector/gestaltmultichannels.md)
- [gestalt16BitAudioSupport](./api-1473081-sound_manager_attribute_selector/gestalt16bitaudiosupport.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1473081-sound_manager_attribute_selector)*