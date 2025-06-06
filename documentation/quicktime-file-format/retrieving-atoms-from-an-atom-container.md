# Retrieving atoms from an atom container

**Framework**: QuickTime File Format

Retrieve information about the types of a parent atom’s children, search for a specific atom, and retrieve a leaf atom’s data.

#### Overview

QuickTime provides functions you can use to retrieve information about the types of a parent atom’s children, to search for a specific atom, and to retrieve a leaf atom’s data.

You can use the `QTCountChildrenOfType` and `QTGetNextChildType` functions to retrieve information about the types of an atom’s children. The `QTCountChildrenOfType` function returns the number of children of a given atom type for a parent atom. The `QTGetNextChildType` function returns the next atom type in the child list of a parent atom.

You can use the `QTFindChildByIndex`, `QTFindChildByID`, and `QTNextChildAnyType` functions to retrieve an atom. You call the `QTFindChildByIndex` function to search for and retrieve a parent atom’s child by its type and index within that type.

The following listing shows the sample code function `SetSpriteData`, which updates an atom container that describes a sprite. For each property of the sprite that needs to be updated, `SetSpriteData` calls `QTFindChildByIndex` to retrieve the appropriate atom from the atom container. If the atom is found, `SetSpriteData` calls `QTSetAtomData` to replace the atom’s data with the new value of the property. If the atom is not found, `SetSpriteData` calls `QTInsertChild` to add a new atom for the property.

```c
OSErr SetSpriteData (QTAtomContainer sprite, Point *location,
    short *visible, short *layer, short *imageIndex)
{
    OSErr err = noErr;
    QTAtom propertyAtom;
 
    // Check if the sprite’s visible property has a new value.
    if (visible)
    {
        // Retrieve the atom for the visible property.
        // If none exists, insert one.
        if ((propertyAtom = QTFindChildByIndex (sprite,
            kParentAtomIsContainer, kSpritePropertyVisible, 1,
            nil)) == 0)
            FailOSErr (QTInsertChild (sprite, kParentAtomIsContainer,
                kSpritePropertyVisible, 1, 1, sizeof(short), visible,
                nil))
 
        // If an atom does exist, update its data.
        else
            FailOSErr (QTSetAtomData (sprite, propertyAtom,
                sizeof(short), visible));
    }
 
    // ...
    // Handle other sprite properties.
    // ...
}
```

You can call the `QTFindChildByID` function to search for and retrieve a parent atom’s child by its type and ID. The sample code function `AddSpriteToSample`, shown in the following listing, adds a sprite, represented by an atom container, to a key sample, represented by another atom container. `AddSpriteToSample` calls `QTFindChildByID` to determine whether the atom container `theSample` contains an atom of type `kSpriteAtomType` with the ID `spriteID`. If not, `AddSpriteToSample` calls `QTInsertChild` to insert an atom with that type and ID. A value of `0` is passed for the index parameter to indicate that the atom should be inserted at the end of the child list. A value of `0` is passed for the `dataSize` parameter to indicate that the atom does not have any data. Then, `AddSpriteToSample` calls `QTInsertChildren` to insert the atoms in the container `theSprite` as children of the new atom. `FailIf` and `FailOSErr` are macros that exit the current function when an error occurs.

```c
OSErr AddSpriteToSample (QTAtomContainer theSample,
    QTAtomContainer theSprite, short spriteID)
{
    OSErr err = noErr;
    QTAtom newSpriteAtom;
 
    FailIf (QTFindChildByID (theSample, kParentAtomIsContainer,
        kSpriteAtomType, spriteID, nil), paramErr);
 
    FailOSErr (QTInsertChild (theSample, kParentAtomIsContainer,
        kSpriteAtomType, spriteID, 0, 0, nil, &newSpriteAtom));
    FailOSErr (QTInsertChildren (theSample, newSpriteAtom, theSprite));
}
```

Once you have retrieved a child atom, you can call `QTNextChildAnyType` function to retrieve subsequent children of a parent atom. `QTNextChildAnyType` returns an offset to the next atom of any type in a parent atom’s child list. This function is useful for iterating through a parent atom’s children quickly.

QuickTime also provides functions for retrieving an atom’s type, ID, and data. You can call `QTGetAtomTypeAndID` function to retrieve an atom’s type and ID. You can access an atom’s data in one of three ways.

- To copy an atom’s data to a handle, you can use the `QTCopyAtomDataToHandle` function.
- To copy an atom’s data to a pointer, you can use the `QTCopyAtomDataToPtr` function.
- To access an atom’s data directly, lock the atom container in memory by calling `QTLockContainer`. Once the container is locked, you can call `QTGetAtomDataPtr` to retrieve a pointer to an atom’s data. When you have finished accessing the atom’s data, call the `QTUnlockContainer` function to unlock the container in memory.

## See Also

- [Creating new atoms](creating_new_atoms.md)
  Create new atoms and insert them in a QT atom container.
- [Copying existing atoms](copying_existing_atoms.md)
  Copy existing atoms within an atom container.
- [Modifying atoms](modifying_atoms.md)
  Modify attributes or data associated with an atom in an atom container.
- [Removing atoms from an atom container](removing_atoms_from_an_atom_container.md)
  Remove atoms from an atom container.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicktime-file-format/retrieving_atoms_from_an_atom_container)*