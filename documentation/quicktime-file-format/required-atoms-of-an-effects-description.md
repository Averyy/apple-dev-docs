# Required atoms of an effects description

**Framework**: QuickTime File Format

Specify the required atoms for your effects description.

#### Overview

There are several required atoms that an effect description must contain. The first is the `kParameterWhatName` atom. The `kParameterWhatName` atom contains the name of the effect. This specifies which of the available effects to use.

The code snippet shown in the following listing adds a `kParameterWhatName` atom to the atom container `effectDescription`. The constant `kCrossFadeTransitionType` contains the name of the cross-fade effect.

```c
effectCode = kCrossFadeTransitionType;
QTInsertChild(effectDescription, kParentAtomIsContainer,
                kParameterWhatName, kParameterWhatID, 0,
                sizeof(effectCode), &effectCode, nil);
```

In addition to the `kParameterWhatName` atom, the effect description for an effect that uses sources must contain one or more `kEffectSourceName` atoms. Each of these atoms contains the name of one of the effect’s sources. An input map is used to map these names to the actual tracks of the movie that are the sources. [`Creating an input map`](creating_an_input_map.md) describes how to create the input map.

## See Also

- [Structure of an effect description](structure_of_an_effect_description.md)
  An effect description is the sole media sample for an effect track.
- [Parameter atoms of an effects description](parameter_atoms_of_an_effects_description.md)
  Customize your effect with parameter atoms.
- [Creating an input map](creating_an_input_map.md)
  Describe and name sources with an input map.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicktime-file-format/required_atoms_of_an_effects_description)*