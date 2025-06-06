# StdFBShmem_t

**Framework**: Kernel  
**Kind**: tag

**Availability**:
- macOS 10.6+

## Declaration

```swift
struct StdFBShmem_t {
    ...
};
```

## Topics

### Instance Properties
- [cursor](stdfbshmem_t/1495696-cursor.md)
- [cursorLoc](stdfbshmem_t/1495693-cursorloc.md)
- [cursorObscured](stdfbshmem_t/1495726-cursorobscured.md)
  If this is true, the cursor has been obscured and cursorShow should not be 0. The cursor will be shown again the next time it is moved.
- [cursorRect](stdfbshmem_t/1495671-cursorrect.md)
  The region that the cursor image currently occupies in software cursor mode.
- [cursorSema](stdfbshmem_t/1495662-cursorsema.md)
- [cursorShow](stdfbshmem_t/1495697-cursorshow.md)
  The cursor is displayed when cursorShow is 0.
- [cursorSize](stdfbshmem_t/1495694-cursorsize.md)
- [frame](stdfbshmem_t/1495728-frame.md)
- [hardwareCursorActive](stdfbshmem_t/1495735-hardwarecursoractive.md)
- [hardwareCursorCapable](stdfbshmem_t/1495677-hardwarecursorcapable.md)
- [hardwareCursorShields](stdfbshmem_t/1495666-hardwarecursorshields.md)
- [hotSpot](stdfbshmem_t/1495721-hotspot.md)
- [oldCursorRect](stdfbshmem_t/1495676-oldcursorrect.md)
- [reservedB](stdfbshmem_t/1495705-reservedb.md)
- [reservedC](stdfbshmem_t/1495738-reservedc.md)
- [saveRect](stdfbshmem_t/1495657-saverect.md)
- [screenBounds](stdfbshmem_t/1495660-screenbounds.md)
- [shieldFlag](stdfbshmem_t/1495709-shieldflag.md)
  When this is set to true the cursor will not be displayed in the region specified by shieldRect.
- [shieldRect](stdfbshmem_t/1495703-shieldrect.md)
- [shielded](stdfbshmem_t/1495714-shielded.md)
- [structSize](stdfbshmem_t/1495664-structsize.md)
- [vblCount](stdfbshmem_t/1495656-vblcount.md)
- [vblDelta](stdfbshmem_t/1495702-vbldelta.md)
- [vblDeltaMeasured](stdfbshmem_t/1495655-vbldeltameasured.md)
- [vblDeltaReal](stdfbshmem_t/1495732-vbldeltareal.md)
- [vblDrift](stdfbshmem_t/1495680-vbldrift.md)
- [vblTime](stdfbshmem_t/1495690-vbltime.md)
  The time of the most recent vertical blanking.
- [version](stdfbshmem_t/1495730-version.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/stdfbshmem_t)*