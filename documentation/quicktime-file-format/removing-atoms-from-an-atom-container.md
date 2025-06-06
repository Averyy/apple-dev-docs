# Removing atoms from an atom container

**Framework**: QuickTime File Format

Remove atoms from an atom container.

#### Overview

To remove atoms from an atom container, you can use the `QTRemoveAtom` and `QTRemoveChildren` functions. The `QTRemoveAtom` function removes an atom and its children, if any, from a container. The `QTRemoveChildren` function removes an atom’s children from a container, but does not remove the atom itself. You can also use `QTRemoveChildren` to remove all the atoms in an atom container. To do so, pass the constant `kParentAtomIsContainer` for the `atom` parameter.

The code sample shown in the following listing adds override samples to a sprite track to animate the sprites in the sprite track. The `sample` and `spriteData` variables are atom containers. The `spriteData` atom container contains atoms that describe a single sprite. The `sample` atom container contains atoms that describe an override sample.

Each iteration of the `for` loop calls `QTRemoveChildren` to remove all atoms from both the `sample` and the `spriteData` containers. The sample code updates the index of the image to be used for the sprite and the sprite’s location and calls `SetSpriteData`, which adds the appropriate atoms to the `spriteData` atom container. Then, the sample code calls `AddSpriteToSample` to add the `spriteData` atom container to the `sample` atom container. Finally, when all the sprites have been updated, the sample code calls `AddSpriteSampleToMedia` to add the override sample to the sprite track.

```c
QTAtomContainer sample, spriteData;
 
// ...
// Add the sprite key sample.
// ...
 
// Add override samples to make the sprites spin and move.
for (i = 1; i <= kNumOverrideSamples; i++)
{
    QTRemoveChildren (sample, kParentAtomIsContainer);
    QTRemoveChildren (spriteData, kParentAtomIsContainer);
 
    // ...
    // Update the sprite:
    // - Update the imageIndex.
    // - Update the location.
    // ...
 
    // Add atoms to spriteData atom container.
    SetSpriteData (spriteData, &location, nil, nil, &imageIndex);
 
    // Add the spriteData atom container to sample.
    err = AddSpriteToSample (sample, spriteData, 2);
 
    // ...
    // Update other sprites.
    // ...
 
    // Add the sample to the media.
    err = AddSpriteSampleToMedia (newMedia, sample,
        kSpriteMediaFrameDuration, false);
}
```

## See Also

- [Creating new atoms](creating_new_atoms.md)
  Create new atoms and insert them in a QT atom container.
- [Copying existing atoms](copying_existing_atoms.md)
  Copy existing atoms within an atom container.
- [Retrieving atoms from an atom container](retrieving_atoms_from_an_atom_container.md)
  Retrieve information about the types of a parent atom’s children, search for a specific atom, and retrieve a leaf atom’s data.
- [Modifying atoms](modifying_atoms.md)
  Modify attributes or data associated with an atom in an atom container.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicktime-file-format/removing_atoms_from_an_atom_container)*