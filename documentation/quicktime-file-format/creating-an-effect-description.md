# Creating an effect description

**Framework**: QuickTime File Format

Tell QuickTime which effect to execute and control how the effect behaves at runtime with an effect description.

#### Overview

An effect description tells QuickTime which effect to execute and contains the parameters that control how the effect behaves at runtime. You create an effect description by creating an atom container, inserting a QT atom that specifies the effect, and inserting a set of QT atoms that set its parameters.

There are support functions you can call to assist you in this process. `QTCreateStandardParameterDialog` returns a complete effect description that you can use, including user-selected settings; you only need to add `kEffectSourceName` atoms to the description for effects that require sources. At a lower level, `QTGetEffectsList` returns a list of the available effects and `ImageCodecGetParameterList` will return a description of the parameters for an effect, including the default value for each parameter in the form of a QT atom that can be inserted directly into an effect description.

## Topics

### Effect descriptions
- [Structure of an effect description](structure_of_an_effect_description.md)
  An effect description is the sole media sample for an effect track.
- [Required atoms of an effects description](required_atoms_of_an_effects_description.md)
  Specify the required atoms for your effects description.
- [Parameter atoms of an effects description](parameter_atoms_of_an_effects_description.md)
  Customize your effect with parameter atoms.
- [Creating an input map](creating_an_input_map.md)
  Describe and name sources with an input map.

## See Also

- [Preparing sound and subtitle alternate groups for use with Apple devices](preparing_sound_and_subtitle_alternate_groups_for_use_with_apple_devices.md)
  Create collections of tracks that all serve the same purpose, where any track in the group can be substituted for another in a movie.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicktime-file-format/creating_an_effect_description)*