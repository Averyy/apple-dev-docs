# upVector

**Framework**: USD

A vector around which the runtime rotates the object.

#### Overview

This property defines the axis around which the runtime rotates the target to create the effect of a prim looking at the user. Normally, an asset defines this value to match the stage’s [`upAxis`](https://developer.apple.comhttps://openusd.org/docs/api/group___usd_geom_up_axis__group.html). The default value points positively in the y-direction.

##### Declaration

```other
uniform vector3d upVector = (0.0, 1.0, 0.0)
```

## See Also

- [info:id](info-id.md)
  The action’s unique identifier.
- [affectedObjects](affectedobjects.md)
  A list of prims that respond to the notification.
- [duration](duration.md)
  The amount of time that the objects face the camera.
- [front](front.md)
  A vector that’s perpendicular to, and points outward from, the object’s face.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usd/upvector)*