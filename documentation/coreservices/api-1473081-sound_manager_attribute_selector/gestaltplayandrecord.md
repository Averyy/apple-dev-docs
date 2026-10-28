# gestaltPlayAndRecord

**Framework**: Core Services  
**Kind**: econst  
**Role**: Enumeration Case

**Availability**:
- Mac Catalyst 17.0+
- macOS 10.0+

## Declaration

```c
gestaltPlayAndRecord = 6
```

## Discussion

Set if the built-in sound hardware is able to play and record sounds simultaneously. If this bit is clear, the built-in sound hardware can either play or record, but not do both at once. This bit is valid only if the `gestaltBuiltInSoundInput` bit is set, and it applies only to any built-in sound input and output hardware.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1473081-sound_manager_attribute_selector/gestaltplayandrecord)*