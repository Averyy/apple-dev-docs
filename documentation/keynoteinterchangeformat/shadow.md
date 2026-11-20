# Shadow

**Framework**: Keynote Interchange Format  
**Kind**: typealias  
**Role**: Type

The kind of shadow cast by an object, or `none` for no shadow.

**Availability**:
- Keynote Interchange Format 1.0+ (Beta)

## Declaration

```
(Shadow.contactShadow | Shadow.curvedShadow | Shadow.dropShadow | string("none")) Shadow
```



**Allowed Types**: `Shadow.contactShadow`, `Shadow.curvedShadow`, `Shadow.dropShadow`, `string("none")`

## Discussion

This value takes one of the following forms:

- `contactShadow`: A contact shadow, cast by a light directly above the object.
- `curvedShadow`: A curved shadow, cast as though the object were curled.
- `dropShadow`: A drop shadow, cast from above the plane of the document.
- `none`: No shadow. This case is accepted when reading but isn’t written; the shadow property is omitted instead.

## Topics

### Dictionaries
- [object Shadow.contactShadow](./shadow/contactshadow.md)
  A contact shadow, cast by a light directly above the object.
- [object Shadow.curvedShadow](./shadow/curvedshadow.md)
  A curved shadow, cast as though the object were curled.
- [object Shadow.dropShadow](./shadow/dropshadow.md)
  A drop shadow, cast from above the plane of the document.

## See Also

### Shadows
- [object ContactShadow](./contactshadow.md)
  A shadow whose silhouette pools under the object’s bottom edge as though the object were standing on a ground plane.
- [object CurvedShadow](./curvedshadow.md)
  A shadow whose silhouette curls away from the object, as if it were a page lifting off the surface rather than lying flat.
- [object DropShadow](./dropshadow.md)
  A shadow whose silhouette appears as though cast by a light source facing down toward the plane of the object.
- [object Reflection](./reflection.md)
  A mirrored copy of the object that the reader drew directly below it on a ground plane aligned to the horizontal axis, fading out with distance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/keynoteinterchangeformat/shadow)*