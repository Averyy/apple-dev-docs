# Copying existing atoms

**Framework**: QuickTime File Format

Copy existing atoms within an atom container.

#### Overview

QuickTime provides several functions for copying existing atoms within an atom container. The `QTInsertChildren` function inserts a container of atoms as children of a parent atom in another atom container. The following figure shows two example QT atom containers, A and B.

![A diagram that shows two vertical arrangements of boxes connected by arrows. The first arrangement, on the left, shows a box with the caption “QT atom container A”, with an arrow pointing down to a box below it. The box below contains two sections stacked vertically. The first section contains the caption “‘abcd’”, and the second section contains the caption “1000”. Below the bottom box are the captions “Index = 1” and “Offset = 10”. The second arrangement, on the right, shows a box with the caption “QT atom container B”, with an arrow that splits in the middle pointing down to two horizontally-aligned boxes below it. The box below and on the left contains two sections stacked vertically. The first section contains the caption “‘defg’”, and the second section contains the caption “900”. Below the bottom box are the captions “Index = 1” and “Offset = 10”. The box below and on the right contains three sections stacked vertically. The first section contains the caption “‘hijk’”, the second section contains the caption “2000”, and the third section contains the caption “Data”. Below the bottom box are the captions “Index = 2” and “Offset = 20”.](https://docs-assets.developer.apple.com/published/95b49617c6077850791c6bab804c6a56/qt-two-containers%402x.png)

The following code sample calls `QTFindChildByID` to retrieve the offset of the atom in container A. Then, the code sample calls the `QTInsertChildren` function to insert the atoms in container B as children of the atom in container A. The following figure shows what container A looks like after the atoms from container B have been inserted.

```c
QTAtom targetAtom;
 
targetAtom = QTFindChildByID (containerA, kParentAtomIsContainer,  'abcd',
    1000, nil);
 
FailOSErr (QTInsertChildren (containerA, targetAtom, containerB));
```

The following figure shows a QT atom container after insert child atoms.

![A diagram that shows a box with the caption “QT atom container A”, with an arrow pointing down to a box below it. The box below contains two sections stacked vertically. The first section contains the caption “‘abcd’”, and the second section contains the caption “1000”. Beside that box are the captions “Index = 1” and “Offset = 10”. Below that box is an arrow that splits in the middle pointing down to two horizontally-aligned boxes below it. The box below and on the left contains two sections stacked vertically. The first section contains the caption “‘defg’”, and the second section contains the caption “900”. Below the bottom box are the captions “Index = 1” and “Offset = 20”. The box below and on the right contains three sections stacked vertically. The first section contains the caption “‘hijk’”, the second section contains the caption “2000”, and the third section contains the caption “Data”. Below the bottom box are the captions “Index = 2” and “Offset = 30”. ](https://docs-assets.developer.apple.com/published/11cf368b2f50f7e23429933c08789d39/qt-after-child-atoms%402x.png)

In the following listing, the `QTInsertChild` function inserts a parent atom into the atom container `theSample`. Then, the code calls `QTInsertChildren` to insert the container `theSprite` into the container `theSample`. The parent atom is `newSpriteAtom`.

```c
FailOSErr (QTInsertChild (theSample, kParentAtomIsContainer,
    kSpriteAtomType, spriteID, 0, 0, nil, &newSpriteAtom));
 
FailOSErr (QTInsertChildren (theSample, newSpriteAtom, theSprite));
```

QuickTime provides three other functions you can use to manipulate atoms in an atom container. The `QTReplaceAtom` function replaces an atom and its children with a different atom and its children. You can call the `QTSwapAtoms` function to swap the contents of two atoms in an atom container; after swapping, the ID and index of each atom remains the same. The `QTCopyAtom` function copies an atom and its children to a new atom container.

## See Also

- [Creating new atoms](creating_new_atoms.md)
  Create new atoms and insert them in a QT atom container.
- [Retrieving atoms from an atom container](retrieving_atoms_from_an_atom_container.md)
  Retrieve information about the types of a parent atom’s children, search for a specific atom, and retrieve a leaf atom’s data.
- [Modifying atoms](modifying_atoms.md)
  Modify attributes or data associated with an atom in an atom container.
- [Removing atoms from an atom container](removing_atoms_from_an_atom_container.md)
  Remove atoms from an atom container.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicktime-file-format/copying_existing_atoms)*